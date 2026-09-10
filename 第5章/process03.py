#!/usr/bin/env python3.6
# coding: utf-8
from multiprocessing import Pool
import os
import socket
def scan_port(ports):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    for port in range(ports,ports+4096):
        result = s.connect_ex((ip, port))
        if result == 0:
            print('I am process %d, port %d is openned!' % (os.getpid(),port))
    s.close()
ip='192.168.3.1'
p = Pool(16)
for i in range(16):
    p.apply_async(scan_port, args=(i*4096,))
p.close()
p.join()
print('All subprocesses had finished!')
