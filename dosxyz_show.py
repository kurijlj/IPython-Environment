#!/usr/bin/env python
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
import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg
from matplotlib.figure import Figure

matplotlib.use("TkAgg")


# =============================================================================
# Utility classes and functions
# =============================================================================

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

    fmtAdition = None
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

class DosXYZShowGui(tk.Tk):
    """ A simple GUI application to show EGS phantom and 3ddose data.
    """

    def __init__(self, *args, **kwargs):

        x = kwargs.pop('dmslicesw', None)
        y = kwargs.pop('dmslicesh', None)
        p = kwargs.pop('dm3dw', None)
        q = kwargs.pop('dm3dh', None)
        bgsl = kwargs.pop('slviewbg', None)
        bg3d = kwargs.pop('view3dbg', None)

        if x is None:
            x = 200
        if y is None:
            y = 300
        if p is None:
            p = 500
        if q is None:
            q = 500
        if bgsl is None:
            bgsl = 'black'
        if bg3d is None:
            bg3d = 'black'

        self.sliceshape = (x, y)
        self.v3dshape = (p, q)
        self.bgcolors = {}
        self.bgcolors['slview'] = bgsl
        self.bgcolors['view3d'] = bg3d

        tk.Tk.__init__(self, *args, **kwargs)

        # Set app icon and window title.
        # tk.Tk.iconbitmap(self, default='dosxyz_show.ico')
        tk.Tk.wm_title(self, 'dosxyz_show.py')

        # Set viewframe and frame with all commands.
        self.viewframe = tk.Frame(self)
        self.viewframe.pack(side=tk.TOP)
        self.commandframe = tk.Frame(self)
        self.commandframe.pack(side=tk.BOTTOM)

        # Set slices view frame and 3D view frame.
        self.sliceframe = tk.Frame(self.viewframe)
        self.sliceframe.pack(side=tk.LEFT)
        self.frame3d = tk.Frame(self.viewframe)
        self.frame3d.pack(side=tk.RIGHT)

        # Set each of slices frames.
        self.frameXZ = tk.Frame(self.sliceframe)
        self.frameXZ.pack()
        self.frameYZ = tk.Frame(self.sliceframe)
        self.frameYZ.pack(side=tk.BOTTOM)
        self.frameXY = tk.Frame(self.sliceframe)
        self.frameXY.pack(side=tk.BOTTOM)

        # Set commands
        button = tk.Button(
                self.commandframe,
                text='Quit',
                command=self.destroy
            )
        button.pack()

        fig = plt.figure()
        canvas = FigureCanvasTkAgg(fig, master=self.frameXZ)
        toolbar = NavigationToolbar2TkAgg(canvas, self.frameXZ)


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
            print('{0}: Missing input phantom file.'.format(self._filelist[0]))
            self._exit_app()

        if not _is_phantom_file(self._filelist[0]):
            print(
                    '{0}: File \'{1}\' is not proper phantom file.'
                    .format(self._programName, self._filelist[0])
                )

            self._exit_app()

        if self._filelist[1] is not None:
            if not _is_dose_file(self._filelist[1]):
                print(
                        '{0}: File \'{1}\' is not proper dose file.'
                        .format(self._programName, self._filelist[1])
                    )

                self._exit_app()

        print(
                '{0}: Phantom file is \'{1}\''
                .format(self._programName, self._filelist[0])
            )

        if self._filelist[1] is not None:
            print(
                    '{0}: Phantom file is \'{1}\'.'
                    .format(self._programName, self._filelist[1])
                )

        gui = DosXYZShowGui()
        gui.mainloop()
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
