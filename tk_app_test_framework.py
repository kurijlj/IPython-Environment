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
import tkinter as tk
import tkinter.ttk as ttk
from sys import float_info as fi
# from os.path import basename


# =============================================================================
# Global constants
# =============================================================================

MIN_FLOAT = fi.min
MAX_FLOAT = fi.max


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
            self._action = _formulate_action(
                DefaultAction,
                prog=self._parser.prog,
                exitf=self._parser.exit
                )

    def run(self):
        """This method executes action code.
        """

        self._action.execute()


# =============================================================================
# GUI classes
# =============================================================================

class TkInputFloat(tk.Frame):
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

        # Pass the rest of arguments to superclass.
        # tk.Frame.__init__(self, kwargs, className='TkInputFloat')
        tk.Frame.__init__(self, *args, **kwargs)

        # Initialize and arrange elemnts on the frame.
        tk.Label(self, text=label, anchor='w').pack(side=tk.TOP, fill=tk.X)

        # Frame to group and align entry field and command button.
        entry_group = ttk.Frame(self)

        # Set variable to keep track of input values.
        self._str_val = tk.StringVar()

        tk.Entry(entry_group, width=12, textvariable=self._str_val)\
            .pack(side=tk.LEFT, fill=tk.Y, padx=1, pady=1)
        tk.Button(entry_group, text=buttontext, command=self._button_pressed)\
            .pack(side=tk.RIGHT, fill=tk.Y)
        entry_group.pack(side=tk.BOTTOM, fill=tk.X)

    def _button_pressed(self):
        val = 0.0

        # Try to convert string value to float.
        try:
            val = float(self._str_val.get())
        except ValueError:
            # We just ignore values that are not of float type.
            pass

        # We only accept values in range [self._bottom, self._top].
        if self._command:
            if val < self._bottom or val > self._top:
                # Out of range so rest to initial value.
                val = 0.0

            self._command(val)

        # Reset entry value.
        self._str_val.set('')


class TkAppMainScreen(tk.Tk):
    """ Application's main screen.
    """

    def __init__(self, program_name):

        tk.Tk.__init__(self, className='GKFilmQAMainScreen')

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

        # ========================
        # Place your widgets here.
        # ========================

        # Set up rotation control.
        rotation_control = ttk.Frame(main_panel)
        tk.Label(rotation_control, text='Image rotation:', anchor='w')\
            .pack(side=tk.TOP, fill=tk.X)

        # Frame to group and align entry field and command button.
        rc_entry_group = ttk.Frame(rotation_control)

        self._rotation_angle = tk.StringVar()

        tk.Entry(rc_entry_group, width=12, textvariable=self._rotation_angle)\
            .pack(side=tk.LEFT, fill=tk.Y, padx=1, pady=1)
        tk.Button(rc_entry_group, text='Rotate', command=self._on_rotate)\
            .pack(side=tk.RIGHT, fill=tk.Y)
        rc_entry_group.pack(side=tk.BOTTOM, fill=tk.X)

        rotation_control.pack(side=tk.TOP, fill=tk.X)

        TkInputFloat(
            main_panel,
            label='Image rotation:',
            buttontext='Rotate',
            bottomlimit=-359.0,
            toplimit=359.0,
            command=self._rc_input
            ).pack(side=tk.TOP, fill=tk.X)

        # ========================

        # Set up some space between test widgets and control widgets.
        ttk.Frame(main_panel).pack(side=tk.TOP, fill=tk.Y, expand=True)

        # Set up control widgets and pack.
        ttk.Button(main_panel, text='Quit', command=self.destroy)\
            .pack(side=tk.TOP, fill=tk.X, padx=1, pady=1)

        # Pack top container widgets.
        main_panel.pack(side=tk.TOP, fill=tk.X, padx=2, pady=2)

        # Update display if necessary.
        # self.update()

    def _on_rotate(self):
        """A callback method for rotation_control.
        """

        # Define storage for input angle value.
        angle_val = 0.0

        # Try to convert string value to float.
        try:
            angle_val = float(self._rotation_angle.get())
        except ValueError:
            # We just ignore values that are not of float type.
            pass

        # Also discard ridicules float values.
        if angle_val > -360.0 and angle_val < 360.0 and 0 != angle_val:
            print(angle_val)
        else:
            print('No rotation')

        # Reset entry value.
        self._rotation_angle.set('')

    def _rc_input(self, angle):
        """A callback method for rc control.
        """

        if angle:
            print('Rotate by {0:.2f}.'.format(angle))
        else:
            print('No rotation.')

    def _update(self):
        """Method to update diplay of main screen.
        """

        pass


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

    def __init__(self, prog, exitf):
        self._programName = prog
        self._exit_app = exitf

    def execute(self):

        # Print some info to the command line.
        print('{0}: Starting GUI ...'.format(self._programName))

        # We have all neccessary files. Start the GUI.
        mainscreen = TkAppMainScreen(
                program_name=self._programName
                )
        mainscreen.mainloop()

        # Print to command line that we are freeing memory and closing app.
        print('{0}: Freeing allocated memory ...'.format(self._programName))

        # Do the cleanup and exit application.
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

    program.parse_args()
    program.run()
