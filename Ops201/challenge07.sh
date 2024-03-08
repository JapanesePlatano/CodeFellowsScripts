#!/bin/bash

# Script Name:                  Ops Challenge - System Information
# Author:                       Gilbert Collado
# Date of latest revision:      02/27/2024
# Purpose:                      Utilize lshw to extract specific system information
# Source1:                      https://g.co/gemini/share/c497aa43840f   
# Source2:                      https://github.com/PaulThomas83/repos1             

# Check if script is run as root
if [ "$(id -u)" -ne 0 ]; then
    echo "Please run the script as root using sudo."
    exit 1
fi

# Declaration of variables

# main

# Display Name of the computer
echo -e "\nName of the computer:"
lshw | grep -i "product:"

# Display CPU information
echo -e "\nCPU:"
lshw | grep -A 5 -i "cpu" | grep -E "product|vendor|physical id|bus info|width"

# Display RAM information
echo -e "\nRAM:"
lshw | grep -A 7 -i "memory" | grep -E "description|physical id|size"

# Display Display adapter information
echo -e "\nDisplay adapter:"
lshw | grep -A 12 -i "display" | grep -E "description|product|vendor|physical id|bus info|width|clock|capabilities|configuration|resources"

# Display Network adapter information
echo -e "\nNetwork adapter:"
lshw | grep -A 15 -i "network" | grep -E "description|product|vendor|physical id|bus info|logical name|version|serial|size|capacity|width|clock|capabilities|configuration|resources"

