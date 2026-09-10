#!/usr/bin/env python3.6
# coding: utf-8
sum=0
x=49
while x<100:
    x=x+1
    if x%2==1:
        continue
    sum=sum+x
print('sum=%d'% sum)
