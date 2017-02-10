#Unrolling Surfaces with Python

import rhinoscriptsyntax as rs
import Rhino

#Load Grasshopper Plugin
gh = Rhino.RhinoApp.GetPlugInObject("Grasshopper")

#Turn Off Redraw
rs.EnableRedraw(False)

#Values for GH Sliders
uv = 5
sides = 6
row = uv * uv
#Spacing for Nesting
offset = 0.25

#Set Sliders Based on Values above
gh.SetSliderValue("da9f4431-7b07-479d-b7be-fbdb78ae08b4", uv)
gh.SetSliderValue("b46e0b0e-643d-4b3a-8a96-c6d4e120e4dd", sides)

#Run it and Bake it
gh.RunSolver("AutoTower.gh")
baked = gh.BakeDataInObject("24a9672f-359d-45a8-9b0a-be7962f2ab46")

#Create an empty list for nesting purposes
#and define the origin for translations
moved = []
origin = [0,0,0]

#create a couple of variables for our loop to increment
# We use these to keep track of the rows / columns of the nested geometry
columncount = 0
biggestY = 0
totalX = 0

#Iterate through the baked objects
for item in baked:
    #unroll the surfaces and join them
    #delete the ones that aren't necessary
    unrolltemp = rs.UnrollSurface(item,False)
    joined = rs.JoinSurfaces(unrolltemp)
    rs.deletobjects(unrolltemp)
    
    #Get the bounding box
    #Bounding Box returns points, so an empty point list should contain them
    boxpts = []
    boxpts = rs.BoundingBox(joined)
    #Get distance for the x and y values of the box
    xdist = rs.Distance(boxpts[0], boxpts[1])
    ydist = rs.Distance(boxpts[1], boxpts[2])
    #Check to see if the y dist is the biggest in the row
    if ydist > biggestY:
        BiggestY = y dist
    #Create a bounding polyline around object
    #this isnt necessary, but is nice
    polyline = rs.AddPolyline(boxpts[0:4])
    
    #define endpoint of xmove vector
    xpt = [xdist + offset, 0 , 0]
    #set totalX
    totalX = totalX + xdist + offset
    #define the xmove vector
    xmove = rs.VectorCreate(origin, xpt)
    #add objects to the moved list
    moved.append(joined)
    moved.append(polyline)
    #move all the objects
    rs.MoveObjects(moved, xmove)