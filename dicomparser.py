#!/usr/bin/env python
# -*- coding: utf-8 -*-
# dicomparser.py
"""Class that parses and returns formatted DICOM RT data."""
# Copyright (c) 2009-2016 Aditya Panchal
# Copyright (c) 2009-2010 Roy Keyes
# This file is part of dicompyler-core, released under a BSD license.
#    See the file license.txt included with this distribution, also
#    available at https://github.com/dicompyler/dicompyler-core/


import logging
import numpy as np
import util
from dicom import read_file
from dicom.dataset import Dataset
#import random
#from numbers import Number
#from six import PY2, iterkeys, string_types, BytesIO
#from six.moves import range
#from dicompylercore import dvh, util

logger = logging.getLogger('dicomparser')

class DicomParser:
    """Parses DICOM files."""

    def __init__(self, dataset):

        if isinstance(dataset, Dataset):
            self.ds = dataset
        elif isinstance(dataset, (string_types, BytesIO)):
            try:
                self.ds = \
                    # defer_size means if a data element value is larger than
                    # defer_size, then the value is not read into memory until
                    # it is accessed in code.
                    read_file(dataset, defer_size=100, force=True)
            except:
                # Raise the error for the calling method to handle
                raise
            else:
                # Sometimes DICOM files may not have headers, but they should
                # always have a SOPClassUID to declare what type of file it is.
                # If the file doesn't have a SOPClassUID, then
                # it probably isn't DICOM.
                if not "SOPClassUID" in self.ds:
                    raise AttributeError
        else:
            raise AttributeError

######################## SOP Class and Instance Methods #######################

    def GetSOPClassUID(self):
        """Determine the SOP Class UID of the current file."""

        if (self.ds.SOPClassUID == '1.2.840.10008.5.1.4.1.1.481.2'):
            return 'rtdose'
        elif (self.ds.SOPClassUID == '1.2.840.10008.5.1.4.1.1.481.3'):
            return 'rtss'
        elif (self.ds.SOPClassUID == '1.2.840.10008.5.1.4.1.1.481.5'):
            return 'rtplan'
        elif (self.ds.SOPClassUID == '1.2.840.10008.5.1.4.1.1.2'):
            return 'ct'
        elif (self.ds.SOPClassUID == '1.2.840.10008.5.1.4.1.1.4'):
            return 'mri'
        elif (self.ds.SOPClassUID == '1.2.840.10008.5.1.4.1.1.12.1'):
            return 'xra'
        else:
            return None

    def GetSOPInstanceUID(self):
        """Determine the SOP Class UID of the current file."""

        return self.ds.SOPInstanceUID

    def GetStudyInfo(self):
        """Return the study information of the current file."""

        study = {}
        if 'StudyDescription' in self.ds:
            desc = self.ds.StudyDescription
        else:
            desc = 'N/A'
        study['description'] = desc
        if 'StudyDate' in self.ds:
            date = self.ds.StudyDate
        else:
            date = 'N/A'
        study['date'] = date
        # Don't assume that every dataset includes a study UID
        if 'StudyInstanceUID' in self.ds:
            study['id'] = self.ds.StudyInstanceUID
        else:
            study['id'] = 'N/A'

        return study

    def GetSeriesInfo(self):
        """Return the series information of the current file."""

        series = {}

        if 'SeriesDescription' in self.ds:
            desc = self.ds.SeriesDescription
        else:
            desc = 'N/A'

        series['description'] = desc
        series['id'] = self.ds.SeriesInstanceUID

        # Don't assume that every dataset includes a study UID
        if 'StudyInstanceUID' in self.ds:
            series['study'] = self.ds.StudyInstanceUID
        else:
            series['study'] = 'N/A'

        if 'FrameOfReferenceUID' in self.ds:
            series['referenceframe'] = self.ds.FrameOfReferenceUID
        else:
            series['referenceframe'] = 'N/A'

        if 'Modality' in self.ds:
            series['modality'] = self.ds.Modality
        else:
            series['modality'] = 'N/A'

        return series

    def GetReferencedSeries(self):
        """Return the SOP Class UID of the referenced series."""

        if "ReferencedFrameOfReferenceSequence" in self.ds:
            frame = self.ds.ReferencedFrameOfReferenceSequence
            if "RTReferencedStudySequence" in frame[0]:
                study = frame[0].RTReferencedStudySequence[0]
                if "RTReferencedSeriesSequence" in study:
                    if "SeriesInstanceUID" in \
                            study.RTReferencedSeriesSequence[0]:
                        series = study.RTReferencedSeriesSequence[0]
                        return series.SeriesInstanceUID
        else:
            return ''

    def GetFrameOfReferenceUID(self):
        """Determine the Frame of Reference UID of the current file."""

        if 'FrameOfReferenceUID' in self.ds:
            return self.ds.FrameOfReferenceUID
        elif 'ReferencedFrameOfReferences' in self.ds:
            return self.ds.ReferencedFrameOfReferences[0].FrameOfReferenceUID
        else:
            return ''

    def GetDemographics(self):
        """Return the patient demographics from a DICOM file."""

        # Set up some sensible defaults for demographics
        patient = {'name': 'None',
                   'id': 'None',
                   'birth_date': None,
                   'gender': 'Other'}
        if 'PatientName' in self.ds:
            name = self.ds.PatientName
            patient['name'] = name
            patient['given_name'] = name.given_name
            patient['middle_name'] = name.middle_name
            patient['family_name'] = name.family_name
        if 'PatientID' in self.ds:
            patient['id'] = self.ds.PatientID
        if 'PatientSex' in self.ds:
            if (self.ds.PatientSex == 'M'):
                patient['gender'] = 'male'
            elif (self.ds.PatientSex == 'F'):
                patient['gender'] = 'female'
            else:
                patient['gender'] = 'N/A'
        if 'PatientBirthDate' in self.ds:
            if len(self.ds.PatientBirthDate):
                patient['birth_date'] = str(self.ds.PatientBirthDate)

        return patient

############################### Image Methods #################################

    def GetImageData(self):
        """Return the image data from a DICOM file."""

        data = {}

        if 'ImagePositionPatient' in self.ds:
            data['position'] = self.ds.ImagePositionPatient
        if 'ImageOrientationPatient' in self.ds:
            data['orientation'] = self.ds.ImageOrientationPatient
        if 'PixelSpacing' in self.ds:
            data['pixelspacing'] = self.ds.PixelSpacing
        else:
            # Revert to sain value
            data['pixelspacing'] = [1, 1]
        data['rows'] = self.ds.Rows
        data['columns'] = self.ds.Columns
        data['samplesperpixel'] = self.ds.SamplesPerPixel
        data['photometricinterpretation'] = self.ds.PhotometricInterpretation
        data['littlendian'] = \
            self.ds.file_meta.TransferSyntaxUID.is_little_endian
        if 'PatientPosition' in self.ds:
            data['patientposition'] = self.ds.PatientPosition
        data['frames'] = self.GetNumberOfFrames()

        return data

    def GetImageLocation(self):
        """Calculate the location of the current image slice."""

        ipp = self.ds.ImagePositionPatient
        iop = self.ds.ImageOrientationPatient

        normal = []
        normal.append(iop[1] * iop[5] - iop[2] * iop[4])
        normal.append(iop[2] * iop[3] - iop[0] * iop[5])
        normal.append(iop[0] * iop[4] - iop[1] * iop[3])

        loc = 0
        for i in range(0, len(normal)):
            loc += normal[i] * ipp[i]

        # The image location is inverted for Feet First images
        if 'PatientPosition' in self.ds:
            if ('ff' in self.ds.PatientPosition.lower()):
                loc = loc * -1

        return loc

    def GetImageOrientationType(self):
        """Get the orientation of the current image slice."""

        if 'ImageOrientationPatient' in self.ds:
            iop = np.array(self.ds.ImageOrientationPatient)

            orientations = [
                ["SA", np.array([1, 0, 0, 0, 1, 0])],      # supine axial
                ["PA", np.array([-1, 0, 0, 0, -1, 0])],    # prone axial
                ["SS", np.array([0, 1, 0, 0, 0, -1])],     # supine sagittal
                ["PS", np.array([0, -1, 0, 0, 0, -1])],    # prone sagittal
                ["SC", np.array([1, 0, 0, 0, 0, -1])],     # supine coronal
                ["PC", np.array([-1, 0, 0, 0, 0, -1])]     # prone coronal
            ]

            for o in orientations:
                if (not np.any(np.array(np.round(iop - o[1]), dtype=np.int32))):
                    return o[0]
        # Return N/A if the orientation was not found or could not be determined
        return 'N/A'

    def GetNumberOfFrames(self):
        """Return the number of frames in a DICOM image file."""

        frames = 1
        if 'NumberOfFrames' in self.ds:
            frames = self.ds.NumberOfFrames.real
        else:
            try:
                self.ds.pixel_array
            except:
                return 0
            else:
                if (self.ds.pixel_array.ndim > 2):
                    if (self.ds.SamplesPerPixel == 1) and not \
                       (self.ds.PhotometricInterpretation == 'RGB'):
                        frames = self.ds.pixel_array.shape[0]
        return frames

    def GetRescaleInterceptSlope(self):
        """Return the rescale intercept and slope if present."""

        intercept, slope = 0, 1
        if ('RescaleIntercept' in self.ds and 'RescaleSlope' in self.ds):
            intercept = self.ds.RescaleIntercept if \
                isinstance(self.ds.RescaleIntercept, Number) else 0
            slope = self.ds.RescaleSlope if \
                isinstance(self.ds.RescaleSlope, Number) else 1

        return intercept, slope

    def GetImage(self, window=0, level=0, size=None, background=False,
                 frames=0):
        """Return the image from a DICOM image storage file."""

        # Return None if the Numpy pixel array cannot be accessed
        try:
            self.ds.pixel_array
        except:
            if size is None:
                return np.zeros(1, dtype=np.uint16)
            else:
                return np.zeros(size, dtype=np.uint16)

        # Samples per pixel are > 1 & RGB format
        if (self.ds.SamplesPerPixel > 1) and \
           (self.ds.PhotometricInterpretation == 'RGB'):

            # Little Endian
            if self.ds.file_meta.TransferSyntaxUID.is_little_endian:
                im = Image.frombuffer('RGB', (self.ds.Columns, self.ds.Rows),
                                      self.ds.PixelData, 'raw', 'RGB', 0, 1)
            # Big Endian
            else:
                im = np.rollaxis(self.ds.pixel_array.transpose(), 0, 2)

        # Otherwise the image is monochrome
        else:
            if ((window == 0) and (level == 0)):
                window, level = self.GetDefaultImageWindowLevel()
            # Rescale the slope and intercept of the image if present
            intercept, slope = self.GetRescaleInterceptSlope()
            # Get the requested frame if multi-frame
            if (frames > 0):
                pixel_array = self.ds.pixel_array[frames]
            else:
                pixel_array = self.ds.pixel_array

            rescaled_image = pixel_array * slope + intercept

            image = self.GetLUTValue(rescaled_image, window, level)
            im = Image.fromarray(image).convert('L')

        # Resize the image if a size is provided
        if size:
            im.thumbnail(size, Image.ANTIALIAS)

        # Add a black background if requested
        if background:
            bg = Image.new('RGBA', size, (0, 0, 0, 255))
            bg.paste(im, ((size[0] - im.size[0]) / 2,
                     (size[1] - im.size[1]) / 2))
            return bg

        return im

    def GetDefaultImageWindowLevel(self):
        """Determine the default window/level for the DICOM image."""

        window, level = 0, 0
        if ('WindowWidth' in self.ds) and ('WindowCenter' in self.ds):
            if isinstance(self.ds.WindowWidth, float):
                window = self.ds.WindowWidth
            elif isinstance(self.ds.WindowWidth, list):
                if (len(self.ds.WindowWidth) > 1):
                    window = self.ds.WindowWidth[1]
            if isinstance(self.ds.WindowCenter, float):
                level = self.ds.WindowCenter
            elif isinstance(self.ds.WindowCenter, list):
                if (len(self.ds.WindowCenter) > 1):
                    level = self.ds.WindowCenter[1]

        if ((window, level) == (0, 0)):
            wmax = 0
            wmin = 0
            # Rescale the slope and intercept of the image if present
            intercept, slope = self.GetRescaleInterceptSlope()
            pixel_array = self.ds.pixel_array * slope + intercept

            if (pixel_array.max() > wmax):
                wmax = pixel_array.max()
            if (pixel_array.min() < wmin):
                wmin = pixel_array.min()
            # Default window is the range of the data array
            window = int(abs(wmax) + abs(wmin))
            # Default level is the range midpoint minus the window minimum
            level = int(window / 2 - abs(wmin))
        return window, level

    def GetLUTValue(self, data, window, level):
        """Apply the RGB Look-Up Table for the data and window/level value."""

        lutvalue =  .piecewise(data,
                                [data <= (level - 0.5 - (window - 1) / 2),
                                 data > (level - 0.5 + (window - 1) / 2)],
                                [0, 255, lambda data:
                                 ((data - (level - 0.5)) / (window-1) + 0.5) *
                                 (255 - 0)])
        # Convert the resultant array to an unsigned 8-bit array to create
        # an 8-bit grayscale LUT since the range is only from 0 to 255
        return np.array(lutvalue, dtype=np.uint8)

    def GetPatientToPixelLUT(self):
        """Get the image transformation matrix from the DICOM standard Part 3
            Section C.7.6.2.1.1"""

        di = self.ds.PixelSpacing[0]
        dj = self.ds.PixelSpacing[1]
        orientation = self.ds.ImageOrientationPatient
        position = self.ds.ImagePositionPatient

        m = np.matrix(
            [[orientation[0]*di, orientation[3]*dj, 0, position[0]],
            [orientation[1]*di, orientation[4]*dj, 0, position[1]],
            [orientation[2]*di, orientation[5]*dj, 0, position[2]],
            [0, 0, 0, 1]])

        x = []
        y = []
        for i in range(0, self.ds.Columns):
            imat = m * np.matrix([[i], [0], [0], [1]])
            x.append(float(imat[0]))
        for j in range(0, self.ds.Rows):
            jmat = m * np.matrix([[0], [j], [0], [1]])
            y.append(float(jmat[1]))

        return (np.array(x), np.array(y))
