#!/usr/bin/env python3.6
# coding: utf-8
from wsgiref import simple_server
def response_hello(env, respose):
#    for key in env:
#        print(key,"=",env[key])
    path_info=env['PATH_INFO'][1:]
    print('path_info=',path_info)
    respose('200 OK', [('Content-Type', 'text/html')])
    body1='<h1>Hello, web!</h1>'
    if path_info=='':
        body2='<p><a href="http://%s/option1">option1</a></p>' % host
        body2=body2+'<p><a href="http://%s/option2">option2</a></p>' % host
    else:
        body2='<h2>Your choice is %s.</h2>' % path_info
    body_list=[body1.encode('utf-8'), body2.encode('utf-8')]
    return body_list
host='192.168.3.13'
port=80
httpd=simple_server.make_server(host, port, response_hello)
print('Serving HTTP on port 80...')
httpd.serve_forever()
