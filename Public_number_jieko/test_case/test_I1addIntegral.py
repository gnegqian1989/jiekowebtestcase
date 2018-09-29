#!/usr/bin/python
#coding:utf-8

import requests
import json
import unittest
import re
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
class test_addIntegral(MyTest):
    '''测试接口：首页签到'''

    def test_addIntegral(self):
        '''测试用例1：首页签到'''

#        ==================get请求==================================

        self.url =(config.TestPlanUrl) +"/publics/hx/baseSign/addIntegral.do?" \
                                        "token=46f1bc4d-fcfc-4143-859b-277a73be32f8&" \
                                        "strLongitude=117.154393&" \
                                        "strApp=hexi&" \
                                        "strLatitude=39.105896&"


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
        #     "appUserTypeCode":"xxy"
        #
        # }
        # self.headers = {"Content-Type": "application/json"}
        # self.r = requests.post(url=self.url, json=self.data, headers=self.headers)

        #=============================================================\
        print(self.r)
        print(self.r.text)
        print(self.r.status_code)

        # 正则表达式提取数字返回值
        s=self.r.text
        print(re.findall(r"\d+\.?\d*", s))

        #  断言  200表示签到成功，424表示今天已签到
        if s == 200 :
            self.assertIn("200", self.r.text)
        else :
            self.assertIn("424", self.r.text)


if __name__ =="__main__":
        unittest.main()