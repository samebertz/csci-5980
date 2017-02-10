#random almost recursive vector transformations

import rhinoscriptsyntax as rs
import random as rand

#rs.EnableRedraw(False)

#ask user to create a point
userPt = rs.GetPoint("Create a point")
pt = rs.AddPoint(userPt)

#create a list of points and append pt to the list
pts = []
pts.append(pt)

for i in range (0,100):
    xDir = rand.uniform(-10.0, 10.0)
    yDir = rand.uniform(-10.0, 10.0)
    zDir = 0.0
    vect = [xDir, yDir, zDir]
    newPt = rs.CopyObject(pts[-1], vect)
    pts.append(newPt)
    

myPolyline = rs.AddPolyline(pts)





rs.EnableRedraw()