import psycopg2
import csv
# import data from csv file

conn = psycopg2.connect(
    host = 'localhost',
    port = 5432,
    dbname = 'postgres',
    user = 'postgres',
    password = 'kooora25'
)

cur = conn.cursor()

with open(r"C:\Users\hp\Desktop\PP2\Lab 10\Phonebook\phonebook.csv", 'r') as file:
    read = csv.reader(file)
    
    # skip first line containing (name, adress, phone num)
    next(read)
    for value in read:
        cur.execute('INSERT INTO phonebook(first_name, last_name, address, phone_number) VALUES (%s, %s, %s, %s);',
                    (value[0], value[1], value[2], value[3]))



conn.commit()

cur.close()
conn.close()