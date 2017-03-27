#http://hal.freedesktop.org/docs/udisks/Device.html

import dbus
import gobject
import dbus.mainloop.glib


def mount(device, fs):
    """
    >>> mount('/dev/sdb1','ext3')
    /media/pendrive
    >>> mount('/dev/sdc2','ext2')
    ''
    """
    res = ''
    _bus = dbus.SystemBus()
    _proxy = _bus.get_object('org.freedesktop.UDisks', '/org/freedesktop/UDisks')
    _iface = dbus.Interface(_proxy, 'org.freedesktop.UDisks')
    for _dev in _iface.EnumerateDevices():
        _dev_obj = _bus.get_object('org.freedesktop.UDisks', _dev)
        _dev_prop = dbus.Interface(_dev_obj, 'org.freedesktop.DBus.Properties')
        if _dev_prop.Get('', 'DeviceFile') == device:
            _idev = dbus.Interface(_dev_obj, 'org.freedesktop.DBus.UDisks.Device')
            res = _idev.get_dbus_method('FilesystemMount', dbus_interface='org.freedesktop.UDisks.Device')(fs, [])
    return res


def unmount(device):
    """
    >>> unmount('/dev/sdb1')
    """
    _bus = dbus.SystemBus()
    _proxy = _bus.get_object('org.freedesktop.UDisks', '/org/freedesktop/UDisks')
    _iface = dbus.Interface(_proxy, 'org.freedesktop.UDisks')
    for _dev in _iface.EnumerateDevices():
        _dev_obj = _bus.get_object('org.freedesktop.UDisks', _dev)
        _dev_prop = dbus.Interface(_dev_obj, 'org.freedesktop.DBus.Properties')
        if _dev_prop.Get('', 'DeviceFile') == device:
            _idev = dbus.Interface(_dev_obj, 'org.freedesktop.DBus.UDisks.Device')
            _idev.get_dbus_method('FilesystemUnmount', dbus_interface='org.freedesktop.UDisks.Device')([])

if __name__ == '__main__':

    _bus = dbus.SystemBus()
    _proxy = _bus.get_object('org.freedesktop.UDisks2', '/org/freedesktop/UDisks2')
    _iface = dbus.Interface(_proxy, 'org.freedesktop.UDisks')
    for _dev in _iface.EnumerateDevices():
        _dev_obj = _bus.get_object('org.freedesktop.UDisks2', _dev)
        _dev_prop = dbus.Interface(_dev_obj, 'org.freedesktop.DBus.Properties')
