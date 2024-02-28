#Task 2


import re

with open(r'C:\Users\hp\Desktop\PP2\Lab 5\a.txt', 'r', encoding='utf-8') as file:
     read = file.read()

match = re.findall(r"a(bb|bbb)", read)
print(match)