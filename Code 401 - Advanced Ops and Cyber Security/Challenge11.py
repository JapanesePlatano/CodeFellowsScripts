# Script Name:                  Network Security Tool with Scapy Part 1 of 3
# Author:                       Gilbert Collado
# Date of latest revision:      05/13/2024
# Purpose:                      TCP Port Range Scanner that tests whether a TCP port is open or closed
# Source1:                      https://dev.to/zeyu2001/network-scanning-with-scapy-in-python-3off
# Source2:                      https://github.com/codefellows/seattle-cybersecurity-401d12/blob/94b03a684510d5e7a1df119d65c1139751492c26/class-11/challenges/DEMO.md

from scapy.all import *
import logging  

# Disable Scapy's verbose logging output
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def scan_port(host, port):
    """
    Scans a single port on the specified host.

    :param host: The IP address of the target host.
    :param port: The TCP port to scan.
    """
    # Create a SYN packet with the target host and port
    syn_packet = IP(dst=host) / TCP(dport=port, flags='S')
    # Send the SYN packet and wait for a response (timeout set to 2 seconds)
    response = sr1(syn_packet, timeout=2, verbose=0)
    
    if response is None:
        # No response received, port is considered filtered and silently dropped
        print(f"Port {port} is filtered and silently dropped.")
        return
    
    # Check if the response contains a TCP layer
    if response.haslayer(TCP):
        # Check the TCP flags in the response
        if response[TCP].flags == 0x12:  # SYN-ACK response indicates the port is open
            # Create and send a RST packet to gracefully close the connection
            rst_packet = IP(dst=host) / TCP(dport=port, flags='R')
            send(rst_packet, verbose=0)
            print(f"Port {port} is open.")
        elif response[TCP].flags == 0x14:  # RST-ACK response indicates the port is closed
            print(f"Port {port} is closed.")
        else:
            # Any other response is considered as the port being filtered
            print(f"Port {port} is filtered.")
    else:
        # No TCP layer in the response, port is considered filtered
        print(f"Port {port} is filtered.")

def scan_ports(host, port_range):
    """
    Scans a range of ports on the specified host.

    :param host: The IP address of the target host.
    :param port_range: A range of ports to scan.
    """
    for port in port_range:
        scan_port(host, port)

if __name__ == "__main__":
    target_host = "192.168.4.62"  # Define the host IP to scan
    ports_to_scan = range(20, 1025)  # Define the range of ports to scan (from port 20 to 1024)

    scan_ports(target_host, ports_to_scan)  # Call the function to scan the specified ports on the target host




