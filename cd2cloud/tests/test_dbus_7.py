from dbus import SessionBus, Interface
import gobject
from dbus.mainloop.glib import DBusGMainLoop


def handler(*args, **kwargs):
    if 'RemoteVolumeMonitor' in kwargs['dbus_interface'] and 'VolumeAdded' in kwargs['DriveChanged']:
        print "-" * 30
        print kwargs
        print args
        lproperties = []
        lproperties = args
        for prop in lproperties:
            print prop


DBusGMainLoop(set_as_default=True)
bus = SessionBus()

bus.add_signal_receiver(
    handler_function=handler,
    interface_keyword="dbus_interface",
    member_keyword="DriveChanged",
    dbus_interface="org.gtk.Private.RemoteVolumeMonitor")

# Start Loop
loop = gobject.MainLoop()
loop.run()
