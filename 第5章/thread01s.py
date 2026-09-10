#!/usr/bin/env python3.6
# coding: utf-8
import threading
import socket
import os
def sendfile(conn):
    str1=conn.recv(1024)
    filename=str1.decode('utf-8')
    print('I am ', threading.current_thread().name)
    print('The client requests my file:',filename)
    if os.path.exists(filename):
        print('I have %s, begin to download!' % filename)
        conn.send(b'yes')
        conn.recv(1024)
        size=1024
        with open(filename,'rb') as f:
            while True:
                data=f.read(size)
                conn.send(data)
                if len(data)<size:
                    break
        print('%s is downloaded successfully!' % filename)
    else:
        print('Sorry, I have no %s!' % filename)
        conn.send(b'no')
    conn.close()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.3.201',8088))
s.listen(100)
print('Wait for connecting...')
while True:
    (conn,addr)=s.accept()
    t = threading.Thread(target=sendfile, args=(conn,))
    t.start()
