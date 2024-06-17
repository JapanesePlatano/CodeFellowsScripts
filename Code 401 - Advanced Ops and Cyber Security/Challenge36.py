# Script Name:                  Web Application Fingerprinting
# Author:                       Gilbert Collado
# Date of latest revision:      06/17/2024
# Purpose:                      This Python script performs banner grabbing on a specified URL or IP address and port using netcat, telnet, and Nmap to identify the services running on the target system.
# Source1:                      https://www.hackingarticles.in/multiple-ways-to-banner-grabbing/
# Source2:                      https://github.com/codefellows/seattle-cybersecurity-401d12/blob/main/class-36/challenges/DEMO.md

#!/usr/bin/env python3

import subprocess

def banner_grab_netcat(address, port):
    print("\n[+] Banner Grabbing using netcat")
    try:
        result = subprocess.run(['nc', '-v', address, str(port)], capture_output=True, text=True, timeout=5)
        print(result.stdout)
    except subprocess.TimeoutExpired:
        print(f"[!] Timeout expired for netcat on {address}:{port}")

def banner_grab_telnet(address, port):
    print("\n[+] Banner Grabbing using telnet")
    try:
        result = subprocess.run(['telnet', address, str(port)], capture_output=True, text=True, timeout=5)
        print(result.stdout)
    except subprocess.TimeoutExpired:
        print(f"[!] Timeout expired for telnet on {address}:{port}")

def banner_grab_nmap(address):
    print("\n[+] Banner Grabbing using Nmap")
    try:
        result = subprocess.run(['nmap', '-sV', address], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"[!] Nmap scan failed: {e}")

def main():
    address = input("Enter the URL or IP address: ")
    port = input("Enter the port number: ")
    
    banner_grab_netcat(address, port)
    banner_grab_telnet(address, port)
    banner_grab_nmap(address)

if __name__ == "__main__":
    main()
