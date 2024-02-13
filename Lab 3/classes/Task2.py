# Task 2: 

# Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. 
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

class Shape():
    def __init__(self):
        pass
    def __area__(self):
        return 0



class Square(Shape):
    def __init__(self, length):
        self.length = length
    def __area__(self):
        return self.length * self.length
    
if __name__== "__main__":
    square = Square(int(input("Enter the length of one side of your square: ")))
    print("The Area is:", square.__area__())
    
