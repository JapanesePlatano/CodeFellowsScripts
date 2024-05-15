# Script Name:                  Network Security Tool with Scapy Part 3 of 3
# Author:                       Gilbert Collado
# Date of latest revision:      05/15/2024
# Purpose:                      TCP Port Range Scanner that tests whether a TCP port is open or closed. ICMP ping sweep mode.
# Source1:                      https://dev.to/zeyu2001/network-scanning-with-scapy-in-python-3off
# Source2:                      https://github.com/codefellows/seattle-cybersecurity-401d12/blob/main/class-13/challenges/DEMO.md
import logging
import ipaddress

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def scan_port(host, port):
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
    for port in port_range:
        scan_port(host, port)

def icmp_ping(host):
    ping_packet = IP(dst=str(host)) / ICMP()
    response = sr1(ping_packet, timeout=2, verbose=0)

    if response is None:
        print(f"Host {host} is down or unresponsive.")
        return False
    elif response.haslayer(ICMP):
        icmp_type = response[ICMP].type
        icmp_code = response[ICMP].code

        if icmp_type == 3 and icmp_code in [1, 2, 3, 9, 10, 13]:
            print(f"Host {host} is actively blocking ICMP traffic.")
            return False
        else:
            print(f"Host {host} is responding.")
            return True
    else:
        print(f"Host {host} is down or unresponsive.")
        return False

def main():
    while True:
        target_host = input("Enter the target host IP (or 'exit' to quit): ")
        
        if target_host.lower() == 'exit':
            print("Exiting.")
            break
        
        try:
            ipaddress.ip_address(target_host)  # Validate IP address
            
            if icmp_ping(target_host):
                start_port = int(input("Enter the start port: "))
                end_port = int(input("Enter the end port: "))
                if not (0 <= start_port <= 65535 and 0 <= end_port <= 65535):
                    raise ValueError
                ports_to_scan = range(start_port, end_port + 1)
                scan_ports(target_host, ports_to_scan)
            else:
                print(f"Host {host} is not responsive. Skipping port scan.")
        
        except ValueError:
            print("Invalid IP address or port range. Please try again.")

if __name__ == "__main__":
    main()
