from time import sleep, time
from datetime import date

from logic import process
from logic.info import Info

from storedata import file_json
from storedata import db


from logic import process

def runV2(timeline: list[Info], application_to_category: dict[str], latest_categories: list[str], interval):
    MAX_LIST = 20
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
        counted_list = Counter(latest_categories)
        # utilizzo di most_common() per trovare l'elemento più comune
        if counted_list:
            cat = counted_list.most_common(1)[0][0]
            
        remember_app = app_name
        app_name += cat
        
    #poi procedo ad inserirlo
    if application_to_category.get(app_name) == None:

        #devo farlo se non è un browser
        """ if remember_app not in browsers:
            cat = ai.get_application_category(app_name) """

        #ora, se non è un browser, genero il suo categoria
        if remember_app not in browsers:
            cat = file_json.random_genere()

        application_to_category[app_name] = cat
        # programs[app_name] = Info(app_name, cat, interval)
    
    #altrimenti era già presente
    else:
        cat = application_to_category.get(app_name)
    

    if len(timeline)==0 or timeline[-1].application_name != app_name:

        timeline.append(Info(
                application_name=app_name,
                category=cat,
                start_time=int(time()),
                seconds_used=interval,
                using_date=date.today().strftime("%d/%m/%Y")
                ))
        
    else:
        timeline[-1].seconds_used+=interval

    #endif
    latest_categories.append(cat)
    if len(latest_categories)>MAX_LIST:
        latest_categories.pop(0)
    

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
    application_to_category: dict[str] = dict()
    latest_categories: list[str] = list()
    count = 0
    # db.drop()
    db.create()

    if ((row := db.load_last()) != None):
        timeline.append(Info( *row ))
    
    #file_json.load_day(timeline, today)
    while True:
        count+=1

        # runV1(programs, l, interval)
        runV2(timeline, application_to_category, latest_categories, interval)

        #scrivo su file
        #ora scrive su db
        if count>=3:
            count=0
            # print("stampo")
            #stampo subito cosi non perdo info, al massimo ho fatto un interval secondi in più nel giorno precedente :D
            # per v1
            #file_json.write_file(timeline, today)
            #db.insert(timeline[0])
            for t in timeline:
                print(t)
            db.insert_all(timeline)
            #se è cambiato il giorno lo aggiorno
            if today != date.today():
                today = date.today()
                # per v1
                # programs = dict()
                timeline = list()            
        sleep(interval)


if __name__ == '__main__':
    
    
    main()
    # prova()
