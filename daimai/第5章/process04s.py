#!/usr/bin/env python3.6
# coding: utf-8
import psutil
import socket
from multiprocessing import Process
import os
def do_cpu():
    cpu_usage_rate_total=str(psutil.cpu_percent(0))+'%\n'
    data=cpu_usage_rate_total
    count=0
    for process in psutil.process_iter():
        data=data+process.name()
        data=data+','+str(process.pid)
        cpu_usage_rate_process=str(process.cpu_percent(0))+'%'
        data=data+','+cpu_usage_rate_process+'\n'
        count+=1
        if count==10:
            break
    return data
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
def send_info(info, addr):
    info_s=info.decode('utf-8')
    print('I am child process %d.'% os.getpid())
    if info_s.upper()=='CPU':
        data=do_cpu()
        s.sendto(data.encode('utf-8'),addr)
        print('The client is ',addr)
        print('Sended CPU data is:',data)
    elif info_s.upper()=='MEMORY':
        data=do_memory()
        s.sendto(data.encode('utf-8'),addr)
        print('The client is ',addr)
        print('Sended memory data is:',data)
    else:
        data='Unkown request!'
        s.sendto(data.encode('utf-8'),addr)
        print('The client is ',addr)
        print('Sended info is:',data)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('192.168.3.201',8095))
print('I am parent process, my ID is', os.getpid())
print('Bind UDP on 8095...')
while True:
    (info,addr)=s.recvfrom(1024)
    p = Process(target=send_info, args=(info,addr))
    p.start()
