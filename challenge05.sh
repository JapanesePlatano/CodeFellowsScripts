#!/bin/bash

# Script Name:                  Platano
# Author:                       Gilbert Collado
# Date of latest revision:      02/2023/2024
# Purpose:                      To run a loop

while true; do
    # Display running processes
    echo -e "\nRunning processes:"
    ps aux

    # Ask the user for a PID
    read -p $'\nEnter the PID to kill (or press Ctrl + C to exit): ' pid_to_kill

    # Check if the input is a valid integer
    if [[ $pid_to_kill =~ ^[0-9]+$ ]]; then
        # Check if the process exists
        if ps -p "$pid_to_kill" > /dev/null; then
            # Kill the process
            kill "$pid_to_kill"
            echo "Process with PID $pid_to_kill killed."
        else
            echo "No process found with PID $pid_to_kill."
        fi
    else
        echo "Invalid input. Please enter a valid PID."
    fi
done