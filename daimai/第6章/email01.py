#!/usr/bin/env python3.6
# coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
host="smtp.qq.com"
port=587
user="594286500"
code="1234567890123456"
sender='594286500@qq.com'
receivers=['zhaoh@lut.edu.cn']
message=MIMEText('I am Hong, sending Email through QQ ...', 'plain', 'utf-8')
message['From']=Header("I", 'utf-8')
message['To']=Header('Me', 'utf-8')
message['Subject']=Header('Python SMTP test', 'utf-8')
try:
    smtp_obj=smtplib.SMTP()
    smtp_obj.connect(host,port)
    smtp_obj.ehlo('smtp.qq.com')
    smtp_obj.starttls()
    print('logining')
    smtp_obj.login(user,code)
    print('logined')
    smtp_obj.sendmail(sender, receivers, message.as_string())
    print("Email is sending successfully!")
except smtplib.SMTPException as e:
    print("Error is ",e)
