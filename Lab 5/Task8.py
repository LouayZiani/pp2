# Task 8: Write a Python program to split a string at uppercase letters.

import re

def split_at_uppercase(string):
    return re.findall(r'[A-Z][^A-Z]*', string)

with open(r'C:\Users\hp\Desktop\PP2\Lab 5\a.txt', 'r', encoding='utf-8') as file:
    read = file.read()

result = split_at_uppercase(read)
print(result)
