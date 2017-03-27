from configparser import ConfigParser

PATH = "/home/ecerquei/git/cd2cloud/conf/cd2cloud.conf"

parser = ConfigParser()
parser.read(PATH)

for section_name in parser.sections():
    print 'Section:', section_name
    print '  Options:', parser.options(section_name)
    for name, value in parser.items(section_name):
        print '  %s = %s' % (name, value)
    print

print parser.get('Ripping', 'workdir')
print parser.get('Ripping', 'abcde_conf')