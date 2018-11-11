#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scapy.all as scapy
import optparse
from colorama import Fore
import sys
import time

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface name.")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please Specify an Interface, use --help for more info.")
    return options

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast = broadcast/arp_request
    answer = scapy.srp(arp_broadcast, timeout=1, verbose=False)[0]
    
    for element in answer:
	 mac = element[1].hwsrc
	 return mac


def sniff(interface):
     print(Fore.GREEN+"\r[+] System is Safe.")
     scapy.sniff(iface=interface, store=False, prn=process_packet)

def process_packet(packet):
     if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
          try:
               real_mac = get_mac(packet[scapy.ARP].psrc)
               response_mac = packet[scapy.ARP].hwsrc
               if real_mac != response_mac:
                    print(Fore.RED+"\r[!] You are Under Attack!!")
                    
          except IndexError:
               pass
          

options = get_arguments()

sniff(options.interface)
