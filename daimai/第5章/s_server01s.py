#!/usr/bin/env python3.6
# coding: utf-8
import socketserver
def factorial(n):
    s=1
    for x in range(2,n+1):
        s=s*x
    return s
class Factorial_server(socketserver.StreamRequestHandler):
    def handle(self):
        conn = self.request
        try:
            data_b = conn.recv(1024)
            data_s=data_b.decode('utf-8')
            data=int(data_s)
            if data>1:
                fact=factorial(data)
            else:
                fact=1
            fact_s=str(fact)
            fact_b=fact_s.encode('utf-8')
            conn.send(fact_b)
            print('factorial(%d)=%s, from %s' % (data, fact_s,self.client_address[0]))
        except Exception as e:
            print('Error is ',e)
ip='192.168.3.201'
server = socketserver.ForkingTCPServer((ip,8899),Factorial_server)
print('Wait for TCP connecting...')
server.serve_forever()
