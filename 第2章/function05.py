#!/usr/bin/env python3.6
# coding: utf-8
def myfun(name,**kwargs):
  print(kwargs)
  print('name:',name)
  for key in kwargs:
      print(key,':',kwargs[key])
  return
myfun('Zhao',age=18,height=1.88,city='Lanzhou')
