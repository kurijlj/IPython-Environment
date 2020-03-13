#!/usr/bin/env python3
# =============================================================================
# <one line to give the program's name and a brief idea of what it does.>
#
#  Copyright (C) <yyyy> <Author Name> <author@mail.com>
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option)
# any later version.
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.
#
# =============================================================================


# =============================================================================
#
# <Put documentation here>
#
# <yyyy>-<mm>-<dd> <Author Name> <author@mail.com>
#
# * <programfilename>.py: created.
#
# =============================================================================


import tkinter as tki


# =============================================================================
# Utility classes and functions
# =============================================================================


# =============================================================================
# View classes
# =============================================================================

class UserView(tki.Frame):
    """ A demo class representing Tk widget to view user data.
    """

    def __init__(self, *args, **kwargs):
        # Pass initialization to superclass.
        tki.Frame.__init__(self, *args, **kwargs)
        self._view_username = tki.Label(self, text='Username', anchor='w').\
            pack(side=tki.TOP, fill=tki.X)
        self._view_password = tki.Label(self, text='Password', anchor='w').\
            pack(side=tki.TOP, fill=tki.X)
        self._view_firstname = tki.Label(self, text='First name', anchor='w').\
            pack(side=tki.TOP, fill=tki.X)
        self._view_lastname = tki.Label(self, text='Last name', anchor='w').\
            pack(side=tki.TOP, fill=tki.X)

        self._update()

    def _update(self):
        pass

    def update(self):
        self._update()
