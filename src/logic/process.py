# import pyautogui
import ctypes
from ctypes import wintypes
import psutil

import platform
import subprocess

""" 
def getBrowserTab():
    return pyautogui.getActiveWindowTitle() """

def get_os():
    return platform.system()


def get_app_name():
    if(get_os() == "Windows"):
        
        user32 = ctypes.windll.user32
        h_wnd = user32.GetForegroundWindow()
        pid = wintypes.DWORD()
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
    

    elif(get_os() == "Linux"):
        #TODO sistema il return
        # Esegui il comando xprop per ottenere l'ID della finestra in foreground
        nome_processo = ""
        try:
            output = subprocess.check_output(['xprop', '-root', '_NET_ACTIVE_WINDOW'])
            wid = output.split()[-1]

            # Verifica che l'ID finestra sia valido prima di passarlo al comando xprop
            if wid != b'0x0':
                output = subprocess.check_output(['xprop', '-id', wid, 'WM_CLASS'])
                nome_processo = output.split(b'=')[-1].strip().decode()
                print(f"Il nome del processo in foreground è: {nome_processo}")
            else:
                print(f"Nessuna finestra attiva")

        except subprocess.CalledProcessError as e:
            print(f"Errore durante l'esecuzione del comando: {e}")

        return nome_processo
