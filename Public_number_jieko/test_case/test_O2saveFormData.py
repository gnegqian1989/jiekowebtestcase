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
class test_saveFormData(MyTest):
    '''测试接口：保存表单录入'''

    def test_saveFormData(self):
        '''测试用例1：保存表单录入'''

#        ==================get请求==================================

        # self.url =(config.TestPlanUrl) +"/publics/hx/infoUserMessage/userMessage.do?" \
        #                                  "strAccount=13820559247&" \
        #                                  "token=9678d11a-33a1-4bb9-9b9d-3a93af491d1d&" \
        #                                  "strApp=hexi&" \
        #                                  "isRead=0&" \
        #                                  "intPageSize=10&" \
        #                                  "searchKey=1&" \
        #
        # print(self.url)
        # self.headers = {"Content-Type":"application/json"}
        #
        # self.r = requests.get(url = self.url)
        # return self.r.json()

#        ==================post请求==================================

        self.url = (config.TestPlanUrl) + "/publics/hx/form/saveFormData.do?"
        self.data = {
                "appUserTypeCode": "xxy",
                "dtFindTime": "2018-09-27 11:56",
                "intSource": "1",
                "strApp": "hexi",
                "strContent": "好喜欢这",
                "multimidea": "{'media_image':'[]','media_video':'','media_voice':''}",
                "strFindPlace": "{'adcode':'120104','latitude':39.104709625244141,'longtitude':117.15407562255859,'address':'天津市南开区科研东路13号'}",
                "strLabel": "9d799bbd-bdb9-440a-9e6c-4234ca5c2650",
                "strReportPlace": "{'adcode':'120104','latitude':39.104709625244141,'longtitude':117.15407562255859,'address':'天津市南开区科研东路13号'}",
                "strTitle": "白血病细胞",
                "strTypeGuid": "031e3a3e-a233-4df1-b1ba-bddc4f07866d",
                "token": "b5c05e03-c5b5-4246-b00b-154c0687dcb1",
                "version": "2.0.1"
            }

            # "strAccount":"13820559247",
            # "token":"9678d11a-33a1-4bb9-9b9d-3a93af491d1d",
            # "strApp":"hexi",
            # "strTypeGuid":"031e3a3e-a233-4df1-b1ba-bddc4f07855d&",
            # "strAttachUrl":"[{'strFilePath': 'aaaaaaa'}]",
            # "appUserTypeCode":"xxy"

        self.headers = {"Content-Type": "application/json"}
        self.r = requests.post(url=self.url, json=self.data, headers=self.headers)

        #=============================================================
        print(self.r)
        print(self.r.text)
        print(self.r.status_code)
        self.assertIn("200",self.r.text)

if __name__ =="__main__":
        unittest.main()