#!/usr/bin/env python
import requests, re, urlparse
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

target_url = options.url
target_links = []

def extract(url):
     try:
	  response = requests.get(url)
     except requests.exceptions.ConnectionError:
	  user= raw_input("[!] Connection Error!")
	  sys.exit()
     return re.findall('(?:herf=")(.*?)"', response.content)
     
def crawl(url):
     herf = extract(url)
     for link in herf:
	  link = urlparse.urljoin(url, link)
	  
	  if "#" in link:
	       link = link.split("#")[0]
	  if target_url in link and link not in target_links:
	       target_links.append(link)
	       print(link)
	       crawl(link)

crawl(target_url)
	  
