import os
import unittest
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import logging

#
# Auxiliary Constants, Functions and Classes
#

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

  def __init__(self, volumeNode):
    self.input_volume = volumeNode
    if self.input_volume.GetAttribute("DICOM.instanceUIDs").split(" "):
      instances = self.input_volume.GetAttribute("DICOM.instanceUIDs").split(" ")
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

      vs = self.input_volume.GetSpacing()
      self.voxel_size = u"{0} mm x {1} mm x {2} mm".format(vs[0], vs[1], vs[2])

      sd = self.input_volume.GetImageData().GetDimensions()
      fov = (vs[0] * sd[0], vs[1] * sd[1], vs[2] * sd[2])
      self.field_of_view = u"{0} mm x {1} mm x {2} mm".format(fov[0], fov[1], fov[2])

      self.series_instance_uid = slicer.dicomDatabase.fileValue(self.volume_file_name, "0020,000E")
      
    else:
      self.number_of_slices = None

  def supported_modality(self):
    """ Write doccumentation.
    """

    if (self.modality == u'CT' or self.modality == u'MR' or self.modality == u'PET'):
      return True
  
    return False

#
# SRSFiducials
#

class SRSFiducials(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "SRSFiducials" # TODO make this more human readable by adding spaces
    self.parent.categories = ["WorkInProgress"]
    self.parent.dependencies = []
    self.parent.contributors = ["Ljubomir Kurij (KCS)"] # replace with "Firstname Lastname (Organization)"
    self.parent.helpText = """
This is an example of scripted loadable module bundled in an extension.
It performs a simple thresholding on the input volume and optionally captures a screenshot.
"""
    self.parent.helpText += self.getDefaultModuleDocumentationLink()
    self.parent.acknowledgementText = """
This file was originally developed by Jean-Christophe Fillion-Robin, Kitware Inc.
and Steve Pieper, Isomics, Inc. and was partially funded by NIH grant 3P41RR013218-12S1.
""" # replace with organization, grant and thanks.

#
# SRSFiducialsWidget
#

class SRSFiducialsWidget(ScriptedLoadableModuleWidget):
  """Uses ScriptedLoadableModuleWidget base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def setup(self):
    ScriptedLoadableModuleWidget.setup(self)

    # Instantiate and connect widgets ...

    #
    # Parameters Area
    #
    parametersCollapsibleButton = ctk.ctkCollapsibleButton()
    parametersCollapsibleButton.text = "Parameters"
    self.layout.addWidget(parametersCollapsibleButton)

    # Layout within the dummy collapsible button
    parametersFormLayout = qt.QFormLayout(parametersCollapsibleButton)

    #
    # input volume selector
    #
    self.inputSelector = slicer.qMRMLNodeComboBox()
    self.inputSelector.nodeTypes = ["vtkMRMLScalarVolumeNode"]
    self.inputSelector.selectNodeUponCreation = True
    self.inputSelector.addEnabled = False
    self.inputSelector.removeEnabled = False
    self.inputSelector.noneEnabled = False
    self.inputSelector.showHidden = False
    self.inputSelector.showChildNodeTypes = False
    self.inputSelector.setMRMLScene( slicer.mrmlScene )
    self.inputSelector.setToolTip( "Pick the input to the algorithm." )
    parametersFormLayout.addRow("Input Volume: ", self.inputSelector)

    # 
    # Spawn table view for common DICOM tags and their values
    # 
    self.taglist = {
      "Patient ID" : "N/A",
      "Patient Name" : "N/A",
      "Patient Birth Date" : "N/A",
      "Patient Sex" : "N/A",
      "Study ID" : "N/A",
      "Study Date" : "N/A",
      "Study Description" : "N/A",
      "Study Instance UID" : "N/A",
      "Series Number" : "N/A",
      "Modality" : "N/A",
      "Series Date" : "N/A",
      "Series Description" : "N/A",
      "Protocol Name" : "N/A",
      "Body Part Examined" : "N/A",
      "Patient Position" : "N/A",
      "Columns" : "N/A",
      "Rows" : "N/A",
      "Number of Slices" : "N/A",
      "Pixel Spacing" : "N/A",
      "Slice Thickness" : "N/A",
      "Spacing Between Slices" : "N/A",
      "Voxel Size" : "N/A",
      "Field of View" : "N/A",
      "Series Instance UID" : "N/A",
    }
    self.table = qt.QTableWidget(parametersCollapsibleButton)
    self.table.setColumnCount(2)
    #self.table.setRowCount(24)
    self.table.setRowCount(len(self.taglist))
    self.table.setHorizontalHeaderLabels(["Attribute", "Value"]) # This must follow table resize

    i = 0
    for key, value in self.taglist.iteritems():
      self.table.setItem(i, 0, qt.QTableWidgetItem(key))
      self.table.setItem(i, 1, qt.QTableWidgetItem(value))
      i = i + 1
    #for i in range(25):
    #  self.table.setItem(i, 1, qt.QTableWidgetItem("N/A"))

    self.table.resizeColumnsToContents()
    self.table.resizeRowsToContents()
    self.table.setAlternatingRowColors(True)
    self.table.setShowGrid(False)
    self.table.verticalHeader().hide()
    parametersFormLayout.addRow("Volume Info:", self.table)

    # connections
    self.inputSelector.connect("currentNodeChanged(vtkMRMLNode*)", self.onSelect)

    # Add vertical spacer
    self.layout.addStretch(1)

    # Refresh Table view state
    self.onSelect(self.inputSelector.currentNode())

  def cleanup(self):
    pass

  def onSelect(self, node):
    slicer.app.processEvents()
    self.logic = VolumeInfoLogic(self.table, node)

  def onSelected(self):
    # Validate if input is selected
    cn = self.inputSelector.currentNode()
    print(type(cn))
    print(bool(cn))
    if bool(cn):
      print(bool(cn.GetImageData()))
      print(cn.GetID())
      if bool(cn.GetImageData()):
        volume_dif = DicomAttributesInterface(cn)
        print(bool(volume_diff))
        if volume_dif.number_of_slices:
          if volume_dif.supported_modality():
            print("Supported modality!")
            self.taglist["Patient ID"] = volume_dif.patient_id
            self.taglist["Patient Name"] = volume_dif.patient_name
            self.taglist["Patient Birth Date"] = volume_dif.patient_birth_date
            self.taglist["Patient Sex"] = volume_dif.patient_sex
            self.taglist["Study ID"] = volume_dif.study_id
            self.taglist["Study Date"] = volume_dif.study_date
            self.taglist["Study Description"] = volume_dif.study_description
            self.taglist["Study Instance UID"] = volume_dif.study_instance_uid
            self.taglist["Series Number"] = volume_dif.series_number
            self.taglist["Modality"] = volume_dif.modality
            self.taglist["Series Date"] = volume_dif.series_date
            self.taglist["Series Description"] = volume_dif.series_description
            self.taglist["Protocol Name"] = volume_dif.protocol_name
            self.taglist["Body Part Examined"] = volume_dif.body_part_examined
            self.taglist["Patient Position"] = volume_dif.patient_position
            self.taglist["Columns"] = volume_dif.columns
            self.taglist["Rows"] = volume_dif.rows
            self.taglist["Number of Slices"] = volume_dif.number_of_slices
            self.taglist["Pixel Spacing"] = volume_dif.pixel_spacing
            self.taglist["Slice Thickness"] = volume_dif.slice_thickness
            self.taglist["Spacing Between Slices"] = volume_dif.spacing_between_slices
            self.taglist["Voxel Size"] = volume_dif.voxel_size
            self.taglist["Field of View"] = volume_dif.field_of_view
            self.taglist["Series Instance UID"] = volume_dif.series_instance_uid

            i = 0
            for key, value in self.taglist.iteritems():
              self.table.setItem(i, 0, qt.QTableWidgetItem(key))
              self.table.setItem(i, 1, qt.QTableWidgetItem(value))
              i = i + 1

          else:
            slicer.util.errorDisplay('Modality not supported.')
      

#
# SRSFiducialsLogic
#

class VolumeInfoLogic(ScriptedLoadableModuleLogic):
  """This class should implement all the actual
  computation done by your module.  The interface
  should be such that other python code can import
  this class and make use of the functionality without
  requiring an instance of the Widget.
  Uses ScriptedLoadableModuleLogic base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, table, volume_node):
    self.taglist = ["Patient ID", "Patient Name", "Patient Birth Date", "Patient Sex",
      "Study ID", "Study Date", "Study Description", "Study Instance UID", "Series Number",
      "Modality", "Series Date", "Series Description", "Protocol Name", "Body Part Examined",
      "Patient Position", "Columns", "Rows", "Number of Slices", "Pixel Spacing",
      "Slice Thickness", "Spacing Between Slices", "Voxel Size", "Field of View",
      "Series Instance UID"]

    self.tags = dict()
    for i, item in enumerate(self.taglist):
      self.tags[item] = u"N/A"
    
    self.table = table
    self.node = volume_node

  def has_image_data(self):
    """This is an example logic method that
    returns true if the passed in volume
    node has valid image data
    """
    if not self.node:
      logging.debug('has_image_data failed: no volume node')
      return False
    if self.node.GetImageData() is None:
      logging.debug('has_image_data failed: no image data in volume node')
      return False
    return True

  def input_data_is_valid(self):
    """Validates if the input is selected
    """
    if not self.node:
      logging.debug('input_data_is_valid failed: no input volume node defined')
      return False
    return True

  def run(self):
    """
    Run the actual algorithm
    """

    if not self.input_data_is_valid():
      slicer.util.errorDisplay('No input volume.')
      return False
      
    if not self.has_image_data():
      slicer.util.errorDisplay('Input volume does not contain image data.')
      return False

    volume_info = DicomAttributesInterface(cn)
    if not volume_info.number_of_slices:
      slicer.util.errorDisplay('Input volume does not contain any slices.')
      return False

    if not volume_info.supported_modality():
      slicer.util.errorDisplay('Image modality not supported.')
      return False

    self.tags["Patient ID"] = volume_info.patient_id
    self.tags["Patient Name"] = volume_info.patient_name
    self.tags["Patient Birth Date"] = volume_info.patient_birth_date
    self.tags["Patient Sex"] = volume_info.patient_sex
    self.tags["Study ID"] = volume_info.study_id
    self.tags["Study Date"] = volume_info.study_date
    self.tags["Study Description"] = volume_info.study_description
    self.tags["Study Instance UID"] = volume_info.study_instance_uid
    self.tags["Series Number"] = volume_info.series_number
    self.tags["Modality"] = volume_info.modality
    self.tags["Series Date"] = volume_info.series_date
    self.tags["Series Description"] = volume_info.series_description
    self.tags["Protocol Name"] = volume_info.protocol_name
    self.tags["Body Part Examined"] = volume_info.body_part_examined
    self.tags["Patient Position"] = volume_info.patient_position
    self.tags["Columns"] = volume_info.columns
    self.tags["Rows"] = volume_info.rows
    self.tags["Number of Slices"] = volume_info.number_of_slices
    self.tags["Pixel Spacing"] = volume_info.pixel_spacing
    self.tags["Slice Thickness"] = volume_info.slice_thickness
    self.tags["Spacing Between Slices"] = volume_info.spacing_between_slices
    self.tags["Voxel Size"] = volume_info.voxel_size
    self.tags["Field of View"] = volume_info.field_of_view
    self.tags["Series Instance UID"] = volume_info.series_instance_uid

    for i, key in enumerate(self.taglist):
      self.table.setItem(i, 0, qt.QTableWidgetItem(key))
      self.table.setItem(i, 1, qt.QTableWidgetItem(self.tags[key]))

    return True


class SRSFiducialsTest(ScriptedLoadableModuleTest):
  """
  This is the test case for your scripted module.
  Uses ScriptedLoadableModuleTest base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def setUp(self):
    """ Do whatever is needed to reset the state - typically a scene clear will be enough.
    """
    slicer.mrmlScene.Clear(0)

  def runTest(self):
    """Run as few or as many tests as needed here.
    """
    self.setUp()
    self.test_SRSFiducials1()

  def test_SRSFiducials1(self):
    """ Ideally you should have several levels of tests.  At the lowest level
    tests should exercise the functionality of the logic with different inputs
    (both valid and invalid).  At higher levels your tests should emulate the
    way the user would interact with your code and confirm that it still works
    the way you intended.
    One of the most important features of the tests is that it should alert other
    developers when their changes will have an impact on the behavior of your
    module.  For example, if a developer removes a feature that you depend on,
    your test should break so they know that the feature is needed.
    """

    self.delayDisplay("Starting the test")
    #
    # first, get some data
    #
    import urllib
    downloads = (
        ('http://slicer.kitware.com/midas3/download?items=5767', 'FA.nrrd', slicer.util.loadVolume),
        )

    for url,name,loader in downloads:
      filePath = slicer.app.temporaryPath + '/' + name
      if not os.path.exists(filePath) or os.stat(filePath).st_size == 0:
        logging.info('Requesting download %s from %s...\n' % (name, url))
        urllib.urlretrieve(url, filePath)
      if loader:
        logging.info('Loading %s...' % (name,))
        loader(filePath)
    self.delayDisplay('Finished with download and loading')

    volumeNode = slicer.util.getNode(pattern="FA")
    logic = SRSFiducialsLogic()
    self.assertIsNotNone( logic.hasImageData(volumeNode) )
    self.delayDisplay('Test passed!')
