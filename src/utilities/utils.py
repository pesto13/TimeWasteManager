import json
import random
import string
import datetime
import os

from logic.info import Info


def get_path(f):
    def inner(*args,**kwargs):

        file_name = args[1] if len(args)>0 else kwargs['day']

        # percorso assoluto della directory in cui si trova il file di script
        script_dir = os.path.dirname(os.path.abspath("main.py"))
        # percorso relativo del file da scrivere
        file_path = os.path.join(script_dir, "daily_track", f"{file_name}.json")
        
        programs = args[0] if len(args)>0 else kwargs['name']

        return f(programs, file_path)
    return inner

#TODO la figata è che basta cambiare questo per modificare il comportamento di tutte le funzioni
@get_path
def load_day(programs: dict[Info], filename: str):

    error = False

    # Apri il file JSON in modalità lettura
    try:
        with open(filename, 'r') as f:
            # Leggi il contenuto del file JSON e deserializzalo in un oggetto Python
            data = json.load(f)
    except FileNotFoundError:
        error = True
        print(f"{filename} non esistente")
    # Usa l'oggetto Python deserializzato
    
    #prendo il json e per ogni elemento ricreo l'oggetto
    if error:
        return
    
    #TODO in particolar modo di questo
    _loadV1(programs, data)

def load_last_days(programs: dict[Info], days: int = 7):
    """
    Load the last few days from today from JSON files

    gets today plus n days before
    passing days=0 means get only today
    passing days=7 gets last week
    """

    today = datetime.date.today()
    start_day = (today-datetime.timedelta(days=days)).strftime("%Y-%m-%d")
    
    load_range_days(programs, start_day, today.strftime("%Y-%m-%d"))

def _generate_dates(date_start: datetime.date, date_end: datetime.date):
    for d in range((date_end-date_start).days + 1):
        yield ((date_start+datetime.timedelta(days=d)).strftime("%Y-%m-%d"))

def _loadV1(programs, data):
    for data_dict in data:
        #print(data_dict)
        programs[data_dict['name']] = Info(**data_dict) if programs.get(data_dict['name'], None) == None else programs[data_dict['name']] + data_dict['seconds']

def load_range_days(programs: dict[Info], start_day: str, end_day:str):
    date_start = datetime.datetime.strptime(start_day, "%Y-%m-%d").date()
    date_end = datetime.datetime.strptime(end_day, "%Y-%m-%d").date()

    dates : list[str] = []
    
    for d in _generate_dates(date_start, date_end):
        print(d)
        load_day(programs, d)




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
