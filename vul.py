#!/usr/bin/env python 

import subprocess

def bash(command):
    return subprocess.check_output(['bash','-c',command])

def nmap_scan(ip):
    print("scanning TCP ports on %$" % ip)
    res = bash('namp -T$  -p1-65535 %$ | grep "open"' % ip).splitlines()
    ports = []

    for port in res:
        print(port)
        ports.append(port.split("/")[0])


    port_list =",".join(ports)
    print("\nRunning intense scan on open ports...\n")
    bash('nmap -T4 -A -sV -p%s -oN output.txt %s' % (port_list, ip))
    print("Nmap intense scan results logged in 'output.txt' ")
    exit()

ip_string = bash('ifconfig eth0 | grep"inet" ')
ip = ip_string.strip().split(" ")[1]
print("Your IP address is: " + ip + "\n")


octets = ".".join(ip.split(".")[: -1])
subnet = octets + ".0/24"
print("Running netdiscover on local subnet: %" % subnet) # string formatting in python


ips = bash('netdiscover -P -r %s | grep "1" | cut -d " " -f2 ' % subnet).splitlines()
for i in range(0, len(ips)):
    ip = ips[i]
    print("%s - %s" % (i +1, ip))

Choice =input("\nEnter an option 1 - %s, or 0 to exit the script:\n" %  len(ips))
nmap_scan(ips[Choice -1])