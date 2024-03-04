#Task 9: Write a Python program to insert spaces between words starting with capital letters.

import re

with open(r'C:\Users\hp\Desktop\PP2\Lab 5\a.txt', encoding='utf-8') as file:
    read = file.read()

insert_space = re.sub(r'([A-Z])', r' \1', read)

print(insert_space)
