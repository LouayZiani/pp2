'''Task 4: Write a Python program that invoke square root function after specific milliseconds.

Sample Input:
25100
2123
Sample Output:
Square root of 25100 after 2123 miliseconds is 158.42979517754858'''

import time
import math

def squareAfterTime(number, wait_time):

    time.sleep(wait_time / 1000)

    sqrt = math.sqrt(number)
    return sqrt


number= int(input("Enter a number: "))
wait_time= int(input("Enter time in miliseconds: "))
print(f"Square root of {number} after {wait_time} miliseconds is {squareAfterTime(number, wait_time)}")
