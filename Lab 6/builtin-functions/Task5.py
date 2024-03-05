#Task 5: Write a Python program with builtin function that returns True if all elements of the tuple are true.

tuple_input = input("Enter elements of your tuple separated by spaces: ")
my_tuple = tuple(tuple_input.split())
my_tuple = tuple(map(eval, my_tuple)) # eval() takes string as input and evaluates it as a Python expression

def all_true(tup):
    return all(tup)

print(all_true(my_tuple))
