#!/bin/bash

# Script Name:                  Ops Challenge - Domain Analyzer
# Author:                       Gilbert Collado
# Date of latest revision:      03/06/2024
# Purpose:                      Create a script that asks a user to type a domain, then displays information about the typed domain
# Source1:                      https://g.co/gemini/share/39019c55366a 
# Source2:                      https://github.com/codefellows/seattle-ops-201d12/blob/main/class-13/challenges/DEMO.md      

# Function to gather information about a domain
get_domain_info() {
	local domain=$1

	echo "WHOIS information for $domain:"
	whois $domain

	echo -e "\nDIG information for $domain:"
	dig $domain

	echo -e "\nHOST information for $domain:"
	host $domain

	echo -e "\nNSLOOKUP information for $domain:"
	nslookup $domain
}

# Main script
while true; do
	echo -e "\nChoose an option:"
	echo "1. WHOIS"
	echo "2. DIG"
	echo "3. HOST"
	echo "4. NSLOOKUP"
	echo "5. Get information for a domain"
	echo "6. Exit"

	read -p "Enter your choice (1-6): " choice

	case $choice in
    	1)
        	read -p "Enter the domain: " domain
        	whois $domain
        	;;
    	2)
        	read -p "Enter the domain: " domain
        	dig $domain
        	;;
    	3)
        	read -p "Enter the domain: " domain
        	host $domain
        	;;
    	4)
        	read -p "Enter the domain: " domain
        	nslookup $domain
        	;;
    	5)
        	read -p "Enter the domain: " user_domain
        	get_domain_info $user_domain
        	;;
    	6)
        	echo "Exiting the script. Goodbye!"
        	exit 0
        	;;
    	*)
        	echo "Invalid choice. Please enter a number between 1 and 6."
        	;;
	esac
done