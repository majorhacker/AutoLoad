#!/bin/bash
function is_it_an_ip()
{
	IIA=$1
	IIAI=${#IIA}
	if [[ "$IIA" = "" ]]
	then
		echo -e ""$RS"Error 9. No parameteres passed"
		sleep 2
	else
		if [[ "$IIAI" -le 15 && "$IIAI" -ge 7 ]]
		then
			echo 1
		else
			echo 0
		fi
	fi
}
function geolocate_ip()
{
	locbool=1
	echo -e ""$BS"Please wait..."$CE""
	A1="$1"
	AA1=$(is_it_an_ip "$A1")
	if [[ "$AA1" = 1 ]]
	then
		country=$(curl ipinfo.io/"$A1"/country 2>/dev/null)
		if [[ "$country" = "" ]]
		then
			country=""$RS"Not found"$CE""
		fi
		loc=$(curl ipinfo.io/"$A1"/loc 2>/dev/null)
		if [[ "$loc" = "" ]]
		then
			locbool=0
			loc=""$RS"Not found"$CE""
		fi
		city=$(curl ipinfo.io/"$A1"/city 2>/dev/null)
		if [[ "$city" = "" ]]
		then
			city=""$RS"Not found"$CE""
		fi
		org=$(curl ipinfo.io/"$A1"/org 2>/dev/null)
		if [[ "$org" = "" ]]
		then
			org=""$RS"Not found"$CE""
		fi
		postal=$(curl ipinfo.io/"$A1"/postal 2>/dev/null)
		if [[ "$postal" = "" ]]
		then
			postal=""$RS"Not found"$CE""
		fi
		region=$(curl ipinfo.io/"$A1"/region 2>/dev/null)
		if [[ "$region" = "" ]]
		then
			region=""$RS"Not found"$CE""
		fi
		hostname=$(curl ipinfo.io/"$A1"/hostname 2>/dev/null)
		if [[ "$hostname" = "" ]]
		then
			hostname=""$RS"Not found"$CE""
		fi
		echo -e "     Country: $country"
		echo -e "      Region: $region"
		echo -e "    Location: $loc"
		echo -e "        City: $city"
		echo -e "      Postal: $postal"
		echo -e "    Hostname: $hostname"
		echo -e "Organization: $org"
		if [[ "$locbool" = 0 ]]
		then
			echo -e ""$RS" m"$CE") Open google maps location"
		else
			echo -e ""$YS" m"$CE") Open google maps location"
		fi
                echo "Press any key to go Back..."
		read ge
		if [[ "$ge" = "m" ]]
		then
			if [[ "$locbool" = 0 ]]
			then
				echo -e ""$RS"Location was not found"$CE""
				sleep 3
			else
				gio open https://www.google.gr/maps/search/"$loc"/
			fi
		else
			clear
			BACKL=1
		fi
	else
		echo 0
	fi
}
echo -e ""$BS"[IP:] >"$CE" "
		read IPG
		clear
		geolocate_ip "$IPG"
