#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# Importa la biblioteca socket para crear enlaces
import socket
# import time

# Inicializa
s = socket.socket()
port = 11111

s.bind(('', port))

s.listen(5)
bandera = True

while(bandera):
    c, addr = s.accept()
    data = c.recv(1024)
    data_return = data.upper()
# Agregar conversión de minúsculas a mayúsculas

    print('Address:', addr, 'Data:', data_return)

    mylist = list(data.split(' '))
    c.send(data_return)
    s.listen(5)

    if data == "-*/d":
        print("Se ha enviado la bandera, se termina la conexión")
        bandera = False

s.close()
