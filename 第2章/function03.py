#!/usr/bin/env python3.6
# coding: utf-8
def myfun(xx,a=3,b=4):
  s=a*a+b*b+xx
  return s
print('result=%d'% myfun(30,b=20,a=10))
