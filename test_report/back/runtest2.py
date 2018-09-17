#!/usr/bin/python
#coading:utf-8

import unittest
import json
import requests
from HTMLTestRunner import HTMLTestRunner
import time

# 加载测试文件
import test


# 构造测试集
suite = unittest.TestSuite() #实例化

suite.addTest(test.test("test"))




if __name__ =="__main__":
    testunit = unittest.TestSuite()
    testunit.addTest(suite)

    #  按照一定的格式获取当前时间
    now = time.strftime("%Y-%m-%d %H_%M_%S")

    # 定义报告存放路径
    filename = './'+ now + 'test_result.html'
    fp = open(filename,"wb")

    #  定义测试报告
    runner = HTMLTestRunner(stream = fp,
                            title = "登录接口报告",
                            description = "测试用例执行情况：")
    # 运行测试
    runner.run(testsuite)
    fp.close()     #关闭文件对象把数据写进磁盘



