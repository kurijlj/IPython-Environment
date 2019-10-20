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


import argparse
import numpy as np
import tkinter as tk
import tkinter.ttk as ttk
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from PIL import Image
from enum import Enum
from imghdr import what
from os.path import basename
from matplotlib import (cbook, use)
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

use("TkAgg")
plt.style.use('bmh')


# =============================================================================
# Global constants
# =============================================================================

# Centimeters per inch.
CM_PER_IN = 2.54


# =============================================================================
# Utility classes and functions
# =============================================================================

class ImageFormats(Enum):
    """Class to wrap up enumerated values that define supoported image formats.
    """

    png = 'png'
    tiff = 'tiff'


class DisplayData(Enum):
    """Class to wrap up enumerated values that describe what image data to
    be displayed.
    """

    original = 0
    red = 1
    green = 2
    blue = 3


class ProgramAction(object):
    """Abstract base class for all program actions, that provides execute.

    The execute method contains code that will actually be executed after
    arguments parsing is finished. The method is called from within method
    run of the CommandLineApp instance.
    """

    def __init__(self, exitf):
        self._exit_app = exitf

    def execute(self):
        pass


def _format_epilog(epilogAddition, bugMail):
    """Formatter for generating help epilogue text. Help epilogue text is an
    additional description of the program that is displayed after the
    description of the arguments. Usually it consists only of line informing
    to which email address to report bugs to, or it can be completely
    omitted.

    Depending on provided parameters function will properly format epilogue
    text and return string containing formatted text. If none of the
    parameters are supplied the function will return None which is default
    value for epilog parameter when constructing parser object.
    """

    fmtMail = None
    fmtEpilog = None

    if epilogAddition is None and bugMail is None:
        return None

    if bugMail is not None:
        fmtMail = 'Report bugs to <{bugMail}>.'\
            .format(bugMail=bugMail)
    else:
        fmtMail = None

    if epilogAddition is None:
        fmtEpilog = fmtMail

    elif fmtMail is None:
        fmtEpilog = epilogAddition

    else:
        fmtEpilog = '{addition}\n\n{mail}'\
            .format(addition=epilogAddition, mail=fmtMail)

    return fmtEpilog


def _formulate_action(Action, **kwargs):
    """Factory method to create and return proper action object.
    """

    return Action(**kwargs)


def _is_image_format_supported(filename):
    """Test if file is one of the image formats supported by application.
    Supported image formats are defined by enumerated class ImageFormats at the
    beginning of this script.
    """

    image_type = what(filename)

    if image_type:
        try:
            ImageFormats(image_type)
            return True
        except ValueError:
            # We just want to stop exception to propagate further up. Nothing
            # to do here actually, so we just pass.
            pass

    return False


# =============================================================================
# Command line app class
# =============================================================================

class CommandLineApp(object):
    """Actual command line app object containing all relevant application
    information (NAME, VERSION, DESCRIPTION, ...) and which instantiates
    action that will be executed depending on the user input from
    command line.
    """

    def __init__(
            self,
            programName=None,
            programDescription=None,
            programLicense=None,
            versionString=None,
            yearString=None,
            authorName=None,
            authorMail=None,
            epilog=None):

        self.programLicense = programLicense
        self.versionString = versionString
        self.yearString = yearString
        self.authorName = authorName
        self.authorMail = authorMail

        fmtEpilog = _format_epilog(epilog, authorMail)

        self._parser = argparse.ArgumentParser(
                prog=programName,
                description=programDescription,
                epilog=fmtEpilog,
                formatter_class=argparse.RawDescriptionHelpFormatter
            )

        # Since we add argument options to groups by calling group
        # method add_argument, we have to sore all that group objects
        # somewhere before adding arguments. Since we want to store all
        # application relevant data in our application object we use
        # this list for that purpose.
        self._argumentGroups = []

    @property
    def programName(self):
        """Utility function that makes accessing program name attribute
        neat and hides implementation details.
        """
        return self._parser.prog

    @property
    def programDescription(self):
        """Utility function that makes accessing program description
        attribute neat and hides implementation details.
        """
        return self._parser.description

    def add_argument_group(self, title=None, description=None):
        """Adds an argument group to application object.
        At least group title must be provided or method will rise
        NameError exception. This is to prevent creation of titleless
        and descriptionless argument groups. Although this is allowed bu
        argparse module I don't see any use of a such utility."""

        if title is None:
            raise NameError('Missing arguments group title.')

        group = self._parser.add_argument_group(title, description)
        self._argumentGroups.append(group)

        return group

    def _group_by_title(self, title):
        group = None

        for item in self._argumentGroups:
            if title == item.title:
                group = item
                break

        return group

    def add_argument(self, *args, **kwargs):
        """Wrapper for add_argument methods of argparse module. If
        parameter group is supplied with valid group name, argument will
        be added to that group. If group parameter is omitted argument
        will be added to parser object. In a case of invalid group name
        it rises ValueError exception.
        """

        if 'group' not in kwargs or kwargs['group'] is None:
            self._parser.add_argument(*args, **kwargs)

        else:
            group = self._group_by_title(kwargs['group'])

            if group is None:
                raise ValueError(
                        'Trying to reference nonexisten argument group.'
                    )

            else:
                kwargsr = {k: kwargs[k] for k in kwargs.keys() if 'group' != k}
                group.add_argument(*args, **kwargsr)

    def parse_args(self, args=None, namespace=None):
        """Wrapper for parse_args method of a parser object. It also
        instantiates action object that will be executed based on a
        input from command line.
        """

        arguments = self._parser.parse_args(args, namespace)

        if arguments.usage:
            self._action = _formulate_action(
                ProgramUsageAction,
                parser=self._parser,
                exitf=self._parser.exit)

        elif arguments.version:
            self._action = _formulate_action(
                ShowVersionAction,
                prog=self._parser.prog,
                ver=self.versionString,
                year=self.yearString,
                author=self.authorName,
                license=self.programLicense,
                exitf=self._parser.exit)

        else:
            filelist = (arguments.iradimage, arguments.preiradimage)
            self._action = _formulate_action(
                DefaultAction,
                prog=self._parser.prog,
                exitf=self._parser.exit,
                filelist=filelist)

    def run(self):
        """This method executes action code.
        """

        self._action.execute()


# =============================================================================
# GUI classes
# =============================================================================

class GKFilmQANavigationToolbar(NavigationToolbar2Tk):
    """ TODO: Add class description.
    """

    def __init__(self, canvas, window):
        self.canvas = canvas
        self.window = window
        NavigationToolbar2Tk.__init__(self, canvas, window)

    def mouse_move(self, event):
        self._set_cursor(event)

        if event.inaxes and event.inaxes.get_navigate():

            try:
                s = 'x:{0:d} y:{1:d}'.format(
                        int(event.xdata),
                        int(event.ydata)
                    )
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


class ImageRenderer(object):
    """ A class that actually does the drawing of the image view.
    """

    def __init__(self, figure, axes, imagedata, what):
        self._figure = figure
        self._axes = axes
        self._imagedata = imagedata
        self._what = what

    def _update(self):
        self._axes.clear()

        title = None
        cmap = None
        displaydata = None

        if DisplayData.red == self._what:
            title = 'Red channel'
            cmap = cm.gray
            displaydata = np.asarray(self._imagedata.getchannel('R'))

        elif DisplayData.green == self._what:
            title = 'Green channel'
            cmap = cm.gray
            displaydata = np.asarray(self._imagedata.getchannel('G'))

        elif DisplayData.blue == self._what:
            title = 'Blue channel'
            cmap = cm.gray
            displaydata = np.asarray(self._imagedata.getchannel('B'))

        else:
            title = 'Original'
            displaydata = self._imagedata

        self._axes.set_title(title)
        self._axes.imshow(
                displaydata,
                cmap=cmap
            )

        self._figure.canvas.draw()

    def on_update(self):
        self._update()


class ImageView(object):
    """ A class used to hold and keep track of figure responsible for image
    display and canvas that figure is drawn on.
    """

    def __init__(self, master):

        # self._figure = plt.Figure(dpi=72)
        self._figure = plt.Figure()
        FigureCanvasTkAgg(self._figure, master)
        self._figure.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self._figure.canvas.draw()

        # Initialize axes.
        self._axes = self._figure.add_subplot(111)

        # Add toolbar to each view so user can zoom, take screenshots, etc.
        self._toolbar = GKFilmQANavigationToolbar(
                self._figure.canvas,
                master
            )

        # Update toolbar display.
        self._toolbar.update()

    @property
    def figure(self):
        return self._figure

    @property
    def axes(self):
        return self._axes


class GKFilmQAMainScreen(tk.Tk):
    """ Application's main screen.
    """

    def __init__(self, program_name, iraddata, preiraddata):

        tk.Tk.__init__(self, className='GKFilmQAMainScreen')

        self._program_name = program_name

        # Set app icon, window title and make window nonresizable.
        # tk.Tk.iconbitmap(self, default='dosxyz_show.ico')
        self.title(basename(iraddata.filename))
        # self.resizable(False, False)
        self.resizable(False, False)

        # Split top frame into two main frames. One for displaying image
        # and other for controling display options.

        # Set up view frame.
        viewframe = ttk.LabelFrame(self, text='View')
        view = ttk.Frame(viewframe, borderwidth=3)
        view.pack(side=tk.TOP, fill=tk.X)
        viewframe.pack(side=tk.LEFT, fill=tk.Y)

        # Print some info to the command line.
        print('{0}: Loading image data ...'.format(self._program_name))

        # Connect view manager for the image frame.
        self._imageview = ImageView(view)
        self._imagerenderer = ImageRenderer(
                self._imageview.figure,
                self._imageview.axes,
                iraddata,
                DisplayData.original
            )

        # Set up control frame.
        controlframe = ttk.LabelFrame(self, text='Controls')

        # Split control frame into upper and lower half. Upper one is to hold
        # actual display controls, while lower one holds 'Quit' button only.
        topcontrol = ttk.Frame(controlframe)

        # Set channel selection controls.
        self._current_view = tk.IntVar()

        self._btnoriginal = ttk.Radiobutton(
                topcontrol,
                text='Original image',
                command=self._on_select_channel,
                value=DisplayData.original.value,
                variable=self._current_view
            )
        self._btnoriginal.pack(side=tk.TOP, fill=tk.X)

        self._btnred = ttk.Radiobutton(
                topcontrol,
                text='Red channel',
                command=self._on_select_channel,
                value=DisplayData.red.value,
                variable=self._current_view
            )
        self._btnred.pack(side=tk.TOP, fill=tk.X)

        self._btngreen = ttk.Radiobutton(
                topcontrol,
                text='Green channel',
                command=self._on_select_channel,
                value=DisplayData.green.value,
                variable=self._current_view
            )
        self._btngreen.pack(side=tk.TOP, fill=tk.X)

        self._btnblue = ttk.Radiobutton(
                topcontrol,
                text='Blue channel',
                command=self._on_select_channel,
                value=DisplayData.blue.value,
                variable=self._current_view
            )
        self._btnblue.pack(side=tk.TOP, fill=tk.X)

        # Set default channel.
        self._current_view.set(DisplayData.original.value)

        topcontrol.pack(side=tk.TOP, fill=tk.X)
        spacer = ttk.Frame(controlframe)
        spacer.pack(side=tk.TOP, fill=tk.Y, expand=True)

        # Set appllication "Quit" button.
        bottomcontrol = ttk.Frame(controlframe)
        ttk.Button(bottomcontrol, text='Quit', command=self.destroy)\
            .pack(side=tk.TOP, fill=tk.X)
        bottomcontrol.pack(side=tk.BOTTOM, fill=tk.X)

        controlframe.pack(side=tk.RIGHT, fill=tk.Y)

        # Update display.
        self.update()

    def _on_select_channel(self):
        """Method to be called when one of channel selection buttons is
        checked. It invokes actual method that turns channel display on/off.
        """

        what = None

        if DisplayData.red.value == self._current_view.get():
            what = 'Red channel.'
        elif DisplayData.green.value == self._current_view.get():
            what = 'Green channel.'
        elif DisplayData.blue.value == self._current_view.get():
            what = 'Blue channel.'
        else:
            what = 'Original image.'

        print('{0}: {1}'.format(self._program_name, what))
        # self._imagerenderer.toggle_channel(what)

    def update(self):
        """Method to update diplay of main screen.
        """
        self._imagerenderer.on_update()


# =============================================================================
# App action classes
# =============================================================================

class ProgramUsageAction(ProgramAction):
    """Program action that formats and displays usage message to the stdout.
    """

    def __init__(self, parser, exitf):
        self._usageMessage = \
                '{usage}Try \'{prog} --help\' for more information.'\
                .format(usage=parser.format_usage(), prog=parser.prog)
        self._exit_app = exitf

    def execute(self):
        print(self._usageMessage)
        self._exit_app()


class ShowVersionAction(ProgramAction):
    """Program action that formats and displays program version information
    to the stdout.
    """

    def __init__(self, prog, ver, year, author, license, exitf):
        self._versionMessage = \
                '{0} {1} Copyright (C) {2} {3}\n{4}'\
                .format(prog, ver, year, author, license)
        self._exit_app = exitf

    def execute(self):
        print(self._versionMessage)
        self._exit_app()


class DefaultAction(ProgramAction):
    """Program action that wraps some specific code to be executed based on
    command line input. In this particular case it prints simple message
    to the stdout.
    """

    def __init__(self, prog, exitf, filelist):
        self._programName = prog
        self._exit_app = exitf
        self._filelist = filelist

    def execute(self):
        # Do some basic sanity checks first.
        if self._filelist[0] is None:
            print('{0}: Missing image file.'
                  .format(self._programName))
            self._exit_app()

        if not _is_image_format_supported(self._filelist[0]):
            print(
                    '{0}: File \'{1}\' is not of supported image format.'
                    .format(self._programName, self._filelist[0])
                )

            self._exit_app()

        if self._filelist[1] is not None:
            if not _is_image_format_supported(self._filelist[1]):
                print(
                        '{0}: File \'{1}\' is not of supported image format.'
                        .format(self._programName, self._filelist[1])
                    )

                self._exit_app()

        # We have a proper iradiated image file. Load the image data.
        iraddata = Image.open(self._filelist[0])
        # print('Image file: {0}'.format(iraddata.filename))
        # print('Image format: {0}'.format(iraddata.format))
        # print('Image mode: {0}'.format(iraddata.mode))
        # print('Resolution (dpi): {0} x {1}'.format(
        #     iraddata.info['dpi'][0],
        #     iraddata.info['dpi'][1]
        #     ))
        # print('Image size (px): {0} x {1}'.format(
        #     iraddata.width,
        #     iraddata.height
        #     ))
        # print('Image size (cm): {0} x {1}'.format(
        #     (iraddata.width / iraddata.info['dpi'][0]) * CM_PER_IN,
        #     (iraddata.height / iraddata.info['dpi'][1]) * CM_PER_IN,
        #     ))
        # print()

        if self._filelist[1] is not None:
            # We have proper preiradiated image file. Load it too.
            preiraddata = Image.open(self._filelist[1])

        else:
            preiraddata = None

        # Print some info to the command line.
        print('{0}: Starting GUI ...'.format(self._programName))

        # We have all neccessary files. Start the GUI.
        mainscreen = GKFilmQAMainScreen(
                program_name=self._programName,
                iraddata=iraddata,
                preiraddata=preiraddata
            )
        mainscreen.mainloop()

        # Print to command line that we are freeing memory and closing app.
        print('{0}: Freeing allocated memory ...'.format(self._programName))

        # Do the cleanup and exit application.
        iraddata.close()

        if preiraddata is not None:
            preiraddata.close()

        self._exit_app()


# =============================================================================
# Script main body
# =============================================================================

if __name__ == '__main__':

    description = 'Framework for application development \
implementing argp option parsing engine.\n\n\
Mandatory arguments to long options are mandatory for \
short options too.'
    license = 'License GPLv3+: GNU GPL version 3 or later \
<http://gnu.org/licenses/gpl.html>\n\
This is free software: you are free to change and \
redistribute it.\n\
There is NO WARRANTY, to the extent permitted by law.'

    program = CommandLineApp(
        programDescription=description.replace('\t', ''),
        programLicense=license.replace('\t', ''),
        versionString='i.i',
        yearString='yyyy',
        authorName='Author Name',
        authorMail='author@mail.com',
        epilog=None)

    program.add_argument_group('general options')
    program.add_argument(
            '-V',
            '--version',
            action='store_true',
            help='print program version',
            group='general options')
    program.add_argument(
            '--usage',
            action='store_true',
            help='give a short usage message')
    program.add_argument(
            'iradimage',
            metavar='IRADIMAGE',
            type=str,
            nargs='?',
            help='image of a scanned iradiated gafchromic film')
    program.add_argument(
            'preiradimage',
            metavar='PREIRADIMAGE',
            type=str,
            nargs='?',
            help='image of a scanned gafchromic film pre irradiation')

    program.parse_args()
    program.run()
