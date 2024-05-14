# Script Name:                  Network Security Tool with Scapy Part 2 of 3
# Author:                       Gilbert Collado
# Date of latest revision:      05/14/2024
# Purpose:                      TCP Port Range Scanner that tests whether a TCP port is open or closed
# Source1:                      https://dev.to/zeyu2001/network-scanning-with-scapy-in-python-3off
# Source2:                      https://github.com/codefellows/seattle-cybersecurity-401d12/blob/94b03a684510d5e7a1df119d65c1139751492c26/class-12/challenges/DEMO.md

from scapy.all import *
import logging
import ipaddress
# Import the ipaddress module, which provides the capabilities to create, manipulate, and operate on IPv4 and IPv6 addresses and networks.
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
# Disable Scapy's verbose logging output to avoid cluttering the console with unnecessary information.

def scan_port(host, port):
    """
    Scans a single port on the specified host.

    :param host: The IP address of the target host.
    :param port: The TCP port to scan.
    """
    syn_packet = IP(dst=host) / TCP(dport=port, flags='S')
    # Create a SYN packet with the target host IP address and the specified port. The TCP flag 'S' (SYN) is set to initiate the connection.
    
    response = sr1(syn_packet, timeout=2, verbose=0)
    # Send the SYN packet and wait for a response, with a timeout of 2 seconds. sr1 sends a packet and returns the first response. The verbose level is set to 0 to suppress output.
    
    if response is None:
        # Check if no response is received.
        print(f"Port {port} is filtered and silently dropped.")
        # Print that the port is filtered and silently dropped.
        return
        # Return from the function.

    if response.haslayer(TCP):
        # Check if the response contains a TCP layer.
        if response[TCP].flags == 0x12:
            # Check if the TCP flags are 0x12 (SYN-ACK), indicating the port is open.
            rst_packet = IP(dst=host) / TCP(dport=port, flags='R')
            # Create a RST packet to gracefully close the connection.
            send(rst_packet, verbose=0)
            # Send the RST packet with verbose level set to 0 to suppress output.
            print(f"Port {port} is open.")
            # Print that the port is open.
        elif response[TCP].flags == 0x14:
            # Check if the TCP flags are 0x14 (RST-ACK), indicating the port is closed.
            print(f"Port {port} is closed.")
            # Print that the port is closed.
        else:
            # If any other TCP flags are received.
            print(f"Port {port} is filtered.")
            # Print that the port is filtered.
    else:
        # If no TCP layer is present in the response.
        print(f"Port {port} is filtered.")
        # Print that the port is filtered.

def scan_ports(host, port_range):
    """
    Scans a range of ports on the specified host.

    :param host: The IP address of the target host.
    :param port_range: A range of ports to scan.
    """
    for port in port_range:
        # Iterate over the given range of ports.
        scan_port(host, port)
        # Call scan_port for each port.

def icmp_ping_sweep(network):
    """
    Performs an ICMP ping sweep on the given network.

    :param network: The network address including CIDR block.
    """
    network = ipaddress.ip_network(network, strict=False)
    # Convert the network address including CIDR block into an ipaddress object.
    
    live_hosts = 0
    # Initialize a counter to keep track of the number of live hosts.
    
    for host in network.hosts():
        # Iterate over all possible host addresses in the network.
        ping_packet = IP(dst=str(host)) / ICMP()
        # Create an ICMP echo request (ping) packet for each host.
        response = sr1(ping_packet, timeout=2, verbose=0)
        # Send the packet and wait for a response with a timeout of 2 seconds.

        if response is None:
            # Check if no response is received.
            print(f"Host {host} is down or unresponsive.")
            # Print that the host is down or unresponsive.
        elif response.haslayer(ICMP):
            # Check if the response contains an ICMP layer.
            icmp_type = response[ICMP].type
            # Extract the ICMP type from the response.
            icmp_code = response[ICMP].code
            # Extract the ICMP code from the response.

            if icmp_type == 3 and icmp_code in [1, 2, 3, 9, 10, 13]:
                # Check if the ICMP type is 3 (Destination Unreachable) and the code is one of [1, 2, 3, 9, 10, 13].
                print(f"Host {host} is actively blocking ICMP traffic.")
                # Print that the host is actively blocking ICMP traffic.
            else:
                # If the host responds and is not blocking ICMP traffic.
                print(f"Host {host} is responding.")
                # Print that the host is responding.
                live_hosts += 1
                # Increment the live host counter.
    
    print(f"Total live hosts: {live_hosts}")
    # Print the total number of live hosts found during the ICMP ping sweep.

def main():
    print("Select mode:")
    # Print a message to prompt the user to select a mode.
    print("1. TCP Port Range Scanner")
    # Print the option for TCP Port Range Scanner.
    print("2. ICMP Ping Sweep")
    # Print the option for ICMP Ping Sweep.
    choice = input("Enter choice (1 or 2): ")
    # Prompt the user to enter their choice and store it in the variable 'choice'.

    if choice == '1':
        # Check if the user selected TCP Port Range Scanner.
        target_host = input("Enter the target host IP: ")
        # Prompt the user for the target host IP and store it in the variable 'target_host'.
        start_port = int(input("Enter the start port: "))
        # Prompt the user for the start port and store it as an integer in the variable 'start_port'.
        end_port = int(input("Enter the end port: "))
        # Prompt the user for the end port and store it as an integer in the variable 'end_port'.
        ports_to_scan = range(start_port, end_port + 1)
        # Create a range of ports to scan from start_port to end_port (inclusive).
        scan_ports(target_host, ports_to_scan)
        # Call scan_ports to scan the specified ports on the target host.

    elif choice == '2':
        # Check if the user selected ICMP Ping Sweep.
        network = input("Enter the network address (including CIDR block, e.g., 10.10.0.0/24): ")
        # Prompt the user for the network address including CIDR block and store it in the variable 'network'.
        icmp_ping_sweep(network)
        # Call icmp_ping_sweep to perform the ping sweep on the specified network.

    else:
        # If the user enters an invalid choice.
        print("Invalid choice. Exiting.")
        # Print an error message and exit the program.

if __name__ == "__main__":
    main()
    # If the script is executed directly (not imported as a module), call the main function to start the program.




