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
class test_userMessage(MyTest):
    '''测试接口：我的消息列表页数据'''

    def test_userMessage(self):
        '''测试用例1：我的消息列表数据'''

#        ==================get请求==================================

        self.url =(config.TestPlanUrl) +"/publics/hx/infoUserMessage/userMessage.do?" \
                                         "strAccount=13820559247&" \
                                         "token=9678d11a-33a1-4bb9-9b9d-3a93af491d1d&" \
                                         "strApp=hexi&" \
                                         "isRead=0&" \
                                         "intPageSize=10&" \
                                         "searchKey=1&" \

        print(self.url)
        self.headers = {"Content-Type":"application/json"}

        self.r = requests.get(url = self.url)
        # return self.r.json()

#        ==================post请求==================================

        # self.url = (config.TestPlanUrl) + "/publics/hx/baseSign/addIntegral.do?"
        # self.data = {
        #     "token": "e133024d-481d-421b-a4cf-24bc3c729eb4",
        #     "strApp": "hexi",
        #     "strLongitude": "117.154393",
        #     "strLatitude": "39.105896",
        #
        # }
        # self.headers = {"Content-Type": "application/json"}
        # self.r = requests.post(url=self.url, json=self.data, headers=self.headers)

        #=============================================================
        print(self.r)
        print(self.r.text)
        print(self.r.status_code)
        self.assertIn("200",self.r.text)

if __name__ =="__main__":
        unittest.main()