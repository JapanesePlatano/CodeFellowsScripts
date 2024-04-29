# Script Name:                  Ops Challenge - Clearing Logs
# Author:                       Gilbert Collado
# Date of latest revision:      03/29/2024
# Purpose:                      Create a bash script that clears logs
# Source1:                      https://g.co/gemini/share/3239efd8fb6d
# Source2:                      https://github.com/codefellows/seattle-ops-301d12/blob/main/class-05/challenges/DEMO.md
# Source3:                      https://www.youtube.com/watch?v=TgquV_OA-lU&ab_channel=HackerSploit

#!/bin/bash

# Define backup directory
backup_dir="/home/gilbertcollado/Desktop/CodeFellowsScripts/Ops301/backup_directory"

# Function to print file size
print_file_size() {
    file=$1
    size=$(du -h "$file" | cut -f1)
    echo "File size of $file: $size"
}

# Print original file sizes
echo "Original File Sizes:"
print_file_size "/var/log/syslog"
print_file_size "/var/log/wtmp"

# Compress and backup log files
timestamp=$(date +"%Y%m%d%H%M%S")
compressed_syslog="$backup_dir/syslog-$timestamp.gz"
compressed_wtmp="$backup_dir/wtmp-$timestamp.gz"

gzip -c /var/log/syslog > "$compressed_syslog"
gzip -c /var/log/wtmp > "$compressed_wtmp"

# Clear log files
echo "Clearing log files..."
sudo truncate -s 0 /var/log/syslog
sudo truncate -s 0 /var/log/wtmp

# Print compressed file sizes
echo "Compressed File Sizes:"
print_file_size "$compressed_syslog"
print_file_size "$compressed_wtmp"

# Compare file sizes
echo "Comparison:"
echo "Original syslog size: $(du -h /var/log/syslog | cut -f1)"
echo "Compressed syslog size: $(du -h "$compressed_syslog" | cut -f1)"
echo "Original wtmp size: $(du -h /var/log/wtmp | cut -f1)"
echo "Compressed wtmp size: $(du -h "$compressed_wtmp" | cut -f1)"

