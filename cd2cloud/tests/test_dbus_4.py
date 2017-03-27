import dbus
import gobject
import dbus.mainloop.glib

def handler(*args, **kwargs):

    for service in dbus.SessionBus().list_names():
        print(service)

    if kwargs["member"] == "DriveChanged":
        device = args[2]
        print device

#         for elem in args:
#             if isinstance(elem, tuple):
#                 for i in elem:
#                     print i


        #print "ARGS\n %s" % str(args)
        #print "*" * 60
        #print "KWARGS\n %s" % str(kwargs)
        #print "-" * 80

dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
bus = dbus.SessionBus()

#props = cd.getProperties(dbus_interface='org.freedesktop.NetworkManager.Devices')

bus.add_signal_receiver(handler, interface_keyword="dbus_interface", member_keyword="member")

# Start Loop
loop = gobject.MainLoop()
loop.run()
