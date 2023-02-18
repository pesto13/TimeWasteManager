import pyautogui
from time import sleep
import ctypes
from ctypes import wintypes
import psutil
# Activate Google Chrome window
# dizionario: key = nome del programma - value la classes
programs = dict()

browsers = ('chrome.exe', 'msedge.exe')

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
    

for time in range (10):
    # Get the title of the active tab
    
    app_name = getAppName()

    tab_title = app_name

    if(tab_title in programs.keys()):
        programs[tab_title] += 1
    else:
        programs[tab_title] = 1

    print(tab_title)
    sleep(1)

print(programs)

# Print the title
