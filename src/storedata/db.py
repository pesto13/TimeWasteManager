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
    
    """ if row != None:
        row = row[:-1] """

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
    conn.execute('''CREATE TABLE IF NOT EXISTS Info
                (application_name TEXT NOT NULL,
                category TEXT NOT NULL,
                start_time TIME NOT NULL,
                seconds_used INT,
                using_date DATE 
                );''')
    

@connection
def insert_all(conn, timeline: list[Info]):

    conn.cursor()
    
    while(len(timeline)>1):
        t = timeline.pop(0)
        values = list(vars(t).values())
        # print(values)

        conn.execute("""INSERT INTO Info (application_name, category, start_time, seconds_used, using_date)
                        VALUES (?, ?, ?, ?, ?)""" , values)





    
        
        
