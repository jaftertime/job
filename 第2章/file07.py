#!/usr/bin/env python3.6
# coding: utf-8
import pickle
class Person:
    def __init__(self,name='Noname',age=0):
        self.name=name
        self.age=age
xx=Person('Zhao',20)
with open('test4.dat','wb') as f:
    pickle.dump(xx,f)
with open('test4.dat','rb') as f:
    yy=pickle.load(f)
print('name=',yy.name,'age=',yy.age)
