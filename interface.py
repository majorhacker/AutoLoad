#!/usr/bin/env python
import os
import sys
import colorama
from colorama import Fore
os.system('clear')
print("")
print("[*] Enter the name of your wireless interface in Monitor Mode....")
print("")
monitor=raw_input('[monitor:] > ')
print("")
print("[*] Enter the name of your wireless interface in Managed Mode....")
print("")
managed=raw_input('[managed:] > ')
print("")
print("[*] Please wait....")
os.system('echo '+managed+' > managed | touch managed')
os.system('echo '+monitor+' > monitor | touch monitor')
os.system('cp /root/AutoLoad/managed /usr/share/managed.txt')
os.system('cp /root/AutoLoad/monitor /usr/share/monitor.txt')
print("")
print("Done...")
print("Now you can run the Script from anywhere in the Terminal")
print("just type 'autoload' to run the script")
print("")
user_input=raw_input("Press Any key to EXIT...")
os.system('exit')
