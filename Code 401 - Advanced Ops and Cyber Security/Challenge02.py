# Script Name:                  Uptime Sensor Tool Part 1 of 2
# Author:                       Gilbert Collado
# Date of latest revision:      04/30/2024
# Purpose:                      create an uptime sensor tool that uses ICMP packets to evaluate if hosts on the LAN are up or down.
# Source1:                      https://github.com/codefellows/seattle-cybersecurity-401d12/blob/main/class-02/challenges/DEMO.md
# Source2:                      https://g.co/gemini/share/39b5982e298f

#!/usr/bin/env python3

import os
import time

def ping_host(ip_address):
    response = os.system("ping -c 1 -W 2 " + ip_address + " > /dev/null 2>&1")
    return response == 0

def main():
    destination_ip = "8.8.8.8"  # Change this to your desired destination IP
    while True:
        status = "Active" if ping_host(destination_ip) else "Inactive"
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S.%f")
        print(f"{timestamp} Network {status} to {destination_ip}")

        time.sleep(2)  # Wait for 2 seconds before next ping

if __name__ == "__main__":
    main()
