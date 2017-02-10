#recursion Factorial
import rhinoscriptsyntax as rs

#3! = 3 * 2 * 1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print factorial(5)

#fibranaci sequence
#1+1+2+3+5+8+13+21.....

def fibseq(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibseq(n-1) + fibseq(n-2)

print fibseq(7)

for i in range (0,20):
    print fibseq(i)


def RecCirc(pt, r):
    if r <= 0:
        print "Done!"
        return 0
    else:
        rs.AddCircle(pt,r)
        return RecCirc(pt, r-1)

pt = rs.GetPoint("Pick Center Point")
r = rs.GetReal("Pick Radius")

RecCirc(pt, r)

