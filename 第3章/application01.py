#!/usr/bin/env python3.6
# coding: utf-8
from urllib import request
url="http://jitong.lut.edu.cn"
header={'Accept':'text/html','Connection':'keep-alive'}
req=request.Request(url,headers=header)
response=request.urlopen(req)
print('Status code=',response.getcode())
print('url=',response.geturl())
print('info=',response.info())
