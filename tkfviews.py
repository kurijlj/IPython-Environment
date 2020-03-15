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
import tkinter.ttk as ttk


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

        # Reference to a controller object must be passed as key-word agrument.
        if 'controller' in kwargs:
            self._controller = kwargs.pop('controller')
        else:
            # No reference to controller object.
            self._controller = None

        # Pass initialization to superclass.
        tki.Frame.__init__(self, *args, **kwargs)

        self._view_username = tki.Label(self, text='Username', anchor='w')
        self._view_username.pack(side=tki.TOP, fill=tki.X)
        self._view_password = tki.Label(self, text='Password', anchor='w')
        self._view_password.pack(side=tki.TOP, fill=tki.X)
        self._view_firstname = tki.Label(self, text='First name', anchor='w')
        self._view_firstname.pack(side=tki.TOP, fill=tki.X)
        self._view_lastname = tki.Label(self, text='Last name', anchor='w')
        self._view_lastname.pack(side=tki.TOP, fill=tki.X)

    def model(self):
        model = None
        if self._controller and hasattr(self._controller, 'usermodel'):
            model = self._controller.usermodel
        return model

    def _update(self):
        model = self.model()
        if model:
            self._view_username['text'] = model.username
            self._view_password['text'] = model.password
            if model.firstname:
                self._view_firstname['text'] = model.firstname
            else:
                self._view_firstname['text'] = 'N/A'
            if model.lastname:
                self._view_lastname['text'] = model.lastname
            else:
                self._view_lastname['text'] = 'N/A'

    def update(self):
        self._update()
        tki.Frame.update(self)


class TkiAppMainWindow(tki.Tk):
    """ Application's main window.
    """

    def __init__(self, *args, **kwargs):

        tki.Tk.__init__(self, className='TkiAppMAinWindow')

        # Since objects instantiated from class are intended to be top level
        # widgets there is no reason to pass reference to master object.

        # Reference to a controller object must be passed as key-word agrument.
        if 'controller' in kwargs:
            self._controller = kwargs['controller']
        else:
            # No reference to controller object.
            self._controller = None

        self.resizable(True, True)
        # self.resizable(False, False)

        # Set up main frame with the label.
        main_panel_frame = ttk.LabelFrame(
                self,
                text='Main Widget Panel',
                borderwidth=3
                )

        # Pack top container widget.
        main_panel_frame.pack(side=tki.TOP, fill=tki.X, padx=2, pady=2)

        # ======================================================================
        # Place your widgets here.
        # ======================================================================

        self._userview = UserView(
            main_panel_frame,
            controller=self._controller
            )
        self._userview.pack(side=tki.TOP, fill=tki.X)

        # ======================================================================

        # Set up some space between test widgets and control widgets.
        ttk.Frame(main_panel_frame).pack(side=tki.TOP, fill=tki.Y, expand=True)

        # Set up control widgets and pack.
        ttk.Button(main_panel_frame, text='Quit', command=self.destroy)\
            .pack(side=tki.BOTTOM, fill=tki.X, padx=1, pady=1)

    def _update(self):
        """Method to update display of main window.
        """
        self._userview.update()

    def update(self):
        self._update()
        tki.Tk.update(self)
