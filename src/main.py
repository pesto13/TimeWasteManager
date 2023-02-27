from time import sleep
from datetime import date

from logic import process
from logic.info import Info
from utilities import utils

def runV1(programs: dict[Info], l: list[str], interval: int):

    browsers = ('chrome', 'firefox', 'msedge', 'iexplore', 'opera', 'brave')
    #attualmente non sta venendo usato ne il path ne il tab_title
    app_name, app_path = process.getAppName()

    tab_title = process.getBrowserTab() if app_name in browsers else app_name

    cat:str = ""
    remember_app: str = ""

    #se l'app è un browser, associo la categoria al browser
    if app_name in browsers:
        from collections import Counter
        # utilizzo di Counter() per contare il numero di occorrenze di ogni elemento
        counted_list = Counter(l)
        # utilizzo di most_common() per trovare l'elemento più comune
        if counted_list:
            cat = counted_list.most_common(1)[0][0]
            
        remember_app = app_name
        app_name += cat
        
    #poi procedo ad inserirlo
    if programs.get(app_name) == None:
        print("non trovato")

        #devo farlo se non è un browser
        """ if remember_app not in browsers:
            cat = ai.get_application_category(app_name) """

        #ora, se non è un browser, genero il suo categoria
        if remember_app not in browsers:
            cat = utils.random_genere()

        programs[app_name] = Info(app_name, cat, interval)
    
    #altrimenti era già presente
    else:
        print("trovato")
        i = programs.get(app_name)
        i.seconds += interval
        cat = i.cathegory
        programs[app_name] = i

    
    

    #endif
    l.append(cat)
    if len(l)>20:
        l.pop(0)

    

def main():
    interval = 1
    programs = dict()
    l = list()
    today = date.today()

    count = 0
    while True:
        count+=1

        runV1(programs, l, interval)
        
        #scrivo su file
        if count>=5:
            count=0

            #stampo subito cosi non perdo info, al massimo ho fatto un interval secondi in più nel giorno precedente :D
            utils.writeOnFile(programs, today)

            #se è cambiato il giorno lo aggiorno
            if today != date.today():
                today = date.today()
                programs = dict()

            
            
            
        sleep(interval)

def prova():
    programs = dict()
    utils.load_last_days(programs, 2)
    for p in programs.values():
        print(p)
    
    """ utils.load_range_days(programs, "2023-02-25", "2023-02-26")
    for p in programs.values():
        print(p) """

if __name__ == '__main__':
    
    #TODO riattivalo nel momento del bisogno
    #TODO non credo serva piu 
    #ai.main()
    #main()
    prova()
