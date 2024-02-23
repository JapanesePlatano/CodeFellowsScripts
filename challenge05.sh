#!/bin/bash

# Script Name:                  Ops Challenge - Loops
# Author:                       Gilbert Collado
# Date of latest revision:      02/23/2024
# Purpose:                      To run a loop
# Source:                       https://chat.openai.com/share/1256b16c-bdd6-470d-96ef-f42aecc7a317

while true; do
    echo -e "\nRunning processes:"
    ps aux

    read -p "Enter the PID to kill (or press Ctrl + C to exit): " pid_to_kill

    if [[ "$pid_to_kill" =~ ^[0-20]+$ ]]; then
        if kill "$pid_to_kill" 2>/dev/null; then
            echo "Process with PID $pid_to_kill killed."
        else
            echo "No process found with PID $pid_to_kill."
        fi
    else
        echo "Invalid input. Please enter a valid PID."
    fi
done