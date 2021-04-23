#!/usr/bin/python3

import nmap
import socket
import threading
from queue import Queue
import time
from colorama import *
import pyfiglet
import subprocess


#banner 
banner = pyfiglet.figlet_format("OPTIMUS-SHELL")
print(Fore.MAGENTA + banner)

#image for script look

print(Fore.RED +'''
                ..:::::::::..
           ..:::aad8888888baa:::..
        .::::d:?88888888888?::8b::::.
      .:::d8888:?88888888??a888888b:::.
    .:::d8888888a8888888aa8888888888b:::.
   ::::dP::::::::88888888888::::::::Yb::::
  ::::dP:::::::::Y888888888P:::::::::Yb::::
 ::::d8:::::::::::Y8888888P:::::::::::8b::::
.::::88::::::::::::Y88888P::::::::::::88::::.
:::::Y8baaaaaaaaaa88P:T:Y88aaaaaaaaaad8P:::::
:::::::Y88888888888P::|::Y88888888888P:::::::
::::::::::::::::888:::|:::888::::::::::::::::
`:::::::::::::::8888888888888b::::::::::::::'
 :::::::::::::::88888888888888::::::::::::::
  :::::::::::::d88888888888888:::::::::::::
   ::::::::::::88::88::88:::88::::::::::::
    `::::::::::88::88::88:::88::::::::::'
      `::::::::88::88::P::::88::::::::'
        `::::::88::88:::::::88::::::'         created by subhash maurya
           ``:::::::::::::::::::''             ##@@** --only use  to scan local area network-- 000**@@##
                ``:::::::::''
''')

print(Fore.YELLOW +'''
----------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------
''')

#showing localhost ip

hostname = socket.gethostname() 
IPAddr = socket.gethostbyname(hostname) 
print(Fore.CYAN + "Your Computer Name is:" +Fore.RED +  hostname)    
print(Fore.CYAN + "Your Computer IP Address is:" +Fore.YELLOW +  IPAddr)    

'''*************************************************************************************************************
def bash(command):
        return subprocess.check_output(['bash', '-c', command])

ip1 = bash('ifconfig eth0 | grep "inet "')
ip = ip1.strip().split(" ")[1]
print("your IP Address is : " + ip)
'''


print(Fore.BLUE + '''
*********************************************************************************************************
*********************************************************************************************************
''')
# for aggresive and fast scan  of open ports of the system
print(Fore.CYAN + "#########for aggresive and  only limited open ports  scanner and local host scanner +++ 1 module")

socket.setdefaulttimeout(0.25)
print_lock = threading.Lock()

target = input('Enter the host to be scanned: ')
t_IP = socket.gethostbyname(target)
print ('Starting scan on host: ', t_IP)

def portscan(port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      con = s.connect((t_IP, port))
      with print_lock:
         print(port, 'is open')
      con.close()
   except:
      pass

def threader():
   while True:
      worker = q.get()
      portscan(worker)
      q.task_done()
      
q = Queue()
startTime = time.time()
   
for x in range(100):
   t = threading.Thread(target = threader)
   t.daemon = True
   t.start()
   
for worker in range(1, 500):
   q.put(worker)
   
q.join()
print('Time taken:', time.time() - startTime)

#using nmap to scan  open ports

scanner = nmap.PortScanner()
print("--------------------Welcome, this is a simple nmap automation tool-----------------------------------")
print("<---------------------------------------------------------------------------------------------------->")

ip_addr = input("Please enter the IP address you want to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

resp = input("""\nPlease enter the type of scan you want to run
                1)SYN ACK Scan
                2)UDP Scan
                3)Comprehensive Scan \n""")
print("You have selected option: ", resp)

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-65000', '-v -sS')
    print(scanner.scaninfo())
    print	("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-6000', '-v -sU')
    print(scanner.scaninfo())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif resp == '3':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-65000', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp >= '4':
    print("Please enter a valid option")








