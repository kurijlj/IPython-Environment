#!/usr/bin/env python

# ============================================================================
# Copyright (C) 2020 Ljubomir Kurij <kurijlj@gmail.com>
#
# This file is part of mda (Measurement Data Analytics).
#
# <program name> is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# ============================================================================


# ============================================================================
#
# 2020-08-31 Ljubomir Kurij <kurijlj@gmail.com>
#
# * mda.py: created.
#
# ============================================================================


# ============================================================================
#
# TODO:
#
#
# ============================================================================


# ============================================================================
#
# References (this section should be deleted in the release version)
#
#
# ============================================================================


# =============================================================================
# Modules import section
# =============================================================================

from enum import Enum  # Required by ReadErrors.
from os.path import isfile
from sys import float_info as fi  # Required by MIN_FLOAT and MAX_FLOAT
import csv
import argparse
import numpy as np


# =============================================================================
# Global constants
# =============================================================================

# Centimeters per inch.
CM_PER_IN = 2.54
MM_PER_IN = 25.4

MIN_FLOAT = fi.min
MAX_FLOAT = fi.max


# =============================================================================
# Utility classes and functions
# =============================================================================

class ProgramAction():
    """Abstract base class for all program actions, that provides execute.

    The execute method contains code that will actually be executed after
    arguments parsing is finished. The method is called from within method
    run of the CommandLineApp instance.
    """

    def __init__(self, exitf):
        self._exit_app = exitf

    def execute(self):
        """Put method documentation here.
        """

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
# Data classes
# =============================================================================


class ReadError(Enum):
    """ Add class description here.
    """

    TOO_MANY_COLUMNS = "Too many columns."
    EMPTY_DATA_SET = "Empty file."
    ROW_WIDTH_TOO_SMALL = "Row width too small."
    ROW_WIDTH_TOO_BIG = "Row width too big."


class DataReader():
    """ Add class description here.
    """

    def __init__(self, max_col_count=26):
        # Set maximum allowed column count per dataset to 26.
        self._max_col_count = max_col_count

        # Set counters and error flags.
        self.filename = None
        self.headers = None
        self.errors = 0
        self.error_rows = None
        self.last_error = None
        self.row_count = -1
        self.column_count = -1

    def read_from_csv(self, fn, fs=','):

        # Reset counters and error flags.
        self.filename = fn
        self.headers = None
        self.errors = 0
        self.error_rows = None
        self.last_error = None
        self.row_count = 0
        self.column_count = 0

        df = open(self.filename)

        # Check if data file comes with column headers.
        try:
            has_headers = csv.Sniffer().has_header(df.read(1024))

        except csv.Error as e:
            # If not set, instantiate error_rows as dictionary.
            if not self.error_rows:
                self.error_rows = dict()

            self.errors += 1
            self.last_error = e
            self.error_rows[-1] = self.last_error
            has_headers = False

        # Reset file position.
        df.seek(0)

        # Lets count rows and columns first
        datareader = csv.reader(df, delimiter=fs)
        for row in datareader:
            if 0 == self.row_count:
                # Set column number from the first row.
                self.column_count = len(row)
            self.row_count += 1
        df.seek(0)  # Reset file position.

        # If file contains headers we have to decrease row count  by one.
        if has_headers:
            self.row_count -= 1

        # We accept datasets only up to 26 columns, so if the dataset contains
        # more than that number of columns set corresponding error flags.
        if self._max_col_count < self.column_count:
            self.errors += 1
            self.last_error = ReadError.TOO_MANY_COLUMNS

        else:
            # If not dealing with an empty data file (column_count > 0 and
            # row_count > 0) proceed to reading dataset.
            if 1 > self.row_count or 1 > self.column_count:
                self.errors += 1
                self.last_error = ReadError.EMPTY_DATA_SET

            else:
                # Allocate memory for storing data.
                data = np.zeros(
                        (self.row_count, self.column_count),
                        dtype=float
                    )

                datareader = csv.reader(df, delimiter=fs)
                ri = 0  # Row index.
                for row in datareader:
                    if has_headers and 0 == ri:
                        self.headers = tuple(row)

                    else:
                        # Check row width, measured in number of fields. If row
                        # has less or more fileds than column_count, assume
                        # error and skip row. Fill the dataset with MIN_FLOAT.
                        if self.column_count != len(row):
                            # If not set instantiate error_rows as dictionary.
                            if not self.error_rows:
                                self.error_rows = dict()

                            if self.column_count > len(row):
                                self.last_error = ReadError.ROW_WIDTH_TOO_SMALL

                            else:
                                self.last_error = ReadError.ROW_WIDTH_TOO_BIG

                            self.errors += 1
                            self.error_rows[ri] = self.last_error

                            # Column index
                            for ci in range(self.column_count):
                                data[ri - 1, ci] = MIN_FLOAT

                        else:
                            # Column index
                            for ci in range(self.column_count):
                                try:
                                    data[ri - 1, ci] = float(row[ci])
                                except ValueError as e:
                                    # If not set instantiate error_rows as
                                    # dictionary.
                                    if not self.error_rows:
                                        self.error_rows = dict()

                                    self.last_error = e
                                    self.errors += 1
                                    self.error_rows[ri] = self.last_error
                                    data[ri - 1, ci] = MIN_FLOAT

                    ri += 1  # Increase row index.
                df.seek(0)  # Reset file position.

        # Close file pointer after reading data.
        df.close()


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
            delimiter = ','

            if arguments.delimiter: delimiter = arguments.delimiter

            self._action = _formulate_action(
                    DefaultAction,
                    prog=self._parser.prog,
                    exitf=self._parser.exit,
                    data_file=arguments.data_file,
                    delimiter=delimiter
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

    def __init__(self, prog, exitf, data_file, delimiter):
        self._programName = prog
        self._exit_app = exitf
        self._data_file = data_file
        self._delimiter = delimiter

    def execute(self):
        # Do some basic sanity checks first.
        if self._data_file is None:
            print('{0}: Missing data file.'.format(self._programName))
            self._exit_app()

        # First check if given files exist at all.
        if not isfile(self._data_file):
            print(
                    '{0}: File \'{1}\' does not exist or is directory.'
                    .format(self._programName, self._data_file)
                )

            self._exit_app()

        data_reader = DataReader()
        data_reader.read_from_csv(fn=self._data_file, fs=self._delimiter)

        print(
                '{0}: Summary of reading file \'{1}\':\n'
                .format(self._programName, self._data_file)
            )
        print(
                '===========================================================' +
                '====================\n'
            )
        if data_reader.errors:
            print('Errors encountered: {0}.\n'.format(data_reader.errors))
            print(
                    'Last encountered error: {0}.\n'
                    .format(data_reader.last_error)
                )
            if data_reader.error_rows:
                print(data_reader.error_rows)

        else:
            print('No errors encountered.\n')

        self._exit_app()


# =============================================================================
# Script main body
# =============================================================================

if __name__ == '__main__':
    program = CommandLineApp(
        programDescription='Small Python script used to inspaect \
            and analyse 2D graph data.\n\
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
            help='print program version'
        )
    program.add_argument(
            '--usage',
            action='store_true',
            help='give a short usage message'
        )
    program.add_argument(
            '-d', '--delimiter',
            action='store',
            metavar='DELIMITER',
            type=str,
            help='field delimiter. Default value is \",\"',
            group='general options'
        )
    program.add_argument(
            'data_file',
            metavar='DATA_FILE',
            type=str,
            nargs='?',
            help='a CSV file containing graph data'
        )

    program.parse_args()
    program.run()
