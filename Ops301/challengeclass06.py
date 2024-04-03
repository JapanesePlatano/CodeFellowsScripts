# Script Name:                  Ops Challenge - bash in pythin
# Author:                       Gilbert Collado
# Date of latest revision:      04/01/2024
# Purpose:                      Create a bash script using python
# Source1:                      https://g.co/gemini/share/62e82d5a81a0
# Source2:                      https://github.com/codefellows/seattle-ops-301d12/blob/main/class-06/challenges/DEMO.md
# Source3:                      https://docs.python.org/3/library/os.html

import os

# Declare and initialize variables
command1 = 'whoami'
command2 = 'ip a'
command3 = 'lshw -short'

# Print informative messages
print("Executing bash commands using Python script...")

# Execute bash commands using os.system()
os.system(command1)
os.system(command2)
os.system(command3)

# Print completion message
print("Bash commands executed successfully.")
