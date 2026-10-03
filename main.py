import time 
import webbrowser 
import os 
import random 
import pyautogui as pag 
from colorama import Fore, Style, init 
import pyfiglet 
 
 
 
 
 
init(autoreset=True) 
 
def wel(): 
    #LINE 
    print(Fore.CYAN + "=" * 55) 
     
#WELCOME 
    welcome_text = pyfiglet.figlet_format("WELCOME", font="standard") 
     
    # LINE 
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA] 
    lines = welcome_text.splitlines() 
     
    for i, line in enumerate(lines): 
        # CYC 
        color = colors[i % len(colors)] 
        print(color + Style.BRIGHT + line) 
         
    #MY SUBTXT 
    print(Fore.CYAN + "=" * 55) 
    print(Fore.YELLOW + Style.BRIGHT + f"{'IT WILL REAPEAT UNTILL YOU STOP IT':^55}") 
    print(Fore.CYAN + "=" * 55) 
 
wel() 
 
time.sleep(2) 
#URL 
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
