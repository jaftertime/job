#!/usr/bin/env python3.6
# coding: utf-8
from types import MethodType
class Person:
    name=None
    age=None
    def __init__(self,name='Noname',age=0):
        self.name=name
        self.age=age
    def print_me(self):
        print('My name is %s, age is %d' % (self.name,self.age))
    def print_color(self):
        self.print_me()
        print('My name is %s, color is %s' % (self.name,self.color))
def my_print(self):
    print('My name is %s, age is %d, color is %s' % (self.name,self.age,self.color))
Person.color='Blue'
zhao=Person('Zhao',20)
zhao.print_me()
zhao.print_color()
del Person.print_color
qian=Person('Qian',30)
qian.color='Green'
qian.print_color=MethodType(my_print,qian)
qian.print_color()
Person.my_print=my_print
del qian.print_color
sun=Person('Sun',40)
sun.my_print()
qian.my_print()
