#!/usr/bin/env python
# -*- coding: utf-8 -*-
# tester.py

try:
    from pydicom.valuerep import DSfloat, DSdecimal
except ImportError:
    from dicom.valuerep import DSfloat, DSdecimal

class SliceLocation(object):
    """
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
            raise AttributeError(
                    '{0}: Not an SliceLocation instance'
                    .format(self.__class__)
                )
        else:
            if self.is_dsclass() and other.is_dsclass():
                return float(self.value_raw()) == float(other.value_raw())

        return False

    def __ne__(self, other):
        if not isinstance(other, SliceLocation):
            raise AttributeError(
                    '{0}: Not an SliceLocation instance'
                    .format(self.__class__)
                )
        else:
            if self.is_dsclass() and other.is_dsclass():
                return float(self.value_raw()) != float(other.value_raw())

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

