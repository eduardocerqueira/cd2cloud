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

from cd2cloud.util import get_args, get_config
from cd2cloud.util.logger import Log
from cd2cloud.util import CalcTime
from cd2cloud.core.CDMonitor import CDMonitor
from cd2cloud.core.Worker import Worker
from logging import getLogger
import cdio
import pycdio


class CD2Cloud():
    """Prog main class"""
    def __init__(self):
        """initialization"""
        # get command line args
        self.args = get_args()

        # Start execution clockwatch
        self.calctime = CalcTime()
        self.start_time = self.calctime.start()

        # start - init log
        # log verbose (arg overrides value declared in config file)
        self.verbose = get_config(self.args.conf, 'Log', 'verbose')
        if self.args.verbose:
            self.verbose = True

        _log_file = get_config(self.args.conf, 'Log', 'path')
        Log(__name__, self.verbose, _log_file).set_logger()
        self.log = getLogger(__name__)
        # end - init log

        # converter main object
        self.converter = CDConverter(self.args)

    def start(self):
        """Start CD2Cloud pipeline"""
        self.converter.start_monitor()


class CDConverter():
    def __init__(self, args):
        """initialization"""
        self.args = args
        self.log = getLogger(__name__)
        self.monitor = CDMonitor(self.cd_rip)   #asynchronously monitor

    def start_monitor(self):
        self.monitor.start()

    def stop_monitor(self):
        self.monitor.stop()

    def is_cd_ready(self=None):
        """Check if CD (drive) is accessible and if there an not empty
        CDROM (media) inserted and ready"""
        # CD-ROM device
        try:
            d = cdio.Device(driver_id=pycdio.DRIVER_UNKNOWN)
            drive_path = d.get_device()
            self.log.info("device %s" % drive_path)
        except (IOError, Exception) as ex:
            self.log.error("CD-ROM not accessible %s" % ex)

        # CD Media
        try:
            i_tracks = d.get_num_tracks()
            self.log.info("number of tracks %d" % i_tracks)
            return True
        except (IOError, Exception) as ex:
            self.log.warn("No media inserted %s" % ex)
            return False

    def cd_rip(self, device):
        self.log.debug(device.device_node)
        self.log.debug(device.device_path)

        if self.is_cd_ready():
            self.log.info("Starting CD ripping")
            rip_workdir = get_config(self.args.conf, 'Ripping', 'workdir')
            ripper = Worker(rip_workdir)
            cd2cloud_cfg = get_config(self.args.conf, 'Ripping', 'abcde_conf')
            #cmd = 'abcde -c %s -N' % cd2cloud_cfg
            cmd = 'cat %s && sleep 20' % cd2cloud_cfg
            ripper.thread(cmd)
            self.log.info("Complete CD ripping")
            self.copy()

    def copy(self):
        self.log.info("Starting copying to cloud")
        self.log.info("Complete copying to cloud")
        self.notify()

    def notify(self):
        self.log.info("Starting notify")
        self.log.info("Complete notify")
