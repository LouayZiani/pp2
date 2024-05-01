# exchange information with the db/ request data from db
import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    port = 5432,
    dbname = 'postgres',
    user = 'postgres',
    password = 'kooora25'
)

cur = conn.cursor()

# 1st filter (print first & last names)
cur.execute('''SELECT first_name, last_name FROM phonebook''')

for row in cur.fetchall():
    print(row)

# 2nd filter (print all the data for each user)
cur.execute('''SELECT * FROM phonebook''')
for row in cur.fetchall():
    print(row)

# 3rd filter (print data but with condition (only print data for last_name Ziani(:)))
cur.execute('''SELECT * FROM phonebook WHERE last_name = 'Ziani';''')
for row in cur.fetchall():
    print(row)

conn.commit()

cur.close()
conn.close()