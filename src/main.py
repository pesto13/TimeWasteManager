from time import sleep, time
from datetime import date, timedelta

from logic import process
from logic.info import Info

from storedata import file_json
from storedata import db


from logic import process

def runV2(timeline: list[Info], application_to_category: dict[str], latest_categories: list[str], interval):
    MAX_LIST = 20
    BROWSERS = ('chrome', 'firefox', 'msedge', 'iexplore', 'opera', 'brave')
    #attualmente non sta venendo usato ne il path ne il tab_title
    app_name = process.get_app_name()

    # tab_title = process.getBrowserTab() if app_name in browsers else app_name

    cat:str = ""
    remember_app: str = ""

    #se l'app è un browser, associo la categoria al browser
    if app_name in BROWSERS:
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
        if remember_app not in BROWSERS:
            cat = file_json.random_genere()

        application_to_category[app_name] = cat
        # programs[app_name] = Info(app_name, cat, interval)
    
    #altrimenti era già presente
    else:
        cat = application_to_category.get(app_name)
    

    #se non ci sono elementi oppure se ho cambiato app
    if len(timeline)==0 or timeline[-1].application_name != app_name:

        timeline.append(Info(
                application_name=app_name,
                category=cat,
                start_time=int(time()),
                seconds_used=interval,
                using_date=date.today().strftime("%d/%m/%Y")
                ))
    #se sto usando la stessa app
    else:
        timeline[-1].seconds_used+=interval

    #endif
    latest_categories.append(cat)
    if len(latest_categories)>MAX_LIST:
        latest_categories.pop(0)

def is_enought_time(seconds: int, interval: int) -> bool:
    """
    return true every interval*MAX seconds
    default interval is 1 (every 10 seconds)
    """
    MAX = 5
    return True if seconds%(interval*MAX)==0 else False

def is_enought_elements(elements_count: int) -> bool:
    MAX_ELEMENTS = 5
    return True if elements_count>MAX_ELEMENTS else False

def startup(timeline: list[Info], application_to_category: dict[str], latest_categories: list[str]):
    row: tuple
    if ((row := db.pop_last()) == None):
        return
    
    i = Info(*row)
    timeline.append(i)
    application_to_category[i.application_name] = i.category
    latest_categories.append(i.category)

def main():
    interval = 1
    today = date.today()
    """
    -una lista del tempo delle app
    -un dizionario per associare app e categoria
    -una lista delle ultime interval * numero di app usate
    """
    timeline: list[Info] = list()
    application_to_category: dict[str] = dict()
    latest_categories: list[str] = list()
    
    # db.drop()
    db.create()

    startup(timeline, application_to_category, latest_categories)
    
    while True:
        
        runV2(timeline, application_to_category, latest_categories, interval)

        if is_enought_time(timeline[-1].seconds_used, interval) or is_enought_elements(len(timeline)):

            for t in timeline:
                print(t)
            
            #se è da tanto che sto usando la stessa app scrivo lo stesso ma elimino la riga
            if(timeline[0].start_time==Info(*db.get_last()).start_time):
                db.pop_last()
            db.insert_all(timeline)

            timeline = [timeline[-1]]

            #se è cambiato il giorno lo aggiorno
            if today != date.today():
                today = date.today()

                timeline = list()            
        sleep(interval)


def prova():
    records = db.load_from_date_to_date(start_date=date.today().timestamp(), end_date=date.today()+timedelta(days=1))
    
    for r in records:
        print(r)

if __name__ == '__main__':
    # main()
    prova()