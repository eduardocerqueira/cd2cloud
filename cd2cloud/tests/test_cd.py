import dbus

bus = dbus.SessionBus()
print bus.list_names()

print "-" * 80

for elem in bus.list_names():
    print elem
