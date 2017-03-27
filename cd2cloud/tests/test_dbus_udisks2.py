import dbus


bus = dbus.SystemBus()

# obj = bus.get_object('org.freedesktop.UDisks2', '/org/freedesktop/UDisks2')
# iface = dbus.Interface(obj, 'org.freedesktop.DBus.ObjectManager')
# print iface.GetManagedObjects()
#
# obj1 = bus.get_object('org.freedesktop.UDisks2', '/org/freedesktop/UDisks2')
# iface = dbus.Interface(obj1, 'org.freedesktop.DBus.Properties')
# print iface
#
# iface1 = dbus.Interface(obj1, 'org.freedesktop.UDisks2.Block')
# print iface1
#
# obj2 = bus.get_object('org.freedesktop.UDisks2', '/org/freedesktop/UDisks2/block_devices/sr0')
# print obj2
#
# iface2 = dbus.Interface(obj2, 'org.freedesktop.UDisks2.Block')
# print iface2
#
# obj2 = bus.get_object('org.freedesktop.UDisks2', '/org/freedesktop/UDisks2/block_devices/sr0')


manager = dbus.Interface(bus.get_object('org.freedesktop.UDisks2', '/org/freedesktop/UDisks2'), "org.freedesktop.DBus.ObjectManager")
objects = manager.GetManagedObjects()

for path in objects.keys():
    print "PATH: [ %s ]" % (path)

    if 'Toshiba' in path:
        interfaces = objects[path]
        for interface in interfaces.keys():
            print "INTERFACES: %s" % (interface)
            properties = interfaces[interface]
            for key in properties.keys():
                print " %s = %s" % (key, properties[key])

