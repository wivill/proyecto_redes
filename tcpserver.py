#!/usr/bin/env python2.7

# Importa la biblioteca socket para crear enlaces
import socket

# Inicializa
s = socket.socket()
port = 11111

s.bind(('', port))

s.listen(5)

while True:
    c, addr = s.accept()
    data = c.recv(1024)

# Agregar conversión de minúsculas a mayúsculas

    print('Address:', addr, 'Data:', data)

    # mylist = list(data.split(':'))
    mylist = list(data.split(' '))
    # intlist = list()

    # for i in range(0, len(mylist)):
    #    intlist.append(int(mylist[i]))

    # intlist.sort()
    c.send(str(mylist))
    c.close()
