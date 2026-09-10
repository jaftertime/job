#!/usr/bin/env python3
# coding: utf-8
class Person:
    name=None
    age=None
    def __init__(self,name='Noname',age=0):
        self.name=name
        self.age=age
    def print_me(self):
        print('My name is %s, age is %d' % (self.name,self.age))
    def print_color(self):
        print('My name is %s, color is %s' % (self.name,self.color))
Person.color='Blue'
zhao=Person('Zhao',20)
zhao.print_me()
zhao.print_color()
del Person.color
qian=Person('Qian',30)
qian.color='Green'
qian.print_me()
qian.print_color()
del qian.color
