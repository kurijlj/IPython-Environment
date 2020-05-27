#!/usr/bin/env python
# =============================================================================
# Dicom Validator - small python script used to validate DICOM files.
#
#  Copyright (C) 2020 Ljubomir Kurij <kurijlj@gmail.com>
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
# 2020-05-26 Ljubomir Kurij <ljubomir_kurij@protonmail.com>
#
# * validate_dicom.py: created.
#
# =============================================================================


import argparse
from os.path import isfile
from pydicom import dcmread
from pydicom import filereader
from colored import fg, attr


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
        fmtMail = 'Report bugs to <{bugMail}>.'.format(bugMail=bugMail)
    else:
        fmtMail = None

    if epilogAddition is None:
        fmtEpilog = fmtMail

    elif fmtMail is None:
        fmtEpilog = epilogAddition

    else:
        fmtEpilog = '{addition}\n\n{mail}'.format(
                addition=epilogAddition,
                mail=fmtMail
            )

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
                epilog=None
            ):

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
                    exitf=self._parser.exit,
                    dicom_file=arguments.dicom_file
                )

    def run(self):
        """This method executes action code.
        """

        self._action.execute()


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

    def __init__(self, prog, exitf, dicom_file):
        self._programName = prog
        self._exit_app = exitf
        self._dicom_file = dicom_file

    def execute(self):
        # Do some basic sanity checks first.
        if self._dicom_file is None:
            print('{0}: Missing DICOM file.'.format(self._programName))
            self._exit_app()

        # First check if given files exist at all.
        if not isfile(self._dicom_file):
            print(
                    '{0}: File \'{1}\' does not exist or is directory.'
                    .format(self._programName, self._dicom_file)
                )

            self._exit_app()

        # Check if we are dealing with a DICOM file.
        fp = open(self._dicom_file, 'rb')
        if not filereader.read_preamble(fp, force=True):
            print(
                    '{0}: File \'{1}\' is not an DICOM file.'
                    .format(self._programName, self._dicom_file)
                )

            fp.close()
            self._exit_app()

        # Close file pointer after check.
        fp.close()

        # We are dealing with the DICOM file so we can open it and test
        # for presence of flags.
        # tags = ('SOPClassUID', 'PatientID')
        tags = {
                (0x0010, 0x0030): 'PatientBirthDate',
                (0x0020, 0x0011): 'SeriesNumber',
                (0x0008, 0x103E): 'SeriesDescription',
                (0x0020, 0x000E): 'SeriesInstanceUID',
                (0x0008, 0x0021): 'SeriesDate',
                (0x0008, 0x0031): 'SeriesTime',
                (0x0008, 0x0020): 'StudyDate',
                (0x0008, 0x0030): 'StudyTime',
                (0x0020, 0x000D): 'StudyInstanceUID',
                (0x0008, 0x0018): 'SOPInstanceUID',
                (0x0008, 0x0022): 'AcquisitionDate',
                (0x0008, 0x0032): 'AcquisitionTime',
                (0x0020, 0x3403): 'ModifiedImageDate',
                (0x0020, 0x3405): 'ModifiedImageTime',
                (0x0008, 0x0012): 'InstanceCreationDate',
                (0x0008, 0x0013): 'InstanceCreationTime',
                (0x0008, 0x0005): 'SpecificCharacterSet',
                (0x0008, 0x0060): 'Modality',
                (0x0008, 0x0070): 'Manufacturer',
                (0x0008, 0x1010): 'Station Name',
                (0x0008, 0x1090): 'ManufacturerModelName',
                (0x0018, 0x0050): 'SliceThickness',
                (0x0018, 0x0088): 'SpacingBetweenSlices',
                (0x0018, 0x0090): 'DataCollectionDiameter',
                (0x0018, 0x1020): 'SoftwareVersions',
                (0x0018, 0x1030): 'ProtocolName',
                (0x0018, 0x1100): 'ReconstructionDiameter',
                (0x0018, 0x5100): 'PatientPosition',
                (0x0018, 0x0080): 'RepetitionTime',
                (0x0018, 0x0081): 'EchoTime',
                (0x0018, 0x0086): 'EchoNumbers',
                (0x0020, 0x0012): 'AcquisitionNumber',
                (0x300A, 0x00C8): 'ReferenceImageNumber',
                (0x0020, 0x0032): 'ImagePositionPatient',
                (0x0020, 0x0037): 'ImageOrientationPatient',
                (0x0020, 0x1040): 'PositionReferenceIndicator',
                (0x0020, 0x1041): 'SliceLocation',
                (0x0028, 0x0002): 'SamplesPerPixel',
                (0x0028, 0x0004): 'PhotometricInterpretation',
                (0x0028, 0x0010): 'Rows',
                (0x0028, 0x0011): 'Columns',
                (0x0028, 0x0030): 'PixelSpacing',
                (0x0028, 0x0100): 'BitsAllocated',
                (0x0028, 0x0101): 'BitsStored',
                (0x0028, 0x0102): 'HighBit',
                (0x0028, 0x0103): 'PixelRepresentation',
                (0x0028, 0x0120): 'PixelPaddingValue',
                (0x0028, 0x1050): 'WindowCenter',
                (0x0028, 0x1051): 'WindowWidth',
                (0x0028, 0x1052): 'RescaleIntercept',
                (0x0028, 0x1053): 'RescaleSlope',
                (0x0028, 0x1054): 'RescaleType'
            }
        failed = int(0)

        dataset = dcmread(self._dicom_file)
        for tag in tags.keys():
            if not hasattr(dataset, tags[tag]):
                print(
                        '{0}: Tag \'{1:26s}\': {2}FAILED{3}'.format(
                            self._dicom_file,
                            tags[tag],
                            fg('red'),
                            attr('reset')
                        )
                    )
            else:
                failed = failed + 1
                print(
                        '{0}: Tag \'{1:26s}\': {2}PASSED{3}'.format(
                            self._dicom_file,
                            tags[tag],
                            fg('green'),
                            attr('reset')
                        )
                    )
        # Calculate pass and fail ratio in percents.
        print('{0}: Failed with {1:.0f}%.'.format(
                self._dicom_file,
                (len(tags.items()) - failed) / len(tags.items()) * 100.0
            ))

        self._exit_app()


# =============================================================================
# Script main body
# =============================================================================

if __name__ == '__main__':
    program = CommandLineApp(
        programDescription='Small Python script used to validate \
            DICOM files by DICOM tags the file contains.\n\
            Mandatory arguments to long options are mandatory for \
            short options too.'.replace('\t', ''),
        programLicense='License GPLv3+: GNU GPL version 3 or later \
            <http://gnu.org/licenses/gpl.html>\n\
            This is free software: you are free to change and \
            redistribute it.\n\
            There is NO WARRANTY, to the extent permitted by \
            law.'.replace('\t', ''),
        versionString='0.1',
        yearString='2020',
        authorName='Ljubomir Kurij',
        authorMail='ljubomir_kurij@protonmail.com',
        epilog=None)

    program.add_argument_group('general options')
    program.add_argument(
            '-V', '--version',
            action='store_true',
            help='print program version',
            group='general options'
        )
    program.add_argument(
            '--usage',
            action='store_true',
            help='give a short usage message'
        )
    program.add_argument(
            'dicom_file',
            metavar='DICOM_FILE',
            type=str,
            nargs='?',
            help='DICOM file to be validated'
        )

    program.parse_args()
    program.run()
