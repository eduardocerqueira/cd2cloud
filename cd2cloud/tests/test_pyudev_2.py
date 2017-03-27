#
# http://pyudev.readthedocs.io/en/latest/guide.html
#

import pyudev

context = pyudev.Context()

for device in context.list_devices(subsystem='block', DEVTYPE='disk'):
    for key, value in device.iteritems():
        print '{key}={value}'.format(key=key, value=value)
