import Rhino
import rhinoscriptsyntax as rs
import time

#Load Grasshopper plugin as gh
gh = Rhino.RhinoApp.GetPlugInObject("Grasshopper")

### This is how you find and print methods in grasshopper
#for func in dir(gh):
#    if not func.startswith('_'): print func

#SetSliderValue("GUID", Number)
#BakeDataInObject("GUID")

rs.EnableRedraw(True)

#set working directory
workingDir = rs.BrowseForFolder(None, "Pick a folder to use as a working directory")
rs.WorkingFolder(workingDir)

#create variable for file naming
num = 0

for i in range(1,3,1):
    #BaseSize Slider = i
    gh.SetSliderValue("adf54977-006a-4877-9e67-81d736ff07de", i)
    for j in range(0,3,1):
        #Rotation Slider = j
        gh.SetSliderValue("061dd51d-3d85-4a32-8aaa-0e6ba809ed75", j)
        for k in range (3,5,1):
            #Number of Sides Slider = k
            gh.SetSliderValue("b46e0b0e-643d-4b3a-8a96-c6d4e120e4dd", k)
            gh.RunSolver("AutoTower.gh")
            baked = gh.BakeDataInObject("72628cf1-020e-425d-9746-6f323f8882f8")
            transVect = (12*i, 12*j, 12*(k-2))
            rs.MoveObject(baked, transVect)
            
            #convert to string and add file name
            strNum = str(num)
            filename = "myfileTest" + strNum + ".3dm"
            
            #call a bunch of rhino cammands to do a selection and export
            rs.Command("_SelNone", True)
            rs.Command("_SelLast", True)
            rs.Command("_-Export " + filename + " _Enter", True)
            rs.Command("_SelNone", True)
            
            #incriment the file name
            
            num = num + 1




