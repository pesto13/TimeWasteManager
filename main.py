import pyautogui
from time import sleep
import ctypes
from ctypes import wintypes
import psutil
import json
import sys
from dataclasses import dataclass
import ai

import debugpy

import tree as t



browsers = ('chrome', 'firefox', 'msedge', 'iexplore', 'opera', 'brave')


@dataclass
class info():
    name: str
    cathegory: str
    seconds: int

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
        print(programs)
        sys.stdout = original_stdout # Reset the standard output to its original value



def runV1(programs: dict, interval):
    
    #prendo il nome dell'app, e se è un browser prendo il nome del tab
    app_name, app_path = getAppName()
    if app_name in browsers:
        tab_title = getBrowserTab()
    else:
        tab_title = app_name


    #print(app_name)


    #se non è presente nel tree allora cerco con ai e aggiungo al tree
    cat:str
    if programs.get(app_name) == None:
        print("non trovato")
        cat = ai.get_application_category(app_name)
        programs[app_name] = info(app_name, cat, interval)
    
    #altrimenti era già presente
    else:
        print("trovato")
        i = programs.get(app_name)
        i.seconds += interval
        #print(i)
        programs[app_name] = i

    

    
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
    debugpy.listen(5678)
    #piccolomain()

    """ myTree = t.AVLTree()
    root = None """

    interval = 5

    programs = dict()

    count = 0
    while True:
        count+=1

        runV1(programs, interval)
        sleep(interval)

        #scrivo su file
        if count>=7:
            #status(programs)
            original_stdout = sys.stdout
            writeOnFile(programs, original_stdout)
            count=0
        
