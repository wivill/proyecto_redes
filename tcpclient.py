#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
import socket



arglen = len(sys.argv)
if arglen < 3:
    print('Ejecute como python tcpclient.py <ip_address> <numbers>')
    exit()
data = str()
data = data + str(sys.argv[2])
for i in range(3, arglen):
    data = data + ' ' + str(sys.argv[i])


data = str()
data = data + str(sys.argv[2])
for i in range(3, arglen):
	data = data + ' ' + str(sys.argv[i])

bandera = 0   
while bandera == 0:
	
	print("Datos enviados")
	print(data)
	
	s = socket.socket()
	port = 11111
	s.connect((sys.argv[1], port))
	s.send(data)
	
	print("\nDatos recibidos")
	datos_recibidos = str()
	datos_recibidos = s.recv(1024)
	print(datos_recibidos)
		
	if datos_recibidos == "-*/D":
		#print("if")
		bandera = 1
	else:
		data = str(raw_input('\nIntroduzca el dato nuevamente. Para finalizar introduzca "-*/d" '))
	
s.shutdown(0)
s.close
	
"""

h= socket.socket()

port = 11111
h.connect((sys.argv[1], port))
data = "-*/d"
h.send(data)

print("\nDatos enviados")
print(data)
"""
