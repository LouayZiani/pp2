# Implement a generator that returns all numbers from (n) down to 0.

def generator(n):
    value = n
    while value >= 0:
        yield value
        value -= 1

x = int(input("Enter a number: "))
for number in generator(x):
    print(number)