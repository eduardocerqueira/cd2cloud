import sys
import cdio
import pycdio

try:
    d = cdio.Device(driver_id=pycdio.DRIVER_UNKNOWN)
    drive_name = d.get_device()
except IOError:
    print("Problem finding a CD-ROM")
    sys.exit(1)

ok, vendor, model, release = d.get_hwinfo()
print("drive: %s, vendor: %s, model: %s, release: %s" % (drive_name, vendor, model, release))

try:
    i_tracks = d.get_num_tracks()
    print i_tracks
except Exception as ex:
    print ex

d.close()
