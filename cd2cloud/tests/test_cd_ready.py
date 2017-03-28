import DiscID


def is_cd_ready():
    try:
        cdrom = DiscID.open()
        disc_id = DiscID.disc_id(cdrom)
        return True
    except Exception as ex:
        print 'disc not inserted %s' % ex
        return False

if __name__ == '__main__':
    print is_cd_ready()
