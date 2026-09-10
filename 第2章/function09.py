#!/usr/bin/env python3.6
# coding: utf-8
def myfun(x,y,z):
  x=x+1
  y.append(3)
  z=[3,4]
  print('x=',x,'id(x)=',id(x))
  print('y=',y,'id(y)=',id(y))
  print('z=',z,'id(z)=',id(z))
  return
a=10
b=[1,2]
c=[1,2]
print('before calling myfun a=',a,'id(a)=',id(a))
print('before calling myfun b=',b,'id(b)=',id(b))
print('before calling myfun c=',c,'id(c)=',id(c))
myfun(a,b,c)
print('after calling myfun a=',a,'id(a)=',id(a))
print('after calling myfun b=',b,'id(b)=',id(b))
print('after calling myfun c=',c,'id(c)=',id(c))
