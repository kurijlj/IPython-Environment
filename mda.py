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


class ReadErrorO(Enum):
    """ Add class description here.
    """

    EMPTY_FILE = 'Empty file.'
    NO_DATA = 'No table data could be found.'
    TOO_MANY_COLUMNS = 'Too many data columns.'
    ROW_WIDTH_TOO_SMALL = 'Row width too small.'
    ROW_WIDTH_TOO_BIG = 'Row width too big.'


class ReadError():
    """ Add class description here.
    """

    EMPTY_FILE = 'Empty file'
    NO_DATA = 'No table data could be found'
    TOO_MANY_COLUMNS = 'Too many data columns'
    ROW_WIDTH_TOO_SMALL = 'Row width too small'
    ROW_WIDTH_TOO_BIG = 'Row width too big'

    def __init__(self, error_code):
        error_codes = (
                self.EMPTY_FILE,
                self.NO_DATA,
                self.TOO_MANY_COLUMNS,
                self.ROW_WIDTH_TOO_SMALL,
                self.ROW_WIDTH_TOO_BIG
            )
        if not error_code in error_codes:
            raise ValueError('Trying to assign unsupported value.')
        self._error_code = error_code

    def __repr__(self):

        str_val = None

        if self.EMPTY_FILE == self._error_code:
            str_val = '.EMPTY_FILE'
        elif self.NO_DATA == self._error_code:
            str_val = '.NO_DATA'
        elif self.TOO_MANY_COLUMNS == self._error_code:
            str_val = '.TOO_MANY_COLUMNS'
        elif self.ROW_WIDTH_TOO_SMALL == self._error_code:
            str_val = '.ROW_WIDTH_TOO_SMALL'
        else:
            str_val = '.ROW_WIDTH_TOO_BIG'

        return self.__class__.__name__ + str_val

    def __str__(self):
        return self._error_code

    def __eq__(self, other):
        return bool(self._error_code == other.val)

    @property
    def val(self):
        """ Add function docstring here.
        """
        return self._error_code


class CSVDataReader():
    """ Add class description here.
    """

    def __init__(self, max_col_count=26):
        # Set maximum allowed column count per dataset to 26.
        self.max_col_count = max_col_count

        # Initialize attributes.
        self.file_name = None  # Name of file containing data.
        self.headers = None  # Tuple holding data column headers.
        self.error_count = 0  # Counts errors encountered while reading data.
        self.errors = list()  # Map of row numbers and encountered errors.
        self.last_error = None  # Last encountered error string.
        self.row_count = -1  # Number of red rows.
        self.column_count = -1  # Number of red columns.

    def _clear_error_log(self):
        """Resets all error attributes and prepares reader for new reading.
        """

        self.file_name = None
        self.headers = None
        self.error_count = 0
        self.errors = list()
        self.last_error = None
        self.row_count = -1
        self.column_count = -1

    def _is_empty(self, data_file):
        """Tests if passed file contains any data at all.

        It returns True if file is empty, othervise returns False.
        """

        state = False

        # Save current position of the read/write pointer and move pointer to
        # the beginning of the file.
        old_pos = data_file.tell()
        data_file.seek(0)

        # Read first character.
        one_char = data_file.read(1)

        # If not fetched then file is empty.
        if not one_char:
            state = True
            self.error_count += 1
            self.last_error = ReadError.EMPTY_FILE
            self.errors.append((0, self.last_error))

        # Restore file pointer position.
        data_file.seek(old_pos)

        return state

    def _has_header(self, data_file):
        """Check if given CSV file contains column header by means of calling
        has_header() method of the Sniffer class from csv module.

        It returns True if file has a header, othervise returns False.
        """

        state = False

        # Save current position of the read/write pointer and move pointer to
        # the beginning of the file.
        old_pos = data_file.tell()
        data_file.seek(0)

        try:
            state = csv.Sniffer().has_header(data_file.read(1024))

        except csv.Error as e:
            self.error_count += 1
            self.last_error = e
            self.errors.append((0, self.last_error))

        # Restore file pointer position.
        data_file.seek(old_pos)

        return state

    def _data_shape(self, data_file, delimiter):
        """Counts rows and columns of the given file.

        It returns tuple of format (row_count, column_count).
        """

        row_count = 0
        column_count = 0

        # Save current position of the read/write pointer and move pointer to
        # the beginning of the file.
        old_pos = data_file.tell()
        data_file.seek(0)

        datareader = csv.reader(data_file, delimiter=delimiter)
        for row in datareader:
            # If this is first row beeing red count number of fields it
            # contains and use that number as number of columns in the dataset.
            if 0 == row_count:
                column_count = len(row)

            # For each row in datareader increase counter by one.
            row_count += 1

        # Restore file pointer position.
        data_file.seek(old_pos)

        # If file has header we have to decrease row count  by one.
        if self._has_header(data_file):
            row_count -= 1

        # If either of the row_count or column_count is equal to 0 we consider
        # take the data set as empty.
        if 1 > row_count or 1 > column_count:
            self.error_count += 1
            self.last_error = ReadError.NO_DATA
            self.errors.append(0, self.last_error)

        return (row_count, column_count)

    def read_data(self, file_name, delimiter=','):
        """Tries to read CSV data from a file designated with a passed file
        name.

        It returns two dimensional array representing data set. If the data set
        contains header it is stored in the header attribute of the
        CSVDataReader instance.

        If it encounters errors while reading file it returns None and propper
        error log is set. This error log can be exained by error_count, errors
        and last_error attributes, where:
            1. error_count represents number of errors encountered while
            reading file;
            2. errors is dictionary representing map of the error strings of
            encountered errors with indexes (starting from 1) of rows in the
            file beeing red where the errors have occured. If the error have
            occured in the header error string is mapped to the zero;
            3. last_error is an error string of the last encountered error.
        """

        # Reset attributes and clear error log.
        self._clear_error_log()
        self.file_name = file_name

        # Initialize data container.
        data = None

        with open(self.file_name) as f:
            # If f is an empty file abort further reading.
            if self._is_empty(f):
                return data

            # Try to determina data set shape (number of rows and columns).
            self.row_count, self.column_count = self._data_shape(
                    f,
                    delimiter
                )

            # If f is an empty data set abort further reading.
            if self.row_count < 1 or self.column_count < 1:
                return data

            has_header = self._has_header(f)

            # Since we don't process data sets with more columns than
            # number of columns set on the intialization of the
            # instance (max_col_count), check if column_count is
            # greater than set limit. If not continue with reading
            # the file, othervise set error log and abort further
            # reading.
            if self.max_col_count < self.column_count:
                self.error_count += 1
                self.last_error = ReadError.TOO_MANY_COLUMNS
                self.errors.append(0, self.last_error)
                return data

            # Allocate memory for storing data.
            data = np.zeros(
                    (self.row_count, self.column_count),
                    dtype=float
                )

            datareader = csv.reader(f, delimiter=delimiter)
            ri = 0  # Row index.

            for row in datareader:
                if has_header and 0 == ri:
                    self.headers = tuple(row)

                else:
                    # Check row width, measured in number of fields. If row
                    # has less or more fileds than column_count, assume
                    # error and skip reading the row. Fill row fields in the
                    # data table with MIN_FLOAT.
                    if self.column_count != len(row):
                        if self.column_count > len(row):
                            self.last_error = ReadError.ROW_WIDTH_TOO_SMALL

                        else:
                            self.last_error = ReadError.ROW_WIDTH_TOO_BIG

                        self.error_count += 1
                        self.errors.append((ri + 1, self.last_error))

                        # Column index.
                        for ci in range(self.column_count):
                            data[ri - 1, ci] = MIN_FLOAT

                    else:
                        # Column index.
                        for ci in range(self.column_count):
                            try:
                                data[ri - 1, ci] = float(row[ci])

                            # If we encounter error converting data set field
                            # into float fill that field in data table with
                            # the MIN_FLOAT.
                            except ValueError as e:
                                self.error_count += 1
                                self.last_error = e
                                self.errors.append((ri + 1, self.last_error))
                                data[ri - 1, ci] = MIN_FLOAT

                ri += 1  # Increase row index.

        return data

    def print_error_report(self):
        """Prints summary error report of encountered errors to the stdout.
        """

        if not self.file_name:
            # No file was red or reader state was reset.
            print('No file was red.')
            return  # Bail out.

        print(
                'Summary of reading file \'{0}\':'
                .format(self.file_name)
            )
        print(
                '=======================================================' +
                '========================\n'
            )
        if self.error_count:
            print(
                    'Errors encountered: {0}.'
                    .format(self.error_count)
                )
            print(
                    'Last encountered error: {0}.'
                    .format(self.last_error)
                )
            for error in self.errors:
                print('Row {0}: {1}.'.format(error[0], error[1]))

        else:
            print('No errors encountered.')


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

            if arguments.delimiter:
                delimiter = arguments.delimiter

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

        data_reader = CSVDataReader()
        print('\n')
        data_reader.print_error_report()
        print('\n')
        data = data_reader.read_data(self._data_file, self._delimiter)
        headers = None
        if data_reader.headers:
            headers = data_reader.headers
        data_reader.print_error_report()
        print('\n')

        #data_reader.read_from_csv(fn=self._data_file, fs=self._delimiter)

        #print(
        #        '{0}: Summary of reading file \'{1}\':\n'
        #        .format(self._programName, self._data_file)
        #    )
        #print(
        #        '===========================================================' +
        #        '====================\n'
        #    )
        #if data_reader.error_count:
        #    print('Errors encountered: {0}.\n'.format(data_reader.error_count))
        #    print(
        #            'Last encountered error: {0}.\n'
        #            .format(data_reader.last_error)
        #        )
        #    if data_reader.errors:
        #        print(data_reader.errors)

        #else:
        #    print('No errors encountered.\n')

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
