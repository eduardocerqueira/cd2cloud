#
#
# https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.MonitorObserver
#
#
#

#
# TODO: config file
# TODO: logging and load msg logger from file and save to file
# TODO: Email notification
# TODO:
#

from pyudev import Context, Monitor, MonitorObserver
from time import sleep
import cdio
import pycdio


def monitor():
    context = Context()
    monitor = Monitor.from_netlink(context)
    observer = MonitorObserver(monitor, callback=print_device_event, name='monitor-observer')
    observer.daemon = False
    return observer

def print_device_event(device):
    print('background event {0.action}: {0.device_path}'.format(device))
    print device.device_node
    print device.device_path
    cd_rip()

def is_cd_ready():
    # CD-ROM device
    try:
        d = cdio.Device(driver_id=pycdio.DRIVER_UNKNOWN)
        drive_path = d.get_device()
        print "device %s" % drive_path
    except (IOError, Exception) as ex:
        print "CD-ROM not accessible %s" % ex

    # CD Media
    try:
        i_tracks = d.get_num_tracks()
        print "number of tracks %d" % i_tracks
        return True
    except (IOError, Exception) as ex:
        print "No media inserted %s" % ex
        return False

def cd_rip():
    if is_cd_ready():
        print "Starting CD ripping"
        sleep(5)
        print "Complete CD ripping"
        copy()

def copy():
    print "Starting copying to cloud"
    sleep(5)
    print "Complete copying to cloud"
    notify()

def notify():
    print "Starting notify"
    sleep(5)
    print "Complete notify"
    print "DONE"

if __name__ == '__main__':
    observer = monitor()
    print "START"
    observer.start()
