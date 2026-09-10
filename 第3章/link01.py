#!/usr/bin/env python3.6
# coding: utf-8
import uuid
node = uuid.uuid1()
print('type(node)=',type(node))
print('node=',node)
hex = node.hex
print('hex=',hex)
mac_addr = hex[-12:]
print('mac_addr=',mac_addr)
