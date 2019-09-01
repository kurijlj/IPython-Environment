#!/usr/bin/env python
# -*- coding: utf-8 -*-


from datetime import date
from fnmatch import fnmatch
from datetime import datetime
from collections import namedtuple
#from os import path

PCECharge = namedtuple('PCECharge', ['input1', 'input2'])
PCECurrent = namedtuple('PCECurrent', ['input1', 'input2'])
PCECorrection = namedtuple('PCECorrection', ['input1', 'input2'])
PCECalibration = namedtuple('PCECalibration', ['input1', 'input2'])

# Define named ranges of relative line positions of data entries to
# "* new measurement *" header.
PCEL_APP_VER = 2
PCEL_DATE_TIME = 3
PCEL_SER_NO = 4
PCEL_BKG_CMP = 5
PCEL_IN1_CORR = 6
PCEL_IN2_CORR = 7
PCEL_BIAS_TYPE = 8
PCEL_DET1 = 9
PCEL_DET2 = 10

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

        # text_buffer must be string or NoneType, else raise TypeError.
        if text_buffer is not None and type(text_buffer) is not str:
            raise TypeError(
                "\'text_buffer\' must be string or NoneType, not {0}".format(
                    text_buffer.__class__.__name__
                )
            )

        self._text_buffer = text_buffer

    def __repr__(self):
        if self._text_buffer is None:
            return 'None'
        else:
            return self._text_buffer

    def data(self, text_buffer):

        # text_buffer must be string or NoneType, else raise TypeError.
        if text_buffer is not None and type(text_buffer) is not str:
            raise TypeError(
                "\'text_buffer\' must be string or NoneType, not {0}".format(
                    text_buffer.__class__.__name__
                )
            )

        self._text_buffer = text_buffer

    def app_version(self):
        if self._text_buffer is None:
            return None
        else:
            # Define named range of application version data field.
            app_ver_fld = 2

            str_data = self._text_buffer.splitlines()[PCEL_APP_VER]
            return str_data.split()[app_ver_fld]

    def log_datetime(self):
        if self._text_buffer is None:
            return None
        else:
            # Define named ranges of log date and time data fields.
            date_fld = 2
            time_fld = 3
            ampm_fld = 4

            str_data = self._text_buffer.splitlines()[PCEL_DATE_TIME]
            lst_data = str_data.split()
            str_datetime = '{0} {1} {2}'.format(
                    lst_data[date_fld],
                    lst_data[time_fld],
                    lst_data[ampm_fld]
                )
            return datetime.strptime(str_datetime, '%m-%d-%Y %I:%M %p')

    def log_date(self):
        if self._text_buffer is None:
            return None
        else:
            log_datetime = self.log_datetime()
            return log_datetime.date()

    def log_time(self):
        if self._text_buffer is None:
            return None
        else:
            log_datetime = self.log_datetime()
            return log_datetime.time()

    def pce_serial_number(self):
        if self._text_buffer is None:
            return None
        else:
            # Define named range of electrometer serial number data field.
            sno_fld = 3

            str_data = self._text_buffer.splitlines()[PCEL_SER_NO]
            return str_data.split()[sno_fld]

    def bkg_compensation(self):
        if self._text_buffer is None:
            return None
        else:
            # Define named range of background compensation data field.
            bkg_cmp_fld = 2

            str_data = self._text_buffer.splitlines()[PCEL_BKG_CMP]
            lst_data = str_data.split()
            str_val = lst_data[bkg_cmp_fld].rstrip(',')
            return  bool('yes' == str_val.lower())

    def bkg_current(self):
        if self._text_buffer is None:
            return None
        else:
            # Define named ranges of background current data fields.
            bkg_curr1_fld = 6
            bkg_curr2_fld = 9

            str_data = self._text_buffer.splitlines()[PCEL_BKG_CMP]
            lst_data = str_data.split()
            value1 = lst_data[bkg_curr1_fld]
            value2 = lst_data[bkg_curr2_fld]
            return PCECurrent(float(value1), float(value2))

    def input_correction(self):
        if self._text_buffer is None:
            return None
        else:
            # Define named range of correction transform data fields.
            corr_qnt_fld = 6

            lines = self._text_buffer.splitlines()
            lst_data1 = lines[PCEL_IN1_CORR].split()
            lst_data2 = lines[PCEL_IN2_CORR].split()
            return PCECorrection(
                    float(lst_data1[corr_qnt_fld].rstrip(',')),
                    float(lst_data2[corr_qnt_fld].rstrip(','))
                )

    def input_calibration(self):
        if self._text_buffer is None:
            return None
        else:
            # Define named range of input laboratory calibration data fields. It
            # is the last field in the sequence, henceforth -1 index.
            lab_cal_fld = -1

            lines = self._text_buffer.splitlines()
            lst_data1 = lines[PCEL_IN1_CORR].split()
            lst_data2 = lines[PCEL_IN2_CORR].split()
            return PCECalibration(
                    float(lst_data1[lab_cal_fld]),
                    float(lst_data2[lab_cal_fld])
                )

    def bias_voltage(self):
        if self._text_buffer is None:
            return None
        else:
            # Define named range of bias voltage data field.
            bias_fld = 2

            lines = self._text_buffer.splitlines()[PCEL_BIAS_TYPE]
            lst_data = str_data.split()
            str_val = lst_data[bias_fld]
            return int(str_val)

    def beam_type(self):
        if self._text_buffer is None:
            return None
        else:
            # Define named range of beam type data field. It is the last field
            # in the sequence, hencforth -1 index.
            beam_type_fld = -1

            lines = self._text_buffer.splitlines()[PCEL_BIAS_TYPE]
            lst_data = str_data.split()
            return lst_data[beam_type_fld]


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
