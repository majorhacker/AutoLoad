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
        print "\033[1;32m[!] Installing Not Finished, Try again Later ! Type 'als' to run the program [!]\033[0m"
        print("")
        user=raw_input("press any key to EXIT!..")
        sys.exit()
    except socket.gaierror as e:
        print("Not Connected to the Internet")
        print "\033[1;32m[!] Installing Not Finished, Try again Later ! Type 'als' to run the program [!]\033[0m"
        print("")
        user=raw_input("press any key to EXIT!..")
        sys.exit()
    else:
        print(Fore.GREEN +"Connected")
os.system('clear')
if not os.geteuid() == 0:
    sys.exit("\033[1;31mPlease run this script as root!\033[0m")

print("")
print("  ------------------")
print("< \033[1;36mAutoLoad Script Installer!!\033[1;36m >")
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
print "\033[1;32m[#] Downloading Files\033[0m"
os.system('apt-get install aircrack-ng -y')
os.system('apt install wifiphisher -y')
os.system('apt install wine32 -y')
os.system('wget ')
os.system('''
winecfg
wine msiexec /i python-2.7.12.msi /L*v log.txt
wine pywin32-220.win32-py2.7.exe
wine pyHook-1.5.1.win32-py2.7.exe
wine /root/.wine/drive_c/Python27/python.exe -m pip install pyinstaller
''')
os.system('apt install metasploit-framework -y')
os.system('apt install nmap -y')
os.system('apt install sslstrip -y')
os.system('sudo apt-get install python-pip -y')
print "\033[1;32m[#] Installing Files\033[0m"
os.system('sudo pip install pyinstaller')
os.system('sudo pip install netfilterqueue')
os.system('sudo pip install validate_email')
os.system('sudo pip install scapy.http')
os.system('sudo pip install pyDNS')
os.system('git clone https://github.com/LeonardoNve/dns2proxy.git')
print "\033[1;32m[!] Finished Installing! Type 'als' to run the program [!]\033[0m"
print("")
user=raw_input("press any key to EXIT!..")
sys.exit()
