# Write a Python program to subtract five days from current date.

from datetime import date
from datetime import timedelta

today = date.today()
new_date = today - timedelta(days = 5)

print(new_date)