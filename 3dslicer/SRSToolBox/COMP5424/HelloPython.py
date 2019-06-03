'''
Max Schultz
SID: 440176697

MAIN FILE FOR TOPIC E - COMP5424
'''

from __main__ import vtk, qt, ctk, slicer
from vtk.util import numpy_support

import numpy as np
import vtkSegmentationCorePython as vtkSegmentationCore
import vtkSlicerSegmentationsModuleLogicPython as vtkSlicerSegmentationsModuleLogic
import SampleData

import unittest
import qt
import slicer
import EditorLib
from EditorLib.EditUtil import EditUtil

from ITBRegionGrow import ITBRegionGrowWidget
growCutAlgo = ITBRegionGrowWidget()


class HelloPython:
    def __init__(self, parent):
        parent.title = "ROI Segmentation"
        parent.categories = ["COMP5424"]
        parent.dependencies = []

        parent.contributors = ["Max Schultz"]
        parent.helpText = """
Module for visualising 3D segments, and then constructing 3D modules of
regions of interest.
        """
        parent.acknowledgementText = """
I'd like to acknowledge Sidong Liu (USYD) for his w in the development of
this module.
        """
        self.parent = parent


class HelloPythonWidget:
    def __init__(self, parent=None):
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

        # strings for node IDs
        self.roiIDString = ""
        self.modelIDString = ""

    def setup(self):
        # Collapsible button
        self.sampleCollapsibleButton = ctk.ctkCollapsibleButton()
        self.sampleCollapsibleButton.text = "ROI Segmentation"
        self.layout.addWidget(self.sampleCollapsibleButton)

        # Layout within the sample collapsible button
        self.sampleFormLayout = qt.QFormLayout(self.sampleCollapsibleButton)

        self.inputFrame = qt.QFrame(self.sampleCollapsibleButton)
        self.inputFrame.setLayout(qt.QHBoxLayout())
        self.sampleFormLayout.addWidget(self.inputFrame)
        self.inputSelector = qt.QLabel("Input Volume: ", self.inputFrame)
        self.inputFrame.layout().addWidget(self.inputSelector)
        self.inputSelector = slicer.qMRMLNodeComboBox(self.inputFrame)
        self.inputSelector.nodeTypes = (("vtkMRMLScalarVolumeNode"), "")
        self.inputSelector.addEnabled = False
        self.inputSelector.removeEnabled = False
        self.inputSelector.setMRMLScene(slicer.mrmlScene)
        self.inputFrame.layout().addWidget(self.inputSelector)

        self.outputFrame = qt.QFrame(self.sampleCollapsibleButton)
        self.outputFrame.setLayout(qt.QHBoxLayout())
        self.sampleFormLayout.addWidget(self.outputFrame)
        self.outputSelector = qt.QLabel("Output Volume: ", self.outputFrame)
        self.outputFrame.layout().addWidget(self.outputSelector)
        self.outputSelector = slicer.qMRMLNodeComboBox(self.outputFrame)
        self.outputSelector.nodeTypes = (("vtkMRMLScalarVolumeNode"), "")
        self.outputSelector.setMRMLScene(slicer.mrmlScene)
        self.outputFrame.layout().addWidget(self.outputSelector)

        selectionNode = slicer.mrmlScene.GetNodeByID("vtkMRMLSelectionNodeSingleton")
        selectionNode.SetReferenceActivePlaceNodeClassName("vtkMRMLAnnotationROINode")
        interactionNode = slicer.mrmlScene.GetNodeByID("vtkMRMLInteractionNodeSingleton")
        interactionNode.SetPlaceModePersistence(1)
        interactionNode.SetCurrentInteractionMode(1)
        print(help(interactionNode))

        # Add a reload button for debug
        reloadButton = qt.QPushButton("Reload")
        reloadButton.toolTip = "Reload this Module"
        self.sampleFormLayout.addWidget(reloadButton)
        reloadButton.connect('clicked()', self.onReload)

        # Set local var as instance attribute
        self.reloadButton = reloadButton

        # Add vertical spacer
        self.layout.addStretch(1)


    ##############################METHODS FOR WIDGETS###############################
     
    #method to get ROI
    def onSeedROI(self):
    
    	selectionNode = slicer.mrmlScene.GetNodeByID("vtkMRMLSelectionNodeSingleton")
    	# place rulers
    	selectionNode.SetReferenceActivePlaceNodeClassName("vtkMRMLAnnotationROINode")
    	
    	interactionNode = slicer.mrmlScene.GetNodeByID("vtkMRMLInteractionNodeSingleton")
    	placeModePersistence = 1
    	interactionNode.SetPlaceModePersistence(placeModePersistence)
    	# mode 1 is Place, can also be accessed via slicer.vtkMRMLInteractionNode().Place
    	interactionNode.SetCurrentInteractionMode(1)
    
    	self.roiMethodCounter += 1
    	self.roiNodeIncrement = self.roiMethodCounter #counter only increments when region is segmented, means visalisation only occurs for this node
    
    #method to visualise segment
    def onVisualise(self) :
    
    	logic = slicer.modules.volumerendering.logic()
    	volumeNode = slicer.mrmlScene.GetNodeByID('vtkMRMLScalarVolumeNode1')
    	displayNode = logic.CreateVolumeRenderingDisplayNode()
    	self.roiIDString = 'vtkMRMLAnnotationROINode' + str(self.roiNodeIncrement) #visualises correct node based on methods
    	 
    	#crop volumeNode for ROINode and visualise
    	displayNode.CroppingEnabledOn()
    	slicer.mrmlScene.AddNode(displayNode)
    	displayNode.UnRegister(logic)
    	logic.UpdateDisplayNodeFromVolumeNode(displayNode, volumeNode)
    	volumeNode.AddAndObserveDisplayNodeID(displayNode.GetID())
    
    	#visualise ROI node
    	displayNode.SetAndObserveROINodeID(self.roiIDString)
    
    	self.roiMethodCounter += 1
    
    
    
    	return
    
    
    #method to segment ROI
    def onCut(self) :
    	
    
    	inputVolume = self.inputSelector.currentNode()
    	outputVolume = self.outputSelector.currentNode()
    	
    	growCutAlgo.onApply() #apply growCut Algo
    	print("Iteration Complete! That was iteration number: %i" % self.modelMethodCounter)
    
    	#define ROI vairables for cutting
    	scene = slicer.mrmlScene
    	self.modelMethodCounter += 1
    	self.modelIDString = "MRBrainTumor" + str(self.modelMethodCounter) + "-label_grow"
    
    	#define nodes
    	hie_node = slicer.vtkMRMLModelHierarchyNode()
    	roi_node = slicer.util.getNode(self.modelIDString)
    
    	#generate model
    	scene.AddNode(hie_node)
    	params = {}
    	params['InputVolume'] = roi_node.GetID()
    	params['ModelSceneFile'] = hie_node.GetID()
    	slicer.cli.run(slicer.modules.modelmaker, None, params)
    	mod_node = hie_node.GetModelNode()
    
    	return

    # method for reloading
    def onReload(self, moduleName="HelloPython"):
        import imp
        import sys
        import os
        import slicer

        widgetName = moduleName + "Widget"

        # reload the source code
        fPath = eval('slicer.modules.%s.path' % moduleName.lower())
        p = os.path.dirname(fPath)
        if not sys.path.__contains__(p):
            sys.path.insert(0, p)
        fp = open(fPath, "r")
        globals()[moduleName] = imp.load_module(
                moduleName, fp, fPath, ('.py', 'r', imp.PY_SOURCE))
        fp.close()

        # rebuild the widget
        print("the module name to be reloaded,", moduleName)
        # find the Button with a name 'moduleName Reolad', then find its parent
        # (e.g., a collasp button) and grand parent (moduleNameWidget)
        result = slicer.util.findChildren(name='%s Reload' % moduleName)
        parent = result[0].parent().parent()
        for child in parent.children():
            try:
                child.hide()
            except AttributeError:
                pass
        # Remove spacer items
        item = parent.layout().itemAt(0)
        while item:
            parent.layout().removeItem(item)
            item = parent.layout().itemAt(0)
        # create new widget inside existing parent
        globals()[widgetName.lower()] \
            = eval('globals()["%s"].%s(parent)' % (moduleName, widgetName))
        globals()[widgetName.lower()].setup()

        return
