import psycopg2

# Establish a connection to the database
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="postgres",
    user="postgres",
    password="kooora25"
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute an INSERT statement to add a new employee to the employees table
people = "INSERT INTO Phonebook (first_name, last_name, address, phone_number ) VALUES (%s, %s, %s, %s) RETURNING id;"

many = "INSERT INTO Phonebook (first_name, last_name, address, phone_number )  VALUES (%s, %s, %s, %s);"

cur.execute(people, ("teacher", "professor", "Almaty", 23232))


p = [
    ('pp2','python', 'KZ', 7700245350),
    ('pp1', 'java', 'Kz', 2987656789)
]
cur.executemany(many, p)



# Commit the transaction
conn.commit()

# Close the cursor and database connection
cur.close()
conn.close()
