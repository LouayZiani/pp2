''' Write a Python program to calculate the area of a parallelogram.
Length of base: 5
Height of parallelogram: 6
Expected Output: 30.0 '''

def area_paral(length_b, height):
    area = length_b * height
    return area

length_base = float(input("Enter the length of base: "))
height = float(input("Enter height of parallelogram: "))

print(area_paral(length_base, height))