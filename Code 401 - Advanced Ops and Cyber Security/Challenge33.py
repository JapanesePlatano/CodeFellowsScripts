# Script Name:                  Signature-based Malware Detection Part 3 of 3
# Author:                       Gilbert Collado
# Date of latest revision:      06/12/2024
# Purpose:                      This Python searches for a specified file name within a given directory and its subdirectories on either Ubuntu Linux or Windows 10 systems. It recursively scans each file and folder in the user-input directory path, printing details for each file found. 
# Source1:                      https://www.tines.com/blog/virustotal-api-security-automation
# Source2:                      https://github.com/eduardxyz/virustotal-search/blob/master/virustotal-search.py
# Source3:                      https://github.com/codefellows/seattle-cybersecurity-401d12/blob/main/class-33/challenges/DEMO.md

#!/usr/bin/env python3

import os
import hashlib
import platform
import datetime
import virustotal_search  # Added import for virustotal_search
import json  # Added import for json

API_KEY = os.getenv('API_KEY_VIRUSTOTAL')  # Added API key environment variable

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
    positives_count = 0  # Added counter for positives

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
            
            if md5_hash:  # Added condition to check if MD5 hash is generated
                response = virustotal_search.search(API_KEY, md5_hash)  # Added VirusTotal API query
                if response:
                    response_data = json.loads(response)  # Added response parsing
                    positives = response_data.get('positives', 0)
                    total = response_data.get('total', 0)
                    positives_count += positives
                    print(f"Positives: {positives}/{total}")
                else:
                    print("Error querying VirusTotal API.")
            else:
                print("Could not generate MD5 hash for the file.")
            
            print("-" * 60)

    print(f"Total files scanned: {file_count}")
    print(f"Total positives detected: {positives_count}")  # Added output for positives count

def main():
    search_directory = input("Enter the directory to search in: ")
    
    if not os.path.isdir(search_directory):
        print("The provided directory does not exist.")
        return

    search_files(search_directory)

if __name__ == "__main__":
    main()

