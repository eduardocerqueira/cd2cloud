import threading
import time


def start_listening():
    import dbus
    from dbus.mainloop.glib import DBusGMainLoop
    DBusGMainLoop(set_as_default=True)
    bus = dbus.SystemBus()

    # Function which will run when signal is received
    def callback_function(*args):
        print('Received something .. ', args)

    # Which signal to have an eye for
    #iface = 'org.freedesktop.DBus.ObjectManager'
    iface = "org.gtk.vfs.MountTracker"
    signal = 'InterfacesAdded'
    bus.add_signal_receiver(callback_function, signal, iface)

    # Let's start the loop
    import gobject
    gobject.threads_init()      # Without this, we will be stuck in the glib loop
    loop = gobject.MainLoop()
    loop.run()

# Our thread will run start_listening
thread = threading.Thread(target=start_listening)
thread.daemon = True              # This makes sure that CTRL+C works
thread.start()

# And our program will continue in this pointless loop
while True:
    time.sleep(1)
    print("tralala")
