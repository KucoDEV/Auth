
import requests
import time
from random import randrange
from pystyle import *
from colorama import Fore, Style
import progressbar
ascii = '''
 ▄▄▄       █    ██ ▄▄▄█████▓ ██░ ██ 
▒████▄     ██  ▓██▒▓  ██▒ ▓▒▓██░ ██▒
▒██  ▀█▄  ▓██  ▒██░▒ ▓██░ ▒░▒██▀▀██░
░██▄▄▄▄██ ▓▓█  ░██░░ ▓██▓ ░ ░▓█ ░██ 
 ▓█   ▓██▒▒▒█████▓   ▒██▒ ░ ░▓█▒░██▓
 ▒▒   ▓▒█░░▒▓▒ ▒ ▒   ▒ ░░    ▒ ░░▒░▒
  ▒   ▒▒ ░░░▒░ ░ ░     ░     ▒ ░▒░ ░
  ░   ▒    ░░░ ░ ░   ░       ░  ░░ ░
      ░  ░   ░               ░  ░  ░'''[1:]
      
System.Clear()
System.Title("Simple Auth System")
print('\n'*2)
print(Colorate.Horizontal(Colors.red_to_black, Center.XCenter(ascii)))


username = input(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "?" + Fore.WHITE + "]" + Fore.RED + " Pseudo >> " + Fore.WHITE)
if username == "Auth":
    password = input(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "?" + Fore.WHITE + "]" + Fore.RED + " Mot de passe >> " + Fore.WHITE)

    url = "https://pastebin.com/raw/J9PJXFQi"

    x = requests.get(url)

    try:
        if password in x.text:
            
            number = 0
            z = randrange(500)
            proxies = randrange(500)

            print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " You are connected to the server." + Fore.RESET)
            
            t = 0.0

            print(Style.BRIGHT + Fore.RED)
            bar = progressbar.ProgressBar(maxval=10, widgets=[
	            ' Starting... ',
	            progressbar.Bar(left='| ', marker='█', right=' | '),
	            progressbar.SimpleProgress(),
            ]).start()
            
            while t <= 10.0:
                bar.update(t)
                time.sleep(0.1)
                t += 0.1
            bar.finish()
    except:
        print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " I can't connect to the server!\nPlease check your internet connection." + Fore.RESET)
        time.sleep(5)
        exit()
else:
    input(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " I can't find an account named '" + Fore.WHITE + f"{username}" + Fore.RED + "'.")
