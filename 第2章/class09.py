#!/usr/bin/env python3
# coding: utf-8
class Person(object):
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
class Student(Person):
    __score=0
    def __init__(self,name='Noname',age=0,score=0):
        super().__init__(name,age)
        self.__score=score
    def set_score(self,score):
        self.__score=score
    def get_score(self):
        return self.__score
wang=Student('Wang')
wang.set_age(22)
wang.set_score(95)
print('name is %s, age is %d,score is %d '% (wang.get_name(),wang.get_age(),wang.get_score()))
