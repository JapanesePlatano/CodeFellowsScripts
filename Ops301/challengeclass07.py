# Script Name:                  Ops Challenge - Directory Creation
# Author:                       Gilbert Collado
# Date of latest revision:      04/02/2024
# Purpose:                      Create a python script that makes directories
# Source1:                      https://g.co/gemini/share/94d8344c6e37
# Source2:                      https://github.com/codefellows/seattle-ops-301d12/tree/main/class-07/challenges
# Source3:                     

#!/usr/bin/env python3

# Import libraries
import os

# Declaration of functions
def generate_directory_structure(directory_path):
    """
    Generates all directories, sub-directories, and files for a given directory path.

    Args:
    directory_path (str): The path of the directory to generate the structure for.
    """
    for (root, dirs, files) in os.walk(directory_path):
        # Print root directory
        print("==root==")
        print(root)
        # Print sub-directories
        print("==dirs==")
        print(dirs)
        # Print files
        print("==files==")
        print(files)

# Main
if __name__ == "__main__":
    # Read user input for directory path
    user_directory_path = input("Enter the directory path: ")

    # Call the function to generate directory structure
    generate_directory_structure(user_directory_path)

