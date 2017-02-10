#Nested For Loops
#Create our own Function
#Color Points

import rhinoscriptsyntax as rs

#Function to create colored points
def createColoredPoint(x,y,z,r,g,b): #def defines a function
    currentColor = [r,g,b]
    pt = rs.AddPoint(x,y,z)
    rs.ObjectColor(pt, currentColor)

rs.EnableRedraw(False) #turns off redraw for speed, make sure to turn it back on so python can draw geometry
step = 10

for x in range(0,256,step):
    for y in range(0,256,step):
        for z in range(0,256,step):
            createColoredPoint(x,y,z,x,y,z)

rs.Redraw()
