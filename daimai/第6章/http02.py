#!/usr/bin/env python3.6
# coding: utf-8
import urllib.request
import re
codes=['101160101','101160102','101160103','101160104']
reg1=r'<title>(【.+】)'
reg1_comp = re.compile(reg1)
reg2 = r'id="hidden_title"\s+value="(.+)"'
reg2_comp = re.compile(reg2)
for code in codes:
    url='http://www.weather.com.cn/weather1d/%s.shtml' % code
    print('url=',url)
    obj=urllib.request.urlopen(url)
    data_b=obj.read()
    data_s=data_b.decode('utf-8')
    reg1_list = reg1_comp.findall(data_s)
    rt_str=reg1_list[0]
    reg2_list = reg2_comp.findall(data_s)
    rt_str+=reg2_list[0]
    print(rt_str)
