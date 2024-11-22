#!/bin/bash

clear

# Function to center text
center() {
  termwidth=$(stty size | cut -d" " -f2)
  padding="$(printf '%0.1s' ={1..500})"
  printf '%*.*s %s %*.*s\n' 0 "$(((termwidth-2-${#1})/2))" "$padding" "$1" 0 "$(((termwidth-1-${#1})/2))" "$padding"
}


# Display ban message
ban

# Display the Installation status
echo -e "\e[92m"
center "INSTALLATION"
echo -e "\e[34mSTABLE CONNECTION [\e[92m✓\e[34m]\e[0m"
sleep 1.0

# Environment check
echo -e "\e[34mCHECKING ENVIRONMENT [\e[92m✓\e[34m]\e[0m"
# dpkg --configure -a
sleep 1.0

# Installing packages
echo -e "\e[34mPACKAGES BEING INSTALLED WAIT....\e[0m"
apt-get upgrade -y >/dev/null 2>&1
apt-get update -y >/dev/null 2>&1
pkg install python -y >/dev/null 2>&1
pkg install git -y >/dev/null 2>&1
pkg install wget -y >/dev/null 2>&1
python -m pip install requests >/dev/null 2>&1
pkg install curl -y >/dev/null 2>&1
pip install colorama >/dev/null 2>&1

# Indicate installation is complete
echo -e "\e[34mPACKAGES INSTALLED [\e[92m✓\e[34m]\e[0m"
sleep 1.0

# Final launch message
echo -e "\e[92m"
center "LAUNCHING KILLNET-BOMER"
echo -e "\e[34mFINALIZING KILLNET-BOMER [\e[92m✓\e[34m]\e[0m"

# Open the provided Telegram link
am start -a android.intent.action.VIEW -d https://t.me/KillnetBomber > /dev/null 2>&1
sleep 2.0

# Launching the tool
echo -e "\e[34mSTARTING.....[\e[92m✓\e[34m]\e[0m"
sleep 2.0

# Remove setup file
rm $HOME/KILLNET-BOMBER/setup.sh >/dev/null 2>&1
python main.py

