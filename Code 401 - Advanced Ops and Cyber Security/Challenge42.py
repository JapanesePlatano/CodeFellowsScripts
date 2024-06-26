# Script Name:                  Attack Tools Part 2 of 3
# Author:                       Gilbert Collado
# Date of latest revision:      06/25/2024
# Purpose:                      The script automates network scanning tasks using Nmap through a Python interface, allowing users to perform different types of scans on specified IP addresses and port ranges.
# Source1:                      https://pypi.org/project/python-nmap/
# Source2:                      https://www.youtube.com/watch?v=t3fuSapseS4
# Source3:                      https://github.com/codefellows/seattle-cybersecurity-401d12/blob/main/class-42/challenges/DEMO.md

#!/usr/bin/python3

import nmap


scanner = nmap.PortScanner()

print("Nmap Automation Tool")
print("--------------------")

ip_addr = input("IP address to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

resp = input("""\nSelect scan to execute:
                1) SYN ACK Scan
                2) UDP Scan
                3) Comprehensive Scan\n""")  # Added the third scan type: Comprehensive Scan
print("You have selected option: ", resp)

# Prompt the user to type in a port range for this tool to scan
range = input("Please enter the port range to scan (e.g., '1-1024'): ")
print("Scanning the following range of ports: ", range)

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    # Completing the UDP scan code block
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sU')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif resp == '3':
    # Adding code block for Comprehensive Scan
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sC -sV -O -A -T4')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr].keys())
elif resp >= '4':
    print("Please enter a valid option")
