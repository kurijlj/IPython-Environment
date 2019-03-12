# -*- coding: utf-8 -*-
'''
Dicom Image IOD
'''
from pydicom.config import logger


class Image(object):
    def __init__(self, dicom_dataset=None):
        self.dicom_dataset = dicom_dataset

    def __repr__(self):
        try:
            output = "\t\t\tImage:[{0}] {1} {2} {3} ({4} {5})\n".format(
                    self.dicom_dataset.SliceLocation(),
                    self.dicom_dataset.ImagePositionPatient(),
                    self.dicom_dataset.ImageOrientationPatient(),
                    self.dicom_dataset.Shape(),
                    self.dicom_dataset.ImageSpacing(),
                    self.dicom_dataset.VoxelSize(),
                )
            return output
        except Exception as e:
            logger.debug("trouble getting Series data", exc_info=e)
            return "\t\t\tImage: N/A\n"

    def __str__(self):
        try:
            return "\t\t\tImage:[{0} {1} {2}] {3} ({4} {5})\n".format(
                    self.dicom_dataset.SliceLocation(),
                    self.dicom_dataset.ImagePositionPatient(),
                    self.dicom_dataset.ImageOrientationPatient(),
                    self.dicom_dataset.Shape(),
                    self.dicom_dataset.ImageSpacing(),
                )
        except Exception as e:
            logger.debug("trouble getting image SOPInstanceUID", exc_info=e)
            return "None"

    def __eq__(self, other):
        try:
            selfuid = self.dicom_dataset.SOPInstanceUID()
            otheruid = other.dicom_dataset.SOPInstanceUID()
            return selfuid == otheruid
        except Exception as e:
            logger.debug("trouble comparing two Images", exc_info=e)
            return False

    def __ne__(self, other):
        try:
            selfuid = self.dicom_dataset.SOPInstanceUID()
            otheruid = other.dicom_dataset.SOPInstanceUID()
            return selfuid != otheruid
        except Exception as e:
            logger.debug("trouble comparing two Images", exc_info=e)
            return True

    def __getattr__(self, name):
        return getattr(self.dicom_dataset, name)
