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
class test_queryNewsDetail(MyTest):
    '''测试接口：新闻资讯新闻详情'''

    def test_queryNewsDetail(self):
        '''测试用例1：新闻资讯新闻详情'''

#        ==================get请求==================================

        # self.url =(config.TestPlanUrl) +"/pc/news/queryNews.do?" \
        #                                  "strGuid=bb2753fa-87cf-47af-8719-fbe5df41ad48&" \
        #                                  "token=9678d11a-33a1-4bb9-9b9d-3a93af491d1d&" \
        #                                  "strApp=hexi&"
        # print(self.url)
        # self.headers = {"Content-Type":"application/json"}
        #
        # self.r = requests.get(url = self.url)
        # return r.json()

#        ==================post请求==================================

        self.url = (config.TestPlanUrl) + "/pc/news/queryNews.do?"
        self.data = {
            "strGuid": "bb2753fa-87cf-47af-8719-fbe5df41ad48",
            "token": "9678d11a-33a1-4bb9-9b9d-3a93af491d1d",
            "strApp": "hexi"
        }
        self.headers = {"Content-Type": "application/json"}
        self.r = requests.post(url=self.url, json=self.data, headers=self.headers)

        #=============================================================
        print(self.r)
        print(self.r.text)
        print(self.r.status_code)
        self.assertIn("200",self.r.text)

if __name__ =="__main__":
        unittest.main()