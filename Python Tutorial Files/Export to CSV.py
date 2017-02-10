#export points to csv

#Uses random number script from earlier

import rhinoscriptsyntax as rs

#Select Pts
pts = rs.GetObjects("Select Points for CSV Export", 1) #data type 1 filters for points

#Create File Name
filename = rs.SaveFileName("Save CSV File", "*.csv||", None, "ptExport", "csv")

#Open the file for writing
file = open(filename, 'w')

headerline = "X,Y,Z,R,G,B\n"
file.write(headerline)

#print pts
for pt in pts:
    ptCoord = rs.PointCoordinates(pt)
    x = ptCoord[0]
    y = ptCoord[1]
    z = ptCoord[2]
    color = rs.ObjectColor(pt)
    r = color.R
    g = color.G
    b = color.B
    #print "x: %.4f, y: %.4f, z: %.4f, r: %d, g: %d, b: %d" %(x,y,z,r,g,b)
    line = "%.4f,%.4f,%.4f,%d,%d,%d \n" %(x,y,z,r,g,b)
    file.write(line)

#Close the file after writing
file.close()

