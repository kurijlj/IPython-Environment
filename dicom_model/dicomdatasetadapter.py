#!/usr/bin/env python
# -*- coding: utf-8 -*-
# dicomparser.py
"""Class that parses and returns formatted DICOM RT data."""
# Copyright (c) 2009-2016 Aditya Panchal
# Copyright (c) 2009-2010 Roy Keyes
# This file is part of dicompyler-core, released under a BSD license.
#    See the file license.txt included with this distribution, also
#    available at https://github.com/dicompyler/dicompyler-core/


# import numpy as np
try:
    # from pydicom.dicomio import read_file
    from pydicom.dataset import Dataset
except ImportError:
    # from dicom import read_file
    from dicom.dataset import Dataset
# from random import randint
# from pydicom.config import logger
from collections import namedtuple
# from numbers import Number
# from six import PY2, iterkeys, string_types, BytesIO
# from six.moves import range
# from dicompylercore import dvh, util
# from dicompylercore.config import pil_available, shapely_available

# if pil_available:
#     from PIL import Image
# if shapely_available:
#     from shapely.geometry import Polygon


# Define named tuple class.
SliceShape = namedtuple('SliceShape', ['rows', 'columns'])
VoxelSize = namedtuple('VoxelSize', ['row', 'column', 'thickness'])


class DicomDatasetAdapter(object):
    """Adapter class for pydicom.Dataset object.
    """

    def __init__(self, dataset):

        if isinstance(dataset, Dataset):
            self._ds = dataset

        else:
            raise ValueError('{0}: Given object is not an pydicom.Dataset \
instance.').format(self.__class__)

# Methods to enable access to SOP Common attributes

    @property
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

        return 'other'

    @property
    def SOPInstanceUID(self):
        """Return th unique identifier of the SOP Instance.
        """

        if 'SOPInstanceUID' not in self._ds:
            raise NameError('{0}: Invalid dataset object. SOPInstanceUID \
attribute is missing.').format(self.__class__)
            return None

        return self._ds.SOPInstanceUID

# Methods to enable access to Patient attributes

    @property
    def PatientID(self):
        """Return primary identifier for the Patient.
        """

        if 'PatientID' not in self._ds:
            raise NameError('{0}: Invalid dataset instance. PatientID \
attribute is missing.').format(self.__class__)
            return None

        return self._ds.PatientID

    @property
    def PatientName(self):
        """Return the full name of a patient for the current file.
        """

        if 'PatientName' in self._ds:
            if self._ds.PatientName:
                return self._ds.PatientName.family_comma_given()

        return 'N/A'

    @property
    def PatientSex(self):
        """Return sex of a patient for the current file.
        """

        if 'PatientSex' in self._ds:
            if self._ds.PatientSex:
                if (self._ds.PatientSex == 'M'):
                    return 'Male'
                elif (self._ds.PatientSex == 'F'):
                    return 'Female'
                else:
                    return 'other'

        return 'N/A'

    @property
    def PatientBirthDate(self):
        """Return birthday of a patient for the current file.
        """

        if 'PatientBirthDate' in self._ds:
            if self._ds.PatientBirthDate:
                return self._ds.PatientBirthDate

        return 'N/A'

# Methods to enable access to Study attributes

    @property
    def StudyInstanceUID(self):
        """Return user or equipment generated Study identifier for the
        current file.
        """

        if 'StudyInstanceUID' not in self._ds:
            raise NameError('{0}: Invalid dataset instance. StudyInstanceUID \
attribute is missing.').format(self.__class__)
            return None

        return self._ds.StudyInstanceUID

    @property
    def StudyID(self):
        """Return user or equipment generated Study identifier for the
        current file.
        """

        if 'StudyID' in self._ds:
            if self._ds.StudyID:
                return self._ds.StudyID

        return 'N/A'

    @property
    def StudyDescription(self):
        """Return institution-generated description or classification of the
        Study (component) performed.
        """

        if 'StudyDescription' in self._ds:
            if self._ds.StudyDescription:
                return self._ds.StudyDescription

        return 'N/A'

    @property
    def StudyDate(self):
        """Return the date the Study started.
        """

        if 'StudyDate' in self._ds:
            if self._ds.StudyDate:
                return self._ds.StudyDate

        return 'N/A'

# Methods to enable access to Series attributes

    @property
    def SeriesInstanceUID(self):
        """Return unique identifier of the Series.
        """

        if 'SeriesInstanceUID' not in self._ds:
            raise NameError('{0}: Invalid dataset instance. SeriesInstanceUID \
attribute is missing.').format(self.__class__)
            return None

        return self._ds.SeriesInstanceUID

    @property
    def SeriesNumber(self):
        """Return a number that identifies a Series for the current file.
        """

        if 'SeriesNumber' in self._ds:
            if str(self._ds.SeriesNumber):
                return str(self._ds.SeriesNumber)

        return 'N/A'

    @property
    def SeriesDescription(self):
        """Return description of the Series.
        """

        if 'SeriesDescription' in self._ds:
            if self._ds.SeriesDescription:
                return self._ds.SeriesDescription

        return 'N/A'

    @property
    def Modality(self):
        """Return type of equipment that originally acquired the data used
        to create the images in this Series.
        """

        if 'Modality' in self._ds:
            if (self._ds.Modality == 'CT'):
                return 'CT'
            elif (self._ds.Modality == 'MR'):
                return 'MR'
            elif (self._ds.Modality == 'PT'):
                return 'PET'
            else:
                return 'other'

        return 'N/A'

    @property
    def ProtocolName(self):
        """Return user-defined description of the conditions under which
        the Series was performed.
        """

        if 'ProtocolName' in self._ds:
            if self._ds.ProtocolName:
                return self._ds.ProtocolName

        return 'N/A'

    @property
    def BodyPartExamined(self):
        """Return text description of the part of the body examined.
        """

        if 'BodyPartExamined' in self._ds:
            if self._ds.BodyPartExamined:
                return self._ds.BodyPartExamined

        return 'N/A'

    @property
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

        return 'N/A'

    @property
    def SeriesDate(self):
        """Return date the Series started.
        """

        if 'SeriesDate' in self._ds:
            if self._ds.SeriesDate:
                return self._ds.SeriesDate

        return 'N/A'

# Methods to enable access to Image attributes

    @property
    def SliceLocation(self):
        """Return relative position of the image plane expressed in mm.
        """

        if 'SliceLocation' in self._ds:
            if '' != self._ds.SliceLocation:
                return self._ds.SliceLocation

        return None

    @property
    def ImageOrientationPatient(self):
        """Return the direction cosines of the first row and the first column
        with respect to the patient.
        """

        if 'ImageOrientationPatient' in self._ds:
            return self._ds.ImageOrientationPatient

        return None

    @property
    def ImagePositionPatient(self):
        """Return the x, y, and z coordinates of the upper left hand corner
        (center of the first voxel transmitted) of the image, in mm.
        """

        if 'ImagePositionPatient' in self._ds:
            return self._ds.ImagePositionPatient

        return None

    @property
    def ImageShape(self):
        """Return named tuple representing number of rows and coluns of the
        current image.
        """

        rows = columns = 0.0
        if 'Rows' in self._ds:
            rows = self._ds.Rows
        if 'Columns' in self._ds:
            columns = self._ds.Columns

        return SliceShape(rows=rows, columns=columns)

    @property
    def ImageVoxelSize(self):
        """Return named tuple representing size of a voxel of the
        current image.
        """

        row = column = thickness = 1.0

        if 'PixelSpacing' in self._ds:
            row = self._ds.PixelSpacing[0]
            column = self._ds.PixelSpacing[1]

        if 'SliceThickness' in self._ds:
            if '' != self._ds.SliceThickness:
                thickness = self._ds.SliceThickness

        return VoxelSize(row, column, thickness)

    @property
    def ImageSpacing(self):
        """Return spacing between slices, in mm. The spacing is measured
        from the center-to-center of each slice.
        """

        if 'SpacingBetweenSlices' in self._ds:
            if '' != self._ds.SpacingBetweenSlices:
                return self._ds.SpacingBetweenSlices
        else:
            return None
