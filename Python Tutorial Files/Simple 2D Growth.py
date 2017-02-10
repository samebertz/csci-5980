#Simple Growth

import rhinoscriptsyntax as rs
import random as ran
rs.EnableRedraw(True)

def placePt(x_range, y_range, z_range):
    x = ran.uniform(0,x_range)
    y = ran.uniform(0,y_range)
    z = ran.uniform(0,z_range)
    pt = [x,y,z]
    return pt

ptZero = [50,50,0]
pts = []
pts.append(ptZero)
#circleZero = rs.AddCircle(ptZero,0.5)
sphereZero = rs.AddSphere(ptZero,0.5)


for i in range(0,500):
    pt = rs.AddPoint(placePt(100,100,100))
    index = rs.PointArrayClosestPoint(pts,pt)
    cp = pts[index]
    vect = rs.VectorCreate(cp, pt)
    unitVect = rs.VectorUnitize(vect)
    subVect = vect - unitVect
    newPt = rs.MoveObject(pt, subVect)
    #rs.AddCircle(newPt, 0.5)
    rs.AddSphere(newPt, 0.5)
    pts.append(newPt)

rs.EnableRedraw()



