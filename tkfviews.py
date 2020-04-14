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
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
# from matplotlib import (cbook, use)
from matplotlib import use
from tkfutils import (
        MIN_FLOAT,
        MAX_FLOAT,
        Message,
        ImageColorMode,
        checktype,
        points_to_centimeters
    )
from matplotlib.backends.backend_tkagg import (
        FigureCanvasTkAgg,
        NavigationToolbar2Tk
    )

use("TkAgg")
plt.style.use('bmh')


# from matplotlib.backend_bases import MouseButton
# from matplotlib.widgets import RectangleSelector


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

    def __init__(self, canvas, window):
        # Pass initialization to the superclass.
        super().__init__(canvas, window)

    def mouse_move(self, event):
        self._set_cursor(event)
        # We don't want any position message in the toolbar.
        self.set_message('')


class FilmView(tki.Frame):
    """ Custom widget base class for displaying film image.
    """

    def __init__(self, *args, **kwargs):

        # Pass the rest of initialization to the superclass.
        tki.Frame.__init__(self, *args, **kwargs)

        # Initialize the figure.
        self._figure = plt.Figure()
        FigureCanvasTkAgg(self._figure, self)
        self._figure.canvas.get_tk_widget().pack(fill=tki.BOTH, expand=True)
        self._figure.canvas.draw()

        # Initialize axes.
        self._axes = self._figure.add_subplot(111)

        # Add toolbar to each view so user can zoom, take screenshots, etc.
        self._toolbar = GKFilmQANavigationToolbar(
                self._figure.canvas,
                self,
            )
        self._toolbar.pack_propagate(0)

        # Update toolbar display.
        self._toolbar.update()

    def _update(self, qafilm):

        # First clear axes.
        self._axes.clear()

        title = None
        cmap = None

        # Set partial title and colormode.
        colormodes = {
                ImageColorMode.fullcolor: 'Fullcolor image',
                ImageColorMode.grayscale: 'Grayscale image',
                ImageColorMode.red: 'Red channel',
                ImageColorMode.green: 'Green channel',
                ImageColorMode.blue: 'Blue channel'
            }

        title = colormodes[qafilm.colormode]
        if 'Fullcolor image' != title:
            cmap = cm.gray

        # Set default axes units.
        units_str = '[px]'

        # Try to set proper scale for axes (in centimeters), if dpi data
        # supplied and the full title.
        if qafilm.image_dpi:
            units_str = '[cm]'
            title = '{0} [dpi: {1}]'.format(title, qafilm.image_dpi)

            ticks_x = ticker.FuncFormatter(lambda x, pos: '{0:.2f}'.format(
                points_to_centimeters(qafilm.image_dpi[0], float(x))
                ))
            self._axes.xaxis.set_major_formatter(ticks_x)

            ticks_y = ticker.FuncFormatter(lambda y, pos: '{0:.2f}'.format(
                points_to_centimeters(qafilm.image_dpi[1], float(y))
                ))
            self._axes.yaxis.set_major_formatter(ticks_y)

        # Set title.
        self._axes.set_title(title)

        # Set units label.
        self._axes.set_xlabel(units_str)
        self._axes.set_ylabel(units_str)

        # Show plot.
        viewdata = qafilm.pixels_from_selection(qafilm.size)
        self._axes.imshow(viewdata, cmap=cmap)
        self._figure.canvas.draw()

        # Update superclass.
        tki.Tk.update(self)

    def update(self, qafilm):
        self._update(qafilm)


class AppControlsView(tki.Frame):
    """ Custom widget class for displaying and taking input from user
    controlls (e.g. fields, buttons, radiobuttonsw, etc.).
    """

    def __init__(self, *args, **kwargs):

        # Reference to a controller object must be passed as key-word agrument.
        # Controller object's class must implement dispatch method takeing
        # following arguments dispatch(sender, message, **kwargs).
        if 'controller' in kwargs:
            self.controller = kwargs.pop('controller')
            if not self.controller or not hasattr(self.controller, 'dispatch'):
                raise TypeError(
                        'Dispatch method not implemented by'
                        ' object\'s class ({0}).'
                        .format(type(self.controller))
                    )
        else:
            # No reference to controller object.
            self.controller = None

        # Reference to the root widget must be passed as key-word agrument.
        if 'mainwindow' in kwargs:
            self._mainwindow = kwargs.pop('mainwindow')
        else:
            # No reference to the root widget.
            self._mainwindow = None

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
        # Set some initial value.
        self._imagecolormode.set(ImageColorMode.fullcolor.value)

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

        if hasattr(self.master, 'dispatch'):
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

        if value and hasattr(self.master, 'dispatch'):
            self.controller.dispatch(self, Message.imgrt, angle=value)

    def _undo_image_rotation(self):
        """A callback method for "Undo rotation" control.
        """

        if hasattr(self.master, 'dispatch'):
            self.controller.dispatch(self, Message.unimgrt)

    @property
    def colormode(self):
        return self._imagecolormode.get()

    @property
    def lastrotation(self):
        return self._last_rotation.get()

    def change_colormode(self, mode):
        checktype(ImageColorMode, mode, 'Colormode')
        self._imagecolormode.set(mode.value)


class TkiAppMainWindow(tki.Tk):
    """ Application's main window class.
    """

    def __init__(self, *args, **kwargs):
        # Since objects instantiated from class are intended to be top level
        # widgets there is no reason to pass reference to master object.

        # Reference to a controller object must be passed as key-word agrument.
        # Controller object's class must implement dispatch method taking
        # following arguments dispatch(sender, message, **kwargs).

        if 'controller' in kwargs:
            self.controller = kwargs.pop('controller')
            if not self.controller or not hasattr(self.controller, 'dispatch'):
                raise TypeError(
                        'Dispatch method not implemented by'
                        ' object\'s class ({0}).'
                        .format(type(self.controller))
                    )
        else:
            # No reference to controller object.
            self.controller = None

        # Pass the rest of initialization to the superclass.
        tki.Tk.__init__(self, className='TkiAppMAinWindow')

        self.resizable(True, True)
        # self.resizable(False, False)

        # ======================================================================
        # Place your widgets here.
        # ======================================================================

        # Set up data view widgets and pack.
        self._qafilmview = FilmView(self)
        self._qafilmview.pack(side=tki.LEFT, fill=tki.Y)

        # Set up some space between test widgets and control widgets.
        ttk.Frame(self).pack(side=tki.LEFT, fill=tki.Y, expand=True)

        # Set up control widgets and pack.
        self._controlpanel = AppControlsView(
                self,
                controller=self,
                mainwindow=self
            )
        self._controlpanel.pack(side=tki.RIGHT, fill=tki.Y)

        # ======================================================================

    def _update(self, qafilm):
        """Method to update display of main window.
        """
        self._controlpanel.change_colormode(qafilm.colormode)
        self._qafilmview.update(qafilm)
        tki.Tk.update(self)

    def dispatch(self, sender, event, **kwargs):
        """A method to mediate messages between GUI objects and GUI objects
        and the controller.
        """

        # So far we send all messages to the controller.
        self.controller.dispatch(sender, event, **kwargs)

    def update(self, qafilm):
        self._update(qafilm)
