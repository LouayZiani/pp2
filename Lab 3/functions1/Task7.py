# Task 7:

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

numbers = input("Enter a list of ints: ")
nums = [int(x) for x in numbers.split()]

result = has_33(nums)
print("Result:", result)
