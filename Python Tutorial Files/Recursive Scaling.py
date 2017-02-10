#Slightly more Complicated Recursion
#Recursive Scaling

import rhinoscriptsyntax as rs

def RecursiveScale(objID, scalePt, scaleFact, scaleVect, num):
    if num == 0:
        return 0
        #exits recursive function and avoids infinity
    else:
        sc = (1.0 / scaleFact)
        scaleVect = [x - sc for x in scaleVect]
        rs.ScaleObject(objID, scalePt, scaleVect, True)
        return RecursiveScale (objID, scalePt, scaleFact, scaleVect, num-1)



objID = rs.GetObject("Pick an Object")
scalePt = rs.GetPoint("Pick a Scale Center")
scaleFact = rs.GetReal("Enter a Scale Facto", 10, 0)
scaleVect = [1.0, 1.0, 1.0]
num = rs.GetInteger("Number of Iterations", 10, 1)

RecursiveScale (objID, scalePt, scaleFact, scaleVect, num)

