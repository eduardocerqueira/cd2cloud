#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from logging import getLogger
from pyudev import Context, Monitor, MonitorObserver


class CDMonitor():
    """
    Monitor Kernel events asynchronously for CD (drive) and CDROM (media)
    and trigger the CD2Cloud process
    """
    def __init__(self, func_name):
        """initialization"""
        self.log = getLogger(__name__)
        context = Context()
        monitor = Monitor.from_netlink(context)
        self.observer = MonitorObserver(monitor, callback=func_name,
                                   name='monitor-observer')
        self.observer.daemon = False

    def start(self):
        """Start monitor"""
        self.observer.start()
        self.log.info('Started CD2Cloud monitor... listening for CD events')

    def stop(self):
        """Stop monitor"""
        self.observer.stop()
        self.log.info('Stopped CD2Cloud monitor')
