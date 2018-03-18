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
                    os.system('python /root/Autoload/updating.py')
               elif userif == 'N':
                    import Autoload
               else:
                    print(Fore.RED +"Try Again")
     except KeyboardInterrupt:
        print("")
        print(Fore.GREEN +"Thanks For Using AutoLoad!")
        sys.exit()

def update_client_version(version):
    with open("/usr/share/version.txt", "r") as vnum:
        if vnum.read() != version:
            return True
        else:
            return False


def main():
    version = urllib2.urlopen("https://github.com/majorhacker/AutoLoad/blob/master/version.txt").read()
    if update_client_version(version) is True:
        print ("[*] Latest version Avalaible..")
        yes_no()
        
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
