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


# import tkfmodels as tkfm
import tkfviews as tkfv
from PIL import Image
from enum import Enum  # Required by ImageFromats
from imghdr import what  # Required by _is_mage_format_supported()


# =============================================================================
# Global constants
# =============================================================================


# =============================================================================
# Utility classes and functions
# =============================================================================

class ImageFormats(Enum):
    """Class to wrap up enumerated values that define supoported image formats.
    """

    png = 'png'
    tiff = 'tiff'


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


def formulate_action(Action, **kwargs):
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

        # Define all models.
        self.model = None

        # Initialize views.
        self._mainscreen = tkfv.TkiAppMainWindow(controller=self)

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
        dataimage = Image.open(self._filelist[0])

        if self._filelist[1] is not None:
            # We have proper preiradiated image file. Load it too.
            controlimage = Image.open(self._filelist[1])

        else:
            controlimage = None

        # Print some info to the command line.
        print('{0}: Starting GUI ...'.format(self._programName))
        print(self._filelist)

        # Initialize all models.

        # We have all neccessary files. Start the GUI.
        self._mainscreen.title(self._programName)
        self._mainscreen.update()  # Update screen.
        self._mainscreen.mainloop()

        # Print to command line that we are freeing memory and closing app.
        print('{0}: Freeing allocated memory ...'.format(self._programName))

        # Do the cleanup and exit application.
        dataimage.close()

        if controlimage is not None:
            controlimage.close()

        self._exit_app()
