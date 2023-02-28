from time import sleep, time
from datetime import date

from logic import process
from logic.info import Info

from storedata import file_json





from logic import process

""" def runV1(programs: dict[Info], l: list[str], interval: int):

    browsers = ('chrome', 'firefox', 'msedge', 'iexplore', 'opera', 'brave')
    #attualmente non sta venendo usato ne il path ne il tab_title
    app_name, app_path = process.getAppName()

    # tab_title = process.getBrowserTab() if app_name in browsers else app_name

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
        if remember_app not in browsers:
            cat = ai.get_application_category(app_name)

        #ora, se non è un browser, genero il suo categoria
        if remember_app not in browsers:
            cat = storedata.random_genere()

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
        l.pop(0) """


def runV2(timeline: list[Info], cat_app: dict[str], latest_cat: list[str], interval):
    browsers = ('chrome', 'firefox', 'msedge', 'iexplore', 'opera', 'brave')
    #attualmente non sta venendo usato ne il path ne il tab_title
    app_name = process.get_app_name()

    # tab_title = process.getBrowserTab() if app_name in browsers else app_name

    cat:str = ""
    remember_app: str = ""

    #se l'app è un browser, associo la categoria al browser
    if app_name in browsers:
        from collections import Counter
        # utilizzo di Counter() per contare il numero di occorrenze di ogni elemento
        counted_list = Counter(latest_cat)
        # utilizzo di most_common() per trovare l'elemento più comune
        if counted_list:
            cat = counted_list.most_common(1)[0][0]
            
        remember_app = app_name
        app_name += cat
        
    #poi procedo ad inserirlo
    if cat_app.get(app_name) == None:

        #devo farlo se non è un browser
        """ if remember_app not in browsers:
            cat = ai.get_application_category(app_name) """

        #ora, se non è un browser, genero il suo categoria
        if remember_app not in browsers:
            cat = file_json.random_genere()

        cat_app[app_name] = cat
        # programs[app_name] = Info(app_name, cat, interval)
    
    #altrimenti era già presente
    else:
        cat = cat_app.get(app_name)
    

    if len(timeline)==0 or timeline[-1].name != app_name:

        timeline.append(Info(
                name=app_name,
                cathegory=cat,
                start_time=int(time()),
                delta_time=interval
                ))
        
    else:
        timeline[-1].delta_time+=interval

    
    

    #endif
    latest_cat.append(cat)
    if len(latest_cat)>20:
        latest_cat.pop(0)
    

def main():
    interval = 1
    """ programs = dict()
    l = list() """
    today = date.today()
    """
    -una lista del tempo delle app
    -un dizionario per associare app e categoria
    -una lista delle ultime interval * numero di app usate
    """
    timeline: list[Info] = list()
    cat_app: dict[str] = dict()
    latest_cat: list[str] = list()
    count = 0
    file_json.load_day(timeline, today)
    while True:
        count+=1

        # runV1(programs, l, interval)
        runV2(timeline, cat_app, latest_cat, interval)

        #scrivo su file
        if count>=3:
            count=0
            print("stampo")
            #stampo subito cosi non perdo info, al massimo ho fatto un interval secondi in più nel giorno precedente :D
            # per v1
            file_json.write_file(timeline, today)
            #timeline = []
            #se è cambiato il giorno lo aggiorno
            if today != date.today():
                today = date.today()
                # per v1
                # programs = dict()
                timeline = list()
            
            
            
        sleep(interval)

def prova():
    
    
    while True:
        process.get_app_name()
        sleep(1)

if __name__ == '__main__':
    
    
    main()
    # prova()
