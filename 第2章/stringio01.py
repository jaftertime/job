#!/usr/bin/env python3.6
# coding: utf-8
from io import StringIO
f=StringIO()
for x in ['aa',123,'文件',True,'ddd']:
    if type(x)==str:
        f.write(x)
f.seek(0)
xx=f.read()
print('xx=',xx)
yy=f.getvalue()
print('yy=',yy)
