#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 22222))
while True:
    data, addr = s.recvfrom(1024)
    data_return = data.upper()
    print('Address:', addr, 'Data:', data_return)
    mylist = list(data.split(':'))
    # intlist = list()
    # for i in range(0, len(mylist)):
    #    intlist.append(int(mylist[i]))
    # intlist.sort()
    s.sendto(str(mylist), addr)
