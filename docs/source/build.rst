.. _build:


Build
======

From your local machine
-----------------------

 ::

	$ cd cd2cloud
	$ make

	Usage: make <target> where <target> is one of

	clean     clean temp files from local workspace
	doc       generate sphinx documentation and man pages
	test      run unit tests locally
	tarball   generate tarball of project
	rpm       build source codes and generate rpm file
	srpm      generate SRPM file
	all       clean test doc rpm
	flake8    check Python style based on flake8


	$ make rpm


Copr
-----

 .. NOTE:: Before doing any release, make sure that you have account on both sites and also make sure that you could
  access to your fedorapeople space [#]_ and have enough permissions [#]_ to build `cd2cloud` in `Copr`.

	$ make srpm

   1. copy rpmbuild/SRPMS/cd2cloud-0.0.1-1.src.rpm to cd2cloud/copr
   2. push cd2cloud/copr to github

  `copr-cli` will be used, installed by `sudo yum/dnf install copr-cli` and configure it. [#]_

Request as `Builder` for projects `cd2cloud`, wait until admin approves.

$ copr-cli build cd2cloud https://github.com/eduardocerqueira/cd2cloud/raw/master/copr/cd2cloud-0.0.1-1.src.rpm

Go and grab a cup of tea or coffee, the release build will be come out soon ::

    # tag based builds: `https://copr.fedorainfracloud.org/coprs/eduardocerqueira/cd2cloud/builds/`


.. [#] https://fedorahosted.org/copr/wiki/HowToEnableRepo
.. [#] http://fedoraproject.org/wiki/Infrastructure/fedorapeople.org#Accessing_Your_fedorapeople.org_Space
.. [#] https://fedorahosted.org/copr/wiki/UserDocs#CanIgiveaccesstomyrepotomyteammate
.. [#] https://copr.fedoraproject.org/api/
