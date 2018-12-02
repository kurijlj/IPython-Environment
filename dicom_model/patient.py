# -*- coding: utf-8 -*-
'''
Dicom Patient IOD
'''
from pydicom.config import logger
from study import Study


class Patient(object):
    def __init__(self, dicom_dataset=None):
        self.studies = list()
        self.dicom_dataset = dicom_dataset
        self.studies.append(Study(dicom_dataset=dicom_dataset))

    def __repr__(self):
        try:
            output = "Patient: [{0}] {1} ({2})\n".format(
                    self.dicom_dataset.PatientSex(),
                    self.dicom_dataset.PatientName(),
                    self.dicom_dataset.PatientBirthDate()
                )
            for x in self.studies:
                output += repr(x)
            return output
        except Exception as e:
            logger.debug("trouble getting Patient data", exc_info=e)
            return "Patient: N/A\n"

    def __str__(self):
        try:
            return "Patient: [{0}] {1} ({2})\n".format(
                    self.dicom_dataset.PatientSex(),
                    self.dicom_dataset.PatientName(),
                    self.dicom_dataset.PatientBirthDate()
                )
        except Exception as e:
            logger.debug("trouble getting image PatientID", exc_info=e)
            return "None"

    def __eq__(self, other):
        try:
            selfid = self.dicom_dataset.PatientID()
            otherid = other.dicom_dataset.PatientID()
            return selfid == otherid
        except Exception as e:
            logger.debug("trouble comparing two patients", exc_info=e)
            return False

    def __ne__(self, other):
        try:
            selfid = self.dicom_dataset.PatientID()
            otherid = other.dicom_dataset.PatientID()
            return selfid != otherid
        except Exception as e:
            logger.debug("trouble comparing two patients", exc_info=e)
            return True

    def __getattr__(self, name):
        return getattr(self.dicom_dataset, name)

    def add_dataset(self, dataset):
        try:
            selfid = self.dicom_dataset.PatientID()
            datasetid = dataset.PatientID()
            if selfid == datasetid:
                for x in self.studies:
                    try:
                        x.add_dataset(dataset)
                        logger.debug("Part of this study")
                        break
                    except Exception:
                        logger.debug("Not part of this study")
                else:
                    self.studies.append(Study(dicom_dataset=dataset))
            else:
                raise KeyError("Not the same PatientIDs")
        except Exception as e:
            logger.debug(
                    "trouble comparing/adding study to patient",
                    exc_info=e
                )
            raise KeyError("Not the same PatientIDs")

    def same_patient(self, other):
        if isinstance(other, Patient):
            if self.dicom_dataset.PatientName().lower() ==\
                    other.dicom_dataset.PatientName().lower():
                if self.dicom_dataset.PatientBirthDate() ==\
                        other.dicom_dataset.PatientBirthDate():
                    if self.dicom_dataset.PatientSex() ==\
                            other.dicom_dataset.PatientSex():
                                return True
            else:
                return False
        else:
            return None
