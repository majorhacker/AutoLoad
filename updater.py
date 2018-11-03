#!/usr/bin/python
import subprocess
import urllib2
import os
import colorama
import sys
from colorama import Fore
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
          print("Download and Install")
     elif update_client_version() is False:
          print("[*] You are already up to date with Latest version.")
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
