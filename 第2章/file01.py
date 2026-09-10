#!/usr/bin/env python3.6
# coding: utf-8
f=open('test1.dat','w')
for x in ['aa',123,'文件',True,'ddd']:
    if type(x)==str:
        f.write(x)
f.close()
f=open('test1.dat','r')
xx=f.read()
print('xx=',xx)
f.close()
