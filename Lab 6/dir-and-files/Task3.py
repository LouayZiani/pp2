# Task 3: Write a Python program to test whether a given path exists or not. 
# If the path exists find the filename and directory portion of the given path.


import os

path = input("Enter path: ") # specify the path


if os.path.exists(path):
    print("Path exists")

  
    dirname, filename = os.path.split(path)
    print("Directory:", dirname)
    if filename:
        print("Filename:", filename)
    else:
        print("There is no filename for this path.")

else:
    print("Path does not exist.")
