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
try:
    # from pydicom.dicomio import read_file
    from pydicom.dataset import Dataset
except ImportError:
    # from dicom import read_file
    from dicom.dataset import Dataset
from random import randint
# from numbers import Number
# from six import PY2, iterkeys, string_types, BytesIO
# from six.moves import range
# from dicompylercore import dvh, util
# from dicompylercore.config import pil_available, shapely_available

# if pil_available:
#     from PIL import Image
# if shapely_available:
#     from shapely.geometry import Polygon

logger = logging.getLogger('dicomparser')


class DicomParser:
    """Parses DICOM files.
    """

    def __init__(self, dataset):

        if isinstance(dataset, Dataset):
            self._ds = dataset

        else:
            raise AttributeError('Not an pydicom.Dataset instance.')

# Methods to enable access to SOP Common attributes

    def SOPClassUID(self):
        """Determine the SOP Class UID of the current file.
        """

        if (self._ds.SOPClassUID == '1.2.840.10008.5.1.4.1.1.2'):
            return 'ct'
        elif (self._ds.SOPClassUID == '1.2.840.10008.5.1.4.1.1.2.1'):
            return 'enhancedct'
        elif (self._ds.SOPClassUID == '1.2.840.10008.5.1.4.1.1.2.2'):
            return 'legacyct'
        elif (self._ds.SOPClassUID == '1.2.840.10008.5.1.4.1.1.4'):
            return 'mri'
        elif (self._ds.SOPClassUID == '1.2.840.10008.5.1.4.1.1.4.1'):
            return 'enhancedmri'
        elif (self._ds.SOPClassUID == '1.2.840.10008.5.1.4.1.1.4.3'):
            return 'colormri'
        elif (self._ds.SOPClassUID == '1.2.840.10008.5.1.4.1.1.4.4'):
            return 'legacymri'
        elif (self._ds.SOPClassUID == '1.2.840.10008.5.1.4.1.1.128'):
            return 'pet'
        elif (self._ds.SOPClassUID == '1.2.840.10008.5.1.4.1.1.130'):
            return 'enhancedpet'
        elif (self._ds.SOPClassUID == '1.2.840.10008.5.1.4.1.1.128.1'):
            return 'legacypet'
        else:
            return 'other'

    def SOPInstanceUID(self):
        """Determine the SOP Class UID of the current file.
        """

        return self._ds.SOPInstanceUID

# Methods to enable access to Patient attributes

    def PatientName(self):
        """Return the full name of a patient for the current file.
        """

        if self._ds.PatientName:
            return self._ds.PatientName.family_comma_given()
        else:
            return 'N/A'

    def PatientSex(self):
        """Return sex of a patient for the current file.
        """

        if self._ds.PateientSex:
            if (self._ds.PatientSex == 'M'):
                return 'Male'
            elif (self._ds.PatientSex == 'F'):
                return 'Female'
            else:
                return 'other'
        else:
            return 'N/A'

    def PatientBirthDate(self):
        """Return birthday of a patient for the current file.
        """

        return self._ds.PatientBirthDate

# Methods to enable access to Patient attributes

    def StudyInstanceUID(self):
        """Return user or equipment generated Study identifier for the
        current file.
        """

        return self._ds.StudyInstanceUID

    def StudyID(self):
        """Return user or equipment generated Study identifier for the
        current file.
        """

        if self._ds.StudyID:
            return self._ds.StudyID
        else:
            return 'N/A'

    def StudyDescription(self):
        """Return institution-generated description or classification of the
        Study (component) performed.
        """

        if 'StudyDescription' in self._ds:
            if self._ds.StudyDescription:
                return self._ds.StudyDescription
            else:
                return 'N/A'
        else:
            return 'N/A'

    def StudyDate(self):
        """Return the date the Study started.
        """

        return self._ds.StudyDate

# Methods to enable access to Series attributes

    def SeriesInstanceUID(self):
        """Return unique identifier of the Series.
        """

        return self._ds.StudyInstanceUID

    def SeriesNumber(self):
        """Return a number that identifies a Series for the current file.
        """

        if str(self._ds.SeriesNumber):
            return str(self._ds.SeriesNumber)
        else:
            return str(randint(0, 65535))

    def SeriesDescription(self):
        """Return description of the Series.
        """

        if 'SeriesDescription' in self._ds:
            if self._ds.SeriesDescription:
                return self._ds.SeriesDescription
            else:
                return 'N/A'
        else:
            return 'N/A'

    def ProtocolName(self):
        """Return user-defined description of the conditions under which
        the Series was performed.
        """

        if 'ProtocolName' in self._ds:
            if self._ds.ProtocolName:
                return self._ds.ProtocolName
            else:
                return 'N/A'
        else:
            return 'N/A'

    def BodyPartExamined(self):
        """Return text description of the part of the body examined.
        """

        if 'BodyPartExamined' in self._ds:
            if self._ds.BodyPartExamined:
                return self._ds.BodyPartExamined
            else:
                return 'N/A'
        else:
            return 'N/A'

    def PatientPosition(self):
        """Return patient position descriptor relative to the equipment.
        """

        if 'PatientPosition' in self._ds:
            if (self._ds.PatientPosition == 'HFP'):
                return 'Head First-Prone'
            elif (self._ds.PatientPosition == 'HFS'):
                return 'Head First-Supine'
            elif (self._ds.PatientPosition == 'HFDR'):
                return 'Head First-Decubitus Right'
            elif (self._ds.PatientPosition == 'HFDL'):
                return 'Head First-Decubitus Left'
            elif (self._ds.PatientPosition == 'FFDR'):
                return 'Feet First-Decubitus Right'
            elif (self._ds.PatientPosition == 'FFDL'):
                return 'Feet First-Decubitus Left'
            elif (self._ds.PatientPosition == 'FFP'):
                return 'Feet First-Prone'
            elif (self._ds.PatientPosition == 'FFS'):
                return 'Feet First-Supine'
            elif (self._ds.PatientPosition == 'LFP'):
                return 'Left First-Prone'
            elif (self._ds.PatientPosition == 'LFS'):
                return 'Left First-Supine'
            elif (self._ds.PatientPosition == 'RFP'):
                return 'Right First-Prone'
            elif (self._ds.PatientPosition == 'RFS'):
                return 'Right First-Supine'
            elif (self._ds.PatientPosition == 'AFDR'):
                return 'Anterior First-Decubitus Right'
            elif (self._ds.PatientPosition == 'AFDL'):
                return 'Anterior First-Decubitus Left'
            elif (self._ds.PatientPosition == 'PFDR'):
                return 'Posterior First-Decubitus Right'
            elif (self._ds.PatientPosition == 'PFDL'):
                return 'Posterior First-Decubitus Left'
            else:
                return 'N/A'
        else:
            return 'N/A'

    def SeriesDate(self):
        """Return date the Series started.
        """

        if 'SeriesDate' in self._ds:
            return self._ds.SeriesDate
        else:
            return 'N/A'

# Methods to enable access to Image attributes

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
        return "NA"

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
