import pyautogui
import ctypes

import psutil

def getBrowserTab():
    return pyautogui.getActiveWindowTitle()

def getAppName():
    user32 = ctypes.windll.user32
    h_wnd = user32.GetForegroundWindow()
    pid = ctypes.wintypes.DWORD()
    user32.GetWindowThreadProcessId(h_wnd, ctypes.byref(pid))
    process = psutil.Process(pid.value)
    process_name = process.name()

    #da quello che ho visto il path esplode in alcuni casi, avevo avviato lol tipo
    """ try:
        process_path = process.exe()
    except :
        print("bro non sono riuscito :D")
        process_path = None """
        
    return process_name.split('.')[0]