#!/usr/bin/env python3.6
# coding: utf-8
import urllib.request
import re
url='http://www.lzu.edu.cn/V2013/szdw/ys/'
pre_url='http://www.lzu.edu.cn'
reg1=r'简介">(.+?)</a></tt>'
reg1_comp = re.compile(reg1)
reg2 = r'img src="(.+?)"'
reg2_comp = re.compile(reg2)
obj=urllib.request.urlopen(url)
data_b=obj.read()
data_s=data_b.decode('utf-8')
reg1_list = reg1_comp.findall(data_s)
reg2_list = reg2_comp.findall(data_s)
k=0
for name in reg1_list:
    url_img=pre_url+reg2_list[k]
    name_photo='./photos/%s.%s' % (name,url_img[-3:])
    urllib.request.urlretrieve(url_img,name_photo)
    print(name_photo,url_img)
    k=k+1
