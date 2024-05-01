import psycopg2

# Update first_name or phonne (the U in CRUD (:)

conn = psycopg2.connect(
    host = 'localhost',
    port = 5432,
    dbname = 'postgres',
    user = 'postgres',
    password = 'kooora25'
)

cur = conn.cursor()

cur.execute('''UPDATE phonebook set first_name = %s, phone_number = %s WHERE first_name = %s;''',
            ('Jimmy', 65465413, 'LeBron'))

conn.commit()

cur.close()
conn.close()
