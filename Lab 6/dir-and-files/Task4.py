# Task 4: Write a Python program to count the number of lines in a text file.

filename = input("Enter file name: ")

with open(filename) as file:
    num_lines = 0
    for line in file:
        num_lines += 1

print("Number of lines:", num_lines)