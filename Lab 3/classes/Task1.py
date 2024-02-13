# Task 1:

# Define a class which has at least two methods: getString: to get a string 
# from console input printString: to print the string in upper case.

class getString:
    def __init__(self, string):
        self.string = string


string1 = getString(input("Enter string: "))

result = string1.string.upper()
print("Your string in Upper case:", result)
