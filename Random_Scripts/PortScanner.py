#!/usr/bin/python3
# Python Script to Scan a Host or Network for open ports TCP & UDP.
# Example Host Scan (TCP): python3 PortScanner.py 192.168.0.130 1 65535
# Example Network Scan (TCP): python3 PortScanner.py 192.168.0. 1 65535 -n
# Example Host Scan (UDP): python3 PortScanner.py 192.168.0.130 1 65535 -u

import socket
import sys


def scanHost(ip, startPort, endPort, protocol='TCP'):
    """ Starts a TCP or UDP scan on a given IP address """
    print(f'[*] Starting {protocol} port scan on host {ip}')
    if protocol.upper() == 'TCP':
        tcp_scan(ip, startPort, endPort)
    elif protocol.upper() == 'UDP':
        udp_scan(ip, startPort, endPort)
    print(f'[+] {protocol} scan on host {ip} complete')


def scanRange(network, startPort, endPort, protocol='TCP'):
    """ Starts a TCP or UDP scan on a given IP address range """
    print(f'[*] Starting {protocol} port scan on network {network}.0')
    for host in range(1, 255):
        ip = f"{network}.{host}"
        if protocol.upper() == 'TCP':
            tcp_scan(ip, startPort, endPort)
        elif protocol.upper() == 'UDP':
            udp_scan(ip, startPort, endPort)
    print(f'[+] {protocol} scan on network {network}.0 complete')


def tcp_scan(ip, startPort, endPort):
    """ Creates a TCP socket and attempts to connect via supplied ports """
    for port in range(startPort, endPort + 1):
        try:
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if not tcp.connect_ex((ip, port)):
                print(f'[+] {ip}:{port}/TCP Open')
            tcp.close()
        except Exception:
            pass


def udp_scan(ip, startPort, endPort):
    """ Creates a UDP socket and attempts to send packets to supplied ports """
    for port in range(startPort, endPort + 1):
        try:
            udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            udp.settimeout(0.1)
            udp.sendto(b'', (ip, port))  # Sending an empty datagram
            try:
                data, _ = udp.recvfrom(1024)  # Expecting no response from open ports
                print(f'[+] {ip}:{port}/UDP Open (Response received)')
            except Exception:
                pass
            finally:
                udp.close()
        except Exception:
            pass


if __name__ == '__main__':
    socket.setdefaulttimeout(0.01)

    if len(sys.argv) < 4:
        print('Usage: python3 PortScanner.py <IP address> <start port> <end port> [-u|-n]')
        print('Example (TCP Host): python3 PortScanner.py 192.168.1.10 1 65535')
        print('Example (TCP Network): python3 PortScanner.py 192.168.1 1 65535 -n')
        print('Example (UDP Host): python3 PortScanner.py 192.168.1.10 1 65535 -u')

    elif len(sys.argv) >= 4:
        network = sys.argv[1]
        startPort = int(sys.argv[2])
        endPort = int(sys.argv[3])
        protocol = 'TCP'  # Default protocol

        if len(sys.argv) == 5:
            if sys.argv[4] == '-n':
                scanRange(network, startPort, endPort, protocol='TCP')
            elif sys.argv[4] == '-u':
                protocol = 'UDP'
                scanHost(network, startPort, endPort, protocol=protocol)
            else:
                print(f"Unknown option: {sys.argv[4]}")
        else:
            scanHost(network, startPort, endPort, protocol=protocol)