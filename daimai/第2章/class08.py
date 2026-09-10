#!/usr/bin/env python3.6
# coding: utf-8
class Person:
    def __init__(self,name='Noname',age=0):
        self.name=name
        self.age=age
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name=name
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,age):
        self._age=age
zhao=Person()
zhao.name='Zhao'
zhao.age=18
print('name is %s, age is %d '% (zhao.name,zhao.age))
