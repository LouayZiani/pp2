# Write a Python program to calculate two date difference in seconds.

from datetime import datetime,timedelta

first_date = input("Enter first date: ")
second_date = input("Enter second date: ")

first_date_time = datetime.strptime(first_date, "%d/%m/%Y")
second_date_time = datetime.strptime(second_date, "%d/%m/%Y")

difference = abs(first_date_time - second_date_time).total_seconds()

print(difference)