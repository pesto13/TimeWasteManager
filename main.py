import pyautogui
from time import sleep
import ctypes
from ctypes import wintypes
import psutil

import json
import sys
from dataclasses import dataclass
import ai

import random
import string



browsers = ('chrome', 'firefox', 'msedge', 'iexplore', 'opera', 'brave')


@dataclass
class info():
    name: str
    cathegory: str
    seconds: int

    def convert_to_dict(self):
        print(self.__dict__)

    #i nodi nell'albero vengono ordinati per nome dell'applicazione, per poi fare una ricerca più veloce
    """ def __lt__(self, other: object|str):
        if type(other) is info:
            return self.name<other.name
        else:
            return self.name<other
    
    def __gt__(self, other: object|str):
        if type(other) is info:
            return self.name>other.name
        else:
            return self.name>other

    def __eq__(self, __o: object|str) -> bool:
        if type(__o) is info:
            return self.name==__o.name
        else:
            return self.name==__o """

def getBrowserTab():
    return pyautogui.getActiveWindowTitle()

def getAppName():
    user32 = ctypes.windll.user32
    h_wnd = user32.GetForegroundWindow()
    pid = wintypes.DWORD()
    user32.GetWindowThreadProcessId(h_wnd, ctypes.byref(pid))
    process = psutil.Process(pid.value)
    process_name = process.name()

    process_path = process.exe()
    
    return process_name.split('.')[0], process_path
    

def writeOnFile(programs, original_stdout):
    with open('filename.txt', 'w') as f:
        sys.stdout = f # Change the standard output to the file we created.
        json_string = ""
        for p in programs.values():
            json_string += json.dumps(p.__dict__, indent=4)+"\n"
        print(json_string)   
        sys.stdout = original_stdout # Reset the standard output to its original value



def runV1(programs: dict[info], l: list[str], interval):
    
    #attualmente non sta venendo usato ne il path ne il tab_title
    app_name, app_path = getAppName()
    if app_name in browsers:
        tab_title = getBrowserTab()
    else:
        tab_title = app_name

    cat:str
    remember_app: str = ""
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
        #cat = ai.get_application_category(app_name)
        
        # Define the length of the random string
        length = 5

        # Define the pool of characters to choose from
        characters = string.ascii_letters + string.digits

        # Generate the random string if is not a browser
        if remember_app not in browsers:
            cat = ''.join(random.choice(characters) for _ in range(length))

        programs[app_name] = info(app_name, cat, interval)
    
    #altrimenti era già presente
    else:
        print("trovato")
        i = programs.get(app_name)
        i.seconds += interval
        cat = i.cathegory
        programs[app_name] = i

        l.append(cat)
        


    #fineif
    if len(l)>20:
        l.pop(0)

    

    
def piccolomain():
    myTree = t.AVLTree()
    root = None
    nodi = [info("ciao", "svago", 3), info("lol", "svago", 6), info("code", "lavoro", 9)]
    for n in nodi:
        root = myTree.insert_node(root, n)

    myTree.preOrder(root)
    print(myTree.find_value(root,"ciao").key.cathegory)


def status(programs: dict):

    for i in programs.values():
        print(i)
    
if __name__ == '__main__':
    
    #piccolomain()
    interval = 5
    programs = dict()
    l = list()

    count = 0
    while True:
        count+=1

        runV1(programs, l, interval)
        

        #scrivo su file
        if count>=1:
            #status(programs)
            original_stdout = sys.stdout
            writeOnFile(programs, original_stdout)
            count=0
            
        sleep(interval)
