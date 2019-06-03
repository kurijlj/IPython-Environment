# COMP5424
Git for COMP5424 components

## Important Files:
  - HelloPython.py (main file)
  - ITBRegionGrow.py (segmentation file)
  - COMP5424_Final_Max_Schultz.pdf (Technical report)

This module allows users to visualise 3D regions of interest (ROI) and then segment relavent features from these ROIs.

## Module Commands:
  - Enter ROI Coordinates: Allows user to input a ROI using the mouse.
  - Turn ON ROI Visualisation: Gives a 3D visualisation of the user's ROI
  - Cut ROI: Generates a 3D model of a relavent features based on an intial seeding point. See below Note for dependancies.
  - Selection Criteria: Allows the user to control the degree of specificty when cutting the ROI.
  - Test Module: Allows user to automatically test the functionality of the module in line with Slicer standards. See below Note for unit test. 
  - Reload: Reloads module and attached scripts.
  
## Note: 
The editor module (in-built into Slicer) is required for the use of this module, as it is required for placing intial seeding points for the 'Cut ROI' command.
Full repository for unit test can be found here: https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/EditorLib/Testing/ThresholdThreadingTest.py

