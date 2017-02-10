#cracking algorithm
import rhinoscriptsyntax as rs #Import RhinoScriptSyntax to access Rhino's API inside the Python Editor

def crackpolygon(pls, count): #This is the function that will drive the cracking algorithm.  It is called later in the script
    print count #look at it count out the recursion
    temppls = pls #creates a temporary list of polygons within this step in the recursion that contains the curves from the previous output
    pls = [] #sets polygons equal to a new empty list
    if count == 0: #at the end of the function count is reduced by 1 before being fed into the next level of recursion
        return #when the function has run the number of times set by the initial count, this line will end it
    else: #The bulk of the function takes place in this else clause, this is where the cracking takes place and the next level of recursion is called
        for pl in temppls: #this "for loop" will run through each item in the temppls list (which is equal to the initial pls list entered into the function
            if rs.CloseCurve(pl) == False: #this function wouldn't work if the curve was open so a fail safe checks to make sure it qualifies
                print "Not a closed curve" #this print line is included so a user will know what went wrong if they choose an open curve
            else:
                centroid = rs.CurveAreaCentroid(pl) #this line finds the centerpoint of a given closed curve from the temppls list
                centpt = rs.AddPoint(centroid[0]) #this line uses the information from centroid to create a point (in rhino space) at the centroid of a given closed curve
                #print centpt #the reason that index 0 of centroid is used to create the point is that rs.CurveAreaCentroid returns more information than point coordinates
                curves = rs.ExplodeCurves(pl) #this line explodes the closed curve into its components
                for crv in curves: #this "for loop" steps through each curve from the exploded polyline
                    pt1 = rs.CurveStartPoint(crv) #finds the start point of a given curve
                    pt2 = rs.CurveEndPoint(crv) #finds the end point of a given curve
                    pts = [] #instantiates an empty list for the points
                    pts.append(pt1) #appends the start point to the empty list
                    pts.append(pt2) #appends the end point to the list
                    pts.append(centpt) #appends the centroid of the exploded closed curve to the list
                    pts.append(pt1) #appends the start point to the list again
                    newpl = rs.AddPolyline(pts) #creates a closed polygon with points at the start and end points of one curve segment with the third point at the centroid
                    pls.append(newpl) #appends this closed polygon to the empty list instantiated in the second line of the function
                    rs.DeleteObject(crv) #deletes the given exploded polyline to clean up geometry in the Rhino environment
                cleanup = [] #an empty cleanup list is instantiated
                cleanup.append(centpt) #the point that was created using the centroid is appended to this empty list
                rs.DeleteObjects(cleanup) #the objects in the cleanup list are deleted.
        count = count-1 #count is reduced by one
        return crackpolygon(pls,count) #the function is called again.  This is what makes it recursive.  Note that the initial count will determine how many times it runs

count = rs.GetInteger("howmany iterations would you like to do?", 3) ##asking for int input in Rhino Window: this number determines how many times the curve is "cracked"
pl = rs.GetCurveObject("Pick a closed curve to crack") #asks 
plguid = pl[0] #index 0 of an object picked from the Rhino environment is its GUID
#print pl
polygons = [] #polygons is created as a list so that as additional curves are generated in the cracking function they can be appended to it
polygons.append(plguid) #its important that the polygon item entry to the function be a list rather than one item as it would be if plguid were entered
crackpolygon(polygons, count) #calling the recursive function

