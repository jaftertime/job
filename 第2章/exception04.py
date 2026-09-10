#!/usr/bin/env python3.6
# coding: utf-8
def print_score(score):
    try:
        if not type(score) in [int,float]:
            raise TypeError('score must be the int or float type!')
        elif not 100>=score>=0:
            raise ValueError('score must be between 0 to 100')
        print('score=%6.2f' % score)
    except Exception as e:
        print('Exception:',e)
print_score(88.5)
print_score(120)
print_score('sss')
print_score(95)
