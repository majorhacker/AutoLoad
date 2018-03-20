#!/usr/bin/env python
import os, sys
from time import sleep
import os
import sys
import requests
import httplib
import socket
import colorama
from colorama import Fore

def check_internet():
    test_con="www.google.com"
    test_res="/intl/en/policies/privacy/"
    test=httplib.HTTPConnection(test_con)
    try:
        test.request("GET",test_res)
        response=test.getresponse()
    except httplib.ResponseNotReady as e:
        print("Improper Connection State")
    except socket.gaierror as e:
        print("Not Connected to the Internet")
    else:
        print(Fore.GREEN +"Connected")
os.system('clear')
if not os.geteuid() == 0:
    sys.exit("\033[1;31mPlease run this script as root!\033[0m")

print("")
print("  ------------------")
print("< \033[1;36mAutoLoad Installer!!\033[1;36m >")
print("  ------------------")
print("         \   ^__^   ")
print("          \  (oo)\_______    ")
print("             (__)\       )\/\  ")
print("                 ||-----||      ")
print("                 ||     ||     ")
print("")
print("")
os.system('mkdir /root/AutoLoad/handshakes')
print(Fore.GREEN +"[*] Enter the name of your wireless interface in Monitor Mode....")
print("")
monitor=raw_input(Fore.BLUE +'[monitor:] > ')
print("")
print(Fore.GREEN +"[*] Enter the name of your wireless interface in Managed Mode....")
print("")
managed=raw_input(Fore.BLUE +'[managed:] > ')
print("")
os.system('echo '+managed+' > managed | touch managed')
os.system('echo '+monitor+' > monitor | touch monitor')
os.system('cp /root/AutoLoad/managed /usr/share/managed.txt')
os.system('cp /root/AutoLoad/monitor /usr/share/monitor.txt')
check_internet()
print("")
print "\033[1;33m[*] Loading...\033[0m"
os.system('apt-get install aircrack-ng')
os.system('apt install wifiphisher ')
os.system('apt install metasploit-framework')
print "\033[1;32m[!] Finished Installing! Run 'autoload' to run program [!]\033[0m"
print("")
user=raw_input("press any key to EXIT!..")
sys.exit()
