import sqlite3
from logic.info import Info
import datetime

def connection(f):
    def inner(*args, **kwargs):
        with sqlite3.connect('bho.sql') as conn:
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



def load_weak(roll_back: int = 0):
    today = datetime.datetime.today().replace(hour=0, minute=0, second=0) \
            - datetime.timedelta(weeks=roll_back)
    # numero_settimana = today.isocalendar()[1]

    # Calcola il lunedì della settimana corrente
    start_monday = today - datetime.timedelta(days=today.weekday())
    # Calcola la domenica della settimana corrente
    end_sunday = start_monday + datetime.timedelta(days=7)

    start_monday = int(start_monday.timestamp())
    end_sunday = int(end_sunday.timestamp())
    
    return load_from_date_to_date(start_monday, end_sunday)


@connection
def load_from_date_to_date(conn, start_date: int, end_date: int):
 
    print(start_date)
    print(end_date)
    query = f"SELECT * FROM info WHERE start_time BETWEEN '{start_date}' AND '{end_date}'"
    cursor = conn.execute(query)
    records = cursor.fetchall()
    return records
    



    
        
        
