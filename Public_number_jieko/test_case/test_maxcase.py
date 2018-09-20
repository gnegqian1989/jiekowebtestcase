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
class test_login_xxyAPP(MyTest):

    def test_login1(self):
        '''测试用例1：信息员端基础地址获取'''
        self.url = "http://service.weijingyuan.com.cn/appsettings/main/getsettings.do?" \
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

    def test_login2(self):
        '''测试用例2：信息员登录'''
        self.url = "https://fresh.weijingyuan.com.cn/JinMen/android/login/login.do?" \
              "&version=2.1.04" \
              "&strApp=hexi" \
              "&appUserTypeCode=xxy" \
              "&strPasswd=1bbd886460827015e5d605ed44252251" \
              "&strAccount=18920615201&"
        self.headers = {"Content-Type":"application/json"}
        self.r = requests.get(url = self.url)
        # return r.json()

        print(self.r.text)
        print(self.r.status_code)
        self.assertIn("200",self.r.text)

if __name__ =="__main__":
        unittest.main()
