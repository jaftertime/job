#!/usr/bin/env python3.6
# coding: utf-8
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s_addr=('192.168.3.201',8091)
s.bind(('192.168.3.7',8888))
s.sendto(b'memory info',s_addr)
(data_b,addr)=s.recvfrom(1024)
data_s=data_b.decode('utf-8')
if addr==s_addr:
    data_s=data_b.decode('utf-8')
    print('Memory status is flowing...')
    data_list=data_s.split(',')
    for xx in data_list:
        print(xx)
s.close()
