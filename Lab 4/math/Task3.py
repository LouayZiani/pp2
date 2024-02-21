'''Write a Python program to calculate the area of regular polygon.
Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625'''

import math

# We have: area = (n * s**2) / (4 * tan(pi / n)) for n : number of sides, and s: length of each side
def area_polygon(num, s_length):
    area = (num * s_length**2)/(4*math.tan(math.pi/num))
    return area

number_sides = float(input("Enter the number of sides: "))
side_length = float(input("Enter side length: "))

print(area_polygon(number_sides, side_length))