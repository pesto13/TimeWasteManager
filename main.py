import pyautogui
from time import sleep
import ctypes
from ctypes import wintypes
import psutil
import json
import sys
from dataclasses import dataclass

# Activate Google Chrome window
# dizionario: key = nome del programma - value la classes
programs = dict()

browsers = ('chrome', 'firefox', 'msedge', 'iexplore', 'opera', 'brave')


@dataclass
class browserTab():
    name: str
    seconds: int

def getBrowserTab():
    return pyautogui.getActiveWindowTitle()

def getAppName():
    user32 = ctypes.windll.user32
    h_wnd = user32.GetForegroundWindow()
    pid = wintypes.DWORD()
    user32.GetWindowThreadProcessId(h_wnd, ctypes.byref(pid))
    process = psutil.Process(pid.value)
    process_name = process.name()
    
    return process_name

def writeOnFile(programs, original_stdout):
    with open('filename.txt', 'w') as f:
        sys.stdout = f # Change the standard output to the file we created.
        print(programs)
        sys.stdout = original_stdout # Reset the standard output to its original value

count = 0
while True:
    # Get the title of the active tab
    count+=1
    app_name = getAppName()
    app_name = app_name.split('.')[0]
    if app_name in browsers:
        tab_title = getBrowserTab()
    else:
        tab_title = app_name

    if(tab_title in programs.keys()):
        programs[tab_title] += 1
    else:
        programs[tab_title] = 1

    print(tab_title)
    sleep(1)

    if count>=7:
        original_stdout = sys.stdout
        writeOnFile(programs, original_stdout)
        count=0
    


# Print the title
