# Implement procedure to deleting data from tables by username or phone

import psycopg2

def delete_data_by_username_or_phone(username, phone):
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="postgres"
    )
    cur = conn.cursor()

    if username is not None:
        # so basically check if user exists, if it does delete data using it
        cur.execute("DELETE FROM Phonebook WHERE first_name = %s OR last_name = %s", (username, username))
    
    if phone is not None:
        # same thing we did with username but now with digits
        cur.execute("DELETE FROM Phonebook WHERE phone_number = %s", (phone,))

    conn.commit()
    cur.close()
    conn.close()

# example
username = 'Louay'
phone = '1234567890'
delete_data_by_username_or_phone(username, phone)