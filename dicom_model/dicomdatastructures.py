#!/usr/bin/env python
# -*- coding: utf-8 -*-
# dicomdatastructures.py


import logging
import numpy as np
try:
    from pydicom.dataset import Dataset
except ImportError:
    from dicom.dataset import Dataset


logger = logging.getLogger('dicomdatastructures')


# Define named tuple class.
class SliceLocation(object):
    """
    """

    def __init__(self, value):
        if isinstance(value, int):
            self._val = value
        else:
            self._val = None

    def __str__(self):
        if self._val is not None:
            return 'SliceLocation(value: \'{0}\')'.format(self._val)

        return str(self._val)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if isinstance(other, SliceLocation):
            result = isinstance(self.value_raw(), int) and\
                     isinstance(other.value_raw(), int)
            if result:
                return self.value_raw() == other.value_raw()

        else:
            raise AttributeError(
                    '{0}: Not an SliceLocation instance'
                    .format(self.__class__)
                )

        return False

    def __ne__(self, other):
        if isinstance(other, SliceLocation):
            result = isinstance(self.value_raw(), int) and\
                     isinstance(other.value_raw(), int)
            if result:
                return self.value_raw() != other.value_raw()

        else:
            raise AttributeError(
                    '{0}: Not an SliceLocation instance'
                    .format(self.__class__)
                )

        return False

    @property
    def value(self):
        if self._val is None:
            return self._val

        return round(self._val, 1)

    def value_raw(self):
        return self._val


class SliceShape(object):
    """
    """

    def __init__(self, rows: int = 0, columns: int = 0):
        self._shape = np.array([rows, columns])

    def __str__(self):
        return 'SliceShape(rows: \'{0}\', columns: \'{1}\')'.format(
                self._shape[0],
                self._shape[1]
            )

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        try:
            return self.shape_raw() == other.shape_raw()
        except Exception as e:
            logger.debug(
                    '{0}: trouble comparing two slice shapes'
                    .format(self.__class__),
                    exc_info=e
                )
            return False

    def __ne__(self, other):
        try:
            return self.shape_raw() != other.shape_raw()
        except Exception as e:
            logger.debug(
                    '{0}: trouble comparing two slice shapes'
                    .format(self.__class__),
                    exc_info=e
                )
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


class VoxelSize(object):
    """
    """

    def __init__(
                self,
                row: float = 1.0,
                column: float = 1.0,
                thickness: float = 1.0
            ):
        self._shape = np.array([row, column, thickness])

    def __str__(self):
        shape = np.round(self._shape, decimals=1)
        return 'VoxelSize(row: \'{0}\', column: \'{1}\', thickness: \'{2}\')'\
            .format(
                    shape[0],
                    shape[1],
                    shape[2],
                )

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        try:
            selfshp = np.round(self.shape_raw(), decimals=1)
            othershp = np.round(other.shape_raw(), decimals=1)
            return selfshp == othershp
        except Exception as e:
            logger.debug(
                    '{0}: trouble comparing two voxel sizes'
                    .format(self.__class__),
                    exc_info=e
                )
            return False

    def __ne__(self, other):
        try:
            selfshp = np.round(self.shape_raw(), decimals=1)
            othershp = np.round(other.shape_raw(), decimals=1)
            return selfshp != othershp
        except Exception as e:
            logger.debug(
                    '{0}: trouble comparing two voxel sizes'
                    .format(self.__class__),
                    exc_info=e
                )
            return False

    @property
    def row(self):
        return np.round(self._shape[0], decimals=1)

    @property
    def column(self):
        return np.round(self._shape[1], decimals=1)

    @property
    def thickness(self):
        return np.round(self._shape[2], decimals=1)

    def shape(self):
        shape = np.round(self._shape, decimals=1)
        return {
            'row': shape[0],
            'column': shape[1],
            'thickness': shape[2]
        }

    def shape_raw(self):
        return self._shape


class Patient(object):
    def __init__(self, dicom_dataset=None):
        self.studies = list()
        self.ds = dicom_dataset
        self.studies.append(Study(dicom_dataset=dicom_dataset))

    def __repr__(self):
        try:
            output = 'Patient: [{0}] {1} ({2})\n'.format(
                    self.ds.PatientSex,
                    self.ds.PatientName,
                    self.ds.PatientBirthDate
                )
            for x in self.studies:
                output += repr(x)
            return output
        except Exception as e:
            logger.debug(
                    '{0}: trouble getting Patient data'.format(self.__class__),
                    exc_info=e
                )
            return 'Patient: N/A\n'

    def __str__(self):
        try:
            return 'Patient {0}\n'.format(self.ds.PatientID)
        except Exception as e:
            logger.debug(
                    '{0}: trouble getting PatientID'.format(self.__class__),
                    exc_info=e
                )
            return None

    def __eq__(self, other):
        try:
            return self.ds.PatientID == other.ds.PatientID
        except Exception as e:
            logger.debug(
                    '{0}: trouble comparing two patients'
                    .format(self.__class__),
                    exc_info=e
                )
            return False

    def __ne__(self, other):
        try:
            return self.ds.PatientID != other.ds.PatientID
        except Exception as e:
            logger.debug(
                    '{0}: trouble comparing two patient'
                    .format(self.__class__),
                    exc_info=e
                )
            return True

    def __getattr__(self, name):
        return getattr(self.ds, name)

    def add_dataset(self, dataset):
        try:
            if self.ds.PatientID == dataset.PatientID:
                for x in self.studies:
                    try:
                        x.add_dataset(dataset)
                        logger.debug(
                                '{0}: Part of this study'
                                .format(self.__class__)
                            )
                        break
                    except Exception:
                        logger.debug(
                                '{0}: Not part of this study'
                                .format(self.__class__)
                            )
                else:
                    self.studies.append(Study(dicom_dataset=dataset))
            else:
                raise KeyError(
                        '{0}: Not the same PatientIDs'
                        .format(self.__class__)
                    )
        except Exception as e:
            logger.debug(
                    '{0}: trouble comparing/adding study to patient'
                    .format(self.__class__),
                    exc_info=e
                )
            raise KeyError(
                    '{0}: Not the same PatientIDs'.format(self.__class__)
                )

    def same_patient(self, other):
        if isinstance(other, Patient):
            nm = self.ds.PatientName.lower() == other.ds.PatientName.lower()
            bd = self.ds.PatientBirthDate == other.ds.PatientBirthDate
            gd = self.ds.PatientSex == other.ds.PatientSex
            if nm and bd and gd:
                return True
            return False

        return None


class Study(object):
    def __init__(self, dicom_dataset=None):
        self.series = list()
        self.ds = dicom_dataset
        self.series.append(Series(dicom_dataset=dicom_dataset))

    def __repr__(self):
        try:
            output = '\tStudy: [{0}] {1} ({2})\n'.format(
                    self.ds.StudyID,
                    self.ds.StudyDescription,
                    self.ds.StudyDate,
                )
            for x in self.series:
                output += repr(x)
            return output
        except Exception as e:
            logger.debug(
                    '{0}: trouble getting Image SOPInstanceUID'.
                    format(self.__class__),
                    exc_info=e
                )
            return None

    def __str__(self):
        try:
            return 'Study {0}\n'.format(self.ds.StudyInstanceUID)
        except Exception as e:
            logger.debug(
                    '{0}: trouble getting image StudyInstanceUID'.
                    format(self.__class__),
                    exc_info=e
                )
            return None

    def __eq__(self, other):
        try:
            return self.ds.StudyInstanceUID == other.ds.StudyInstanceUID
        except Exception as e:
            logger.debug(
                    '{0} trouble comparing two Studies'
                    .format(self.__class__),
                    exc_info=e
                )
            return False

    def __ne__(self, other):
        try:
            return self.ds.StudyInstanceUID != other.ds.StudyInstanceUID
        except Exception as e:
            logger.debug(
                    '{0} trouble comparing two Studies'
                    .format(self.__class__),
                    exc_info=e
                )
            return True

    def __getattr__(self, name):
        return getattr(self.ds, name)

    def add_dataset(self, dataset):
        try:
            if self.ds.StudyInstanceUID == dataset.StudyInstanceUID:
                for x in self.series:
                    try:
                        x.add_dataset(dataset)
                        logger.debug(
                                '{0}: Part of this series'
                                .format(self.__class__)
                            )
                        break
                    except Exception:
                        logger.debug(
                                '{0}: Not part of this series'
                                .format(self.__class__)
                            )
                else:
                    self.series.append(Series(dicom_dataset=dataset))
            else:
                raise KeyError(
                        '{0}: Not the same StudyInstanceUIDs'
                        .format(self.__class__)
                    )
        except Exception as e:
            logger.debug(
                    '{0}: trouble adding series to study'
                    .format(self.__class__),
                    exc_info=e
                )
            raise KeyError(
                    '{0}: Not the same StudyInstanceUIDs'
                    .format(self.__class__)
                )


class Series(object):
    def __init__(self, dicom_dataset=None):
        self.images = list()
        self.ds = dicom_dataset
        self.images.append(Image(dicom_dataset=dicom_dataset))

    def __repr__(self):
        try:
            output = '\t\tSeries: [{0} {1}] {2} ({3} {4})\n'.format(
                    self.ds.Modality,
                    self.ds.ProtocolName,
                    self.ds.SeriesDescription,
                    self.ds.BodyPartExamined,
                    self.ds.PatientPosition
                )
            for x in self.images:
                output += repr(x)
            return output
        except Exception as e:
            logger.debug(
                    '{0}: trouble getting Series data'
                    .format(self.__class__),
                    exc_info=e
                )
            return '\t\tSeries: N/A\n'

    def __str__(self):
        try:
            return 'Series {0}\n'.format(self.ds.SeriesInstanceUID)
        except Exception as e:
            logger.debug(
                    '{0}: trouble getting image SeriesInstanceUID'.
                    format(self.__class__),
                    exc_info=e
                )
            return None

    def __eq__(self, other):
        try:
            return self.ds.SeriesInstanceUID == other.ds.SeriesInstanceUID
        except Exception as e:
            logger.debug(
                    '{0}: trouble comparing two Series'.
                    format(self.__class__),
                    exc_info=e
                )
            return False

    def __ne__(self, other):
        try:
            return self.ds.SeriesInstanceUID != other.ds.SeriesInstanceUID
        except Exception as e:
            logger.debug(
                    '{0}: trouble comparing two Series'.
                    format(self.__class__),
                    exc_info=e
                )
            return True

    def __getattr__(self, name):
        return getattr(self.ds, name)

    def add_dataset(self, dataset):
        try:
            if self.ds.SeriesInstanceUID == dataset.SeriesInstanceUID:
                for x in self.images:
                    if x.SOPInstanceUID == dataset.SOPInstanceUID:
                        logger.debug(
                                '{0}: Image is already part of this series'.
                                format(self.__class__)
                            )
                        break
                else:
                    self.images.append(Image(dicom_dataset=dataset))

            else:
                raise KeyError(
                        '{0}: Not the same SeriesInstanceUIDs'
                        .format(self.__class__)
                    )
        except Exception as e:
            logger.debug(
                    '{0}: trouble adding image to series'.
                    format(self.__class__),
                    exc_info=e
                )
            raise KeyError(
                    '{0}: Not the same SeriesInstanceUIDs'
                    .format(self.__class__)
                )


class Image(object):
    def __init__(self, dicom_dataset=None):
        self.ds = dicom_dataset

    def __repr__(self):
        try:
            output = "\t\t\tImage:[{0}] {1} {2} {3} ({4} {5})\n".format(
                    self.ds.SliceLocation.value,
                    np.round(self.ds.ImageOrientationPatient, decimals=1),
                    np.round(self.ds.ImagePositionPatient, decimals=1),
                    self.ds.ImageShape,
                    self.ds.ImageVoxelSize,
                    self.ds.ImageSpacing,
                )
            return output
        except Exception as e:
            print(e)
            logger.debug(
                    '{0}: trouble getting Image data'.
                    format(self.__class__),
                    exc_info=e
                )
            return '\t\t\tImage: N/A\n'

    def __str__(self):
        try:
            return 'Image {0}\n'.format(self.ds.SOPInstanceUID)
        except Exception as e:
            logger.debug(
                    '{0}: trouble getting Image SOPInstanceUID'.
                    format(self.__class__),
                    exc_info=e
                )
            return None

    def __eq__(self, other):
        try:
            return self.ds.SOPInstanceUID == other.ds.SOPInstanceUID
        except Exception as e:
            logger.debug(
                    '{0}: trouble comparing two Images'.
                    format(self.__class__),
                    exc_info=e
                )
            return False

    def __ne__(self, other):
        try:
            return self.ds.SOPInstanceUID != other.ds.SOPInstanceUID
        except Exception as e:
            logger.debug(
                    '{0}: trouble comparing two Images'.
                    format(self.__class__),
                    exc_info=e
                )
            return True

    def __getattr__(self, name):
        return getattr(self.ds, name)


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
                return SliceLocation(self._ds.SliceLocation)

        return SliceLocation(None)

    @property
    def ImageOrientationPatient(self):
        """Return the direction cosines of the first row and the first column
        with respect to the patient.
        """

        if 'ImageOrientationPatient' in self._ds:
            return np.array(self._ds.ImageOrientationPatient)

        return None

    @property
    def ImagePositionPatient(self):
        """Return the x, y, and z coordinates of the upper left hand corner
        (center of the first voxel transmitted) of the image, in mm.
        """

        if 'ImagePositionPatient' in self._ds:
            return np.array(self._ds.ImagePositionPatient)

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
        current image in mm.
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
