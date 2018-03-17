#!/bin/bash
echo "[*]Installing............."
sudo cp /root/Autoload/autoload /usr/local/share/autoload
sudo cp /root/Autoload/autoload /usr/local/bin/autoload
sudo cp /root/Autoload/autoload /usr/bin/autoload
sudo cp /root/Autoload/autoload /usr/share/autoload
sudo cp /root/Autoload/autoload /usr/sbin/autoload
sudo cp /root/Autoload/autoload /usr/local/share/Autoload.py
sudo cp /root/Autoload/autoload /usr/local/bin/Autoload.py
sudo cp /root/Autoload/autoload /usr/share/Autoload.py
sudo cp /root/Autoload/autoload /usr/bin/Autoload.py
sudo cp /root/Autoload/autoload /usr/sbin/Autoload.py
#------------------------------------------------------------------
sudo cp /root/Autoload/GeoLiteCity.dat /usr/share/GeoLiteCity.dat
sudo cp /root/Autoload/GeoLiteCity.dat /usr/bin/GeoLiteCity.dat
sudo cp /root/Autoload/GeoLiteCity.dat /usr/sbin/GeoLiteCity.dat
sudo cp /root/Autoload/GeoLiteCity.dat /usr/local/share/GeoLiteCity.dat
sudo cp /root/Autoload/GeoLiteCity.dat /usr/local/bin/GeoLiteCity.dat
sudo cp /root/Autoload/GeoLiteCity.dat /usr/bin/GeoLiteCity.dat
#------------------------------------------------------------------------------------
sudo cp /root/Autoload/loading.py /usr/local/share/loading.py
sudo cp /root/Autoload/loading.py /usr/local/bin/loading.py
sudo cp /root/Autoload/loading.py /usr/bin/loading.py
sudo cp /root/Autoload/loading.py /usr/share/loading.py
sudo cp /root/Autoload/loading.py /usr/bin/loading.py
sudo cp /root/Autoload/loading.py /usr/sbin/loading.py
#------------------------------------------------------------------------------
sudo cp /root/Autoload/updater.py /usr/local/share/updater.py
sudo cp /root/Autoload/updater.py /usr/local/bin/updater.py
sudo cp /root/Autoload/updater.py /usr/bin/updater.py
sudo cp /root/Autoload/updater.py /usr/share/updater.py
sudo cp /root/Autoload/updater.py /usr/bin/updater.py
sudo cp /root/Autoload/updater.py /usr/sbin/updater.py
#-----------------------------------------------------------------------------------
sudo cp /root/Autoload/version.txt /usr/local/share/version.txt
sudo cp /root/Autoload/version.txt /usr/local/bin/version.txt
sudo cp /root/Autoload/version.txt /usr/bin/version.txt
sudo cp /root/Autoload/version.txt /usr/share/version.txt
sudo cp /root/Autoload/version.txt /usr/bin/version.txt
sudo cp /root/Autoload/version.txt /usr/sbin/version.txt
#------------------------------------------------------------------------------------
sudo cp /root/Autoload/geoip.sh /usr/local/share/geoip.sh
sudo cp /root/Autoload/geoip.sh /usr/local/bin/geoip.sh
sudo cp /root/Autoload/geoip.sh /usr/bin/geoip.sh
sudo cp /root/Autoload/geoip.sh /usr/share/geoip.sh
sudo cp /root/Autoload/geoip.sh /usr/bin/geoip.sh
sudo cp /root/Autoload/geoip.sh /usr/sbin/geoip.sh
#------------------------------------------------------------------------------------

sudo chmod +x /usr/local/share/autoload
sudo chmod +x /usr/local/bin/autoload
sudo chmod +x /usr/bin/autoload
sudo chmod +x /usr/share/autoload
sudo chmod +x /usr/bin/autoload
sudo chmod +x /usr/sbin/autoload
echo ""
echo "[*]Done.."
echo "[*]Now you can run the script anywhere in the terminal "
echo "[*]just type 'autoload' "
