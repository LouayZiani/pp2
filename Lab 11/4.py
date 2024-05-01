# Create function to querying data from the tables with pagination (by limit and offset)

import psycopg2

def query_data_with_pagination(table_name, limit, offset):
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="postgres"
    )
    cur = conn.cursor()
# pagination c veut dire divider une grande liste en petits parties
    query = f"SELECT * FROM {table_name} LIMIT %s OFFSET %s"
    cur.execute(query, (limit, offset))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()

# example
table_name = "Phonebook"
limit = 10
offset = 0
query_data_with_pagination(table_name, limit, offset)