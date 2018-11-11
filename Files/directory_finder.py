
#!/usr/bin/env python

import requests
import optparse
import sys
from colorama import Fore

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-u", "--url", dest="url", help="url .")
    (options, arguments) = parser.parse_args()
    if not options.url:
        parser.error("[-] Please Specify an URL, use --help for more info.")
    return options

options = get_arguments()
target = options.url
print("[+] Testing URL'S")
def request(url):
     try:
	  return requests.get("http://" + url)
     except requests.exceptions.ConnectionError:
	  print("[!] Not Found " +url)
     except requests.exceptions.InvalidURL:
	  pass


with open("/root/AutoLoad/Files/diclist.txt") as diclist:
     for line in diclist:
	  word = line.strip()
	  test_url = target + "/" + word
	  response = request(test_url)
	  if response:
	       print(Fore.GREEN+"[+] URL Found --> " + test_url)
	       with open("URL of" + target, 'w') as out:
		    out.write("\n"+test_url+ "\"")

user = raw_input("[+] Founded URL'S saved in a File!")
sys.exit()
