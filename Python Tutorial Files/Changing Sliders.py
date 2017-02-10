import Rhino
import rhinoscriptsyntax as rs
import time

#Load Grasshopper plugin as gh
gh = Rhino.RhinoApp.GetPlugInObject("Grasshopper")

### This is how you find and print methods in grasshopper
for func in dir(gh):
    if not func.startswith('_'): print func

#SetSliderValue("GUID", Number)

rs.EnableRedraw(True)

fori in range(0,11,1):
    gh.SetSliderValue("d08dc0c7-80ce-4de2-a9a5-8df9558f6319", 8)
    gh.RunSolver(