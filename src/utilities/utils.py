import json
import random
import string
import datetime
from logic.info import Info 

def get_path(f):
    def inner(*args,**kwargs):

        file_name = args[1] if len(args)>0 else kwargs['day']

        import os
        # percorso assoluto della directory in cui si trova il file di script
        script_dir = os.path.dirname(os.path.abspath("main.py"))
        # percorso relativo del file da scrivere
        file_path = os.path.join(script_dir, "daily_track", f"{file_name}.json")
        
        programs = args[0] if len(args)>0 else kwargs['name']

        return f(programs, file_path)
    return inner

#TODO probabilmente non è corrette 100%, sovrascrive i dati
@get_path
def load_today(programs: dict[Info], filename: str):
    # Apri il file JSON in modalità lettura
    with open(filename, 'r') as f:
        # Leggi il contenuto del file JSON e deserializzalo in un oggetto Python
        data = json.load(f)

    # Usa l'oggetto Python deserializzato
    
    #prendo il json e per ogni elemento ricreo l'oggetto
    for data_dict in data:
        programs[data_dict['name']] = Info(**data_dict)
       
def load_last_days(programs: dict[Info], days: int = 7):
    today = datetime.date.today()
    dates = []
    for d in range(days):
        dates.append(  (today-datetime.timedelta(days=d)).strftime("%Y-%m-%d") )
    
    for d in dates:
        load_today(programs, d)

#TODO sistema per giorno
@get_path
def write_file(programs: dict[Info], file_path: str):

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
