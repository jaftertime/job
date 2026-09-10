#!/usr/bin/env python3.6
# coding: utf-8
import urllib.request
import json
code='101160101'
url='http://www.weather.com.cn/data/cityinfo/%s.html' % code
print('url=',url)
obj=urllib.request.urlopen(url)
print('type(obj)=',type(obj))
data_b=obj.read()
print('data_b=',data_b)
data_s=data_b.decode('utf-8')
print('data_s=',data_s)
data_dict=json.loads(data_s)
print('data_dict=',data_dict)
rt = data_dict['weatherinfo']
print('rt=',rt)
my_rt=('%s,%s,%s~%s') % (rt['city'],rt['weather'],rt['temp1'],rt['temp2'])
print(my_rt)
