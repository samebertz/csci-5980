import Rhino
import rhinoscriptsyntax as rs
import time

#Load Grasshopper plugin as gh
gh = Rhino.RhinoApp.GetPlugInObject("Grasshopper")

### This is how you find and print methods in grasshopper
for func in dir(gh):
    if not func.startswith('_'): print func