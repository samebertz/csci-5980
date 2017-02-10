#Arrays/Lists
import rhinoscriptsyntax as rs

#because of the coercePt command all of the lists/strings below will be able to creat points
# [ ] brackets define lists
# ( ) perenthesis define touples
arrPt1 = [1,3,9]
arrPt2 = [4,5,6]
arrPt3 = [-1,-2,-3]
arrPt4 = [7,8,9]

rs.AddPoint(arrPt1)
rs.AddPoint (arrPt2)
rs.AddPoint (arrPt3)
rs.AddPoint (arrPt4)

points = []
points.append(arrPt1)
points.append(arrPt2)
points.append(arrPt3)
points.append(arrPt4)

print (points)

print(points[1])
rs.AddPolyline(points)


#print (arrPt1[2])

