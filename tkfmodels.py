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


# =============================================================================
# Utility classes and functions
# =============================================================================

def _checktype(tp, var, vardsc):
    """ Utility routine used to check if given variable (var) is of requested
    type (tp). If not it raises TypeError exception with a appropriate message.
    """

    if var is not None and type(var) is not tp:
        raise TypeError('{0} must be {1} or NoneType, not {2}'.format(
            vardsc,
            tp.__name__,
            type(var).__name__
        ))


# =============================================================================
# Model classes
# =============================================================================

class User(object):
    """ A demo class representing user with general data about user.
    """

    def __init__(self, un='user', psswd='p4s5w0rd', fn=None, ln=None):
        self._username = un
        self._password = psswd
        self._firstname = fn
        self._lastname = ln

    def __repr__(self):
        str_type = type(self).__name__
        str_un = 'Username: {0}'.format(self._username)
        str_psswd = 'Password: {0}'.format(self._password)

        if self._firstname:
            str_fn = 'First Name: {0}'.format(self._firstname)
        else:
            str_fn = 'First Name: N/A'

        if self._lastname:
            str_ln = 'Last Name: {0}'.format(self._lastname)
        else:
            str_ln = 'Last Name: N/A'

        return str_type + '(\n' + str_un + ',\n' + str_psswd + ',\n' +\
            str_fn + ',\n' + str_ln + '\n)'

    def changepassword(self, pw):
        _checktype(str, pw, 'Password')
        self._password = pw

    def changefirstname(self, fn):
        _checktype(str, fn, 'First name')
        self._firstname = fn

    def changelastname(self, ln):
        _checktype(str, ln, 'Last name')
        self._lastname = ln

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def firstname(self):
        return self._firstname

    @property
    def lastname(self):
        return self._lastname
