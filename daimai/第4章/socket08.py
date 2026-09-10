#!/usr/bin/env python3.6
# coding: utf-8
import socket
import struct
import binascii
s = socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.htons(0x0800))
for xx in range(10):
    data = s.recvfrom(2048)
    print('\nFrame number is %d:' % xx)
    packet=data[0]
    frame_header_b = packet[0:14]
    frame_header_s = struct.unpack("!6s6s2s",frame_header_b)
    source_MAC_Addr=binascii.hexlify(frame_header_s[0])
    dest_MAC_Addr=binascii.hexlify(frame_header_s[1])
    proto_type=binascii.hexlify(frame_header_s[2])
    print('Souce MAC address is ',source_MAC_Addr)
    print('Destination MAC address is ',dest_MAC_Addr)
    print('Protocol type is ',proto_type)
    ip_header_b = packet[14:34]
    ip_header_s = struct.unpack("!12s4s4s",ip_header_b)
    print("Protocol is " , ip_header_s[0][9:10])
    print("Source IP address is " + socket.inet_ntoa(ip_header_s[1]))
    print("Destination IlutP address is " + socket.inet_ntoa(ip_header_s[2]))
s.close()
