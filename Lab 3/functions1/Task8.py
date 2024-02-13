# Task 8:

# Write a function that takes in a list of integers and returns True if it contains 007 in order
def has_007(nums):
    for i in range(len(nums)-2):
        if nums[i] == 0 and nums[i+1] == 0 and nums[i+2] == 7:
            return True
    return False

my_list = input("Enter a list of ints: ")
lista = [int(x) for x in my_list.split()]

result = has_007(lista)
print("Result:", result)
