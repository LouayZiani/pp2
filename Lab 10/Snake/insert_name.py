import psycopg2

def insert_data(nickname):
    # insertion de data dans tableau
    data = (nickname, 0)
    command = """
        INSERT INTO scores(user_name, score) 
        VALUES(%s, %s)
        """
    try:
        with psycopg2.connect(host="localhost", database="postgres", user="postgres", password="kooora25") as conn:
            with conn.cursor() as cur:
                cur.execute(command, data)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
