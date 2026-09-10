#!/usr/bin/env python3.6
# coding: utf-8
try:
    s = 10 / 0
    print('It is my turn!')
except ZeroDivisionError as e:
    print('Exception:', e)
    s=0
finally:
    print('Finally, s=',s)
print('Program is ended!')
