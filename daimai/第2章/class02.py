#!/usr/bin/env python3.6
# coding: utf-8
class Person:
    name=None
    age=None
    def __init__(self,name='Noname',age=0,color='No color'):
        self.name=name
        self.age=age
        self.color=color
    def print_me(self):
        print('My name is %s, age is %d' % (self.name,self.age))
    def print_color(self):
        print('My name is %s, color is %s' % (self.name,self.color))
zhao=Person('Zhao',20,'Red')
zhao.print_me()
zhao.print_color()
qian=Person('Qian',30)
del qian.color
qian.print_me()
