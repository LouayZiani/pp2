#Task 2: Write a Python program with builtin function that accepts a string 
# and calculate the number of upper case letters and lower case letters

def upper_lower_count(str):
    upper = 0
    lower = 0
    for i in range(len(str)):
        if str[i].isupper():
            upper += 1
        elif str[i].islower():
            lower += 1
    return upper, lower

sentence = input("Enter a string: ")
print(upper_lower_count(sentence))