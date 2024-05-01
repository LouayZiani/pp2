# Create procedure to insert many new users by list of name and phone. Use loop and if statement in 
# stored procedure. Check correctness of phone in procedure and return all incorrect data.

import psycopg2

def insert_users(user_list):
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="postgres"
    )
    cur = conn.cursor()
    invalid_data = []

    for entry in user_list:
        first_name, last_name, phone = entry.split('|')
        
        # Vérifier si le num de telephone est correct ou pas
        if not phone.isdigit() or len(phone) < 10:
            invalid_data.append(entry)
        else:
            # vérifier si l'utilisateur existe
            cur.execute("SELECT COUNT(*) FROM Phonebook WHERE first_name = %s AND last_name = %s", (first_name, last_name))
            count = cur.fetchone()[0]

            if count > 0:
                # Mise a jour du num de tel pour l'utilisateur existant
                cur.execute("UPDATE Phonebook SET phone_number = %s WHERE first_name = %s AND last_name = %s", (phone, first_name, last_name))
            else:
                # Insérer nouveau utlisateur
                cur.execute("INSERT INTO Phonebook (first_name, last_name, phone_number) VALUES (%s, %s, %s)", (first_name, last_name, phone))

    conn.commit()
    cur.close()
    conn.close()

    return invalid_data

# Example
user_list = ['Louay|Ziani|1234567890', 'Jimmy|Butler|987654321', 'Invalid|User|123']
invalid_data = insert_users(user_list)
print('Invalid Data:', invalid_data)