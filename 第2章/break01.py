#!/usr/bin/env python3.6
# coding: utf-8
sum=0
for x in range(50,101):
    sum=sum+x
    if sum>=1000:
        break
print('sum=%d,x=%d'% (sum,x))
