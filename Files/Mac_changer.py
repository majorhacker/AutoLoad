#!/usr/bin/env python

import subprocess
import optparse
import re
import sys

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to Change its MAC address.")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address.")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please Specify an Interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please Specify a new MAC address, use --help for more info.")
    return options

def change_mac(interface, new_mac):
    print("[*] Changing Mac Address for " +interface+ " to " +new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_mac(interface):
    result = subprocess.check_output(["ifconfig", interface])
    mac_add = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", result)
    if mac_add:
        return(mac_add.group(0))
    else:
        print("[!] Error MAC address not Found!")
        sys.exit()

options = get_arguments()

current_mac = get_mac(options.interface)
print("current MAC = " + str(current_mac))
change_mac(options.interface, options.new_mac)
current_mac = get_mac(options.interface)

if current_mac == options.new_mac :
    print("MAC changed Succesfully")
else:
    print("[!] Error MAC not changed.")
