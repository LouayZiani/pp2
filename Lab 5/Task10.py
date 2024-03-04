#Write a Python program to convert a given camel case string to snake case.
import re

def camel_to_snake(camel):
    snake = re.sub(r'(?<=[a-z0-9])([A-Z])', r'_\1', camel)
    return snake.lower()

with open(r'C:\Users\hp\Desktop\PP2\Lab 5\a.txt', encoding='utf-8') as file:
     read = file.read()

result = camel_to_snake(read)
print(result)
