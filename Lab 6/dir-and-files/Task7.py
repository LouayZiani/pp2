# Task 7: Write a Python program to copy the contents of a file to another file


file1 = input("Enter first file name: ")
with open(file1, 'r') as input_file:

    contents = input_file.read()

file2 = input("Enter second file name: ")
with open(file2, 'w') as output_file:

    output_file.write(contents)