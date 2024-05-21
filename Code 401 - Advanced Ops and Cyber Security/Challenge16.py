# Script Name:                  Automated Brute Force Wordlist Attack Tool Part 1 of 3
# Author:                       Gilbert Collado
# Date of latest revision:      05/20/2024
# Purpose:                      This script iterates through a word list with a delay or checks if a specific word exists in the list, offering two modes: Offensive (Dictionary Iterator) and Defensive (Password Recognized).
# Source1:                      https://www.geeksforgeeks.org/iterate-over-a-set-in-python/
# Source2:                      https://github.com/codefellows/seattle-cybersecurity-401d12/blob/main/class-16/challenges/DEMO.md

#!/usr/bin/env python3

import time
import nltk
from nltk.tokenize import word_tokenize

# Ensure necessary NLTK data files are downloaded
nltk.download('punkt')

# Function for Offensive Mode
def offensive_mode():
    # Prompt user for the path to the word list file
    word_list_path = input("Enter the path to the word list file: ")
    # Prompt user for the delay between words
    delay = float(input("Enter the delay between words (in seconds): "))
    
    try:
        # Open the word list file for reading
        with open(word_list_path, 'r') as file:
            # Iterate through each line in the file
            for line in file:
                # Tokenize the line into words
                words = word_tokenize(line)
                # Print each word to the screen with delay
                for word in words:
                    print(word)
                    # Pause for the specified delay
                    time.sleep(delay)
    except FileNotFoundError:
        # Print an error message if the file is not found
        print("File not found. Please check the path and try again.")

# Function for Defensive Mode
def defensive_mode():
    # Prompt user for the string to search for
    search_string = input("Enter the string to search for: ")
    
    # Prompt user for the path to the word list file
    word_list_path = input("Enter the path to the word list file: ")
    
    # Initialize a flag to indicate whether the string is found
    found = False
    
    try:
        # Open the word list file for reading
        with open(word_list_path, 'r') as file:
            # Iterate through each line in the file
            for line in file:
                # Tokenize the line into words
                word_tokens = set(word_tokenize(line.strip()))
                # Check if the search string is in the tokenized words
                if search_string in word_tokens:
                    # Set the flag to True if a match is found
                    found = True
                    # Exit the loop early since the string is found
                    break
    except FileNotFoundError:
        # Print an error message if the file is not found
        print("File not found. Please check the path and try again.")
        # Return early since the file was not found
        return

    # Print whether the string was found or not
    if found:
        print(f"The string '{search_string}' was found in the word list.")
    else:
        print(f"The string '{search_string}' was not found in the word list.")

# Main function to select and run the appropriate mode
def main():
    # Print options for the user to select a mode
    print("Select a mode:")
    print("1: Offensive; Dictionary Iterator")
    print("2: Defensive; Password Recognized")
    
    # Prompt user to enter the mode number
    mode = input("Enter the mode number (1 or 2): ")
    
    # Check the user input and call the corresponding function
    if mode == '1':
        offensive_mode()
    elif mode == '2':
        defensive_mode()
    else:
        # Print an error message if the user input is invalid
        print("Invalid mode selected. Please enter 1 or 2.")

# Check if the script is being run directly
if __name__ == "__main__":
    # Call the main function to start the script
    main()
