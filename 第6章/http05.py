#!/usr/bin/env python3.6
# coding: utf-8
import urllib.request
import urllib.parse
import gzip
import re
import http.cookiejar
def ungzip(data):
    print('Decompressing.....')
    try:
        data=gzip.decompress(data)
    except:
        print('Need not decompress!')
    return data
def opener_obj(header_str):
    cj=http.cookiejar.CookieJar()
    handler=urllib.request.HTTPCookieProcessor(cj)
    opener=urllib.request.build_opener(handler)
    header=[]
    for key, value in header_str.items():
        elem=(key, value)
        header.append(elem)
    opener.addheaders=header
    return opener
host='www.taobao.com'
header={
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Accept-Encoding': 'gzip, deflate',
    'Host': host,
    'DNT': '1'
}
url='https://'+host
opener=opener_obj(header)
obj=opener.open(url)
print('Status code=',obj.getcode())
print('url=',obj.geturl())
print('info=',obj.info())
data_gz=obj.read()
data_b=ungzip(data_gz)
data_s=data_b.decode('utf-8')
#print(data_s)
reg=r'&amp;q=(.+?)&amp;.*">(.+?)</a>'
rt_list=re.findall(reg,data_s)
print('\nHot searching goods are:')
for xx in rt_list:
    print(xx[0])
