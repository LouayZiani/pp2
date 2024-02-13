# Task 10:

# Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.

def unique(my_list):
    unique_list = []
    for element in my_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

x = input("Enter a list of integers: ")
lista = [int(num) for num in x.split()]

result = unique(lista)
print("Unique elements:", result)
