#Task 5: Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'

import re

with open(r'C:\Users\hp\Desktop\PP2\Lab 5\a.txt', encoding='utf-8') as file:
    read = file.read()

match = re.findall(r"a.*b$", read)
print(match)
