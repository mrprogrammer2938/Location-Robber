#!/usr/bin/python3
# This code write by Mr.nope
import os
import time
from colorama import Fore,init
init()
def screen():
    os.system("figlet -f slant Locatin-robber")
def banner():
    print(Fore.GREEN)
    screen()
    print(Fore.WHITE)
def version():
    print(Fore.RED + "Version: " + Fore.BLUE + "1.2.0" + Fore.WHITE)