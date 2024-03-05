# Task 3: Write a Python program with builtin function that checks whether a passed string is palindrome or not.

def isPalindrome(str):
    if str[::-1] == str:
        return True
    else:
        return False
        

txt = input("Enter yor string: ")

if isPalindrome(txt):
    print("Yes, it is a palindrome!")
else:
    print("No, it is not a palindrome!")