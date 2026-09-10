#!/usr/bin/env python3.6
# coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
host="mail.lut.cn"
port=25
user="zhaoh"
password="xxxxxx"
sender='zhaoh@lut.cn'
receivers=['594286500@qq.com']
msg="""
<p>Python SMTP for HTML</p>
<p><a href="http://www.lut.edu.cn"> Welcome to LUT!</a></p>
"""
message=MIMEText(msg, 'html', 'utf-8')
message['From']=Header("Python SMTP", 'utf-8')
message['To']=Header('Receivers', 'utf-8')
message['Subject']=Header('Python SMTP to receivers', 'utf-8')
try:
    smtp_obj=smtplib.SMTP()
    smtp_obj.connect(host,port)
    smtp_obj.ehlo('mail.lut.cn')
    print('logining')
    smtp_obj.login(user,password)
    print('logined')
    smtp_obj.sendmail(sender,receivers, message.as_string())
    print("Email is sending successfully!")
except Exception as e:
    print("Error is ",e)
smtp_obj.quit()
