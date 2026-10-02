import time
import webbrowser
import os
import random
import pyautogui as pag


url = input("Enter the url: ")

#BODY
while True:
    #Random MOVEMENTS
    x = random.randint(900, 1200)
    y = random.randint(400, 600)
    
    #DURATION
    duration = random.randint(3, 13)

    webbrowser.open(url)
    time.sleep(int(duration))
    pag.moveTo(x, y)
    pag.click()
    os.system("taskkill /F /IM msedge.exe")
