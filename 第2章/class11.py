#!/usr/bin/env python3
# coding: utf-8
class Person(object):
    name=None
    def __init__(self,name='Noname'):
        self.name=name
class Student(Person):
    __score=0
    def __init__(self,name='Noname',score=0):
        super().__init__(name)
        self.__score=score
    def get_score(self):
        return self.__score
p1=Person('Zhao')
p2=Student('Qian',90)
print("p1 is an instance of Person? ",isinstance(p1,Person))
print("p2 is an instance of Person? ",isinstance(p2,Person))
print("p1 is an instance of Student? ",isinstance(p1,Student))
print("p2 is an instance of Student? ",isinstance(p2,Student))
print("p2 is a subclass of Person? ",issubclass(Student,Person))
print("p1 has the name atrribute? ",hasattr(Person,'name'))
print("p2 has the __score atrribute? ",hasattr(p2,'__score'))
print("get p2's get_score() method. ",getattr(Student,'get_score'))
print("get p2's name attribute. ",getattr(p2,'name'))
print("run p2's get_score() method. ",getattr(p2,'get_score')())
setattr(p1,'name','Zhao Yun')
setattr(Student,'height',1.88)
print("p1.name=",p1.name)
print("Student.height=",Student.height)
