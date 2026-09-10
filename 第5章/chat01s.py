#!/usr/bin/env python3.6
# coding: utf-8
import socketserver
class Chat_server(socketserver.StreamRequestHandler):
    def handle(self):
        conn = self.request
        try:
            while True:
                data_b = conn.recv(1024)
                print('data_b=',data_b)
                if conns.count(conn)==0:
                    conns.append(conn)
                    name_s=data_b.decode('utf-8')
                    users.setdefault(conn,name_s)
                    data='Welcome '+name_s+'!'
                    data_s=''
                else:
                    name_s=users.get(conn)
                    data_s=data_b.decode('utf-8')
                    data=name_s+': '+data_s
                for cn in conns:
                    data_b=data.encode('utf-8')
                    cn.send(data_b)
                if data_s.upper()[0:3]=='BYE':
                    print('%s is exited!' % name_s)
                    conns.remove(conn)
                    del(users[conn])
                    break;
                print('data=',data)
        except Exception as e:
            print('Error is ',e)
conns=[]
users={}
ip='192.168.3.201'
server = socketserver.ThreadingTCPServer((ip,9988),Chat_server)
print('Wait for TCP connecting...')
server.serve_forever()
