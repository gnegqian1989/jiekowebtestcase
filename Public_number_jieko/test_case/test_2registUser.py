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
class test_registUser(MyTest):

    def test_registUser(self):
        '''测试用例2：河西力量公众号注册接口'''
        self.url = "http://gzh.weijingyuan.com.cn/JinMen/hxpublic/user/registUser.do？" \
              "&strApp=hexi" \
              "&strMobile=18920615201" \
              "&strPasswd=11111111" \
              "&strRePasswd=11111111"
        self.headers = {"Content-Type":"application/json"}
        self.r = requests.get(url = self.url)
        # return r.json()

        print(self.r.text)
        print(self.r.status_code)
        self.assertIn("success",self.r.text)

if __name__ =="__main__":
        unittest.main()