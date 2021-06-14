#!/usr/bin/python3
# This code write by Mr.nope
from colorama import Fore,init
from modules import banner
import os
import sys
import time
import ipapi
init()
noth = "\nPlease Enter IP!"
url_loc = "\nEnter url: "
web = "\nEnter ip: "
def cls():
    os.system("clear")
def title():
    os.system("xtitle Loaction-Robber")
def run():
    title()
    cls()
    banner.banner()
    banner.version()
    try:
       print("\nIf you do not have an ip address, enter the (url)!")
       print(noth)
       ip = input(web)
       if ip == 'url':
           print("\nPlease, Enter url!\nAnd copy ip!\n")
           ping_url = input(url_loc)
           os.system("ping -w 1 " + ping_url)
           time.sleep(2)
           try2()
       else:
           search = ipapi.location(ip=ip, key=None)
           print("\n")
           print(Fore.RED + "[~] " + Fore.WHITE + "Ip: " + Fore.GREEN + search["ip"])
           print(Fore.RED + "[~] " + Fore.WHITE + "City " + Fore.GREEN + search["city"])
           print(Fore.RED + "[~] " + Fore.WHITE + "Region " + Fore.GREEN + search["region"])
           print(Fore.RED + "[~] " + Fore.WHITE + "Country: " + Fore.GREEN + search["country"])
           print(Fore.RED + "[~] " + Fore.WHITE + "Org: " + Fore.GREEN + search["org"])
           print(Fore.RED + "[~] " + Fore.WHITE + "Time Zone: " + Fore.GREEN + search["timezone"])
           print(Fore.RED + "[~] " + Fore.WHITE + "Languages: " + Fore.GREEN + search["languages"])
           time.sleep(2)
           try1()
    except KeyboardInterrupt:
        print("\nCtrl + C")
        print(Fore.RED + "\nError" + Fore.WHITE + ", Please Try Again!")
        sys.exit()
def try1():
    try_meinmenu = input("\033[33mDo you want to try again? [y/n] " + Fore.WHITE)
    if try_meinmenu == 'y':
        run()
    elif try_meinmenu == 'n':
        cls()
        print(Fore.GREEN + "Exiting..." + Fore.WHITE)
        sys.exit()
    else:
        try1()
def try2():
    try_meinmenu = input("\npress Enter...")
    if try_meinmenu == '':
        run()
    else:
        run()
if __name__ == '__main__':
    try:
        run()
    except:
        print(" ")
        sys.exit()