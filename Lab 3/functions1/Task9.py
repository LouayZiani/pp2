# Task 9:
# Since V = 4/3 × π × r^3 

def volume(sphere):
    return ((4/3) * 3.14159 * (radius**3))

radius = float(input("Enter Radius: "))
print("Volume of sphere is:", volume(radius))
