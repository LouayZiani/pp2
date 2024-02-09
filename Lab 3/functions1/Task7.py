# Task 7:

def contains33(nums):
    for i in range(len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            return True
    return False
    
a=input()
List=[int(nums) for nums in a.split()]
result=contains33(List)
print (result)