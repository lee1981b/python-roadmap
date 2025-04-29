#!/usr/bin/python3

# This Script Will Defang IP addresses.

def ip_address(address):
    new_address = ""
    split_address = address.split(".")
    seperator = "[.]"
    new_address = seperator.join(split_address)
    return new_address
IPad=input("Enter your IP address : ")
ipaddress = ip_address(IPad)
print(ipaddress)
