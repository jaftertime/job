#!/usr/bin/env python3.6
# coding: utf-8
import pickle
with open('test2.dat','wb') as f:
    for x in ['aa',123,'文件','c',(3+4j)]:
        pickle.dump(x,f)
with open('test2.dat','rb') as f:
    f.seek(0,2)
    endp=f.tell()
    f.seek(0)
    xx=pickle.load(f)
    while xx is not None:
        print('xx=',xx)
        if f.tell()>=endp:
            break
        xx=pickle.load(f)
