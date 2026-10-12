import sqlite3

def get_connection():
    connection = sqlite3.Connection("app/repositories/tasks.db")
    cursos = connection.cursor() 
    return connection, cursos

def create_table(conn: sqlite3.Connection, cursos: sqlite3.Cursor):
    
    cursos.execute("""CREATE TABLE IF NOT EXISTS Tasks(
    id text,
    title text,
    description, text,
    is_completed integer
    )""")

    conn.commit()
    conn.close()