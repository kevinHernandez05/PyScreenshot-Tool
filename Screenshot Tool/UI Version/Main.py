#GUI Screenshot Tool written in Python
#Packages used: pyautogui, tkinter

from datetime import datetime
import time
import pyautogui as ss
import tkinter as tk

def screenshot():
    
    now = datetime.now()
    name = 'screenshot-' + now.strftime("%a-%d-%m") + '.png'
    img = ss.screenshot(name)
    img.show()


root = tk.Tk()
root.title("Screenshot app")
root.geometry("282x43")
frame = tk.Frame(root)
frame.pack()



button = tk.Button(
    frame,
    text = "Shoot!",
    command = screenshot

)

button.pack(side = tk.LEFT)

closeBtn = tk.Button(
    frame,
    text = "Close",
    command = quit
)

closeBtn.pack(side = tk.LEFT)

root.mainloop()



