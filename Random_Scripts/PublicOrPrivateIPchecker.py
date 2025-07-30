#!/usr/bin/env python3
"""
This Script defines if an IP is private or public.
Install dependency's:
pip install ipaddress
"""
import ipaddress

def check_private_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        return ip_obj.is_private
    except ValueError:
        return False

ip = input("Enter IP Address: ")
print(f"Is {ip} private? {check_private_ip(ip)}")