#!/usr/bin/env python
# -*- coding: utf-8 -*-


from datetime import date
from fnmatch import fnmatch
#from os import path


def is_snc_log(fn):
    """ Test if the given path is a valid Sun Nuclear PC Electrometer log file.
    Test is performed by reading the first 53 bytes of the file and checking
    that they match the standard PC Electrometer log file header.

    It is up to the user to first check if the file exists on the disk.

    If the file is a valid log file, the function returns True, otherwise
    it returns False.
    """

    #if not path.exists(fn):
    #    raise ValueError('Given file does not exist.', fn)
    #    return False

    # Header for PC Electrometer log file is 53 bytes long
    header_length = 53

    # Define standard header lines
    header_line_1 = 'Sun Nuclear Corporation'
    header_line_2 = 'PC Electrometer - Log file'

    # Define default result
    result = True

    # Save old file pointer position
    pointer = fn.tell()

    # Set file pointer to beginning of the file
    fn.seek(0, 0)

    header = fn.read(header_length).splitlines()

    if not fnmatch(header[0], header_line_1):
        result = False
    elif not fnmatch(header[1], header_line_2):
        result = False

    # Set file pointer to saved position
    fn.seek(pointer, 0)

    return result


def map_measurements(snlog):
    """ Map position of measurement entries in a Sun Nuclear PC Electrometer
    Log file.
    """

    # Define structure to hold list of pointers to measurements entry in the
    # file. The list contains line indexes of each measurement entry.
    msrmnt_pointers = []

    # Define current pointer
    pointer = 0

    # Define measurement header
    msrmnt_header = '* new measurement *'

    # Save old file pointer position
    old_pos = snlog.tell()

    # Set file pointer to beginning of the file
    snlog.seek(0, 0)

    for line in snlog:
        if fnmatch(line, msrmnt_header):
            msrmnt_pointers.append(pointer)
        pointer += len(line)

    # Set file pointer to saved position
    snlog.seek(old_pos, 0)

    return tuple(msrmnt_pointers)


def measurements(snlog):
    """Retrieve measurements from an Sun Nuclear PC Electrometer Log file as
    list.
    """

    msrmap = map_measurements(snlog)
    measurement = None
    result = []
    old_pos = snlog.tell()

    for index, pointer in enumerate(msrmap):
        # Determine topmost index value
        top = len(msrmap) - 1
        snlog.seek(pointer, 0)
        if index < top:
            next_ptr = msrmap[index + 1]
            buffer_size = next_ptr - pointer
            measurement = PCELogMeasurement(snlog.read(buffer_size))
        else:
            measurement = PCELogMeasurement(snlog.read())
        result.append(measurement)

    snlog.seek(old_pos, 0)
    return tuple(result)


class PCELogMeasurement(object):
    """This is one measurement entry from Sun Nuclear PC Electrometer Log file.
    It holds text lines loaded from log file that contain data for given
    measurement. Use class methods to access measurement data.
    """

    def __init__(self, text_buffer=None):
        self._text_buffer = text_buffer

    def __repr__(self):
        return self._text_buffer


class EnvConds(object):
    """
    """

    def __init__(self,
                 t: float = 20.0,
                 p: float = 101.3,
                 RH: float = 50.0,
                 ref: bool = True,
                 ):
        self._t = t
        self._p = p
        self._RH = RH
        self._ref = ref

    def __repr__(self):
        objstr = str()
        if self._ref:
            objstr = (self.__class__.__name__ +
                      ('(t0={0} 0C, p0={1} kPa, RH={2} %)'
                          .format(self._t, self._p, self._RH)))
        else:
            objstr = (self.__class__.__name__ +
                      ('(t0={0} 0C, p0={1} kPa, RH={2} %)'
                          .format(self._t, self._p, self._RH)))

        return objstr

    @property
    def t(self):
        """
        """

        return self._t

    @property
    def p(self):
        """
        """

        return self._p

    @property
    def RH(self):
        """
        """

        return self._RH

    def asdict(self):
        """
        """
        if self._ref:
            return {'t0': self._t, 'p0': self._p, 'RH': self._RH}
        else:
            return {'t': self._t, 'p': self._p, 'RH': self._RH}


class CalibratedInstrument(object):
    """Abstract class.
    """

    def __init__(self,
                 mnfc: str = 'Unknown',
                 model: str = 'Uknown',
                 SNo: str = 'Unknown'
                 ):
        self._mnfc = mnfc
        self._model = model
        self._SNo = SNo
        self._certificate = None

    @property
    def mnfc(self):
        """
        """

        return self._mnfc

    @property
    def model(self):
        """
        """

        return self._model

    @property
    def SNo(self):
        """
        """

        return self._SNo

    @property
    def certificate(self):
        """
        """

        return self._certificate

    def asdict(self):
        """
        """

        return {'Manufacturer': self._mnfc,
                'Model': self._model,
                'Serial Number': self._SNo}


class CalibrationCertificate(object):
    """Abstract class.
    """

    def __init__(self,
                 lab: str = 'Unknown',
                 dt: date = date.today(),
                 factor: float = 1.0):
        self._lab = lab
        self._date = dt
        self._factor = factor

    @property
    def lab(self):
        """
        """

        return self._lab

    @property
    def date(self):
        """
        """

        return self._date

    @property
    def factor(self):
        """
        """

        return self._factor

    def asdict(self):
        """I am an abstract class. Subclasses must override this.
        """

        raise TypeError('I am an abstract class. ' +
                        'Subclasses must override this.')
