# Script Name:                  Signature-based Malware Detection Part 1 of 3
# Author:                       Gilbert Collado
# Date of latest revision:      06/10/2024
# Purpose:                      This Python script searches for a specified file name within a given directory and its subdirectories on either Ubuntu Linux or Windows 10 systems. 
# Source1:                      https://www.howtogeek.com/112674/how-to-find-files-and-folders-in-linux-using-the-command-line/
# Source2:                      https://www.howtogeek.com/206097/how-to-use-find-from-the-windows-command-prompt/
# Source3:                      https://github.com/codefellows/seattle-cybersecurity-401d12/blob/main/class-31/challenges/DEMO.md

#!/usr/bin/env python3

import os
import platform

def search_files(filename, search_directory):
    file_count = 0
    hit_count = 0
    
    for root, dirs, files in os.walk(search_directory):
        for file in files:
            file_count += 1
            if filename in file:
                hit_count += 1
                print(f"Found: {file} in {root}")
    
    print(f"Total files searched: {file_count}")
    print(f"Total hits found: {hit_count}")

def main():
    filename = input("Enter the file name to search for: ")
    search_directory = input("Enter the directory to search in: ")
    
    if not os.path.isdir(search_directory):
        print("The provided directory does not exist.")
        return

    search_files(filename, search_directory)

if __name__ == "__main__":
    main()

