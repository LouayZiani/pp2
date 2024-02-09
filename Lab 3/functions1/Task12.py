# Task 12:

def histogram(numbers):
    for i in numbers:
        print('*' * i)

x = input()
list=[int(nums) for nums in x.split()]
answer = histogram(list)
print(answer)