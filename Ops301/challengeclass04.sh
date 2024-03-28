# Script Name:                  Ops Challenge - Conditionals in Menu Systems
# Author:                       Gilbert Collado
# Date of latest revision:      03/27/2024
# Purpose:                      Create a bash script that launches a menu system asking the user to select an option that meets a condition
# Source1:                      https://g.co/gemini/share/57ca309a5b5b
# Source2:                      https://github.com/codefellows/seattle-ops-301d12/blob/main/class-03/challenges/DEMO.md
# Source3:                      https://linuxhint.com/bash_conditional_statement/

#!/bin/bash

# Function to display the menu
show_menu() {
    echo "Menu:"
    echo "1. Hello world"
    echo "2. Ping self"
    echo "3. IP info"
    echo "4. Exit"
    echo "Please enter your choice:"
}

# Function to execute user's choice
execute_choice() {
    case $1 in
        1)
            echo "Hello world!"
            ;;
        2)
            ping -c 4 localhost
            ;;
        3)
            ifconfig
            ;;
        4)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid choice. Please try again."
            ;;
    esac
}

# Main loop
while true; do
    show_menu
    read choice
    execute_choice $choice
done

