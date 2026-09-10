#!/usr/bin/env python3
# coding: utf-8
class Person(object):
    __name=None
    def __init__(self,name='Noname'):
        self.__name=name
    def get_name(self):
        return self.__name
    def whoami(self):
        print('I am a person, My name is ', self.__name)
class Student(Person):
    __score=0
    def __init__(self,name='Noname',score=0):
        super().__init__(name)
        self.__score=score
    def whoami(self):
        print('I am a student, My name is %s, score is %d' % ((super().get_name(),self.__score)))
class Teacher(Person):
    __title=None
    def __init__(self,name='Noname',title='none'):
        super().__init__(name)
        self.__title=title
    def whoami(self):
        print('I am a teacher, My name is %s, title is %s' % ((super().get_name(),self.__title)))
def whoareyou(xx):
    xx.whoami()
p1=Person('Zhao')
p2=Student('Qian',90)
p3=Teacher('Sun','Professor')
whoareyou(p1)
whoareyou(p2)
whoareyou(p3)
