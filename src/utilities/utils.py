import json
import random
import string

from logic.info import Info 

def readFile(filename: str):
    # Apri il file JSON in modalità lettura
    with open(filename, 'r') as f:
        # Leggi il contenuto del file JSON e deserializzalo in un oggetto Python
        data = json.load(f)

    # Usa l'oggetto Python deserializzato
    print(data)


#TODO sistema per giorno
def writeOnFile(programs: dict[Info], day: str):

    import os

    # percorso assoluto della directory in cui si trova il file di script
    script_dir = os.path.dirname(os.path.abspath("main.py"))

    # percorso relativo del file da scrivere
    file_path = os.path.join(script_dir, "daily_track", f"{day}.json")

    with open(file_path, 'w') as f:
        json.dump([p.__dict__ for p in programs.values()], f, indent=4)


#funzione di aiuto
def random_genere() -> str:
    # Define the length of the random string
    length: int = 5

    # Define the pool of characters to choose from
    characters = string.ascii_letters + string.digits

    # Generate the random string
    return ''.join(random.choice(characters) for _ in range(length))


def status(programs: dict[Info]):

    for i in programs.values():
        print(i)


""" def piccolomain():
    myTree = t.AVLTree()
    root = None
    nodi = [Info("ciao", "svago", 3), Info("lol", "svago", 6), Info("code", "lavoro", 9)]
    for n in nodi:
        root = myTree.insert_node(root, n)

    myTree.preOrder(root)
    print(myTree.find_value(root,"ciao").key.cathegory) """