#!/usr/bin/env python3.6
# coding: utf-8
def myfun(name,*,age,city):
  print('name:',name)
  print('age:',age)
  print('city:',city)
  return
myfun('Zhao',age=18,city='Lanzhou')
