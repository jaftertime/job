#!/usr/bin/env python3.6
# coding: utf-8
import socket
import psutil
def do_memory():
    memory_status=mm=psutil.virtual_memory()
    data='total='+str(memory_status.total)
    data=data+',available='+str(memory_status.available)
    data=data+',percent='+str(memory_status.percent)+'%'
    data=data+',used='+str(memory_status.used)
    data=data+',free='+str(memory_status.free)
    data=data+',active='+str(memory_status.active)
    data=data+',inactive='+str(memory_status.inactive)
    data=data+',buffers='+str(memory_status.buffers)
    data=data+',cached='+str(memory_status.cached)
    data=data+',shared='+str(memory_status.shared)
    return data
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('192.168.3.201',8091))
print('Bind UDP on 8091...')
while True:
    (info,addr)=s.recvfrom(1024)
    data=do_memory()
    s.sendto(data.encode('utf-8'),addr)
    print('The client is ',addr)
    print('Sended memory data is:',data)
