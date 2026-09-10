#!/usr/bin/env python3.6
# coding: utf-8
from scapy.all import conf,dhcp_request
conf.checkIPaddr=0
info=dhcp_request()
print('summary is:\n',info.summary())
option_dhcp=info.sprintf("%DHCP.options%")
print('Options of DHCP is: \n',option_dhcp)
