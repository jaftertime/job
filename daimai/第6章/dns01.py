#!/usr/bin/env python3.6
# coding: utf-8
import dns.resolver
def resolver(domain,type):
    rt_obj=dns.resolver.query(domain, type)
    ans_list=rt_obj.response.answer
    print('Type %s records are:' % type)
    for xx in ans_list:
        print(xx.to_text())
resolver('www.baidu.com','A')
resolver('baidu.com','MX')
resolver('baidu.com','NS')
resolver('www.baidu.com','CNAME')
resolver('baidu.com','SOA')
