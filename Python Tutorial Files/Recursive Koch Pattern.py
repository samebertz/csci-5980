#Koch Snowflake in Python using recursion

import rhinoscriptsyntax as rs

#define a function to get normal/perp vector
def getnormal (pt1,pt2):
    dx = pt2[0] - pt1[0]
    dy = pt2[1] - pt1[1]
    return [-dy, dx, 0]

#split line recursive function
def splitlines(lines, count):
    #temp list and clear the input list
    templines = lines
    lines = []
    #make sure there is a mechanism that breaks the recursion
    if count ==0:
        return 1
    else:
        for line in templines:
            #get properties of the line (endpoints, length, direction, domain)
            stpt = rs.CurveStartPoint(line)
            endpt = rs.CurveEndPoint(line)
            length = rs.Distance(stpt, endpt)
            dir1 = rs.VectorCreate(endpt, stpt)
            crvdomain = rs.CurveDomain(line)
            #parameters for midpt and pts 1/3 and 2/3 along the line
            t0 = crvdomain[1] / 2.0
            t1 = crvdomain[1] / 3.0
            t2 = t1 * 2
            midpt = rs.EvaluateCurve(line, t0)
            ptatonethird = rs.EvaluateCurve(line, t1)
            ptattwothird = rs.EvaluateCurve(line, t2)
            
            midpt = rs.AddPoint(midpt)
            #call normal function
            normal = getnormal(stpt, endpt)
            #move midpt perpendicular to line at 1/3 the length of the line
            scaled = rs.VectorScale(normal, 0.333333)
            rs.MoveObject(midpt, scaled)
            #create the 4 new lines and add them to the list
            newline1 = rs.AddLine(stpt, ptatonethird)
            newline2 = rs.AddLine(ptatonethird, midpt)
            newline3 = rs.AddLine(midpt, ptattwothird)
            newline4 = rs.AddLine(ptattwothird, endpt)
            lines.append(newline1)
            lines.append(newline2)
            lines.append(newline3)
            lines.append(newline4)
            
            #time to clean up
            cleanup = []
            cleanup.append(line)
            cleanup.append(midpt)
            rs.DeleteObjects(cleanup)
            
            
        count = count - 1
        return splitlines(lines, count)

#get two points to start
pt1 = rs.GetPoint("Pick a Start Point")
pt2 = rs.GetPoint("Pick an End Point")

lines = []
line = rs.AddLine(pt1, pt2)
lines.append(line)

count = rs.GetInteger("How many iterations would you like to calculate?", 3)


splitlines(lines,count)
