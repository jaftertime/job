#!/usr/bin/env python3.6
# coding: utf-8
sum=0
x=50
while x<=100:
    if x%2==1:
        continue
    sum=sum+x
    x=x+1
print('sum=%d'% sum)
