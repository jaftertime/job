#!/usr/bin/env python3.6
# coding: utf-8
import pickle
from io import BytesIO
f=BytesIO()
for x in ['aa',123,'文件',True,'ddd']:
    pickle.dump(x,f)
f.seek(0)
while True:
    try:
        xx=pickle.load(f)
        print('xx=',xx)
    except EOFError:
        break
