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
class test_initIndexData(MyTest):
    '''测试接口：首页统计接口'''

    def test_initIndexData(self):
        '''测试用例1：首页统计接口'''

#        ==================get请求==================================

        self.url =(config.TestPlanUrl) +"/publics/hx/login/initIndexData.do?" \
                                         "strAccount=13820559247&" \
                                         "token=9678d11a-33a1-4bb9-9b9d-3a93af491d1d&" \
                                         "strApp=hexi&" \
                                         "appUserTypeCode=xxy"

        print(self.url)
        self.headers = {"Content-Type":"application/json"}

        self.r = requests.get(url = self.url)
        # return self.r.json()

#        ==================post请求==================================

        # self.url = (config.TestPlanUrl) + "/publics/hx/form/saveFormData.do?"
        # self.data = {
        #     "strAccount":"13820559247",
        #     "token":"9678d11a-33a1-4bb9-9b9d-3a93af491d1d",
        #     "strApp":"hexi",
        #     "strTypeGuid":"031e3a3e-a233-4df1-b1ba-bddc4f07855d&",
        #     "strAttachUrl":"[{'strFilePath': 'aaaaaaa'}]"
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