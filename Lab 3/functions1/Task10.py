# Task 10:

def unique(nums):
    uniqueList = []
    for element in nums:
        if element not in uniqueList:
            uniqueList.append(element)
    return uniqueList

a=input()
list=[int(nums) for nums in a.split()]
answer = unique(list)
print(answer)