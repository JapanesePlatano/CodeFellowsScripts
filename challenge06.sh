#!/bin/bash
set -x

# Script Name:                  Ops Challenge - conditionals
# Author:                       Gilbert Collado
# Date of latest revision:      02/24/2024
# Purpose:                      To run a conditional
# Source:                       https://chat.openai.com/share/7ac3ae91-7371-456a-81a6-802b4670aa6d

# Array to store dish names
dishes=("Mangu" "Sancocho" "Moro")

# Loop through the array
for dish in "${dishes[@]}"; do
    # Check if the dish file or directory exists
    if [ -e "$dish" ]; then
        echo "$dish exists."
    else
        # Create the dish file or directory if it does not exist
        if [ -f "$dish" ]; then
            touch "$dish"
            echo "File $dish created."
        elif [ -d "$dish" ]; then
            mkdir "$dish"
            echo "Directory $dish created."
        fi
    fi
done