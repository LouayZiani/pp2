# Task 2: Write a Python program to check for access to a specified path. Test the existence, readability, 
# writability and executability of the specified path

# I will use text1.txt for test
import os

path = input("Enter path: ") 


if os.path.exists(path):
    print("Path exists.")

   
    if os.access(path, os.R_OK):  # to check whether it is readable
        print("Yes it is readable ")
    else:
        print("No.")

    
    if os.access(path, os.W_OK): # to check it is writable we use W_OK
        print("Yes.")
    else:
        print("No.")

    
    if os.access(path, os.X_OK):
        print("Yes.") # check executable
    else:
        print("No .")

else:
    print("It does not exist.")