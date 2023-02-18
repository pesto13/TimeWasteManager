import ctypes
from ctypes import wintypes
import psutil
import time

user32 = ctypes.windll.user32

while True:
    h_wnd = user32.GetForegroundWindow()
    pid = wintypes.DWORD()
    user32.GetWindowThreadProcessId(h_wnd, ctypes.byref(pid))
    process = psutil.Process(pid.value)
    process_name = process.name()
    print(process_name)
    print("...")
    time.sleep(1)