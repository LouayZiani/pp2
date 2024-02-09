# Task 4:

def prime(nums):
    if nums < 2:
        return False
    for i in range(2, nums):
        if nums % i == 0:
            return False
    return True

def filter_prime(num):
    return[nums for nums in num if prime(nums)]

a = input()
a_list = [int(nums)for nums in a.split()]

prime = filter_prime(a_list)
print(prime)