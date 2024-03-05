# Task 8: Write a Python program to delete file by specified path. 
# Before deleting check for access and whether a given path exists or not.

import os

file_path = "b.txt"

if os.path.exists(file_path):
    if os.access(file_path, os.R_OK) and os.access(file_path, os.W_OK):
        os.remove(file_path)
        print("File deleted")
    else:
        print("You don't have permissions to delete the file.")

else:
    print("File not found.")