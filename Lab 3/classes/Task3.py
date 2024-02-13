#Task 3:

from Task2 import Shape

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def __area__(self):
        return self.length * self.width
    

rectangleLength = int(input("Enter the length of your rectangle: "))
rectangleWidth = int(input("Enter the width of your rectangle: "))
rec = Rectangle(rectangleLength, rectangleWidth)
print("The Area is:", rec.__area__())
