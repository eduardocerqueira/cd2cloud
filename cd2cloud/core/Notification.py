# -*- coding: UTF-8 -*-

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
from subprocess import Popen, PIPE

class Notification():
    def __init__(self):
        self.log = getLogger(__name__)

    def gnome(self, msg):
        cmd = "notify-send --icon=/usr/share/pixmaps/disks.png \"cd2cloud\" \"%s\" " % msg
        proc = Popen(cmd, stdout=PIPE, shell=True)
        self.log.info('gnome notification sent for %s' % msg)
