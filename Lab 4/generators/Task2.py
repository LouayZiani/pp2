# Write a program using generator to print the even numbers between 0 and n
# in comma separated form where n is input from console.

def generate_test(x):
    value = 0
    while value <= x:
        if value % 2 == 0:
            yield value
        value += 1

num = int(input("Enter a number: "))
even = [str(number) for number in generate_test(num)]

print(','.join(even))