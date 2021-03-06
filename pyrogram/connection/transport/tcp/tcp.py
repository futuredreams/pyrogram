# Pyrogram - Telegram MTProto API Client Library for Python
# Copyright (C) 2017 Dan Tès <https://github.com/delivrance>
#
# This file is part of Pyrogram.
#
# Pyrogram is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pyrogram is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

import logging
import socket

log = logging.getLogger(__name__)


class TCP(socket.socket):
    def __init__(self):
        super().__init__()

    def send(self, *args):
        pass

    def recv(self, *args):
        pass

    def close(self):
        try:
            self.shutdown(socket.SHUT_RDWR)
        except OSError:
            pass
        finally:
            super().close()

    def recvall(self, length: int) -> bytes or None:
        data = b""

        while len(data) < length:
            try:
                packet = super().recv(length - len(data))
            except OSError:
                return None
            else:
                if packet:
                    data += packet
                else:
                    return None

        return data
