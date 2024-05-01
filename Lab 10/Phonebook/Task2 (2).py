import psycopg2

# entering data from console

conn = psycopg2.connect(
    host = 'localhost',
    port = 5432,
    dbname = 'postgres',
    user = 'postgres',
    password = 'kooora25'
)

cur = conn.cursor()

console_input = 'INSERT INTO phonebook(first_name, last_name, address, phone_number) VALUES (%s, %s, %s, %s);'

cur.execute(console_input, ('Leo', 'Messi', 'Argentina', 854525410))
conn.commit()

cur.close()
conn.close()