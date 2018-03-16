#!/usr/bin/env	python
# -*- coding: utf-8 -*-

import sys,os
import time
from colorama import Fore,Back,Style
def loading():
	red_bold = Style.BRIGHT + Fore.GREEN
	reset = Style.RESET_ALL
	loading = "loading AutoLoad Script"
	action = 0
	while action < 1:
		for i,char in enumerate(loading):
			if i == 0:
				print "%s%s%s%s" %(red_bold,char.upper(),reset,loading[1:])
			elif i == 1:
				old_loading = loading[0].lower()
				print "%s%s%s%s%s" %(old_loading,red_bold,char.upper(),reset,loading[2:])
			elif i == i:
				old_loading = loading[-0:i].lower()
				print "%s%s%s%s%s" %(old_loading,red_bold,char.upper(),reset,loading[i+1:])
			time.sleep(0.1)
			os.system('clear')
		action += 1
	return True

loading()		
