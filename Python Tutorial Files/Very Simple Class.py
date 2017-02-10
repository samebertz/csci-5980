#Very simple class tutorial

import rhinoscriptsyntax as rs


#this class creates a line based off two points and already basically exists
#classes are typically spelled with a capitol letter
class MyLine:
    
    def __init__(self, pt1, pt2):
        
        self.pt1 = pt1
        self.pt2 = pt2
        
    def makeLine(self):
        rs.AddLine(self.pt1, self.pt2)
        

line1 = MyLine([0,0,0],[3,3,3])
line1.makeLine()

line2 = MyLine([0,0,0],[-3,-3,-3])
line2.makeLine()

