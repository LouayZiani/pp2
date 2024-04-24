import psycopg2
import csv

# Establish a connection to the database
conn = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="kooora25"
)




cur = conn.cursor()

with open(r"C:\Users\hp\Desktop\PP2\Lab 10\Phonebook\phoneBook - Sheet1.csv", 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        cur.execute("INSERT INTO Phonebook(first_name, last_name, address,phone_number) VALUES (%s, %s, %s, %s);",
            (row[0], row[1], row[2], row[3]))

conn.commit()

cur.close()
conn.close()