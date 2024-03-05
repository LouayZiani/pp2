# Task 1: Write a Python program to list only directories, files and all directories, files in a specified path.


import os

path = input("Enter path: ") # specify the path

# list only directories
print("Directories:")
for item in os.listdir(path):
    if os.path.isdir(os.path.join(path, item)):
        print(item)

# list only files
print("Files:")
for item in os.listdir(path):
    if os.path.isfile(os.path.join(path, item)):
        print(item)

# list all directories and files
print("All Directories and Files:")
for item in os.listdir(path):
    print(item)