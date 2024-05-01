import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    port = 5432,
    dbname = 'postgres',
    user = 'postgres',
    password = 'kooora25'
    )

cur = conn.cursor()

# Designing tables (with first & last names, address, and digits)

cur.execute('''CREATE TABLE phonebook (
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            address VARCHAR(255),
            phone_number INT
)''')

conn.commit()

cur.close()
conn.close()