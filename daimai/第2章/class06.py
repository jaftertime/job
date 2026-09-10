#!/usr/bin/env python3.6
# coding: utf-8
class Person:
    name=None
    age=None
    def __init__(self,name='Noname',age=0):
        self.name=name
        self.age=age
zhao=Person('Zhao',20)
print('zhao.age=%d '% zhao.age)
zhao.age=22
print('zhao.age=%d '% zhao.age)
