#!/usr/bin/python
#coading:utf-8

import unittest
import requests
from HTMLTestRunner import HTMLTestRunner
import time
import os
import smtplib
import email
from email.mime.text import MIMEText
from email.header import Header

#=======定义发送邮件=======
def send_mail(file_new):
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body,'html','utf-8')
    msg['Subject'] = Header('测试接口自动化测试报告','utf-8')

    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com')
    smtp.login('1585620775@qq.com','zbhrftpklsirjafb')
    smtp.sendmail('1585620775@qq.com','1585620775@qq.com',msg.as_string())
    smtp.quit()
    print('邮件已发送，请注意查收')


#     =====查找测试目录，找到最新生成的测试报告====
def new_report(test_report):
    lists = os.listdir(test_report)
    lists.sort(key=lambda fn:os.path.getmtime(test_report +'\\' + fn))
    file_new = os.path.join(test_report,lists[-1])
    print(file_new)
    return file_new

if __name__ =="__main__":
    test_dir = r"D:\shuo-hua\jiekojicheng0914\test_case"
    test_report = r"D:\shuo-hua\jiekojicheng0914\test_report\html_report"



    discover = unittest.defaultTestLoader.discover(test_dir,pattern = 'test*.py')

    #按照一定的格式获取当前时间
    now = time.strftime("%Y-%m-%d_%H-%M_%S-")

    #定义报告存放路径
    filename =  test_report + "\\" + now + 'result.html'
    fp = open(filename,'wb')

#     #定义测试报告
    runner = HTMLTestRunner(stream = fp,
                            title = "邮件接口测试报告",
                            description = "测试用例执行情况：")
    #运行测试
    runner.run(discover)
    fp.close()



    new_report = new_report(test_report)
    send_mail( new_report)
