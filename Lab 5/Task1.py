#Task 1

import re

with open(r'C:\Users\hp\Desktop\PP2\Lab 5\a.txt', 'r', encoding='utf-8') as file:
     g = file.read()

match = re.findall(r"ab*", g)
print(match)