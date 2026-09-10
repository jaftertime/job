#!/usr/bin/env python3.6
# coding: utf-8
def myfun(x):
  if x>1:
      return x*myfun(x-1)
  else:
      return 1
print('Factorial result is %d' % myfun(10))
