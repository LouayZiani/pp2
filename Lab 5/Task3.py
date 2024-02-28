# Task 3: Write a Python program to find sequences of lowercase letters joined with a underscore.

import re

with open(r'C:\Users\hp\Desktop\PP2\Lab 5\a.txt', 'r', encoding='utf-8') as file:
    read = file.read()

sequence = re.findall(r"\b[a-z]+_[a-z]+\b", read)
print(sequence)
