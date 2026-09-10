#!/usr/bin/env python3
# coding: utf-8
class Person:
    __slots__=('name','age','myprint')
def my_print(self):
    print('My name is %s, age is %d' % (self.name,self.age))
zhao=Person()
zhao.name='zhao'
zhao.age=18
print(zhao.name,zhao.age)
Person.myprint=my_print
zhao.myprint()
#zhao.color='Red'
