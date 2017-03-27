import dbus
from dbus.mainloop.glib import DBusGMainLoop
DBusGMainLoop(set_as_default=True)

bus = dbus.SystemBus()


def callback_function(path, interfaces):
    try:
        obj = bus.get_object('org.freedesktop.UDisks2', path)
        iface = dbus.Interface(obj, 'org.freedesktop.UDisks2.Filesystem')
        path = iface.get_dbus_method('Mount', dbus_interface='org.freedesktop.UDisks2.Filesystem')([])
        print "Mounted at %s" % (path)
    except ValueError:
        return

iface = 'org.freedesktop.DBus.ObjectManager'
signal = 'InterfacesAdded'
bus.add_signal_receiver(callback_function, signal, iface)

import gobject
loop = gobject.MainLoop()
loop.run()
