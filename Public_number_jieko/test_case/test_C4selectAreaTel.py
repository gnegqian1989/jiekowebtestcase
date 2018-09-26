#!/usr/bin/python
#coding:utf-8

import requests
import json
import unittest
import sys
sys.path.append(r'D:\shuo-huahua\Public_number_jieko_0919\Public_number_jieko\config')
import config
# print (config.TestPlanUrl)


class MyTest(unittest.TestCase):
    def setUp(self):
        print('start test')
        pass
    def tearDown(self):
        print('end test')
        pass
class test_selectAreaTel(MyTest):
    '''测试接口：常用电话'''

    def test_selectAreaTel(self):
        '''测试用例1：常用电话'''
        self.url =(config.TestPlanUrl) + "/publics/hx/tel/selectAreaTel.do?" \
                                         "token=9678d11a-33a1-4bb9-9b9d-3a93af491d1d&" \
                                         "strApp=hexi&"
        self.headers = {"Content-Type":"application/json"}
        self.r = requests.get(url = self.url)
        # return r.json()

        print(self.r.text)
        print(self.r.status_code)
        self.assertIn("200",self.r.text)

if __name__ =="__main__":
        unittest.main()