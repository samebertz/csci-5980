#Class Tutorial

import rhinoscriptsyntax as rs
import math

rs.EnableRedraw(False)

class MyPolygon:
    
    def __init__(self, radius, sides, origin):
        self.radius = radius
        self.sides = sides
        self.origin = origin
        theta = (2 * math.pi) / self.sides
        x = origin[0] + self.radius
        y = origin[1]
        z = origin[2]
        pt01 = rs.AddPoint(x,y,z)
        pts = []
        pts.append(pt01)
        degrees = theta * (180/math.pi)
        for i in range(1,self.sides):
            tempPt = pts[-1]
            newPt = rs.RotateObject(tempPt, origin, degrees, None, True)
            pts.append(newPt)
        pts.append(pt01)
        self.polygon = rs.AddPolyline(pts)
        
    def fillPolygon(self):
        return rs.AddPlanarSrf(self.polygon)
    def extrudePolygon(self, height):
        startPt = self.origin
        newZ = self.origin[2] + height
        endPt = [self.origin[0], self.origin[1], newZ]
        return rs.ExtrudeCurveStraight(self.polygon, startPt, endPt)


Origin01 = rs.GetPoint("Pick a Center Point")
Polygon01 = MyPolygon(6,6, Origin01)
Polygon01.fillPolygon()
Polygon01.extrudePolygon(5)

Origin01 = rs.GetPoint("Pick a Second Center Point")
Polygon02 = MyPolygon(8,12, Origin01)
Polygon02.fillPolygon()
Polygon02.extrudePolygon(3)

rs.EnableRedraw()
