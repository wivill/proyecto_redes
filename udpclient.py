#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import socket
import sys

arglen = len(sys.argv)
if arglen < 3:
    print('please run as python UDPclient.py <ip_address> <numbers>')
    exit()


data = str()
data = data + sys.argv[2]

for i in range(3, len(sys.argv)):
    data = data + ' ' + sys.argv[i]


bandera = 0   
while bandera == 0:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	port = 22222
	addr = sys.argv[1]
	s.sendto(data, (addr, port))
	print("\n Datos enviados")
	print(data)
	datos_recibidos = str()
	datos_recibidos, addr = s.recvfrom(1024)
	
	print("\nDatos recibidos")
	print(datos_recibidos)
	
	if datos_recibidos == "-*/D":
		#print("if")
		bandera = 1
	else:
		data = str(raw_input('\nIntroduzca el dato nuevamente. Para finalizar introduzca "-*/d" '))
	
s.close
	
