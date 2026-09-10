#!/usr/bin/env python3.6
# coding: utf-8
import netifaces
info=netifaces.gateways()
print('info=',info)
print('type(info)=',type(info))
gateway_addr=info['default'][2][0]
print('gateway_addr=',gateway_addr)
