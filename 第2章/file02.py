#!/usr/bin/env python3
# coding: utf-8
f=open('test1.dat','w')
try:
    for x in ['aa',123,'文件',True,'ddd']:
        if type(x)==str:
            f.write(x)
except Exception as e:
    print('File exception:',e)
finally:
    f.close()
