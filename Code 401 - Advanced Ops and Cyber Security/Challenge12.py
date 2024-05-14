# Script Name:                  Network Security Tool with Scapy Part 2 of 3
# Author:                       Gilbert Collado
# Date of latest revision:      05/14/2024
# Purpose:                      TCP Port Range Scanner that tests whether a TCP port is open or closed
# Source1:                      https://dev.to/zeyu2001/network-scanning-with-scapy-in-python-3off
# Source2:                      https://github.com/codefellows/seattle-cybersecurity-401d12/blob/94b03a684510d5e7a1df119d65c1139751492c26/class-12/challenges/DEMO.md

from scapy.all import *
import logging
import ipaddress

# Disable Scapy's verbose logging output
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def scan_port(host, port):
    """
    Scans a single port on the specified host.

    :param host: The IP address of the target host.
    :param port: The TCP port to scan.
    """
    syn_packet = IP(dst=host) / TCP(dport=port, flags='S')
    response = sr1(syn_packet, timeout=2, verbose=0)
    
    if response is None:
        print(f"Port {port} is filtered and silently dropped.")
        return
    
    if response.haslayer(TCP):
        if response[TCP].flags == 0x12:
            rst_packet = IP(dst=host) / TCP(dport=port, flags='R')
            send(rst_packet, verbose=0)
            print(f"Port {port} is open.")
        elif response[TCP].flags == 0x14:
            print(f"Port {port} is closed.")
        else:
            print(f"Port {port} is filtered.")
    else:
        print(f"Port {port} is filtered.")

def scan_ports(host, port_range):
    """
    Scans a range of ports on the specified host.

    :param host: The IP address of the target host.
    :param port_range: A range of ports to scan.
    """
    for port in port_range:
        scan_port(host, port)

def icmp_ping_sweep(network):
    """
    Performs an ICMP ping sweep on the given network.

    :param network: The network address including CIDR block.
    """
    network = ipaddress.ip_network(network, strict=False)
    live_hosts = 0
    
    for host in network.hosts():
        ping_packet = IP(dst=str(host)) / ICMP()
        response = sr1(ping_packet, timeout=2, verbose=0)
        
        if response is None:
            print(f"Host {host} is down or unresponsive.")
        elif response.haslayer(ICMP):
            icmp_type = response[ICMP].type
            icmp_code = response[ICMP].code
            
            if icmp_type == 3 and icmp_code in [1, 2, 3, 9, 10, 13]:
                print(f"Host {host} is actively blocking ICMP traffic.")
            else:
                print(f"Host {host} is responding.")
                live_hosts += 1
    
    print(f"Total live hosts: {live_hosts}")

def main():
    print("Select mode:")
    print("1. TCP Port Range Scanner")
    print("2. ICMP Ping Sweep")
    choice = input("Enter choice (1 or 2): ")
    
    if choice == '1':
        target_host = input("Enter the target host IP: ")
        start_port = int(input("Enter the start port: "))
        end_port = int(input("Enter the end port: "))
        ports_to_scan = range(start_port, end_port + 1)
        scan_ports(target_host, ports_to_scan)
    elif choice == '2':
        network = input("Enter the network address (including CIDR block, e.g., 10.10.0.0/24): ")
        icmp_ping_sweep(network)
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()




