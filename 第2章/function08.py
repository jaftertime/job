#!/usr/bin/env python3.6
# coding: utf-8
def myfun(x,y):
  print('x=',x,'id(x)=',id(x))
  print('y=',y,'id(y)=',id(y))
  return
a=10
b=[1,2]
print('a=',a,'id(a)=',id(a))
print('b=',b,'id(b)=',id(b))
myfun(a,b)
