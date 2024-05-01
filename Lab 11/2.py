# Create procedure to insert new user by name and phone, update phone if user already exists

import psycopg2

def insert_or_update_user(name, phone):
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="postgres"
    )
    cur = conn.cursor()

    # Vérifier si l'utilisateur existe ou pas
    cur.execute("SELECT COUNT(*) FROM Phonebook WHERE first_name = %s", (name,)) 
    # count(*) compte tous les lignes (rows)
    
    count = cur.fetchone()[0]

    if count > 0:   
        cur.execute("UPDATE Phonebook SET phone_number = %s WHERE first_name = %s", (phone, name))
        print("the name exist")
    else:
        # Insérer le nouveau utilisateur
        cur.execute("INSERT INTO Phonebook (first_name, phone_number) VALUES (%s, %s)", (name, phone))

    conn.commit()
    cur.close()
    conn.close()

# Example
a= input("enter the name:   ")
b= int(input("enter the phone number:   "))
insert_or_update_user(a, b)