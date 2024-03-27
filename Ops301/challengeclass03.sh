# Script Name:                  Ops Challenge - File Permissions
# Author:                       Gilbert Collado
# Date of latest revision:      03/27/2024
# Purpose:                      Prompts user for input directory path, Prompts user for input permissions number, Navigates to the directory input by the user and changes all files inside it to the input setting. Prints to the screen the directory contents and the new permissions settings of everything in the directory
# Source1:                      https://g.co/gemini/share/a63ca1c90164 
# Source2:                      https://github.com/codefellows/seattle-ops-301d12/blob/main/class-03/challenges/DEMO.md

#!/bin/bash

# Prompt user for input directory path
read -p "Enter directory path: " directory_path

# Check if directory exists
if [ ! -d "$directory_path" ]; then
    echo "Error: Directory not found."
    exit 1
fi

# Prompt user for input permissions number
read -p "Enter permissions number (e.g. 777): " permissions

# Change permissions of files in the directory
chmod -R "$permissions" "$directory_path"

# Print directory contents and new permissions
echo "Directory contents:"
ls -l "$directory_path"
