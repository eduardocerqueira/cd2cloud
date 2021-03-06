default: help

NAME=cd2cloud
MAN=cd2cloud.1
VERSION=0.0.1
RPMDIST=$(shell rpm --eval '%dist')
#RELEASE=1$(rpmsuffix)$(RPMDIST)
RELEASE=1
PWD=$(shell bash -c "pwd -P")
RPMTOP=$(PWD)/rpmbuild
SPEC=$(NAME).spec
TARBALL=$(NAME)-$(VERSION).tar.gz
SRPM=$(NAME)-$(VERSION)-$(RELEASE).src.rpm

help:
	@echo
	@echo "Usage: make <target> where <target> is one of"
	@echo
	@echo "clean     clean temp files from local workspace"
	@echo "doc       generate sphinx documentation and man pages"
	@echo "test      run unit tests locally"
	@echo "tarball   generate tarball of project"
	@echo "rpm       build source codes and generate rpm file"
	@echo "srpm      generate SRPM file"
	@echo "all       clean test doc rpm"
	@echo "flake8    check Python style based on flake8"
	@echo "dev       short cut for devel, see Makefile"
	@echo

all: clean test doc rpm

prep:
	#rpmdev-setuptree into project folder
	@mkdir -p rpmbuild/{BUILD,BUIDLROOT,RPMS,SOURCES,SPECS,SRPMS}

set-version:
	@echo $(VERSION)-$(RELEASE) > $(RPMTOP)/SOURCES/version.txt
	@cp $(RPMTOP)/SOURCES/version.txt $(RPMTOP)/BUILD/version.txt

clean:
	$(RM) $(NAME)*.tar.gz $(SPEC)
	$(RM) -r rpmbuild
	@find -name '*.py[co]' -delete
	make clean -C docs/
	rm -rf docs/build build dist cd2cloud.egg-info

doc: prep set-version
	make -C docs/ html
	make -C docs/ man
	cp docs/build/man/cd2cloud.1 cd2cloud.1  

spec: $(SPEC).in prep doc
	sed \
		-e 's/@RPM_VERSION@/$(VERSION)/g' \
		-e 's/@RPM_RELEASE@/$(RELEASE)/g' \
		< $(SPEC).in \
		> $(RPMTOP)/SPECS/$(SPEC)

tarball: spec
	git ls-files | tar --transform='s|^|$(NAME)/|' \
	--files-from /proc/self/fd/0 \
	-czf $(RPMTOP)/SOURCES/$(TARBALL) $(RPMTOP)/SPECS/$(SPEC)

srpm: tarball
	rpmbuild --define="_topdir $(RPMTOP)" --define "_specdir $(RPMTOP)/SPECS" \
	-ts $(RPMTOP)/SOURCES/$(TARBALL)

rpm: srpm
	rpmbuild --define="_topdir $(RPMTOP)" --rebuild $(RPMTOP)/SRPMS/$(SRPM)

git:
	git status
	git add .

# build local rpm, remove previous, install new and print cd2cloud version
dev: clean git rpm
ifneq ("$(wildcard /usr/bin/paws)","")
	sudo dnf remove cd2cloud -y > /dev/null
endif
	sudo dnf install $(shell bash -c "find $(RPMTOP)/RPMS/ -name '$(NAME)-$(VERSION)-$(RELEASE)*'") -y > /dev/null
	echo "Ready to GO!"

# Unit tests
TEST_SOURCE=tests
TEST_OUTPUT=$(RPMTOP)/TESTS
TEST_UNIT_FILE=unit-tests.xml

test: prep
	nosetests --verbosity=3 -x --with-xunit --xunit-file=$(TEST_OUTPUT)/$(TEST_UNIT_FILE)	
	@echo

# Check code convention based on flake8
CHECK_DIRS=.
FLAKE8_CONFIG_DIR=tox.ini

flake8:
	flake8 $(CHECK_DIRS) --config=$(FLAKE8_CONFIG_DIR)
