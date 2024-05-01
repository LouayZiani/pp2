import psycopg2

def update(nickname, score):
    # Met à jour le compte d'un utilisateur ou crée un nouvel utilisateur s'il n'en existe pas.
    command = """
        UPDATE scores
        SET score =  %s 
        WHERE user_name = %s;
        """
    try:
        with psycopg2.connect(host="localhost", database="postgres", user="postgres", password="kooora25") as conn:
            with conn.cursor() as cur:
                cur.execute(command, (score, nickname))
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
