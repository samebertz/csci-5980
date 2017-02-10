#if elif and else statements

import rhinoscriptsyntax as rs

color01 = (255,0,255) #magenta
color02 = (0,255,255) #cyan
color03 = (125,30,205) #purple
rs.EnableRedraw(False)

for x in range(0,100,1):
    for y in range(0,100,1):
        pt = rs.AddPoint(x,y,0)
        if x % 3 == 0 and y % 5 == 0:  #% is called modulo  == tests for equality
            rs.ObjectColor(pt, color01)
        elif x % 3 == 0 or y % 5 ==0:
            rs.ObjectColor(pt, color02)
        else:
            rs.ObjectColor(pt, color03)


rs.Redraw()