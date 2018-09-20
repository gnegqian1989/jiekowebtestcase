#!/usr/bin/python
#coading:utf-8

# https://blog.csdn.net/FloraCHY/article/details/80253846

import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import time
import unittest
from BSTestRunner import BSTestRunner

class Send_NewReport():
    # 存放测试报告文件夹
    report_dire =r'D:\shuo-huahua\Public_number_jieko_0919\test_report\fujian_reoprt'
    def Send_NewReport(report_dire):
        # os.listdir()方法用于返回指定文件包含文件或者文件夹的名字列表
        lists = os.listdir(report_dire)
        # 按照时间顺序对该目录文件夹下面的文件进行排序
        lists.sort(key=lambda fn: os.path.getatime(report_dire + '\\' + fn))
        # 输出最近的报告路径
        file = os.path.join(report_dire,lists[-1])
        print(file)
        # return file
        # 发送邮件
        # 发送邮件服务器 qq邮箱

        smtpserver = 'smtp.qq.com'
        # 发送邮箱用户名和密码
        sender = '1585620775@qq.com'
        passwd = 'zbhrftpklsirjafb'
        # 发送和接收邮件邮箱
        user = '1585620775@qq.com'
        receiver = ['1585620775@qq.com']
        # 发送邮件和内容
        dateT = time.strftime('%Y-%m-%d')
        subject = '人力情报.liate Test Report'+dateT
        content = '<html><h1>人力情报 Test Report %s</h1>' \
                  '<body><body><p>Please download the testreport,Thank you!  此报告建议下载后查看！谢谢！</p></html>'%dateT

        # 构造附件内容
        # send_file = open(r'D:\shuo-huahua\Public_number_jieko_0919\test_report','rb').read()
        send_file = open(file,'rb').read()
        att = MIMEText(send_file,'base54','utf-8')
        att['Content-Type'] = 'application/octest-stream'
        att['Content-Disposition'] = 'attachment;filename =%s' % lists[-1]
         # 构建发送和接收消息
        msg = MIMEMultipart()
        msg.attach(MIMEText(content,'html','utf-8'))
        msg['Subject'] = Header(subject,'utf-8')
        msg['From'] = sender
        msg['To'] = ','.join(receiver)
        msg.attach(att)

        # SSL协议端口号使用
        smtp = smtplib.SMTP_SSL(smtpserver,465)
        # 向服务器表示用户身份
        smtp.helo(smtpserver)
        # 服务器返回结果确认
        smtp.ehlo(smtpserver)
        # 登录邮箱服务器用户和密码
        smtp.login(user,passwd)
        print("Start Send Email....")
        smtp.sendmail(sender,receiver,msg.as_string())
        smtp.quit()
        print('Email Send Sucess!')

if __name__ == '__main__':
    # 定位到当前目录
    test_dir = r'D:\shuo-huahua\Public_number_jieko_0919\test_case'
    # 执行所有test开头方法
    discovery = unittest.defaultTestLoader.discover(test_dir,pattern = 'test*.py')
    #存放测试报告的文件夹
    report_dir = r'D:\shuo-huahua\Public_number_jieko_0919\test_report\fujian_reoprt'
    #报告命名格式
    now = time.strftime('%Y-%m-%d %H%M%S')
    #报告文件完整路径
    report_name = report_dir + '\\'+ now + ' result.html'
    #打开文件再报告文件写入测试结果
    with open(report_name,'wb') as f:
        runner = BSTestRunner(stream = f,title ='人力情报 Test Report',
                              description = 'Test Case Result by Chy'
        )
        runner.run(discovery)
     #    通过邮件发送最新的报告
    Send_NewReport.Send_NewReport(report_dir)


