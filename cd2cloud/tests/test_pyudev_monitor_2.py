import pyudev

def device_added_callback():
    print "OK"

def device_changed_callback():
    print "NAO"

if __name__ == '__main__':
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)

    observer = pyudev.pygtk.GUDevMonitorObserver(monitor)
    observer.connect('device-added', device_added_callback)
    observer.connect('device-changed', device_changed_callback)
    monitor.enable_receiving()
    mainloop = gobject.MainLoop()
    mainloop.run()