import psycopg2

# Deleting Data
conn = psycopg2.connect(
    host = 'localhost',
    port = 5432,
    dbname = 'postgres',
    user = 'postgres',
    password = 'kooora25'
)

cur = conn.cursor()

# Delete by username (if first_name is Leo or last_name is James)
cur.execute('''DELETE FROM phonebook WHERE first_name = 'Leo' OR last_name = 'James';''')

# Delete by Phone Number
cur.execute('''DELETE FROM phonebook WHERE phone_number = 66666666;''')

conn.commit()

cur.close()
conn.close()