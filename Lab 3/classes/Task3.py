#Task 3:

class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    def area(self):
        return self.length*self.length

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

squareLength = float(input())
s = Square(squareLength)
print(s.area())

rectangleLength = float(input())
rectangleWidth = float(input())
r = Rectangle(rectangleLength, rectangleWidth)
print(r.area())