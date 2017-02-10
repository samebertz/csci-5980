#Import Points from CSV

import rhinoscriptsyntax as rs

#select a file to open
filename = rs.OpenFileName("Open CSV file", "*.csv|", None, None, None)

#open file for reading
file = open(filename,'r')

print(file)

lines = file.readlines()

file.close()

#Delete the first line since its a header
del lines[0]

#print(lines)

ptNumber = 0

for line in lines:
    #remove the \n
    line = line.strip()
    #split the line by the comma
    ptInfo = line.split(',')
    #print(ptInfo)
    x = float(ptInfo[0])
    y = float(ptInfo[1])
    z = float(ptInfo[2])
    r = int(ptInfo[3])
    g = int(ptInfo[4])
    b = int(ptInfo[5])
    pt = rs.AddPoint(x,y,z)
    print(pt)
    color = [r,g,b]
    rs.ObjectColor(pt, color)
    name = 'pt_' + str(ptNumber)
    rs.ObjectName(pt, name)
    ptNumber += 1