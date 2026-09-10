#!/usr/bin/env python3.6
# coding: utf-8
import threadpool
import socket
def scan_port(num):
    ports=num*4096
    thread_name='thread'+str(num)
    for port in range(ports,ports+4096):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((ip, port))
        if result == 0:
            print('I am %s, port %d is openned!' % (thread_name, port))
        s.close()
ip='192.168.3.9'
p=threadpool.ThreadPool(16)
num_list=list(range(16))
tasks=threadpool.makeRequests(scan_port, num_list)
for task in tasks:
    p.putRequest(task)
p.wait()
print('All threads had finished!')
