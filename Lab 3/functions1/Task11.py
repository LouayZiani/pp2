# Task 11:

# Write a Python function that checks whether a word or phrase is palindrome or not

def is_palindrome(string):
    if string == string[-1::-1]:
        return True
    return False

text = input("Enter a string: ")
print(is_palindrome(text))
