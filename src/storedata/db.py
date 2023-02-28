import sqlite3

# Apre la connessione al database
conn = sqlite3.connect('bho.sqlite')

# Crea la tabella
conn.execute('''CREATE TABLE IF NOT EXISTS persone
             (id INTEGER PRIMARY KEY,
             nome TEXT NOT NULL,
             eta INTEGER NOT NULL);''')

# Inserisce dei dati nella tabella
conn.execute("INSERT INTO persone (nome, eta) VALUES (?, ?)", ("Mario", 35))
conn.execute("INSERT INTO persone (nome, eta) VALUES (?, ?)", ("Luigi", 28))
conn.execute("INSERT INTO persone (nome, eta) VALUES (?, ?)", ("Paolo", 42))

# Salva le modifiche e chiude la connessione
conn.commit()
conn.close()
