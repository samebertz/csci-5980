#Variables and Simple User Input/Output
import rhinoscriptsyntax as rs

#String Examples
strGreeting = "Hello World"
print strGreeting

#strInput = rs.GetString("Type String to Print")
#print strInput
#comment used to disable code


#Number Examples
dblRadius01 = 2.0
print dblRadius01

dblRadius02 = rs.GetReal("Enter a Number for Radius02", 3.0)
print dblRadius02

#%d holds a place until the end of the line
#\n is an escape character
#print "Radius01 : %d \nRadius02 : %d" % (dblRadius01, dblRadius02)
strMessage = "Radius01 : %d \nRadius02 : %d" % (dblRadius01, dblRadius02)

rs.MessageBox(strMessage)
