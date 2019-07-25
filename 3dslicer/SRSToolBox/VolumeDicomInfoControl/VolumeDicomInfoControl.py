import os
import unittest
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import logging


PATIENT_POSITION = {
  u'HFP' : u'Head First-Prone',
  u'HFS' : u'Head First-Supine',
  u'FFP' : u'Feet First-Prone',
  u'FFS' : u'Feet First-Supine',
  u'LFP' : u'Left First-Prone',
  u'LFS' : u'Left First-Supine',
  u'RFP' : u'Right First-Prone',
  u'RFS' : u'Right First-Supine',
  u'HFDR' : u'Head First-Decubitus Right',
  u'HFDL' : u'Head First-Decubitus Left',
  u'FFDR' : u'Feet First-Decubitus Right',
  u'FFDL' : u'Feet First-Decubitus Left',
  u'AFDR' : u'Anterior First-Decubitus Right',
  u'AFDL' : u'Anterior First-Decubitus Left',
  u'PFDR' : u'Posterior First-Decubitus Right',
  u'PFDL' : u'Posterior First-Decubitus Left',
}


TAGLIST = ['Patient ID', 'Patient Name', 'Patient Birth Date', 'Patient Sex',
  'Study ID', 'Study Date', 'Study Description', 'Study Instance UID', 'Series Number',
  'Modality', 'Series Date', 'Series Description', 'Protocol Name', 'Body Part Examined',
  'Patient Position', 'Columns', 'Rows', 'Number of Slices', 'Pixel Spacing',
  'Slice Thickness', 'Spacing Between Slices', 'Voxel Size', 'Field of View',
  'Series Instance UID']


class DicomAttributesDictionary(dict):
  """ Write doccumentation.
  """

  def __init__(self, volume_node=None):
    """ Write doccumentation.
    """

    if volume_node is not None:
      uids = volume_node.GetAttribute('DICOM.instanceUIDs')
      if uids is not None:
        #print(uids.split(' ')[0])
        self.populate(volume_node)
      else:
        #print('No UIDs!')
        self.populate()
    else:
      #print('NoneType object!')
      self.populate()

  def populate(self, volume_node=None):
    """ Write doccumentation.
    """

    if volume_node is not None:
      instances = volume_node.GetAttribute('DICOM.instanceUIDs').split(' ')
      self['Number of Slices'] = u'{0}'.format(len(instances))
      volume_file_name = slicer.dicomDatabase.fileForInstance(instances[0])
      self['Patient ID'] = slicer.dicomDatabase.fileValue(volume_file_name, '0010,0020')
      self['Patient Name'] = slicer.dicomDatabase.fileValue(volume_file_name, '0010,0010')

      ds = slicer.dicomDatabase.fileValue(volume_file_name, '0010,0030')
      self['Patient Birth Date'] =  u'{0}/{1}/{2}'.format(ds[4:6], ds[6:], ds[:4])

      self['Patient Sex'] = slicer.dicomDatabase.fileValue(volume_file_name, '0010,0040')
      self['Study ID'] = slicer.dicomDatabase.fileValue(volume_file_name, '0020,0010')
      
      ds = slicer.dicomDatabase.fileValue(volume_file_name, '0008,0020')
      self['Study Date'] = u'{0}/{1}/{2}'.format(ds[4:6], ds[6:], ds[:4])
      
      self['Study Description'] = slicer.dicomDatabase.fileValue(volume_file_name, '0008,1030')
      self['Study Instance UID'] = slicer.dicomDatabase.fileValue(volume_file_name, '0020,000D')
      self['Series Number'] = slicer.dicomDatabase.fileValue(volume_file_name, '0020,0011')
      self['Modality'] = slicer.dicomDatabase.fileValue(volume_file_name, '0008,0060')
      
      ds = slicer.dicomDatabase.fileValue(volume_file_name, '0008,0021')
      self['Series Date'] = u'{0}/{1}/{2}'.format(ds[4:6], ds[6:], ds[:4])
      
      self['Series Description'] = slicer.dicomDatabase.fileValue(volume_file_name, '0008,103E')
      self['Protocol Name'] = slicer.dicomDatabase.fileValue(volume_file_name, '0018,1030')
      self['Body Part Examined'] = slicer.dicomDatabase.fileValue(volume_file_name, '0018,0015')
      
      ds = slicer.dicomDatabase.fileValue(volume_file_name, '0018,5100')
      if PATIENT_POSITION.has_key(ds):
        self['Patient Position'] = PATIENT_POSITION[ds]
      else:
        self['Patient Position'] = ds
      
      self['Columns'] = slicer.dicomDatabase.fileValue(volume_file_name, '0028,0011')
      self['Rows'] = slicer.dicomDatabase.fileValue(volume_file_name, '0028,0010')

      ds = slicer.dicomDatabase.fileValue(volume_file_name, '0028,0030')
      self['Pixel Spacing'] = u'{0} mm'.format(ds)

      ds = slicer.dicomDatabase.fileValue(volume_file_name, '0018,0050')
      self['Slice Thickness'] = u'{0} mm'.format(ds)

      ds = slicer.dicomDatabase.fileValue(volume_file_name, '0018,0088')
      self['Spacing Between Slices'] = u'{0} mm'.format(ds)

      vs = volume_node.GetSpacing()
      self['Voxel Size'] = u'{0} mm x {1} mm x {2} mm'.format(vs[0], vs[1], vs[2])

      sd = volume_node.GetImageData().GetDimensions()
      fov = (vs[0] * sd[0], vs[1] * sd[1], vs[2] * sd[2])
      self['Field of View'] = u'{0} mm x {1} mm x {2} mm'.format(fov[0], fov[1], fov[2])

      self['Series Instance UID'] = slicer.dicomDatabase.fileValue(volume_file_name, '0020,000E')

    else:
      for i, key in enumerate(TAGLIST):
        self[key] = None


class DicomAttributesTableWidget(qt.QTableWidget):
  """ Write doccumentation.
  """

  def __init__(self, parent=None):
    """ Write doccumentation.
    """

    qt.QTableWidget.__init__(parent)

  #  self.setColumnCount(2)
  #  #self.table.setRowCount(24)
  #  self.setRowCount(len(TAGLIST))
  #  self.setHorizontalHeaderLabels(["Attribute", "Value"]) # This must follow table resize
  #  self.setAlternatingRowColors(True)
  #  self.setShowGrid(False)
  #  self.verticalHeader().hide()

  #  listdata = DicomAttributesDictionary(None)
  #  self.set_table_data(listdata)

  def set_table_data(self, data_dict):
    """ Write doccumentation.
    """

    for i, key in enumerate(TAGLIST):
      self.setItem(i, 0, qt.QTableWidgetItem(key))
      if data_dict(key) is not None:
        self.setItem(i, 1, qt.QTableWidgetItem(data_dict(key)))
      else:
        self.setItem(i, 1, qt.QTableWidgetItem(u'N/A'))
    self.resizeColumnsToContents()
    self.resizeRowsToContents()

  def set_up_table(self):
    """ Write documentation.
    """

    self.setColumnCount(2)
    self.setRowCount(len(TAGLIST))
    self.setHorizontalHeaderLabels(["Attribute", "Value"]) # This must follow table resize
    self.setAlternatingRowColors(True)
    self.setShowGrid(False)
    self.verticalHeader().hide()


#
# VolumeSelectControl
#

class VolumeDicomInfoControl(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = 'VolumeDicomInfoControl' # TODO make this more human readable by adding spaces
    self.parent.categories = ['WorkInProgress']
    self.parent.dependencies = []
    self.parent.contributors = ['Ljubomir Kurij (KCS)'] # replace with "Firstname Lastname (Organization)"
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

class VolumeDicomInfoControlWidget(ScriptedLoadableModuleWidget):
  """Uses ScriptedLoadableModuleWidget base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def setup(self):
    """ Write doccumentation.
    """

    ScriptedLoadableModuleWidget.setup(self)

    # Instantiate and connect widgets ...

    #
    # Parameters Area
    #
    parametersCollapsibleButton = ctk.ctkCollapsibleButton()
    parametersCollapsibleButton.text = 'Parameters'
    self.layout.addWidget(parametersCollapsibleButton)

    # Layout within the dummy collapsible button
    parametersFormLayout = qt.QFormLayout(parametersCollapsibleButton)

    #
    # input volume selector
    #
    self.inputSelector = slicer.qMRMLNodeComboBox()
    self.inputSelector.nodeTypes = ['vtkMRMLScalarVolumeNode']
    self.inputSelector.selectNodeUponCreation = True
    self.inputSelector.addEnabled = False
    self.inputSelector.removeEnabled = False
    self.inputSelector.noneEnabled = True
    self.inputSelector.showHidden = False
    self.inputSelector.showChildNodeTypes = False
    self.inputSelector.setMRMLScene(slicer.mrmlScene)
    self.inputSelector.setToolTip('Choose a volume with a DICOM images.')
    parametersFormLayout.addRow('Input Volume: ', self.inputSelector)

    #
    # Spawn table view for common DICOM tags and their values
    #
    self.table = DicomAttributesTableWidget(parametersCollapsibleButton)
    parametersFormLayout.addRow("Volume Info:", self.table)
    self.table.set_up_table()

    # connections
    self.inputSelector.connect('currentNodeChanged(bool)', self.onSelectNode)

    # Add vertical spacer
    self.layout.addStretch(1)

    # Refresh Table view state
    self.repaint()

  def cleanup(self):
    """ Write doccumentation.
    """

    pass

  def onSelect(self, node):
    """ Write doccumentation.
    """

    #slicer.app.processEvents()
    #DicomAttributesDictionary(node)
    #print("On select!")

  def onSelectNode(self, isValid):
    """ Write doccumentation.
    """

    if isValid:
      print(DicomAttributesDictionary(self.inputSelector.currentNode()))
    else:
      print(DicomAttributesDictionary(None))