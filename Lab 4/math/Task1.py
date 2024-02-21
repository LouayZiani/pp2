''' Write a Python program to convert degree to radian.
Input degree: 15
Output radian: 0.261904 '''

 
import math
 
def degtorad(degree):
    radians = math.radians(degree)
    return radians
 
print("Output in radian:", degtorad(float(input("Enter degree: "))))
