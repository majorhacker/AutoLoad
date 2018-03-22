#!/usr/bin/python
import subprocess
import urllib2
import os
import colorama
import sys
from colorama import Fore
def yes_no():
     try:
          print("")
          print("You want to Update!")
          userif = ' '
          while not(userif == 'Y' or userif == 'N'):
               userif=raw_input("[Type [y] YES or [n] NO:] > ").upper()
               if userif == 'Y':
                    os.system('gnome-terminal --window --working-directory=/root/Downloads  -- python /root/AutoLoad/updating.py')
               elif userif == 'N':
                    import Autoload
               else:
                    print(Fore.RED +"Try Again")
     except KeyboardInterrupt:
        print("")
        print(Fore.GREEN +"Thanks For Using AutoLoad!")
        sys.exit()

def update_client_version():
     version = urllib2.urlopen("https://github.com/majorhacker/AutoLoad/blob/master/version.txt").read()
     vnum=open("/usr/share/version.txt", "r").read()
     if vnum != version:
          return True
     else:
          return False


def main():
     if update_client_version() is True:
          print ("[*] Latest version Avalaible..")
          yes_no()
     elif update_client_version() is False:
          print("[*] You are already up to date with git origin master.")
          print("")
          user_input=raw_input("Press Any key to Go back...")
          import Autoload
     else:
          print("[*] You are already up to date with git origin master.")
          print("")
          user_input=raw_input("Press Any key to Go back...")
          import Autoload
          
try:
     print("[*] Checking version information..")
     main()
except KeyboardInterrupt:
     print("")
     print(Fore.GREEN +"Thanks For Using AutoLoad!")
     sys.exit()
