#!/usr/bin/env python3
# coding: utf-8
score=int(input('Enter your score :'))
if score>=90:
    print('grade is "A"')
    print('excellent!')
elif score>=80:
    print('grade is "B"')
    print('good!')
elif score>=70:
    print('grade is "C"')
    print('common!')
elif score>=60:
    print('grade is "D"')
    print('just passed!')
else:
    print('not passed!')
    print('bad!')
