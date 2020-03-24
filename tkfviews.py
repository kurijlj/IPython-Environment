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
from matplotlib import (cbook, use)
from tkfutils import (
        MIN_FLOAT,
        MAX_FLOAT,
        Message,
        ImageColorMode,
        checktype,
        points_to_centimeters
    )
from matplotlib.backends.backend_tkagg import (
        # FigureCanvasTkAgg,
        NavigationToolbar2Tk
    )

use("TkAgg")


# =============================================================================
# View specific utility classes and functions
# =============================================================================


# =============================================================================
# View classes
# =============================================================================

class TkiInputFloat(tki.Frame):
    """ Custom widget to collect user input of float values.
    """

    def __init__(self, *args, **kwargs):

        # Following arguments we use locally and rest we send to superclass:
        #          label: Label for input field. Text displayed above
        #                 entry widget;
        #     buttontext: Text displayed on control button explaining
        #                 command to be executed;
        #    bottomlimit: Bottom limit of possible values that can be entered.
        #                 Default value is set to MIN_FLOAT;
        #       toplimit: Top limit of possible values that can be entered.
        #                 Default value is set to MAX_FLOAT;
        #        command: A callback method for pasing input values.
        #                 Default value is None.
        #       variable: Coupled tkinter variable of type DoubleVar used to
        #                 track enetred float values. Default value is set
        #                 to 0.0 .

        label = None
        buttontext = None

        if 'label' in kwargs:
            label = kwargs.pop('label')
        else:
            label = 'Float:'

        if 'buttontext' in kwargs:
            buttontext = kwargs.pop('buttontext')
        else:
            buttontext = 'Input'

        if 'bottomlimit' in kwargs:
            self._bottom = kwargs.pop('bottomlimit')
        else:
            self._bottom = MIN_FLOAT

        if 'toplimit' in kwargs:
            self._top = kwargs.pop('toplimit')
        else:
            self._top = MAX_FLOAT

        if 'command' in kwargs:
            self._command = kwargs.pop('command')
        else:
            self._command = None

        if 'variable' in kwargs:
            self._variable = kwargs.pop('variable')
            checktype(tki.DoubleVar, self._variable, 'Angle of rotation')
        else:
            self._variable = None

        # Pass the rest of arguments to superclass.
        tki.Frame.__init__(self, *args, **kwargs)

        # Initialize and arrange elemnts on the frame.
        tki.Label(self, text=label, anchor='w').pack(side=tki.TOP, fill=tki.X)

        # Frame to group and align entry field and command button.
        entry_group = ttk.Frame(self)

        # Set variable to keep track of input values.
        self._str_val = tki.StringVar()

        if self._variable:
            self._variable.set(0.0)

        tki.Entry(entry_group, width=12, textvariable=self._str_val)\
            .pack(side=tki.LEFT, fill=tki.Y, padx=1, pady=1)
        tki.Button(entry_group, text=buttontext, command=self._button_pressed)\
            .pack(side=tki.RIGHT, fill=tki.Y)
        entry_group.pack(side=tki.BOTTOM, fill=tki.X)

    def _button_pressed(self):
        val = 0.0

        # Try to convert string value to float.
        try:
            val = float(self._str_val.get())
        except ValueError:
            # We just ignore values that are not of float type.
            pass

        # We only accept values in range [self._bottom, self._top].
        if val < self._bottom or val > self._top:
            # Out of range so reset to initial value.
            val = 0.0

        if self._variable:
            self._variable.set(val)

        if self._command:
            self._command(val)

        # Reset entry value.
        self._str_val.set('')


class GKFilmQANavigationToolbar(NavigationToolbar2Tk):
    """ TODO: Add class description.
    """

    def __init__(self, canvas, window, image_dpi=None):
        self.canvas = canvas
        self.window = window
        self._image_dpi = image_dpi

        # Pass the rest of initialization to the superclass.
        super().__init__(canvas, window)

    def mouse_move(self, event):
        self._set_cursor(event)

        if event.inaxes and event.inaxes.get_navigate():

            try:
                xdata = event.xdata
                ydata = event.ydata
                x = int(xdata)
                y = int(ydata)

                if self._image_dpi:
                    xcm = points_to_centimeters(
                        self._image_dpi[0],
                        float(xdata)
                    )
                    ycm = points_to_centimeters(
                        self._image_dpi[1],
                        float(ydata)
                    )
                    s = 'x: {0:.2f} cm [{1:d} pxs], y: {2:.2f} cm [{3:d} pxs],\
 value: '.format(xcm, x, ycm, y)
                else:
                    s = 'x: {0:d}, y: {1:d}, value: '.format(x, y)
            except (ValueError, OverflowError):
                pass
            else:
                artists = [a for a in event.inaxes._mouseover_set
                           if a.contains(event) and a.get_visible()]

                if artists:
                    a = cbook._topmost_artist(artists)
                    if a is not event.inaxes.patch:
                        data = a.get_cursor_data(event)
                        if data is not None:
                            data_str = a.format_cursor_data(data)
                            if data_str is not None:
                                s = s + ' ' + data_str

                if len(self.mode):
                    self.set_message('%s, %s' % (self.mode, s))
                else:
                    self.set_message(s)
        else:
            self.set_message(self.mode)


class UserView(tki.Frame):
    """ A demo class representing Tk widget to view user data.
    """

    def __init__(self, *args, **kwargs):

        # Reference to a controller object must be passed as key-word agrument.
        if 'controller' in kwargs:
            self.controller = kwargs.pop('controller')
        else:
            # No reference to controller object.
            self.controller = None

        # Pass the rest of initialization to the superclass.
        tki.Frame.__init__(self, *args, **kwargs)

        # Set label frame to distinct main panel from the rest of the GUI.
        labelframe = ttk.LabelFrame(self, text='Main Panel')
        labelframe.pack(side=tki.RIGHT, fill=tki.Y, padx=5, pady=5)

        self._view_username = tki.Label(
                labelframe,
                text='Username',
                anchor='w'
            )
        self._view_username.pack(side=tki.TOP, fill=tki.X)
        self._view_password = tki.Label(
                labelframe,
                text='Password',
                anchor='w'
            )
        self._view_password.pack(side=tki.TOP, fill=tki.X)
        self._view_firstname = tki.Label(
                labelframe,
                text='First name',
                anchor='w'
            )
        self._view_firstname.pack(side=tki.TOP, fill=tki.X)
        self._view_lastname = tki.Label(
                labelframe,
                text='Last name',
                anchor='w'
            )
        self._view_lastname.pack(side=tki.TOP, fill=tki.X)

    def model(self):
        model = None
        if self.controller and hasattr(self.controller, 'usermodel'):
            model = self.controller.usermodel
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


class AppControlsView(tki.Frame):
    """ Custom widget class for displaying and taking input from user
    controlls (e.g. fields, buttons, radiobuttonsw, etc.).
    """

    def __init__(self, *args, **kwargs):

        # Reference to the root widget must be passed as key-word agrument.
        if 'mainwindow' in kwargs:
            self._mainwindow = kwargs.pop('mainwindow')
        else:
            # No reference to the root widget.
            self._mainwindow = None

        # Reference to a controller object must be passed as key-word agrument.
        if 'controller' in kwargs:
            self.controller = kwargs.pop('controller')
        else:
            # No reference to controller object.
            self.controller = None

        # Pass the rest of initialization to the superclass.
        tki.Frame.__init__(self, *args, **kwargs)

        # Set label frame to distinct control panel from the rest of the GUI.
        labelframe = ttk.LabelFrame(self, text='Control Panel')
        labelframe.pack(side=tki.RIGHT, fill=tki.Y, padx=5, pady=5)

        # Split control view into upper and lower half. Upper one is to hold
        # actual display controls, while lower one holds 'Quit' button only.
        top_frame = ttk.Frame(labelframe)
        top_frame.pack(side=tki.TOP, fill=tki.X, padx=5, pady=5)
        spacer = ttk.Frame(labelframe)
        spacer.pack(side=tki.TOP, fill=tki.Y, expand=True)
        bottom_frame = ttk.Frame(labelframe)
        bottom_frame.pack(side=tki.BOTTOM, fill=tki.X, padx=5, pady=5)

        # Set image color mode controls. First set parameter to keep track of
        # user selected color mode of displayed film image.
        self._imagecolormode = tki.StringVar()
        self._imagecolormode.set(ImageColorMode.fullcolor.value)
        self._select_mode()  # Send message to a controller.

        colormodes = {
                'fullcolor': ImageColorMode.fullcolor.value,
                'grayscale': ImageColorMode.grayscale.value,
                'red': ImageColorMode.red.value,
                'green': ImageColorMode.green.value,
                'blue': ImageColorMode.blue.value
            }

        for mode, value in colormodes.items():
            ttk.Radiobutton(
                    top_frame,
                    text=mode,
                    command=self._select_mode,
                    value=value,
                    variable=self._imagecolormode
                ).pack(side=tki.TOP, fill=tki.X)

        # Set image rotation control. First set parameter to keep track of
        # user inputed rotation angles of displayed film image.
        self._last_rotation = tki.DoubleVar()
        self._last_rotation.set(0.0)
        TkiInputFloat(
                top_frame,
                label='Image rotation:',
                buttontext='Rotate',
                bottomlimit=-359.0,
                toplimit=359.0,
                command=self._rotate_image,
                variable=self._last_rotation
            ).pack(side=tki.TOP, fill=tki.X)

        # Set undo button.
        ttk.Button(
                top_frame,
                text='Undo rotation',
                command=self._undo_image_rotation
            ).pack(side=tki.TOP, fill=tki.X)

        # Set appllication "Quit" button.
        destroycmd = None
        if self._mainwindow and hasattr(self._mainwindow, 'destroy'):
            destroycmd = self._mainwindow.destroy

        ttk.Button(bottom_frame, text='Quit', command=destroycmd)\
            .pack(side=tki.TOP, fill=tki.X)

    def _select_mode(self):
        """Method to be called when one of color mode selection buttons is
        checked. It invokes actual method that turns color mode display on/off.
        """

        if self.controller and hasattr(self.controller, 'dispatch'):
            colormodes = {
                    'fullcolor': ImageColorMode.fullcolor,
                    'grayscale': ImageColorMode.grayscale,
                    'R': ImageColorMode.red,
                    'G': ImageColorMode.green,
                    'B': ImageColorMode.blue
                }
            self.controller.dispatch(
                    self,
                    Message.cmchngd,
                    colormode=colormodes[self._imagecolormode.get()]
                )

    def _rotate_image(self, value):
        """A callback method for "Image rotation" control.
        """

        if value and self.controller and hasattr(self.controller, 'dispatch'):
            self.controller.dispatch(self, Message.imgrt, angle=value)

    def _undo_image_rotation(self):
        """A callback method for "Undo rotation" control.
        """

        if self.controller and hasattr(self.controller, 'dispatch'):
            self.controller.dispatch(self, Message.unimgrt)

    @property
    def colormode(self):
        return self._imagecolormode.get()

    @property
    def lastrotation(self):
        return self._last_rotation.get()


class TkiAppMainWindow(tki.Tk):
    """ Application's main window class.
    """

    def __init__(self, *args, **kwargs):

        # Pass the rest of initialization to the superclass.
        tki.Tk.__init__(self, className='TkiAppMAinWindow')

        # Since objects instantiated from class are intended to be top level
        # widgets there is no reason to pass reference to master object.

        # Reference to a controller object must be passed as key-word agrument.
        if 'controller' in kwargs:
            self.controller = kwargs['controller']
        else:
            # No reference to controller object.
            self.controller = None

        self.resizable(True, True)
        # self.resizable(False, False)

        # ======================================================================
        # Place your widgets here.
        # ======================================================================

        self._userview = UserView(
                self,
                controller=self.controller
            )
        self._userview.pack(side=tki.LEFT, fill=tki.Y)

        # ======================================================================

        # Set up some space between test widgets and control widgets.
        ttk.Frame(self)\
            .pack(side=tki.LEFT, fill=tki.X, expand=True)

        # Set up control widgets and pack.
        self._controlpanel = AppControlsView(
                self,
                mainwindow=self,
                controller=self.controller
            )
        self._controlpanel.pack(side=tki.RIGHT, fill=tki.Y)

    def _update(self):
        """Method to update display of main window.
        """
        self._userview.update()

    def update(self):
        self._update()
        tki.Tk.update(self)
