#!/usr/bin/env python3.6
# coding: utf-8
from ftplib import FTP
def ftp_connect(host,username,password):
    ftp=FTP()
    ftp.connect(host,21)
    ftp.login(username, password)
    return ftp
def ftp_download(ftp,remotefile,localfile):
    f=open(localfile, 'wb')
    ftp.retrbinary('RETR ' +remotefile,f.write)
    f.close()
def ftp_upload(ftp,remotefile, localfile):
    f=open(localfile, 'rb')
    ftp.storbinary('STOR ' +remotefile,f)
    f.close()
ftp=ftp_connect("192.168.3.18","ftpuser","123456")
print(ftp.getwelcome())
file_list=ftp.nlst()
print(file_list)
ftp_download(ftp, "test.txt", "./download/test.txt")
ftp_download(ftp, "tt.dat", "./download/tt.dat")
ftp_upload(ftp, "ls", "/bin/ls")
file_list=ftp.nlst()
print(file_list)
ftp.quit()
