import sqlite3
from logic.info import Info
from datetime import date

def connection(f):
    def inner(*args, **kwargs):

        conn = sqlite3.connect('bho.sqlite')
        print("mi connetto")
        f(conn, *args, **kwargs)
        conn.commit()
        conn.close()

    return inner

@connection
def create(conn):


    # Crea la tabella
    conn.execute('''CREATE TABLE IF NOT EXISTS Info
                (name TEXT NOT NULL,
                cathegory TEXT NOT NULL,
                start_time TIME NOT NULL,
                delta_time INT,
                file_name DATE 
                );''')
    

@connection
def insert_all(conn, timeline: list[Info]):
    d = date().today()
    for t in timeline:
        values = vars(t).values()
        
        conn.execute("INSERT INTO Info (name, cathegory, start_time, delta_time) VALUES (?, ?, ?, ?, ?)", (values, d))

