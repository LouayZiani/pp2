# Task 4 : Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re

with open(r'C:\Users\hp\Desktop\PP2\Lab 5\a.txt', 'r', encoding='utf-8') as file:
     read = file.read()

sequence = re.findall(r"\b[A-Z][a-z]+", read)
print(sequence)