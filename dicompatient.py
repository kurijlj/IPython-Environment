#!/usr/bin/env python
# -*- coding: utf-8 -*-


from datetime import date, time
from enum import Enum


class PatientSex(Enum):
    """Class wrapping enumerated values describing patient sex. Accessible
    values are:
            na: indicating that patient sex information is not available
         other: indicating that patient is nor a female or a male
        female: indicating that patient is a female
          male: indicating that patient is a male
    """
    na = 0
    other = 1
    female = 2
    male = 3


class QualityControlSubject(Enum):
    """Class wrapping enumerated values describing if patient is a quality
    control subject (phantom) or not. Accessible values are:
         no: indicating that patient is not quality control subject
        yes: indicating that patient is a quality control subject
    """
    no = 0
    yes = 1


class DicomPatient(object):
    """Class representing DICOM Patient IE (information entity) objects.
    The Patient IE defines the characteristics of a patient who is subject of
    one or more medical studies.

    The Patient IE is modality independent.
    """

    def __init__(self):
        # Patient's full name
        self.name = str()
        # Primary hospital identification number or code for the patient.
        # In the Serbia it is "LBO"
        self.id = int()
        # Birthdate of the patient
        self.birthdate = date()
        # Sex of the named patient
        self.sex = PatientSex.na
        # Indicates whether or not the subject is a quality control phantom
        self.qcs = QualityControlSubject.no
        # List of studies for the named patient
        self.studies = list()


class DicomGeneralStudy(object):
    """Class representing DICOM General Study objects. General Study objects
    represent attributes that describe and identify the Study performed upon
    the Patient.
    """

    def __init__(self):
        # Unique identifier for the Study
        self.studyinstanceuid = int()
        # Date the Study started
        self.studydate = date()
        # Time the Study started
        self.studytime = time()
        # User or equipment generated Study identifier
        self.studyid = int()
        # Institution-generated description or classification of the Study
        # (component) performed
        self.studydesc = str()


class DicomPatientStudy(object):
    """Class representing DICOM Patient Study objects. Patient Study objects
    represent attributes that provide information about the Patient at the time
    the Study started.
    """

    def __init__(self):
        # Age of the Patient
        self.age = int()
        # Length or size of the Patient, in meters
        self.size = int()
        # Weight of the Patient, in kilograms
        self.weight = int()
        # Description of the admitting diagnosis (diagnoses)
        self.admtdgsdesc = str()


class DicomStudy(object):
    """Class representing DICOM Study IE (information entity) objects.
    The Study IE defines the characteristics of a medical study performed on
    a patient. A study is a collection of one or more series of medical images,
    presentation states, and/or SR documents that are logically related for
    the purpose of diagnosing a patient. Each study is associated with exactly
    one patient.

    A study may include composite instances that are created by a single
    modality, multiple modalities or by multiple devices of the same modality.

    The Study IE is modality independent.
    """

    def __init__(self):
        self.series = list()


class DicomSeries(object):
    """Class representing DICOM Series IE (information entity) objects.
    The Series IE defines the Attributes that are used to group composite
    instances into distinct logical sets. Each series is associated with
    exactly one Study.

    The following criteria group composite instances into a specific series:
        a. All composite instances within a series must be of the same modality
        b. Each series may be associated with exactly one Frame of Reference
           IE, and if so associated all composite instances within the series
           shall be spatially or temporally related to each other
        c. All composite instances within the series shall be created by the
           same equipment; therefore, each series is associated with exactly
           one Equipment IE
        d. All composite instances within a series shall have the same
           series information

    Presentation States shall be grouped into Series without Images (i.e., in a
    different Series from the Series containing the Images to which
    they refer).

    Note that the Series containing Grayscale, Color and Pseudo-Color Softcopy
    Presentation States and the Series containing the Images to which they
    refer are both contained within the same Study, except for Blended
    Presentation States, which may refer to images from different Studies.

    Waveforms shall be grouped into Series without Images. A Frame of Reference
    IE may apply to both Waveform Series and Image Series.

    SR Documents shall be grouped into Series without Images. The Frame of
    Reference IE may apply to SR Document Series, for SR Documents that
    contain 3D spatial coordinates relative to one or more spatial Frames of
    Reference, or temporal coordinates that require a temporal
    Frame of Reference.
    """

    def __init__(self):
        # Indicates equipment used to acquire given series
        self.equipment = DicomEquipment()
        self.frameofreference = DicomFrameOfReference()
        self.modalitylut = DicomModalityLUT()
        self.images = list()


class DicomEquipment(object):
    """Class representing DICOM Equipment IE (information entity) objects. The
    Equipment IE describes the particular device that produced the series of
    composite instances. A device may produce one or more series within
    a study. The Equipment IE does not describe the data acquisition or image
    creation Attributes used to generate the composite instances within
    a series. These Attributes are described in the composite instance specific
    IEs (e.g., the Image IE).
    """

    def __init__(self):
        # Manufacturer of the equipment that produced the composite instances.
        # Attribute requirement type 2
        self.manufacturer = str()
        # Institution where the equipment that produced the composite instances
        # is located. Attribute requirement type 3
        self.institutionname = str()
        # Mailing address of the institution where the equipment that produced
        # the composite instances is located. Attribute requirement type 3
        self.institutionaddress = str()
        # User defined name identifying the machine that produced the composite
        # instances. Attribute requirement type 3
        self.stationname = str()
        # Department in the institution where the equipment that produced the
        # composite instances is located. Attribute requirement type 3
        self.deptname = str()
        # Manufacturer's model name of the equipment that produced the
        # composite instances. Attribute requirement type 3
        self.modelname = str()
        # Manufacturer's serial number of the equipment that produced the
        # composite instances. Attribute requirement type 3
        self.devicesno = str()
        # Manufacturer's designation of software version of the equipment that
        # produced the composite instances. Attribute requirement type 3
        self.softwarever = str()
        # Identifier of the gantry or positioner. Attribute requirement type 3
        self.gantryid = str()
        # The inherent limiting resolution in mm of the acquisition equipment
        # for high contrast objects for the data gathering and reconstruction
        # technique chosen. Attribute requirement type 3
        self.spatialresolution = float()
        # Date and time when the image acquisition device calibration was last
        # changed in any way. Multiple entries may be used. Attribute
        # requirement type 3
        self.calibrationtime = list()
        # Single pixel value or one limit (inclusive) of a range of pixel
        # values used in an image to pad to rectangular format or to signal
        # background that may be suppressed. Attribute requirement type 1C
        self.pixelpaddingval = int()


class CalibrationTime(object):
    """Class representing date and time when the image acquisition device
    calibration was last changed in any way. The Attribute Date of Last
    Calibration may be supported alone, however, Time of Last Calibration
    Attribute has no meaning unless Attribute Date of Last Calibration is also
    supported. The order for each Attribute shall be from the oldest
    date/time to the most recent date/time. When the Attributes are both
    supported they shall be provided as pairs.
    """

    def __init__(self):
        # Date when the image acquisition device calibration was last changed
        # in any way. Attribute requirement type 3
        self.date = date()
        # Time when the image acquisition device calibration was last changed
        # in any way. Attribute requirement type 3
        self.time = time()


class DicomFrameOfReference(object):
    """Class representing DICOM Frame of Reference IE (information entity)
    objects. The Frame of Reference IE identifies the coordinate system that
    conveys spatial and/or temporal information of composite instances in
    a series.

    When present, a Frame of Reference IE may be related to one or more series.
    In this case, it provides the ability to spatially or temporally relate
    multiple series to each other. In such cases, the series may share the UID
    of the Frame of Reference, or alternatively, a Registration SOP Instance
    may specify the spatial relationship explicitly, as a spatial
    transformation. A Frame of Reference IE may also spatially register a Frame
    of Reference to an atlas.
    """

    def __init__(self):
        # Uniquely identifies the frame of reference for a Series. Attribute
        # requirement type 3
        self.foruid = str()
        # Part of the imaging target used as a reference. Attribute
        # requirement type 3
        self.prindicator = str()


class DicomImage(object):
    """Class representing DICOM Image IE (information entity) objects.
    The Image IE defines the Attributes that describe the pixel data of
    an image. The pixel data may be generated as a direct result of patient
    scanning (termed an Original Image) or the pixel data may be derived from
    the pixel data of one or more other images (termed a Derived Image). An
    image is defined by its image plane, pixel data characteristics, gray scale
    and/or color mapping characteristics, overlay planes and modality specific
    characteristics (acquisition parameters and image creation information).

    An image is related to a single series within a single study.

    The pixel data within an Image IE may be represented as a single frame of
    pixels or as multiple frames of pixel data. The frames of a Multi-frame
    image (a cine run or the slices of a volume) are sequentially ordered and
    share a number of common properties. A few Attributes may vary between
    frames (e.g., Time, Angular Displacement, Slice Increment). All common
    Image IE Attributes refer to the first frame of a multiple frame image.

    Overlay and Lookup Table data may be included within an Image IE only if
    this information is directly associated with the image.
    """

    def __init__(self):
        pass


class DicomModalityLUT(object):
    """Class representing DICOM Modality LUT IE (information entity) objects.
    The Modality LUT IE defines the Attributes that describe the transformation
    of manufacturer dependent pixel values into pixel values that are
    manufacturer independent (e.g., Hounsfield units for CT, Optical Density
    for film digitizers, etc.). The Modality LUT may be contained within an
    image, or a presentation state that references an image. When the
    transformation is linear, the Modality LUT is described by Rescale
    Slope (0028,1053) and Rescale Intercept (0028,1052). When the
    transformation is non-linear, the Modality LUT is described by Modality LUT
    Sequence (0028,3000).
    """

    def __init__(self):
        pass
