#!/usr/bin/env python3.6
# coding: utf-8
f=open('test1.dat','w')
for x in ['aa',123,'文件',True,'ddd']:
    if type(x)==str:
        f.write(x+'\n')
f.close()
f=open('test1.dat','r')
xx=f.readline()
xx=xx[0:-1]
my_list=[]
while xx!='':
    print('xx=',xx)
    my_list.append(xx)
    xx=f.readline()
    xx=xx[0:-1]
f.close()
print('my_list=',my_list)
