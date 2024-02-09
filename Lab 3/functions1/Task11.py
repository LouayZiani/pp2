# Task 11:

def palindrome(str):
    if str==str[-1::-1]:
        return True
    return False
    
x = input()
answer = palindrome(x)
print(answer)