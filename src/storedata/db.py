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
def pop_last(conn: sqlite3.Connection, index=1):
    
    
    row : tuple = conn.execute(
        f"""
        SELECT * FROM Info
        ORDER BY rowid DESC
        LIMIT {index}
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
def get_last(conn: sqlite3.Connection, index=1):
    
    
    row : tuple = conn.execute(
        f"""
        SELECT * FROM Info
        ORDER BY rowid DESC
        LIMIT {index}
        """).fetchone()
   
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
    
    values = [tuple(vars(t).values()) for t in timeline]

    sql = """INSERT INTO Info (application_name, category, start_time, seconds_used, using_date)
             VALUES (?, ?, ?, ?, ?)"""
    
    conn.executemany(sql , values)





    
        
        
