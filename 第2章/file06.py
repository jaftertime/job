#!/usr/bin/env python3.6
# coding: utf-8
import pickle
xx=['aa',123,'文件','c',(3+4j)]
yy=pickle.dumps(xx)
with open('test3.dat','wb') as f:
    f.write(yy)
with open('test3.dat','rb') as f:
    yy=f.read()
zz=pickle.loads(yy)
print("xx==zz?",xx==zz)
print('zz=',zz)
