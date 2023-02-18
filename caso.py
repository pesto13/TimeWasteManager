import pyautogui
from time import sleep
# Activate Google Chrome window
# dizionario: key = nome del programma - value la classes
programs = dict()

for time in range (10):
    # Get the title of the active tab
    tab_title = pyautogui.getActiveWindowTitle()
    #diobestia
    if(tab_title in programs.keys()):
        programs[tab_title] += 1
    else:
        programs[tab_title] = 1

    print(tab_title)
    sleep(1)

print(programs)

# Print the title
