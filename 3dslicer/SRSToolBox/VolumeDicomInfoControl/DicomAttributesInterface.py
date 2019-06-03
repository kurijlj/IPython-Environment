
PATIENT_POSITION = {
    u"HFP" : u"Head First-Prone",
    u"HFS" : u"Head First-Supine",
    u"FFP" : u"Feet First-Prone",
    u"FFS" : u"Feet First-Supine",
    u"LFP" : u"Left First-Prone",
    u"LFS" : u"Left First-Supine",
    u"RFP" : u"Right First-Prone",
    u"RFS" : u"Right First-Supine",
    u"HFDR" : u"Head First-Decubitus Right",
    u"HFDL" : u"Head First-Decubitus Left",
    u"FFDR" : u"Feet First-Decubitus Right",
    u"FFDL" : u"Feet First-Decubitus Left",
    u"AFDR" : u"Anterior First-Decubitus Right",
    u"AFDL" : u"Anterior First-Decubitus Left",
    u"PFDR" : u"Posterior First-Decubitus Right",
    u"PFDL" : u"Posterior First-Decubitus Left",
}

class DicomAttributesInterface(object):
    """ Write doccumentation.
    """

    def __init__(self, volume_node):
        if volume_node.GetAttribute("DICOM.instanceUIDs").split(" ") is not None:
            instances = volume_node.GetAttribute("DICOM.instanceUIDs").split(" ")
            self.number_of_slices = u"{0}".format(len(instances))
            self.volume_file_name = slicer.dicomDatabase.fileForInstance(instances[0])
            self.patient_id = slicer.dicomDatabase.fileValue(self.volume_file_name, "0010,0020")
            self.patient_name = slicer.dicomDatabase.fileValue(self.volume_file_name, "0010,0010")

            ds = slicer.dicomDatabase.fileValue(self.volume_file_name, "0010,0030")
            self.patient_birth_date =  u"{0}/{1}/{2}".format(ds[4:6], ds[6:], ds[:4])

            self.patient_sex = slicer.dicomDatabase.fileValue(self.volume_file_name, "0010,0040")
            self.study_id = slicer.dicomDatabase.fileValue(self.volume_file_name, "0020,0010")

            ds = slicer.dicomDatabase.fileValue(self.volume_file_name, "0008,0020")
            self.study_date = u"{0}/{1}/{2}".format(ds[4:6], ds[6:], ds[:4])

            self.study_description = slicer.dicomDatabase.fileValue(self.volume_file_name, "0008,1030")
            self.study_instance_uid = slicer.dicomDatabase.fileValue(self.volume_file_name, "0020,000D")
            self.series_number = slicer.dicomDatabase.fileValue(self.volume_file_name, "0020,0011")
            self.modality = slicer.dicomDatabase.fileValue(self.volume_file_name, "0008,0060")

            ds = slicer.dicomDatabase.fileValue(self.volume_file_name, "0008,0021")
            self.series_date = u"{0}/{1}/{2}".format(ds[4:6], ds[6:], ds[:4])

            self.series_description = slicer.dicomDatabase.fileValue(self.volume_file_name, "0008,103E")
            self.protocol_name = slicer.dicomDatabase.fileValue(self.volume_file_name, "0018,1030")
            self.body_part_examined = slicer.dicomDatabase.fileValue(self.volume_file_name, "0018,0015")

            ds = slicer.dicomDatabase.fileValue(self.volume_file_name, "0018,5100")
            if PATIENT_POSITION.has_key(ds):
                self.patient_position = PATIENT_POSITION[ds]
            else:
                self.patient_position = ds

            self.columns = slicer.dicomDatabase.fileValue(self.volume_file_name, "0028,0011")
            self.rows = slicer.dicomDatabase.fileValue(self.volume_file_name, "0028,0010")

            ds = slicer.dicomDatabase.fileValue(self.volume_file_name, "0028,0030")
            self.pixel_spacing = u"{0} mm".format(ds)

            ds = slicer.dicomDatabase.fileValue(self.volume_file_name, "0018,0050")
            self.slice_thickness = u"{0} mm".format(ds)

            ds = slicer.dicomDatabase.fileValue(self.volume_file_name, "0018,0088")
            self.spacing_between_slices = u"{0} mm".format(ds)

            vs = volume_node.GetSpacing()
            self.voxel_size = u"{0} mm x {1} mm x {2} mm".format(vs[0], vs[1], vs[2])

            sd = volume_node.GetImageData().GetDimensions()
            fov = (vs[0] * sd[0], vs[1] * sd[1], vs[2] * sd[2])
            self.field_of_view = u"{0} mm x {1} mm x {2} mm".format(fov[0], fov[1], fov[2])

            self.series_instance_uid = slicer.dicomDatabase.fileValue(self.volume_file_name, "0020,000E")

        else:
            self.number_of_slices = None
            self.volume_file_name = None
            self.patient_id = None
            self.patient_name = None
            self.patient_birth_date = None
            self.patient_sex = None
            self.study_id = None
            self.study_date = None
            self.study_description = None
            self.study_instance_uid = None
            self.series_number = None
            self.modality = None
            self.series_date = None
            self.series_description = None
            self.protocol_name = None
            self.body_part_examined = None
            self.patient_position = None
            self.patient_position = None
            self.columns = None
            self.rows = None
            self.pixel_spacing = None
            self.slice_thickness = None
            self.spacing_between_slices = None
            self.voxel_size = None
            self.field_of_view = None
            self.series_instance_uid = None

    def supported_modality(self):
        """ Write doccumentation.
        """

        if (self.modality == u'CT' or self.modality == u'MR' or self.modality == u'PET'):
            return True

        return False

    def string_formatted_values(self):
        res = dict()
        for key, val in enumerate(self):
            if val is None:
                res[key] = 'N/A'
            else:
                res[key] = val