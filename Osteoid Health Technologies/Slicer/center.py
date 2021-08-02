# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 10:44:10 2021

@author: YBurakD
"""

import slicer
import os
import numpy as np
import vtk
from msvcrt import getch
import shutil
def center():
    inputFile = "E:/ACIBADEM_512/"
    transformFile = "E:/ACIBADEM_512_ROTATED/"
    outputFileLocation = "E:/ACIBADEM_512_ROTATED/"
    saveFilePath = os.path.join(outputFileLocation,"savefile.txt")
    if(not os.path.exists(saveFilePath)):
        savefile = open(saveFilePath,"w")
        savefile.close()
    
    savefile = open(saveFilePath,"r")
    checkpoint = savefile.read()
    savefile.close()
    
    print(checkpoint)
    if(checkpoint != ""):
        checkpointFlag = False
    else:
        checkpointFlag = True
        
    for folder in os.listdir(inputFile):
        inputFileLocation = os.path.join(inputFile,folder)
        for file in os.listdir(inputFileLocation):
            
            if file == checkpoint:
                checkpointFlag = True
                continue
            if ".mhd" in file and checkpointFlag:
                
                if(not os.path.exists(transformFile+folder+"/"+file)):
                    continue
                with open(transformFile+folder+"/"+file,"r") as infile:
                    meta = {}
                    for line in infile.read().strip().split("\n"):
                
                        info = line.split("=")
                        if(len(info)>1):
                            meta[info[0].strip()] = info[1].strip()
                    tMatrix = np.float32(np.array(meta["TransformMatrix"].split()).reshape(3,3))
                    for i in range(3):
                        for j in range(3):
                            if((i<2 and j == 2) or (i == 2 and j < 2)):
                                tMatrix[i,j] = -1*float(tMatrix[i,j])
                            else:
                                tMatrix[i,j] = float(tMatrix[i,j])
                    tMatrix = tMatrix.reshape(3,3).T
                
                filePath = os.path.join(inputFileLocation, file)
                
                slicer.util.mainWindow().moduleSelector().selectModule('Transforms')
                transformNode = slicer.vtkMRMLTransformNode()
                slicer.mrmlScene.AddNode(transformNode)
                
                volumeNode = slicer.util.loadVolume(filePath)
                volRenLogic = slicer.modules.volumerendering.logic()
                
                #Display the volume
                displayNode = volRenLogic.CreateDefaultVolumeRenderingNodes(volumeNode)
                displayNode.SetVisibility(True)
                
                displayNode.GetVolumePropertyNode().Copy(volRenLogic.GetPresetByName('CT-Muscle'))
                
                #Center 3d Volume
                layoutManager = slicer.app.layoutManager()
                threeDWidget = layoutManager.threeDWidget(0)
                threeDView = threeDWidget.threeDView()
                threeDView.resetFocalPoint()
                
                volumeNode.SetAndObserveTransformNodeID(transformNode.GetID())
                
                slicer.app.pythonConsole().clear()
                print(folder)
                transformMatrix = vtk.vtkMatrix4x4()
                for i in range(3):
                    for j in range(3):
                        transformMatrix.SetElement(i,j,tMatrix[i,j])
                        
                transformNode.SetMatrixTransformToParent(transformMatrix)
                flag = input("\nyo: ")
                if(flag == "ç"):
                    savefile = open(saveFilePath,"w")
                    savefile.write(file)
                    savefile.close()
                    shutil.rmtree(outputFileLocation+folder)
                    slicer.mrmlScene.RemoveNode(transformNode)
                    slicer.mrmlScene.RemoveNode(volumeNode)
                    slicer.app.pythonConsole().clear()
                    continue
                    
                emptyVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", "output volume")
                
                
                params = {}
                
                params["inputVolume"] = volumeNode
                params["outputVolume"] = emptyVolumeNode
                params["referenceVolume"] = volumeNode
                
                params["transformationFile"] = transformNode
                
                params["defaultPixelValue"] = -1024.0
                
                resampleModule = slicer.modules.resamplescalarvectordwivolume
                cliNode = slicer.cli.runSync(resampleModule,None,params)
                if cliNode.GetStatus() & cliNode.ErrorsMask:
                    # error
                    errorText = cliNode.GetErrorText()
                    slicer.mrmlScene.RemoveNode(cliNode)
                    raise ValueError("CLI execution failed: " + errorText)
                # success 
                
                slicer.mrmlScene.RemoveNode(cliNode)
                
                slicer.app.pythonConsole().clear()
            
                os.remove(outputFileLocation+folder+"/"+file)
                os.remove(outputFileLocation+folder+"/"+file.replace("mhd","zraw"))
                slicer.util.saveNode(emptyVolumeNode,os.path.join(outputFileLocation,folder,file))
                
                slicer.mrmlScene.RemoveNode(transformNode)
                slicer.mrmlScene.RemoveNode(volumeNode)
                slicer.mrmlScene.RemoveNode(emptyVolumeNode)
                
                savefile = open(saveFilePath,"w")
                savefile.write(file)
                savefile.close()
    print("All files have been centered\n")
                
def moduleParams():
    cliModule = slicer.modules.resamplescalarvectordwivolume
    n=cliModule.cliModuleLogic().CreateNode()
    for groupIndex in range(n.GetNumberOfParameterGroups()):
      print(f'Group: {n.GetParameterGroupLabel(groupIndex)}')
      for parameterIndex in range(n.GetNumberOfParametersInGroup(groupIndex)):
        print('  {0} [{1}]: {2}'.format(n.GetParameterName(groupIndex, parameterIndex),
          n.GetParameterTag(groupIndex, parameterIndex),n.GetParameterLabel(groupIndex, parameterIndex)))
                    