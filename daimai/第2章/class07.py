#!/usr/bin/env python3.6
# coding: utf-8
class Person:
    __name=None
    __age=None
    def __init__(self,name='Noname',age=0):
        self.__name=name
        self.__age=age
    def set_name(self,name):
        self.__name=name
    def set_age(self,age):
        self.__age=age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
zhao=Person('Zhao',20)
zhao.set_age(22)
print('name is %s, age is %d '% (zhao.get_name(),zhao.get_age()))
