#!/usr/bin/python
import os
import sys
def main():
     print("")
     print("[*] Updating.....")
     print("")
     print("Removing Old Files")
     os.system('chmod +x /root/Autoload/uninstall.sh')
     os.system('bash /root/Autoload/uninstall.sh')
     print("")
     print("Downloding Update")
     os.system('cd Downloads/')
     os.system('git clone https://github.com/majorhacker/AutoLoad.git')
     print("")
     print("Installing New Files..")
     os.system('chmod +x /root/Downloads/AutoLoad/setup.sh')
     os.system("bash /root/Downloads/AutoLoad/setup.sh")
     os.system('rm -r /root/Downloads/AutoLoad')
     print("")
     print("[*] Updating Complete")
     sys.exit()

main()
     
