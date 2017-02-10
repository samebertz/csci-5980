#Recursive Tree Algorithm

import rhinoscriptsyntax as rs
import math
import random as ran

#attempting to create the tree algorithm beginning pg 65 of RhinoPythonPrimer

#only two methods of adding angles in Phython
#rs.AddArc(Plane, Radius, Angle)
#rs.AddArc3Pt(point, point, point)
#because the desired approach for this recursion is with a directional vector...
#Some math will be required to mirror this with the three point approach




def AddArcDir (ptStart, ptEnd, vecDir):
    vecBase = rs.PointSubtract(ptEnd, ptStart)
    if rs.VectorLength(vecBase) == 0: return
    
    if rs.IsVectorParallelTo(vecBase, vecDir): return
    
    vecBase = rs.VectorUnitize(vecBase)
    vecDir = rs.VectorUnitize(vecDir)
    
    vecBisector = rs.VectorAdd(vecDir, vecBase)
    vecBisector = rs.VectorUnitize(vecBisector)
    
    dotProd = rs.VectorDotProduct(vecBisector, vecDir)
    midLength = (0.5 * rs.Distance(ptStart, ptEnd)) / dotProd
    
    vecBisector = rs.VectorScale(vecBisector, midLength)
    return rs.AddArc3Pt(ptStart, rs.PointAdd(ptStart, vecBisector), ptEnd)

Pt01 = rs.GetPoint("Pick Start Point")
Pt02 = rs.GetPoint("Pick End Point")
Pt03 = rs.GetPoint("Pick Directional Vector")
Vec01 = rs.PointSubtract(Pt03, Pt01)
print Vec01

AddArcDir(Pt01, Pt02, Pt03)
