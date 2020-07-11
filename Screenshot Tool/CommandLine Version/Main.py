#Command line Screenshot Tool written in Python
#Packages used: pyautogui

from datetime import datetime
import time
import pyautogui

def screenshot():
    
    now = datetime.now()
    name = 'screenshot-' + now.strftime("%a-%d- %m") + '.png'
    time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()

    exit()

screenshot()






