# Script Name:                  Ops Challenge - Python File Handling
# Author:                       Gilbert Collado
# Date of latest revision:      04/05/2024
# Purpose:                      Create a script that uses file handling in python
# Source1:                      https://github.com/codefellows/seattle-ops-301d12/tree/main/class-10/challenges

# Create a new .txt file
file_name = 'example.txt'
with open(file_name, 'w') as file:
    file.write("First line\n")
    file.write("Second line\n")
    file.write("Third line\n")

# Read and print the first line
with open(file_name, 'r') as file:
    first_line = file.readline()
    print("First line from the file:", first_line)

# Delete the .txt file
import os
os.remove(file_name)
print("File", file_name, "deleted successfully.")
