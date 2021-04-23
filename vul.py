#!/usr/bin/python3

import pyfiglet
from colorama import *
import socket
import re, uuid
import platform
import subprocess
import threading
from queue import Queue
import time



#banner images
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


print(Fore.YELLOW +'''
----------------------------------------------------------------------------------------------------------
''')
#finding mac address of the system
print(Fore.CYAN + "The MAC address of this computer is : ",end="") 
print (':'.join(re.findall('..', '%012x' % uuid.getnode())))

print(Fore.YELLOW +'''
----------------------------------------------------------------------------------------------------------
''')

#finding operating-system

plt = platform.system()

if plt == "Windows":
    print(Fore.GREEN + "Your operating system is= 'Windows' ")
    # do x y z
elif plt == "Linux":
    print("Your operating system is= 'Linux' ")
    # do x y z
elif plt == "Darwin":
    print("Your operating system is= 'MacOS' ")
    # do x y z
else:
    print("Unidentified system")

print(Fore.YELLOW +'''
----------------------------------------------------------------------------------------------------------
''')

# getting meta data of the wifi network 
meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']) 

# decoding meta data from byte to string 
data = meta_data.decode('utf-8', errors ="backslashreplace") 

# spliting data by line by line 
# string to list 
data = data.split('\n') 

# creating a list of wifi names 
names = [] 

# traverse the list 
for i in data: 
	
	# find "All User Profile" in each item 
	# as this item will have the wifi name 
	if "All User Profile" in i : 
		
		# if found split the item 
		# in order to get only the name 
		i = i.split(":") 
		
		# item at index 1 will be the wifi name 
		i = i[1] 
		
		# formatting the name 
		# first and last chracter is use less 
		i = i[1:-1] 
		
		# appending the wifi name in the list 
		names.append(i) 

# printing the wifi names 
print(Fore.BLUE + "All wifi that system has connected. ")



print(Fore.GREEN + "-----------------------------------------") 
for name in names: 
	print(name) 

print(Fore.CYAN + "*****************************************")




results = subprocess.check_output(["netsh", "wlan", "show", "network"])
results = results.decode("ascii")
results = results.replace("\r","")
ls = results.split("\n")
ls = ls[4:]
ssids = []
x = 0
while x < len(ls):
    if x % 5 == 0:
        ssids.append(ls[x])
    x += 1
print(ssids)

'''******************************************************************************'''
results = subprocess.check_output(["netsh", "wlan", "show", "network"])
results = results.decode("ascii")
results = results.replace("\r","")
ls = results.split("\n")
ls = ls[4:]
ssids = []
x = 0
while x < len(ls):
    if x % 5 == 0:
        ssids.append(ls[x])
    x += 1
print(ssids)

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
print (Fore.RED + 'Starting scan on host: ', t_IP)

def portscan(port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      con = s.connect((t_IP, port))
      with print_lock:
         print(port, 'is open and vulnerable')
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
   
for worker in range(1, 6000):
   q.put(worker)
   
q.join()
print(Fore.GREEN + 'Time taken:', time.time() - startTime)










