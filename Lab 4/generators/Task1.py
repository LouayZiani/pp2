# Create a generator that generates the squares of numbers up to some number N.

def generate_test(n):
    value = 0
    while value <= n:
        yield value**2
        value += 1
 
x = int(input("Enter a number: "))
for number in generate_test(x):
    print(number)