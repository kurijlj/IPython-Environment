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
import tkfviews as tkfv


# =============================================================================
# Global constants
# =============================================================================


# =============================================================================
# Utility classes and functions
# =============================================================================


# =============================================================================
# GUI classes
# =============================================================================

class TkiAppMainWindow(tki.Tk):
    """ Application's main window.
    """

    def __init__(self, program_name):

        tki.Tk.__init__(self, className='TkiAppMAinWindow')

        self._program_name = program_name

        # Set app icon, window title and make window nonresizable.
        # tk.Tk.iconbitmap(self, default='dosxyz_show.ico')
        self.title(program_name)
        self.resizable(True, True)
        # self.resizable(False, False)

        # Set up main frame with the label.
        main_panel = ttk.LabelFrame(
                self,
                text='Main Widget Panel',
                borderwidth=3
                )

        # Pack top container widget.
        main_panel.pack(side=tki.TOP, fill=tki.X, padx=2, pady=2)

        # ======================================================================
        # Place your widgets here.
        # ======================================================================

        tkfv.UserView(main_panel).pack(side=tki.TOP, fill=tki.X)

        # ======================================================================

        # Set up some space between test widgets and control widgets.
        ttk.Frame(main_panel).pack(side=tki.TOP, fill=tki.Y, expand=True)

        # Set up control widgets and pack.
        ttk.Button(main_panel, text='Quit', command=self.destroy)\
            .pack(side=tki.BOTTOM, fill=tki.X, padx=1, pady=1)

        # Update display if necessary.
        self._update()

    def _update(self):
        """Method to update display of main window.
        """

        pass
