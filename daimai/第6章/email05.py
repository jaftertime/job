#!/usr/bin/env python3.6
# coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
host="mail.lut.cn"
port=25
user="zhaoh"
password="xxxxxx"
sender='zhaoh@lut.cn'
receivers=['594286500@qq.com','601400175@qq.com','1176218460@qq.com']
msg="""
<p>Python SMTP for HTML</p>
<p><a href="http://www.lut.edu.cn" >
<img src="cid:image" alt="Welcome to LUT" title='LUT'/>
</a></p>
"""
msgtxt=MIMEText(msg, 'html', 'utf-8')
message=MIMEMultipart()
message.attach(msgtxt)
message['From']=Header("Python SMTP", 'utf-8')
message['To']=Header('Receivers', 'utf-8')
message['Subject']=Header('Python SMTP to receivers', 'utf-8')
img=MIMEImage(open('test.png','rb').read())
img['Content-ID']='image'
message.attach(img)
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
