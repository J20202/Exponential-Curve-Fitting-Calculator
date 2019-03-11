from fractions import Fraction
import numpy as np

#Problem variables
print ("----------------------------")
a = int(input("Insert y-int: "))
x = int(input("Insert x of point: "))
y = int(input("Insert y of point: "))
u = int(input("Insert x of unkown variable: "))
e = 2.718281828

#Variables
print ("----------------------------")
print ("y-int: " + str(a))
print ("point: (" + str(x) + "," + str(y) + ")")
print ("Missing Variable: " + str(u))


#line work
print ("----------------------------")
print ("Line work:")
print ("")

#slope
slopey = (y-a)
slopex = (x-0)
slope = Fraction(slopey,slopex)

print ("Slope = " + str(slope))

#equation
print ("Equation = " + "y="+str(slope)+"x+"+str(a))

#missing
print ("")
print ("Missing number: " + str(float((slope*u)+a)))


#Exponential work
print ("----------------------------")
print ("Exponential work")
print ("")

#Equation
print ("Equation = y=" + str(a) + "e^((ln"+str(y) + "/"+str(a) + ")/" + str(x) + ")" + "x)")
print ("")

print ("Missing number: " + str(a*(e**((np.log(y/a)/x)*u))))
print ("----------------------------")
