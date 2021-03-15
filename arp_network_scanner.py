import scapy.all as scapy

import re

#This is a regex to recognize IPv4 addresses
ip_address_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

while True:
    ip_address_range_entered = input("\nPlease enter the IP address and range that you want scan: ")
    if ip_address_range_pattern.search(ip_address_range_entered):
        print(f"{ip_address_range_entered} is a valid IP address range.")
        break

arp_result = scapy.arping(ip_address_range_entered)