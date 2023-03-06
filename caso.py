import time
import subprocess

while True:
    import gi
    gi.require_version("Wnck", "3.0")
    from gi.repository import Wnck

    scr = Wnck.Screen.get_default()
    scr.force_update()
    print(scr.get_active_window().get_name())

    time.sleep(3)
