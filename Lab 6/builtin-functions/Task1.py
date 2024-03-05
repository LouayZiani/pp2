#Task 1: Write a Python program with builtin function to multiply all the numbers in a list


from functools import reduce

def multiply_list(numbers):
    result = reduce((lambda x, y: x * y), numbers)
    return result

numbers= input("Enter list of numbers: ")
lista = [int(nums) for nums in numbers.split()]
result= multiply_list(lista)
print(result)