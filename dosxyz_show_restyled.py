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
import egsdosetools as edt
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from enum import Enum
from matplotlib import (cbook, use)
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.colors import ListedColormap

use('TkAgg')


# =============================================================================
# Utility classes and functions
# =============================================================================

class DisplayPlane(Enum):
    """Class to wrap up enumerated values that describe plane of 3D space to
    be displayed.
    """

    xz = 0
    yz = 1
    xy = 2


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


def _is_phantom_file(filename):
    """Test if file is dosxyznrc phantom file, i.e. chechk if .egsphant
    suffix is present in the given filename.
    """

    ext = filename.split('.')[-1]

    if 'egsphant' == ext:
        return True
    else:
        return False


def _is_dose_file(filename):
    """Test if file is dosxyznrc dose file, i.e. chechk if .3ddose
    suffix is present in the given filename.
    """

    ext = filename.split('.')[-1]

    if '3ddose' == ext:
        return True
    else:
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
            filelist = (arguments.phantomfile, arguments.dosefile)
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

class DosXYZNavigationToolbar(NavigationToolbar2Tk):
    """
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


class SliceTracker(object):
    """
    """

    def __init__(self, figure, axes, phantomData, doseData, plane):
        self._figure = figure
        self._axes = axes
        self._phantomdata = phantomData
        self._dosedata = doseData
        self._plane = plane

        if DisplayPlane.xy == self._plane:
            self._slices = phantomData.shape[0]

        elif DisplayPlane.yz == self._plane:
            self._slices = phantomData.shape[1]

        else:
            self._slices = phantomData.shape[2]

        self._index = self._slices // 2

        if self._dosedata is None:
            self._showdosewash = False
            self._showdoselines = False
        else:
            self._showdosewash = True
            self._showdoselines = True

    @property
    def voxsdens(self):
        return self._phantomdata.voxelsdensity

    @property
    def voxsdens_min(self):
        return self._phantomdata.voxelsdensity.min()

    @property
    def voxsdens_max(self):
        return self._phantomdata.voxelsdensity.max()

    @property
    def dose(self):
        return (self._dosedata.dose / self._dosedata.dose.max()) * 100.0

    @property
    def dose_min(self):
        return (self._dosedata.dose.min() / self._dosedata.dose.max()) * 100.0

    @property
    def dose_max(self):
        return 100.0

    def toggle_dosewash(self):
        self._showdosewash = not self._showdosewash
        self._update()

    def toggle_doselines(self):
        self._showdoselines = not self._showdoselines

    def on_scroll(self, event):
        if event.button == 'up':
            self._index = (self._index + 1) % self._slices
        else:
            self._index = (self._index - 1) % self._slices
        self._update()

    def _update(self):
        self.on_update()

    def on_update(self):
        self._axes.clear()

        title = None
        density = None
        dose = None
        localdosemax = None

        if DisplayPlane.xy == self._plane:
            title = 'XY plane'
            density = self.voxsdens[self._index, :, :]
            if self._dosedata is not None and self._showdosewash:
                dose = self.dose[self._index, :, :]
                localdosemax = self.dose[self._index, :, :].max()

        elif DisplayPlane.yz == self._plane:
            title = 'YZ plane'
            density = self.voxsdens[:, self._index, :]
            if self._dosedata is not None and self._showdosewash:
                dose = self.dose[:, self._index, :]
                localdosemax = self.dose[:, self._index, :].max()

        else:
            title = 'XZ plane'
            density = self.voxsdens[:, :, self._index]
            if self._dosedata is not None and self._showdosewash:
                dose = self.dose[:, :, self._index]
                localdosemax = self.dose[:, :, self._index].max()

        self._axes.set_title(title)
        self._axes.set_xlabel('slice: {0}'.format(self._index))
        self._axes.imshow(
                density,
                cmap=cm.gray,
                vmin=self.voxsdens_min,
                vmax=self.voxsdens_max
            )

        if self._dosedata is not None and self._showdosewash:
            self._axes.imshow(
                    dose,
                    cmap=cm.jet,
                    interpolation="bilinear",
                    vmin=self.dose_min,
                    vmax=self.dose_max,
                    alpha=0.6)

            levels = np.arange(10.0, localdosemax, 10.0)
            if 0 != len(levels):
                contours = self._axes.contour(
                        dose,
                        levels,
                        linewidths=0.3,
                        cmap=cm.jet)
                self._axes.clabel(contours, levels, fmt='%3d %%')

        self._figure.canvas.draw()


class SliceView(object):
    """
    """

    def __init__(self, master):

        self._figure = plt.Figure(dpi=72)
        FigureCanvasTkAgg(self._figure, master)
        self._figure.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self._figure.canvas.draw()

        # Initialize axes.
        self._axes = self._figure.add_subplot(111)

        # Add toolbar to each view so user can zoom, take screenshots, etc.
        self._toolbar = DosXYZNavigationToolbar(
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

    def connect_tracker(self, tracker):
        # Enable tracker to respond to scroll events.
        self._figure.canvas.mpl_connect('scroll_event', tracker.on_scroll)


class DosXZYMainScreen(tk.Tk):
    """ A simple GUI application to show EGS phantom and 3ddose data.
    """

    def __init__(self, phantomData, doseData):

        tk.Tk.__init__(self, className='DosXZYMainScreen')

        # Set app icon, window title and make window nonresizable.
        # tk.Tk.iconbitmap(self, default='dosxyz_show.ico')
        self.title('dosxyz_show.py v1.1')
        self.resizable(False, False)

        viewframe = ttk.LabelFrame(self, text='View')

        topview = ttk.Frame(viewframe)
        xzframe = ttk.Frame(topview, borderwidth=3)
        xzframe.pack(side=tk.LEFT)
        yzframe = ttk.Frame(topview, borderwidth=3)
        yzframe.pack(side=tk.LEFT)
        topview.pack(side=tk.TOP, fill=tk.X)

        bottomview = ttk.Frame(viewframe)
        xyframe = ttk.Frame(bottomview, borderwidth=3)
        xyframe.pack(side=tk.LEFT)
        threedframe = ttk.Frame(bottomview, borderwidth=3)
        threedframe.pack(side=tk.LEFT, fill=tk.X)
        bottomview.pack(side=tk.TOP, fill=tk.X)

        self._xzview = SliceView(xzframe)
        self._yzview = SliceView(yzframe)
        self._xyview = SliceView(xyframe)

        self._xztracker = SliceTracker(
                self._xzview.figure,
                self._xzview.axes,
                phantomData,
                doseData,
                DisplayPlane.xz
            )
        self._yztracker = SliceTracker(
                self._yzview.figure,
                self._yzview.axes,
                phantomData,
                doseData,
                DisplayPlane.yz
            )
        self._xytracker = SliceTracker(
                self._xyview.figure,
                self._xyview.axes,
                phantomData,
                doseData,
                DisplayPlane.xy
            )

        self._xzview.connect_tracker(self._xztracker)
        self._yzview.connect_tracker(self._yztracker)
        self._xyview.connect_tracker(self._xytracker)
        viewframe.pack(side=tk.LEFT, fill=tk.Y)

        controlframe = ttk.LabelFrame(self, text='Controls')
        topcontrol = ttk.Frame(controlframe)
        # Set check buttons. If dose data is supplied, enable check buttons.
        state = 'disabled'
        if doseData:
            state = 'normal'
        ttk.Checkbutton(
                topcontrol,
                text='show dose',
                state=state,
                command=self.on_check_dosewash
            ).pack(side=tk.TOP, fill=tk.X)
        ttk.Checkbutton(
                topcontrol,
                text='show dose lines',
                state=state,
                command=self.on_check_doselines
            ).pack(side=tk.TOP, fill=tk.X)
        topcontrol.pack(side=tk.TOP, fill=tk.X)
        spacer = ttk.Frame(controlframe)
        spacer.pack(side=tk.TOP, fill=tk.Y, expand=True)

        # Set appllication "Quit" button.
        bottomcontrol = ttk.Frame(controlframe)
        ttk.Button(bottomcontrol, text='Quit', command=self.destroy)\
            .pack(side=tk.TOP, fill=tk.X)
        bottomcontrol.pack(side=tk.TOP, fill=tk.X)

        controlframe.pack(side=tk.LEFT, fill=tk.Y)

        # Update screen.
        self.update()

    def on_check_dosewash(self):
        self._xztracker.toggle_dosewash()
        self._yztracker.toggle_dosewash()
        self._xytracker.toggle_dosewash()

    def on_check_doselines(self):
        self._xztracker.toggle_doselines()
        self._yztracker.toggle_doselines()
        self._xytracker.toggle_doselines()

    def update(self):
        self._xztracker.on_update()
        self._yztracker.on_update()
        self._xytracker.on_update()


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
        # Set local variables first.
        phantomdata = None
        dosedata = None

        # Do some basic sanity checks first for the phantom file.
        if self._filelist[0] is None:
            print('{0}: Missing input phantom file.'.format(self._filelist[0]))
            self._exit_app()

        if not _is_phantom_file(self._filelist[0]):
            print(
                    '{0}: File \'{1}\' is not a proper phantom file.'
                    .format(self._programName, self._filelist[0])
                )

            self._exit_app()

        # We have a proper phantom file. Load the data.
        phantomdata = edt.xyzcls.PhantomFile(self._filelist[0])

        # Check if dose data provided.
        if self._filelist[1] is not None:
            if not _is_dose_file(self._filelist[1]):
                print(
                        '{0}: File \'{1}\' is not a proper dose file.'
                        .format(self._programName, self._filelist[1])
                    )

                self._exit_app()

            else:
                # We have proper dose file. Load it too.
                dosedata = edt.xyzcls.DoseFile(self._filelist[1])

                # Another sanity check. Number of segments along axes
                # for two files must coincide.
                if phantomdata.shape != dosedata.shape:
                    print('{0}: (ERROR) Number of segments for phantom data\
 and dose data must coincide!'.format(self._programName))
                    self._exit_app()

        # We have all neccessary files. Start the GUI.
        mainscreen = DosXZYMainScreen(
                phantomData=phantomdata,
                doseData=dosedata
            )
        mainscreen.mainloop()

        # Main screen is closed so exit the application.
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
            'phantomfile',
            metavar='PHANTOMFILE',
            type=str,
            help='dosxyznrc .egsphant file')
    program.add_argument(
            'dosefile',
            metavar='DOSEFILE',
            type=str,
            nargs='?',
            help='dosxyznrc .3ddose file')

    program.parse_args()
    program.run()
