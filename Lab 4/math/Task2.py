'''Write a Python program to calculate the area of a trapezoid.
Height: 5
Base, first value: 5
Base, second value: 6
Expected Output: 27.5'''

import math

def area_trap(height, base1, base2):
    # We know that: area = (1/2) * h * (b1+b2) 
    area = (1/2)* height *(base1 + base2)
    return area

height = int(input("Enter height: "))
base1 = float(input("Enter first base length: "))
base2 = float(input("Enter second base length: "))

print(area_trap(height, base1, base2))