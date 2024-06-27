# Script Name:                  Create a Port Scanner
# Author:                       Gilbert Collado
# Date of latest revision:      06/26/2024
# Purpose:                      This script checks whether a specified port on a given host IP address is open or closed.
# Source1:                      https://docs.python.org/3/library/socket.html
# Source2:                      https://github.com/codefellows/seattle-cybersecurity-401d12/blob/94b03a684510d5e7a1df119d65c1139751492c26/class-44/challenges/DEMO.md                   

#!/usr/bin/python3

import socket

# Set a timeout value here
timeout = 1.0
sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockmod.settimeout(timeout)

# Collect a host IP from the user
hostip = input("Enter the host IP: ")

# Collect a port number from the user, then convert it to an integer data type
portno = int(input("Enter the port number: "))

def portScanner(portno):
    try:
        # Attempt to connect to the host IP and port number
        result = sockmod.connect_ex((hostip, portno))
        if result == 0:
            print(f"Port {portno} is open")
        else:
            print(f"Port {portno} is closed")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        sockmod.close()

portScanner(portno)
