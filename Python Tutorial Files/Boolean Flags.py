#If Else with Math and Boolean Flags

import rhinoscriptsyntax as rs
import math

#Boolean Flag
flip = True
color01 = [255,0,255] #cyan?
color02 = [0,255,255]
step = 0.1

for i in rs.frange(0.0,10.0, step):
    ptsForCurve = []
    for j in rs.frange(0.0, 10.0, step):
        x = j
        y = i
        z = math.sin(i)*math.sin(j)
        pt = [x,y,z]
        ptsForCurve.append(pt)
    curve = rs.AddCurve(ptsForCurve)
    if flip == True:
        rs.ObjectColor(curve, color01)
        flip = False
    else:
        rs.ObjectColor(curve, color02)
        flip = True






rs.EnableRedraw()

