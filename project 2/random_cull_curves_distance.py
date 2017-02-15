#pseudo-random culling algorithm with variable probability based on distance to a control point
import rhinoscriptsyntax as rs
import random

random.seed()
def cull(pt, curves, s):
    cull = []
    for curve in curves:
        if rs.CloseCurve(curve) == False:
            print('invalid curve: not closed')
        #calculate the distance from the control point to the centroid of the curve
        d = rs.Distance(pt, rs.CurveAreaCentroid(curve)[0])
        #scale culling probability by s (probably distance to an attractor point)
        if(random.random() < 1 / (s * d)):
            cull.append(curve)
    for curve in cull:
        curves.remove(curve)
    return curves
C = cull(P, C, S)