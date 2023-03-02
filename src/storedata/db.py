import sqlite3
from logic.info import Info
import datetime

def connection(f):
    def inner(*args, **kwargs):
        with sqlite3.connect('bho.sqlite') as conn:
            row = f(conn, *args, **kwargs)
            conn.commit()
            return row
    return inner

@connection
def drop(conn: sqlite3.Connection):
    conn.execute("DROP TABLE Info")

@connection
def load_last(conn: sqlite3.Connection):
    
    
    row : tuple = conn.execute(
        f"""
        SELECT * FROM Info
        ORDER BY rowid DESC
        LIMIT 1
        """).fetchone()
    
    if row != None:
        row = row[:-1]

    if row:
        conn.execute(
            f"""
            DELETE FROM Info
            WHERE start_time = {row[2]}
            """
        )
   
    return row

    

@connection
def create(conn):
    # Crea la tabella
    conn.execute('''CREATE TABLE IF NOT EXISTS Info
                (name TEXT NOT NULL,
                cathegory TEXT NOT NULL,
                start_time TIME NOT NULL,
                delta_time INT,
                using_date DATE 
                );''')
    

@connection
def insert_all(conn, timeline: list[Info]):
    today = datetime.date.today()
    while(len(timeline)>1):
        t = timeline.pop(0)
        values = vars(t).values()
        conn.execute("INSERT INTO Info (name, cathegory, start_time, delta_time, using_date) VALUES (?, ?, ?, ?, ?)", (*values, today.strftime("%Y-%m-%d")))

    
        
        
