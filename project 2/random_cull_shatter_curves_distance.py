#pseudo-random culling algorithm with variable probability based on distance to a control point
import rhinoscriptsyntax as rs
import random

random.seed(u)

pt = y
bb = rs.ExplodeCurves(B)
print(bb)
print(rs.Distance(rs.CurveStartPoint(bb[0]), rs.CurveEndPoint(bb[0])))
s = z / rs.Distance(rs.CurveStartPoint(bb[0]), rs.CurveEndPoint(bb[0]))
print(s)

def shatter_cull(curves, r):
    print(curves)
    cull = []
    shatter = []
    scurves = []
    for curve in curves:
        if rs.CloseCurve(curve) == False:
            print('invalid curve: not closed')
        #calculate the distance from the control point to the centroid of the curve
        d = rs.Distance(pt, rs.CurveAreaCentroid(curve)[0])
        #scale culling probability by s (probably distance to an attractor point)
        if(random.random() < 1 / (s * d)):
            if(random.random() < .5):
                shatter.append(curve)
            else:
                cull.append(curve)
    for curve in cull:
        curves.remove(curve)
    for curve in shatter:
        for segment in rs.ExplodeCurves(curve):
            v = [rs.CurveStartPoint(segment),
                 rs.CurveEndPoint(segment),
                 rs.CurveAreaCentroid(curve)[0],
                 rs.CurveStartPoint(segment)]
            pl = rs.AddPolyline(v)
            scurves.append(rs.AddPolyline(v))
        curves.remove(curve)
    n=[]
    if(len(scurves) > 0 and r < R):
        print('recursing ' + str(r))
        n = shatter_cull(scurves, r+1)
#    curves.append(n)
#    print(curves)
    return curves+n
a = shatter_cull(x, 0)