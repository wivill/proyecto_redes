#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# Importa la biblioteca socket para crear enlaces
import socket
# import time

# Inicializa

print("Bienvenido. Esperando la recepción de solicitudes...\n\n")
s = socket.socket()
port = 11111
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', port))

s.listen(5)
bandera = True
primer_mensaje = False
msj_bienvenida = True

while(bandera):
    c, addr = s.accept()
    data = c.recv(1024)
    data_return = data.upper()
# Agregar conversión de minúsculas a mayúsculas
    if (msj_bienvenida is True):
        c.send("Bienvenido. Esperando la recepción de solicitudes...\n\n")
        msj_bienvenida = False

    if (primer_mensaje is False):
        print("Primer mensaje recibido. Esperando solicitudes.\n")
        # c.send("Primer mensaje recibido. Esperando solicitudes.\n")
        primer_mensaje = True
    else:
        print("Mensaje recibido. Esperando solicitudes.\n")
        # c.send("Mensaje recibido. Esperando solicitudes.\n")

    print('Address:', addr, 'Data:', data_return)

    mylist = list(data.split(' '))
    c.send(data_return)
    s.listen(5)

    if data == "-*/d":
        print("Se ha enviado la bandera, se termina la conexión.\n")
        bandera = False

s.close()
