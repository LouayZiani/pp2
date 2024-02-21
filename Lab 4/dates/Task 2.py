# Write a Python program to print yesterday, today, tomorrow.
 
from datetime import date
from datetime import timedelta

today = date.today()
yesterday = today - timedelta(days = 1)
tomorrow = today + timedelta(days = 1)

print(f"Yesterday was {yesterday}")
print(f"Today is {today}")
print(f"Tomorrow will be {tomorrow}")
