#!/usr/bin/env python
# -*- coding: utf-8 -*-
# tester.py

try:
    from pydicom.valuerep import DSfloat, DSdecimal
except ImportError:
    from dicom.valuerep import DSfloat, DSdecimal
import numpy as np


class SliceLocation(object):
    """A class to handle resaults of accessing pydicom's dataset SliceLocation
    property, case when there is no SliceLocation property, and to provide
    basic relation operations between instances of slice location class.

    In the case that dicom dataset does not contain a SliceLocation property
    SliceLocation class stores None. Otherwise it stores value returned by a
    call to dicom datasets SliceLocation property. Returned value can be an
    empty string or an instance of a DSclass.

    One can only compare two SliceLocation instances containing DSclass
    objects. An attempt to compare SliceLocation instance containing an None or
    an empty string with any other SliceLocation instance, holding None or
    empty string too will return False.

    An attempt to do comparison with a non SliceLocation type would result in a
    TypeError.
    """

    def __init__(self, value):
            self._val = value

    def __str__(self):
        if isinstance(self._val, int):
            return 'SliceLocation(value: \'{0} mm\')'.format(self._val)

        return str(self._val)

    def __repr__(self):
        return "\"" + str(self) + "\""

    def __eq__(self, other):
        if not isinstance(other, SliceLocation):
            raise TypeError(
                    '\'==\' not supported between instances of \'{0}\' '
                    .format(self.__class__) +
                    'and \'{0}\''.format(type(other))
                )
        else:
            if self.is_dsclass() and other.is_dsclass():
                return float(self.value_raw()) == float(other.value_raw())

        return False

    def __ne__(self, other):
        if not isinstance(other, SliceLocation):
            raise TypeError(
                    '\'==\' not supported between instances of \'{0}\' '
                    .format(self.__class__) +
                    'and \'{0}\''.format(type(other))
                )
        else:
            if self.is_dsclass() and other.is_dsclass():
                return float(self.value_raw()) != float(other.value_raw())

        return False

    def __lt__(self, other):
        if not isinstance(other, SliceLocation):
            raise TypeError(
                    '\'<\' not supported between instances of \'{0}\' '
                    .format(self.__class__) +
                    'and \'{0}\''.format(type(other))
                )
        else:
            if self.is_dsclass() and other.is_dsclass():
                return float(self.value_raw()) < float(other.value_raw())

        return False

    def __gt__(self, other):
        if not isinstance(other, SliceLocation):
            raise TypeError(
                    '\'>\' not supported between instances of \'{0}\' '
                    .format(self.__class__) +
                    'and \'{0}\''.format(type(other))
                )
        else:
            if self.is_dsclass() and other.is_dsclass():
                return float(self.value_raw()) > float(other.value_raw())

        return False

    @property
    def value(self):
        if self.is_none() or self.is_empty_string():
            return self._val

        return round(self._val, 1)

    def value_raw(self):
        return self._val

    def is_none(self):
        return self._val is None

    def is_empty_string(self):
        return '' == self._val

    def is_dsclass(self):
        return isinstance(self._val, (DSfloat, DSdecimal))


class SliceShape(object):
    """A class to store DICOM image shape i.e. rows and columns.
    """

    def __init__(self, rows, columns):
        if not isinstance(rows, int):
            raise TypeError(
                    'SliceShape() rows argument must be an integer, ' +
                    'not \'{0}\''.format(rows.__class__)
                )
        if not isinstance(columns, int):
            raise TypeError(
                    'SliceShape() columns argument must be an integer, ' +
                    'not \'{0}\''.format(columns.__class__)
                )
        self._shape = np.array([rows, columns])

    def __str__(self):
        return 'SliceShape(rows: \'{0}\', columns: \'{1}\')'.format(
                self._shape[0],
                self._shape[1]
            )

    def __repr__(self):
        return "\"" + str(self) + "\""

    def __eq__(self, other):
        if not isinstance(other, SliceShape):
            raise TypeError(
                    '\'==\' not supported between instances of \'{0}\' '
                    .format(self.__class__) +
                    'and \'{0}\''.format(type(other))
                )
        else:
            return self.rows == other.rows and self.columns == other.columns

        return False

    def __ne__(self, other):
        if not isinstance(other, SliceShape):
            raise TypeError(
                    '\'!=\' not supported between instances of \'{0}\' '
                    .format(self.__class__) +
                    'and \'{0}\''.format(type(other))
                )
        else:
            return self.rows != other.rows or self.columns != other.columns

        return False

    @property
    def rows(self):
        return self._shape[0]

    @property
    def columns(self):
        return self._shape[1]

    def shape(self):
        return {'rows': self._shape[0], 'columns': self._shape[1]}

    def shape_raw(self):
        return self._shape
