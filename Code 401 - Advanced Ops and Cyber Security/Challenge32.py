# Script Name:                  Signature-based Malware Detection Part 2 of 3
# Author:                       Gilbert Collado
# Date of latest revision:      06/11/2024
# Purpose:                      This Python searches for a specified file name within a given directory and its subdirectories on either Ubuntu Linux or Windows 10 systems. It recursively scans each file and folder in the user-input directory path, printing details for each file found. 
# Source1:                      https://docs.python.org/3/library/hashlib.html
# Source2:                      https://www.programiz.com/python-programming/examples/hash-file
# Source3:                      https://github.com/codefellows/seattle-cybersecurity-401d12/blob/main/class-32/challenges/DEMO.md

#!/usr/bin/env python3

import os
import hashlib
import platform
import datetime

def generate_md5(file_path):
    """Generate MD5 hash for the given file."""
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except IOError:
        return None

def search_files(search_directory):
    """Recursively scan each file and folder in the directory."""
    file_count = 0
    for root, dirs, files in os.walk(search_directory):
        for file in files:
            file_count += 1
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            md5_hash = generate_md5(file_path)
            print(f"Timestamp: {timestamp}")
            print(f"File: {file}")
            print(f"Size: {file_size} bytes")
            print(f"Path: {file_path}")
            print(f"MD5: {md5_hash}")
            print("-" * 60)

    print(f"Total files scanned: {file_count}")

def main():
    search_directory = input("Enter the directory to search in: ")
    
    if not os.path.isdir(search_directory):
        print("The provided directory does not exist.")
        return

    search_files(search_directory)

if __name__ == "__main__":
    main()
