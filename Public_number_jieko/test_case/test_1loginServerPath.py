#!/usr/bin/python
#coding:utf-8

import requests
import json
import unittest
import sys
class MyTest(unittest.TestCase):
    def setUp(self):
        print('start test')
        pass
    def tearDown(self):
        print('end test')
        pass
class test_loginServerPath(MyTest):

    def test_loginServerPath(self):
        '''测试用例1：河西力量公众号基础地址获取'''
        self.url = "http://gzh.weijingyuan.com.cn/JinMen/android/login/loginServerPath.do？" \
              "&version=2.1.04" \
              "&brand=HUAWEI" \
              "&strApp=hexi" \
              "&appUserTypeCode=xxy&"
        self.headers = {"Content-Type":"application/json"}
        self.r = requests.get(url = self.url)
        # return r.json()

        print(self.r.text)
        print(self.r.status_code)
        self.assertIn("success",self.r.text)

if __name__ =="__main__":
        unittest.main()