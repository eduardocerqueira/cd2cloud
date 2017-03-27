import pyudev
import psutil


if __name__ == '__main__':
    context = pyudev.Context()

    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by('block')

    for device in iter(monitor.poll, None):
        if device.get('ID_VENDOR') and 'Toshiba' in device.get('ID_VENDOR'):
            print "ACTION: %s" % device.action
            print "DEVNAME: %s" % device.get('DEVNAME')


removable = [device for device in context.list_devices(subsystem='block', DEVTYPE='disk') if device.attributes.asstring('removable') == "1"]
for device in removable:
    partitions = [device.device_node for device in context.list_devices(subsystem='block', DEVTYPE='partition', parent=device)]
    print("All removable partitions: {}".format(", ".join(partitions)))
    print("Mounted removable partitions:")
    for p in psutil.disk_partitions():
        if p.device in partitions:
            print("  {}: {}".format(p.device, p.mountpoint))