import CDDB
import DiscID

cdrom = DiscID.open()
disc_id = DiscID.disc_id(cdrom)

(query_status, query_info) = CDDB.query(disc_id)
if query_status == 200:
    print query_info['title']

(read_status, read_info) = CDDB.read(query_info['category'], query_info['disc_id'])

for i in range(disc_id[1]):
    print "Track %d %s" % (i, read_info['TTITLE%s' % str(i)])
