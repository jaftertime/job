#!/usr/bin/env python3.6
# coding: utf-8
class Person:
    name=None
    age=None
    def __init__(self,name='Noname',age=0):
        self.name=name
        self.age=age
    def print_me(self):
        print('My name is %s, age is %d' % (self.name,self.age))
zhao=Person('Zhao',20)
zhao.print_me()
qian=Person('Qian',30)
qian.print_me()
