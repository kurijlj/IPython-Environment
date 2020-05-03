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


import tkfviews as tkfv
import tkfmodels as models
from PIL import Image
from os.path import isfile
from tkfutils import (ImageColorMode, Message, is_image_format_supported)


# =============================================================================
# Actions specific global constants
# =============================================================================


# =============================================================================
# Actions specific utility classes and functions
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


def formulate_action(Action, **kwargs):
    """Factory method to create and return proper action object.
    """

    return Action(**kwargs)


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
        self.qafilmmodel = None

        # Initialize views.
        self._mainscreen = None

    def dispatch(self, sender, event, **kwargs):
        """A method to mediate messages between app objects.
        """

        if Message.cmchngd == event:
            if 'colormode' in kwargs:
                self.qafilmmodel.change_color_mode(kwargs['colormode'])
                self._mainscreen.update(self.qafilmmodel)  # Update screen.
            else:
                print('{0}: \'colormode\' parameter is missing.'
                      .format(self._programName))

        if Message.imgrt == event:
            if 'angle' in kwargs:
                self.qafilmmodel.rotate(kwargs['angle'])
                self._mainscreen.update(self.qafilmmodel)  # Update screen.
            else:
                print('{0}: \'angle\' parameter is missing.'
                      .format(self._programName))

        if Message.edgdet == event:
            if 'sigma' in kwargs and 'lowtr' in kwargs and 'hightr' in kwargs:
                print(kwargs['sigma'], kwargs['lowtr'], kwargs['hightr'])
                self.qafilmmodel.detect_edges(
                        kwargs['sigma'],
                        kwargs['lowtr'],
                        kwargs['hightr']
                    )
                self._mainscreen.update(self.qafilmmodel)  # Update screen.
            else:
                for par, label in {
                            kwargs['sigma']: 'sigma',
                            kwargs['lowtr']: 'low threshold',
                            kwargs['sigma']: 'high threshold'
                        }.items():
                    if not par:
                        print('{0}: \'{1}\' parameter is missing.'
                              .format(self._programName, label))

        if Message.unimgrt == event:
            self.qafilmmodel.undo_rotation()
            self._mainscreen.update(self.qafilmmodel)  # Update screen.

    def execute(self):
        # Do some basic sanity checks first.
        if self._filelist[0] is None:
            print('{0}: Missing image file.'.format(self._programName))
            self._exit_app()

        # First check if given files exist at all.
        if not isfile(self._filelist[0]):
            print(
                    '{0}: File \'{1}\' does not exist or is directory.'
                    .format(self._programName, self._filelist[0])
                )

            self._exit_app()

        if self._filelist[1] is not None:
            if not isfile(self._filelist[1]):
                print(
                        '{0}: File \'{1}\' does not exist or is directory.'
                        .format(self._programName, self._filelist[1])
                    )

                self._exit_app()

        # Now check if we are dealing with supported image format.
        if not is_image_format_supported(self._filelist[0]):
            print(
                    '{0}: File \'{1}\' is not of supported image format.'
                    .format(self._programName, self._filelist[0])
                )

            self._exit_app()

        if self._filelist[1] is not None:
            if not is_image_format_supported(self._filelist[1]):
                print(
                        '{0}: File \'{1}\' is not of supported image format.'
                        .format(self._programName, self._filelist[1])
                    )

                self._exit_app()

        # We have a proper iradiated image file. Load the image data.
        print('{0}: Loading data image ...'.format(self._programName))
        dataimage = Image.open(self._filelist[0])

        if self._filelist[1] is not None:
            # We have proper preiradiated image file. Load it too.
            print('{0}: Loading control image ...'.format(self._programName))
            controlimage = Image.open(self._filelist[1])

        else:
            controlimage = None

        # Print some info to the command line.
        print('{0}: Starting GUI ...'.format(self._programName))

        # Initialize all models.
        self.qafilmmodel = models.QAFilm(dataimage, self)
        self.qafilmmodel.change_color_mode(ImageColorMode.fullcolor)

        # Initialize views.
        self._mainscreen = tkfv.TkiAppMainWindow(controller=self)

        # We have all neccessary files. Start the GUI.
        self._mainscreen.title(self._programName)
        self._mainscreen.update(self.qafilmmodel)
        self._mainscreen.mainloop()

        # Print to command line that we are freeing memory and closing app.
        print('{0}: Freeing allocated memory ...'.format(self._programName))

        # Do the cleanup and exit application.
        del self.qafilmmodel
        dataimage.close()

        if controlimage is not None:
            controlimage.close()

        self._exit_app()
