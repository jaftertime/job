#!/usr/bin/env python3.6
# coding: utf-8
import json
class Person:
    def __init__(self,name='Noname',age=0):
        self.name=name
        self.age=age
def person2dict(p):
    return {'name':p.name,'age':p.age}
def dict2person(d):
    return Person(d['name'],d['age'])
xx=Person('Zhao',20)
with open('test6.dat','w') as f:
    json.dump(xx,f,default=person2dict)
with open('test6.dat','r') as f:
    yy=json.load(f,object_hook=dict2person)
print('type(yy)=',type(yy))
print('name=',yy.name,'age=',yy.age)
