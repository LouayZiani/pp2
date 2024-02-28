# Task 6: Write a Python program to replace all occurrences of space, comma, or dot with a colon.

import re

with open(r'C:\Users\hp\Desktop\PP2\Lab 5\a.txt', 'r', encoding='utf-8') as file:
     read = file.read()

swap = re.sub(r"[ ,.]", ":", read) 
print(swap)