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

from logging import DEBUG, INFO, getLogger, Formatter, FileHandler

class Log():
    def __init__(self, name=None, verbose=None, path=None):
        """ """
        self.name = name
        self.verbose = verbose
        self.path = path
        self.logger = self.set_logger()

    def set_logger(self):
        """Custom logging"""
        logger = getLogger(self.name)
        logger.propagate = False

        if self.verbose:
            console = ("%(asctime)s %(levelname)s "
                       "[%(name)s.%(funcName)s:%(lineno)d] %(message)s")
        else:
            console = ("%(asctime)s %(levelname)s %(message)s")

        # set logging formatter
        formatter = Formatter(console, datefmt='%Y-%m-%d %H:%M:%S')

        # save to file
        if self.path:
            handler = FileHandler(self.path)
            handler.setFormatter(formatter)
            logger.handlers[:] = [handler]

        if self.verbose is None:
            logger.setLevel(INFO)
            return logger

        if self.verbose is True or 'True' in self.verbose:
            logger.setLevel(DEBUG)
        else:
            logger.setLevel(INFO)

        return logger
