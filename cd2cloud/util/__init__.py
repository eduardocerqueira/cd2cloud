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

from configparser import ConfigParser
from os.path import exists
import argparse
import sys
from time import time


def get_args():
    """
    Get user args if exist;

    Arguments:

    --conf: full path for cd2cloud config file
    """
    parser = argparse.ArgumentParser(prog='cd2cloud')
    required_named = parser.add_argument_group('required arguments')

    required_named.add_argument('--conf', default=True,
                                help="full path for cd2cloud.conf",
                                required=True,
                                type=str,
                                action='store')

    parser.add_argument("--verbose",
                        help="run on verbose mode (DEBUG) level",
                        default=False,
                        action="store_true")

    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.print_help()
        sys.exit(1)

    return args

def read_config(path):
    """ """
    if not exists(path):
        raise IOError("File % doesn't exist" % path)

    parser = ConfigParser()
    parser.read(path)
    return parser

def get_config(path, cfg_section, cfg_property):
    """hook to get property from cd2cloud.conf file """
    config = read_config(path)
    return config.get(cfg_section, cfg_property)


class CalcTime(object):
    """Calculate elapsed time."""

    def __init__(self):
        """Constructor """
        # time
        self.start_time = None
        self.end_time = None
        self.duration = None

    def start(self):
        """Set start time."""
        self.start_time = time()
        return self.start_time

    def end(self):
        """Set end time."""
        self.end_time = time()

    def delta(self):
        """Calculate time delta between start and end times.

        :return: Hours, minutes, seconds
        """
        elapsed = self.end_time - self.start_time
        hours = elapsed // 3600
        elapsed = elapsed - 3600 * hours
        minutes = elapsed // 60
        seconds = elapsed - 60 * minutes

        return hours, minutes, seconds
