# Task 7: Write a python program to convert snake case string to camel case string.

import re

def convert(str):
    sentence = str.split('_')
    answer = sentence[0] + ''.join(word.capitalize() for word in sentence[1:])
    return answer

with open(r'C:\Users\hp\Desktop\PP2\Lab 5\a.txt', 'r', encoding='utf-8') as file:
     read = file.read()

result = convert(read)
print(result)