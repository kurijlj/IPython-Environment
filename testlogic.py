#!/usr/bin/env python
""" Add module docstring here.
"""

class ReadError():
    """ Add class description here.
    """

    EMPTY_FILE = 'Empty file.'
    NO_DATA = 'No table data could be found.'
    TOO_MANY_COLUMNS = 'Too many data columns.'
    ROW_WIDTH_TOO_SMALL = 'Row width too small.'
    ROW_WIDTH_TOO_BIG = 'Row width too big.'

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
