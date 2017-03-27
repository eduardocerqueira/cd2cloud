#!/usr/bin/env python

import dbus
import gobject
import os


class DeviceAddedListener:

    def __init__(self):
        self.bus = dbus.SystemBus()
        self.hal_manager_obj = self.bus.get_object("org.freedesktop.Hal", "/org/freedesktop/Hal/Manager")
        self.hal_manager = dbus.Interface(self.hal_manager_obj, "org.freedesktop.Hal.Manager")
        self.hal_manager.connect_to_signal("DeviceAdded", self.added)

    def show(self, name, udi):
        d_object = self.bus.get_object('org.freedesktop.Hal', udi)
        d_interface = dbus.Interface(d_object, 'org.freedesktop.Hal.Device')
        if d_interface.QueryCapability("volume"):
            print name
            props = ["block.device", "volume.label", "volume.fstype", "volume.is_mounted", "volume.mount_point", "volume.size"]
            for p in props:
                print '\t', p, " = ",
                try:
                    print d_interface.GetProperty(p)
                except:
                    print "Fail"

    def added(self, udi):
        self.show("DeviceAdded", udi)
        self.bus.add_signal_receiver(self.property_modified,
                                     "PropertyModified",
                                     "org.freedesktop.Hal.Device",
                                     "org.freedesktop.Hal",
                                     udi,
                                     path_keyword="sending_device")

    def property_modified(self, numupdates, updates, sending_device=None):
        self.show("PropertyModified", sending_device)


if __name__ == '__main__':
    from dbus.mainloop.glib import DBusGMainLoop
    DBusGMainLoop(set_as_default=True)
    loop = gobject.MainLoop()
    DeviceAddedListener()
    print "running"
    loop.run()
