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
from cd2cloud.core.Notification import Notification
from logging import getLogger
import CDDB
import DiscID


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

    def stop(self):
        """Stop CD2Cloud pipeline"""
        self.converter.stop_monitor()


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
        try:
            cdrom = DiscID.open()
            disc_id = DiscID.disc_id(cdrom)
            return True
        except:
            self.log.warn('no disc in CD drive')
            return False

    def cd_rip(self, device):
        self.log.debug(device.device_node)
        self.log.debug(device.device_path)

        if self.is_cd_ready():
            try:
                # cddb
                cd_title = None
                cdrom = DiscID.open()
                disc_id = DiscID.disc_id(cdrom)
                (query_status, query_info) = CDDB.query(disc_id)
                if query_status == 200:
                    cd_title = query_info['title'][:20]

                self.log.info("Starting CD ripping for %s" % cd_title)
                rip_workdir = get_config(self.args.conf, 'Ripping', 'workdir')
                ripper = Worker(rip_workdir)
                cd2cloud_cfg = get_config(self.args.conf, 'Ripping', 'abcde_conf')
                cmd = '/usr/bin/abcde -c %s -j 5 -N' % cd2cloud_cfg

                #ripper.thread(cmd)
                ripper.run_cmd(cmd)
                self.log.info("Complete CD ripping for %s" % cd_title)
                self.notify(cd_title)
            except:
                msg = 'FAILED %s' % cd_title
                self.notify(msg)

    def notify(self, msg):
        self.log.info("Starting notify")
        notify = Notification()
        notify.gnome(msg)
        self.log.info("Complete notify")
