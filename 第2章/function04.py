#!/usr/bin/env python3.6
# coding: utf-8
def myfun(*args):
  print(args)
  s=0
  for xx in args:
      s=s+xx
  return s
print('result=%d'% myfun(2,4,6,8))
