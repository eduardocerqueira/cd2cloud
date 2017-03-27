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

from cd2cloud.core import CD2Cloud
import sys


if __name__ == '__main__':
    try:
        cd = CD2Cloud()
        cd.start()

    except Exception as ex:
        cd.log.error(ex)

    except (KeyboardInterrupt, SystemExit) as ex:
        cd.log.error(ex)
        cd.cd.stop_monitor()
        sys.exit(1)

#     finally:
#         # End execution
#         cd.calctime.end()
#         hours, minutes, seconds = cd.calctime.delta()
#         cd.log.info("End execution in %dh:%dm:%ds", hours, minutes, seconds)
