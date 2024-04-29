# Script Name:                  Ops Challenge - Append; Date and Time
# Author:                       Gilbert Collado
# Date of latest revision:      03/26/2024
# Purpose:                      Create a bash script that copies /var/log/syslog to the current working directory and appends the current date and time to the filename
# Source1:                      https://g.co/gemini/share/f07c4fcd2c29 
# Source2:                      https://github.com/codefellows/seattle-ops-301d12/blob/main/class-02/challenges/DEMO.md

#!/bin/bash

# Define source file and destination directory
source_file="/var/log/syslog"
destination_dir="$(pwd)"

# Get current date and time
current_date=$(date +"%Y-%m-%d_%H-%M-%S")

# Construct new filename with date and time appended
new_filename="syslog_${current_date}"

# Copy syslog to destination directory with new filename
cp "$source_file" "$destination_dir/$new_filename"

echo "Copied $source_file to $destination_dir/$new_filename"

