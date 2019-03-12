# This file is a part of WTFIX.
#
# Copyright (C) 2018,2019 John Cass <john.cass77@gmail.com>
#
# WTFIX is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.
#
# WTFIX is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public
# License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from wtfix.apps.base import BaseApp
from wtfix.conf import settings


logger = settings.logger


class OutboundLoggingApp(BaseApp):
    """
    Logs outbound messages.
    """

    name = "outbound_logger"

    def on_send(self, message):
        logger.info(f" --> {message}")

        return message


class InboundLoggingApp(BaseApp):
    """
    Logs inbound messages.
    """

    name = "inbound_logger"

    def on_receive(self, message):
        logger.info(f" <-- {message}")

        return message