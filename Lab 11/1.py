# Function that returns all records based on a pattern (example of pattern: part of name, surname, phone number)

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()

name_pattern = input("Enter the name pattern: ")
surname_pattern = input("Enter the last name pattern: ")
phone_pattern = int(input("Enter the first digit of the phone number: "))

cur.execute("SELECT * FROM Phonebook WHERE first_name ILIKE %s OR last_name ILIKE %s OR phone_number LIKE %s", (name_pattern+'%', surname_pattern+'%', str(phone_pattern+'%')))
# LIKE is for pattern matching
# ILIKE même chose- case insensitive (Miniscule et Majuscule)
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()