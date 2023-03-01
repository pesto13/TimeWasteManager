import sqlite3
from logic.info import Info
import datetime



def connection(f):
    def inner(*args, **kwargs):

        conn = sqlite3.connect('bho.sqlite')
        print("mi connetto")
        f(conn, *args, **kwargs)
        conn.commit()
        conn.close()

    return inner

@connection
def drop(conn: sqlite3.Connection):
    conn.execute("DROP TABLE Info")

@connection
def load_last(conn: sqlite3.Connection):
    
    
    val = conn.execute(
        f"""
        SELECT * FROM Info
        ORDER BY ID
        LIMIT 1
        """).fetchone()
    
    print(val)

    

@connection
def create(conn):
    # Crea la tabella
    conn.execute('''CREATE TABLE IF NOT EXISTS Info
                (id int PRIMARY KEY,
                name TEXT NOT NULL,
                cathegory TEXT NOT NULL,
                start_time TIME NOT NULL,
                delta_time INT,
                using_date DATE 
                );''')
    

@connection
def insert_all(conn, timeline: list[Info]):
    today = datetime.date.today()
    print(today)
    for t in timeline:
        values = vars(t).values()
        
        conn.execute("INSERT INTO Info (name, cathegory, start_time, delta_time, using_date) VALUES (?, ?, ?, ?, ?)", (*values, today.strftime("%Y-%m-%d")))
        print("fatto")

