#!/usr/bin/python
#coading:utf-8

import requests
import json
import unittest
import sys
class MyTest(unittest.TestCase):
    def setUp(self):
        # a = 'start test'
        # print (a.encode('utf-8'))
        pass
    def tearDown(self):
        # b = 'end test'
        # print(b.encode('utf-8'))
        pass
class test_xxx_get(MyTest):

    def test_xxx_get1(self):
        '''测试用例1：哈哈'''
        self.url = "https://fresh.weijingyuan.com.cn/JinMen/main/login.do?account=admin&psw=23698741&strApp=hexi"
        self.headers = {"Content-Type":"application/json"}
        # self.data = {
        #
        # }
        # r = requests.get(url=self.url,json = self.data,headers =self.headers)

        self.r = requests.get(url = self.url)
        # return r.json()

        # print(self.r.text)
        # print(self.r.status_code)
        self.assertIn("成功",self.r.text)

if __name__ =="__main__":
        unittest.main()
