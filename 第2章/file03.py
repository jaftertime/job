#!/usr/bin/env python3.6
# coding: utf-8
with open('test1.dat','w') as f:
    for x in ['aa',123,'文件',True,'ddd']:
        if type(x)==str:
            f.write(x)
