#!/usr/bin/env python3.6
# coding: utf-8
from wsgiref import simple_server
def response_hello(env, respose):
#    for key in env:
#        print(key,"=",env[key])
    respose('200 OK', [('Content-Type', 'text/html')])
    body1='<h1>Hello, web!</h1>'
    body2='<p><h2>I am a tester!</h2></p>'
    body_list=[body1.encode('utf-8'), body2.encode('utf-8')]
    return body_list
host='192.168.3.13'
port=80
httpd=simple_server.make_server(host, port, response_hello)
print('Serving HTTP on port 80...')
httpd.serve_forever()
