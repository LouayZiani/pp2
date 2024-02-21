# Implement a generator called squares to yield the square of all numbers from (a) to (b).
# Test it with a "for" loop and print each of the yielded values.

def squares(a, b):
    value = a
    while value <= b:
        yield value**2
        value += 1

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

for number in squares(a, b):
    print(number)