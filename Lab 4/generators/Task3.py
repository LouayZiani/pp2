# Define a function with a generator which can iterate the numbers, 
# which are divisible by 3 and 4, between a given range 0 and n.

def generate_test(n):
    value = 0
    while value <= n:
        if value % 3 == 0 and value % 4 == 0:
            yield value
        value += 1
        
x = int(input("Enter a number: "))

for number in generate_test(x):
    print(number)

