import pyautogui
from random import *
from time import sleep
sleep(5)  
writes = ["Hello, World!", "Python is great!", "Automating tasks is fun!", "Let's write some code!", "PyAutoGUI is powerful!"]
for n in range(0,10):
    write = choice(writes)
    pyautogui.write(write, interval=0.25)  
    pyautogui.press('enter') 