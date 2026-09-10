#!/usr/bin/env python3.6
# coding: utf-8
import struct
import array
import time
import socket
def checksum(packet):
    if len(packet) & 1:
        packet = packet + '\0'
    words = array.array('h', packet)
    sum = 0
    for word in words:
        sum +=  (word & 0xffff)
    sum = (sum >> 16) + (sum & 0xffff)
    sum = sum + (sum >> 16)
    return (~sum) & 0xffff
header = struct.pack('bbHHh', 8, 0, 0, 1234, 5)
data = struct.pack('d', time.time())
packet = header + data
chkSum = checksum(packet)
header = struct.pack('bbHHh', 8, 0, chkSum, 1234, 5)
packet=header + data
s=socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.getprotobyname("icmp"))
s.settimeout(3)
ip=input('ip adress is:')
for kk in range(4):
    try:
        t1=time.time()
        s.sendto(packet, (ip, 0))
        (r_data,r_addr)=s.recvfrom(1024)
        t2=time.time()
    except Exception as e:
        print('Error is ',e)
        continue
    print('Receive the respond from %s, data is %d bytes, time is %.2f ms' \
    % (r_addr[0],len(r_data),(t2-t1)*1000))
    (h1,h2,h3,h4,h5)=struct.unpack('bbHHh', r_data[20:28])
    print('type=%d,code=%d,chksum=%u,Id=%u,SN=%d' %(h1,h2,h3,h4,h5))
