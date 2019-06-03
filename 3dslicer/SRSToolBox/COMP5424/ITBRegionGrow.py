from __main__ import vtk, qt, ctk, slicer
from vtk.util import numpy_support
import numpy as np

#
# ITBRegionGrow
#
class ITBRegionGrow:
  def __init__(self, parent):
    parent.title = "ITB RegionGrow Segmentation"
    parent.categories = ["COMP5424"]
    parent.dependencies = []
    parent.contributors = [ """
    Sidong Liu (USYD) 
    Siqi Liu (Simense)
    """]
    parent.helpText = """
    Example of scripted loadable extension for the ITB Medical Image Segmentation lab.
    """
    parent.acknowledgementText = """
    This python program shows a simple implementation of the 3D region growing algorithm for 
    the ITB LabW5.
    """ 
    self.parent = parent

#
# The main widget
#
class ITBRegionGrowWidget:
  def __init__(self, parent = None):
    if not parent:
      self.parent = slicer.qMRMLWidget()
      self.parent.setLayout(qt.QVBoxLayout())
      self.parent.setMRMLScene(slicer.mrmlScene)
    else:
      self.parent = parent
    self.layout = self.parent.layout()
    if not parent:
      self.setup()
      self.parent.show()

    self.roiCounter = 0
    self.roiID = ""

  #  Setup the layout
  def setup(self):

    # Collapsible button
    self.laplaceCollapsibleButton = ctk.ctkCollapsibleButton()
    self.laplaceCollapsibleButton.text = "3D Region Grow Inputs"

    # Layout within the laplace collapsible button
    self.segmentationFormLayout = qt.QFormLayout(self.laplaceCollapsibleButton)
    self.inputSelector = slicer.qMRMLNodeComboBox()
    self.inputSelector.nodeTypes = ( ("vtkMRMLScalarVolumeNode"), "" )
    self.inputSelector.addEnabled = True
    self.inputSelector.removeEnabled = True
    self.inputSelector.setMRMLScene( slicer.mrmlScene )
    self.seedingSelector = slicer.qMRMLNodeComboBox()
    self.seedingSelector.nodeTypes = ( ("vtkMRMLLabelMapVolumeNode"), "" )
    self.seedingSelector.addEnabled = True
    self.seedingSelector.removeEnabled = True
    self.seedingSelector.setMRMLScene( slicer.mrmlScene )

    # Change the parameters
    #selCriteria = updateParameterCollapsibleButtion
    updateParameterCollapsibleButtion      = ctk.ctkCollapsibleButton()
    updateParameterCollapsibleButtion.text = "Selection Criteria"
    self.layout.addWidget(updateParameterCollapsibleButtion)
    updateParameterFormLayout              = qt.QFormLayout(updateParameterCollapsibleButtion)


    chooseGlobalFrame, chooseGlobalSlider, chooseGlobalSliderSpinBox = numericInputFrame(self.parent, \
                                                              "Maximum Global Intensity Difference:   ", \
                                                              "Determin the global range of intensity values", \
                                                              1, 50, 1, 0)
    updateParameterFormLayout.addWidget(chooseGlobalFrame)

    chooseLocalFrame, chooseLocalSlider, chooseLocalSliderSpinBox = numericInputFrame(self.parent, \
                                                              "Maximum Local Intensity Difference:     ", \
                                                              "Determine the local range of of intensity values", 0, 50, 1, 0)
    updateParameterFormLayout.addWidget(chooseLocalFrame)

    
    class state(object):
      maxGlobalDiff    = 5
      maxLocalDiff     = 5

    scopeLocals    = locals()

    def connect(obj, evt, cmd):
      def callback(*args):
        currentLocals = scopeLocals.copy()
        currentLocals.update({'args':args})
        exec cmd in globals(), currentLocals
        updateGUI()
      obj.connect(evt, callback)

    def updateGUI():
      chooseGlobalSlider.value          = state.maxGlobalDiff
      chooseGlobalSliderSpinBox.value   = state.maxGlobalDiff
      chooseLocalSlider.value           = state.maxLocalDiff
      chooseLocalSliderSpinBox.value    = state.maxLocalDiff
      
    connect(chooseGlobalSlider, 'valueChanged(double)', 'state.maxGlobalDiff = args[0]')
    connect(chooseGlobalSliderSpinBox, 'valueChanged(double)', 'state.maxGlobalDiff = args[0]')
    connect(chooseLocalSlider, 'valueChanged(double)', 'state.maxLocalDiff = args[0]')
    connect(chooseLocalSliderSpinBox, 'valueChanged(double)', 'state.maxLocalDiff = args[0]')

    updateGUI()
    self.updateGUI  = updateGUI
    self.state      = state
    self.layout.addStretch(1)


  # When the apply button is clicked
  def onApply(self):

    # Read in the input volume
    inputVolume = slicer.mrmlScene.GetNodeByID('vtkMRMLScalarVolumeNode1')
    inputVolumeData = slicer.util.array(inputVolume.GetID())

    # Read in the seeding ROI
    idString = ""
    if slicer.util.getNode('vtkMRMLLabelMapVolumeNode1') is None:
      idString = 'vtkMRMLLabelMapVolumeNode2'
    else:
    	idString = 'vtkMRMLLabelMapVolumeNode1'  
    seedingROI = slicer.mrmlScene.GetNodeByID(idString)
    seedingROIData  = slicer.util.array(seedingROI.GetID())
    
    
    # Copy image node, create a new volume node
    self.roiCounter += 1
    outputROI_name = "MRBrainTumor" + str(self.roiCounter) + "-label_grow"
    outputROI       = slicer.modules.volumes.logic().CloneVolume(slicer.mrmlScene, seedingROI, outputROI_name)
    outputROIData   = slicer.util.array(outputROI.GetID())
    
    # Get the mean of the seeding ROI
    seedingROI_coords   = np.where(seedingROIData > 0)
    seedingROI_values   = inputVolumeData[seedingROI_coords]
    
    # # the location of the seeding voxel
    sx = seedingROI_coords[0][seedingROI_values.argmax()]
    sy = seedingROI_coords[1][seedingROI_values.argmax()]
    sz = seedingROI_coords[2][seedingROI_values.argmax()]

    # The global parameter is used to select the voxels within a range  
    ROI_min = seedingROI_values.min() - self.state.maxGlobalDiff 
    ROI_max = seedingROI_values.max() + self.state.maxGlobalDiff

    # Dimension of the input volume 
    dx, dy, dz = inputVolumeData.shape

    iteration = 0
    # the local searching radius
    radius = 1

    while True:
        
        iteration = iteration + 1
        #print 'INFO Current Iteration: ', iteration
        
        # First stop criterion: reach the boundary of the image
        searching_extend    = np.array([iteration+radius-sx, sx+iteration+radius+1-dx, \
                                         iteration+radius-sy, sy+iteration+radius+1-dy, \
                                         iteration+radius-sz, sz+iteration+radius+1-dz])
        if (searching_extend >= 0).any(): 
            break

        # Second stop criterion: there is no new voxel with in the global value range 
        new_voxel_coords    = find_new_voxels(sx, sy, sz, iteration)
        new_voxel_values    = inputVolumeData[new_voxel_coords[:, 0], new_voxel_coords[:, 1], new_voxel_coords[:, 2]]
        glb_voxel_indices   = np.where(np.logical_and(new_voxel_values < ROI_max, new_voxel_values > ROI_min))        
        
        if not glb_voxel_indices: 
            break
        
        else:
            for i in glb_voxel_indices[0]:
                lx, ly, lz          = new_voxel_coords[i, :] 
                patch_boolen        = outputROIData[lx - 1 : lx + 2, ly - 1 : ly + 2, lz - 1 : lz + 2]   
                
                if patch_boolen.sum() > 1:
                    local_value     = inputVolumeData[lx, ly, lz] 
                    patch_values    = inputVolumeData[lx - 1 : lx + 2, ly - 1 : ly + 2, lz - 1 : lz + 2]  
                    boolen_values   = patch_values[:] * patch_boolen[:]
                    
                    existing_values = boolen_values[np.where(boolen_values > 0)]
                    local_min       = existing_values.min() - self.state.maxLocalDiff
                    local_max       = existing_values.max() + self.state.maxLocalDiff
                    
                    # Third stop criterion: the voxel value is beyond the range of local existing neighbors
                    if local_value < local_max and local_value > local_min:
                        outputROIData[lx, ly, lz] = 1

    #######################################################

    outputROI.GetImageData().Modified()
    
    # make the output volume appear in all the slice views
    selectionNode = slicer.app.applicationLogic().GetSelectionNode()
    selectionNode.SetReferenceActiveLabelVolumeID(outputROI.GetID())
    slicer.app.applicationLogic().PropagateVolumeSelection(0)
    
  # 
  # Supporting Functions
  # 
  # Reload the Module
  def onReload(self, moduleName = "ITBRegionGrow"):
    import imp, sys, os, slicer
    widgetName = moduleName + "Widget"
    fPath = eval('slicer.modules.%s.path' % moduleName.lower())
    p = os.path.dirname(fPath)
    if not sys.path.__contains__(p):
      sys.path.insert(0,p)
    fp = open(fPath, "r")
    globals()[moduleName] = imp.load_module(
        moduleName, fp, fPath, ('.py', 'r', imp.PY_SOURCE))
    fp.close()
    print "the module name to be reloaded,", moduleName
    # find the Button with a name 'moduleName Reolad', then find its parent (e.g., a collasp button) and grand parent (moduleNameWidget)
    parent = slicer.util.findChildren(name = '%s Reload' % moduleName)[0].parent().parent()
    for child in parent.children():
      try:
        child.hide()
      except AttributeError:
        pass
    item = parent.layout().itemAt(0)
    while item:
      parent.layout().removeItem(item)
      item = parent.layout().itemAt(0)
    globals()[widgetName.lower()] = eval('globals()["%s"].%s(parent)' % (moduleName, widgetName))
    globals()[widgetName.lower()].setup()


# Numeric parameter input
def numericInputFrame(parent, label, tooltip, minimum, maximum, step, decimals):
  inputFrame              = qt.QFrame(parent)
  inputFrame.setLayout(qt.QHBoxLayout())
  inputLabel              = qt.QLabel(label, inputFrame)
  inputLabel.setToolTip(tooltip)
  inputFrame.layout().addWidget(inputLabel)
  inputSpinBox            = qt.QDoubleSpinBox(inputFrame)
  inputSpinBox.setToolTip(tooltip)
  inputSpinBox.minimum    = minimum
  inputSpinBox.maximum    = maximum
  inputSpinBox.singleStep = step
  inputSpinBox.decimals   = decimals
  inputFrame.layout().addWidget(inputSpinBox)
  inputSlider             = ctk.ctkDoubleSlider(inputFrame)
  inputSlider.minimum     = minimum
  inputSlider.maximum     = maximum
  inputSlider.orientation = 1
  inputSlider.singleStep  = step
  inputSlider.setToolTip(tooltip)
  inputFrame.layout().addWidget(inputSlider)
  return inputFrame, inputSlider, inputSpinBox

# define the cartesian function
def cartesian(arrays, out = None):
    arrays = [np.asarray(x) for x in arrays]
    dtype = arrays[0].dtype    
    n = np.prod([x.size for x in arrays])
    if out is None:
        out = np.zeros([n, len(arrays)], dtype = dtype)    
    m = n / arrays[0].size
    out[:,0] = np.repeat(arrays[0], m)    
    if arrays[1:]:
        cartesian(arrays[1:], out = out[0:m, 1:])
        for j in xrange(1, arrays[0].size):
            out[j*m:(j+1)*m, 1:] = out[0:m, 1:]    
    return out

# find the coordinates of new voxels
def find_new_voxels(sx, sy, sz, iteration, out = None):

    new_voxel_coordinates_yz = cartesian((np.array([sx-iteration, sx+iteration]), \
                                      np.arange(sy-iteration, sy+iteration+1), \
                                      np.arange(sz-iteration, sz+iteration+1)))

    new_voxel_coordinates_xz = cartesian((np.arange(sx-iteration+1, sx+iteration), \
                                      np.array([sy-iteration, sy+iteration]), \
                                      np.arange(sz-iteration, sz+iteration+1)))

    new_voxel_coordinates_xy = cartesian((np.arange(sx-iteration+1, sx+iteration), \
                                      np.arange(sy-iteration+1, sy+iteration), \
                                      np.array([sz-iteration, sz+iteration])))

    new_voxel_coordinates = np.concatenate((new_voxel_coordinates_yz, np.concatenate((new_voxel_coordinates_xz, new_voxel_coordinates_xy))))
    return new_voxel_coordinates
