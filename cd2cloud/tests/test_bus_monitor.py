#
# https://linuxmeerkat.wordpress.com/2014/11/12/python-detection-of-usb-storage-device/
# https://dbus.freedesktop.org/doc/dbus-python/api/dbus.bus.BusConnection-class.html
# http://mindbending.org/en/python-and-udisks-part-5
# https://udisks.freedesktop.org/docs/latest/gdbus-org.freedesktop.UDisks2.Block.html

import threading, time
import sys
import dbus
from dbus.mainloop.glib import DBusGMainLoop


def prog_header():
    print "=" * 40
    print "CD2CLOUD"
    print "=" * 40

def waiting():
    prog_header()
    counter = 1
    while True:
        time.sleep(1)
        if counter <= 4:
            print ".",
            sys.stdout.flush()
        else:
            sys.stdout.write("\033[F")  # Cursor up one line
            #sys.stdout.write("\033[K") # Clear to the end of line
            print "\r" + " " * 40
            counter = 1
        counter = counter + 1

def start_listening():
    DBusGMainLoop(set_as_default=True)
    bus = dbus.SystemBus()

    # Function which will run when signal is received
    def callback_function(*args):
        print('event received: ', args)

    # Which signal to have an eye for
    iface  = 'org.freedesktop.UDisks2.ObjectManager'
    signal = 'InterfacesAdded'

    #iface  = 'org.freedesktop.DBus.ObjectManager'
    #signal = 'InterfacesAdded'
    bus.add_signal_receiver(callback_function, signal, iface)

    # Let's start the loop
    import gobject
    gobject.threads_init()      # Without this, we will be stuck in the glib loop
    loop = gobject.MainLoop()
    loop.run()

# Our thread will run start_listening
thread=threading.Thread(target=start_listening)
thread.daemon=True              # This makes sure that CTRL+C works
thread.start()

# And our program will continue in this pointless loop
while True:
    time.sleep(1)
    print "."
#waiting()