#David Bombal created a video regarding this script.
#https://github.com/davidbombal/red-python-scripts/blob/main/port_scanner_regex.py
#I added a secondary message to the socket script.
#I also added the socket and nmap scan options together with a question on which one you want to use.

import socket
import nmap
import re

ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")

port_range_pattern = re.compile("([0-9]+)-([0-9]+)")

port_min = 0
port_max = 65535

choice = input("Would you like to use Socket or Nmap to perform your scan? (enter s or n): ")


def socket_scan():
    print("Port Scanning Script using python socket")
    print("\n")

    open_ports = []

    while True:
        ip_add_entered = input("\nPlease enter the ip address that you want to scan: ")
        if ip_add_pattern.search(ip_add_entered):
            print(f"{ip_add_entered} is a valid ip address")
            break
    while True:
        print("Please enter the range of ports you want to scan in format: <int>-<int> (ex: 20-40)")
        port_range = input("Enter port range: ")
        port_range_valid = port_range_pattern.search(port_range.replace(" ", ""))
        if port_range_valid:
            port_min = int(port_range_valid.group(1))
            port_max = int(port_range_valid.group(2))
            break


    for port in range(port_min, port_max + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                s.connect((ip_add_entered, port))
                open_ports.append(port)
        except:
            pass

    for port in open_ports:
        print(f"Port {port} is open on {ip_add_entered}.")

    if open_ports == []:
        print("\nNone of the port numbers provided are open.")
#Need to have python-nmap installed (pip install python-nmap)        
def nmap_scan():
    print("\nPort Scanning Script using python nmap")
    print("\n")

    open_ports = []
    while True:
        ip_add_entered = input("\nPlease enter the ip address that you want to scan: ")
        if ip_add_pattern.search(ip_add_entered):
            print(f"{ip_add_entered} is a valid ip address")
            break
    while True:
        print("Please enter the range of ports you want to scan in format: <int>-<int> (ex: 20-40)")
        port_range = input("Enter port range: ")
        port_range_valid = port_range_pattern.search(port_range.replace(" ", ""))
        if port_range_valid:
            port_min = int(port_range_valid.group(1))
            port_max = int(port_range_valid.group(2))
            break
    nm = nmap.PortScanner()
    for port in range(port_min, port_max + 1):
        try:
            result = nm.scan(ip_add_entered, str(port))
            port_status = (result['scan'][ip_add_entered]['tcp'][port]['state'])
            print(f"Port {port} is {port_status}")
        except:
            print(f"Cannot scan port {port}.")

if choice == "s":
    socket_scan()
elif choice == "n":
    nmap_scan()