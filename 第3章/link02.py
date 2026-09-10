#!/usr/bin/env python3.6
# coding: utf-8
import psutil
info = psutil.net_if_addrs()
print('info=',info)
print('type(info)=',type(info))
net1=info['ens33']
print('net1=',net1)
print('type(net1)=',type(net1))
packet=net1[2]
print('packet=',packet)
print('type(packet)=',type(packet))
print('mac_addr=',packet.address)
