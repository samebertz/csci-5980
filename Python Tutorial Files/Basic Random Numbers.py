#random Number

import rhinoscriptsyntax as rs
import random
rs.EnableRedraw(False)
#prints a random floating point number from 0.0 to 1.0

print (random.random())

#prints a random integer from 0 to 100

print (random.randint(0,100))

#prints a random floating point value from 0 to 100

print (random.uniform(0,100))

for i in range(0,1000):
    x = random.uniform(0,100)
    y = random.uniform(0,100)
    z = random.uniform(0,100)
    
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    color = [r,g,b]
    pt = rs.AddPoint(x,y,z)
    rs.ObjectColor(pt, color)
    

rs.EnableRedraw()
