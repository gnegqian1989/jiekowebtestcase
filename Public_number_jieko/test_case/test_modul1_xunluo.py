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

class test_startTrack(MyTest):
        '''测试接口:开始巡逻接口'''

        def test_startTrack(self):
            '''测试用例1：开始巡逻接口'''

            #        ==================get请求==================================

            self.url = (config.TestPlanUrl) + "/publics/hx/taskTrack/startTrack.do?" \
                                              "strAccount=13820559247&" \
                                              "token=9678d11a-33a1-4bb9-9b9d-3a93af491d1d&" \
                                              "strApp=hexi&" \
                                              "strTaskGuid=hexixunluo&"
            print(self.url)
            self.headers = {"Content-Type": "application/json"}

            self.r = requests.get(url=self.url)
class test_saveTrackPoint(MyTest):
    '''测试接口:保存巡逻数据接口'''

    def test_saveTrackPoint(self):
        '''测试用例1：保存巡逻数据接口'''

#        ==================get请求==================================

        self.url =(config.TestPlanUrl) +"/publics/hx/taskTrackPoint/saveTrackPoint.do?" \
                                         "strAccount=13820559247&" \
                                         "token=9678d11a-33a1-4bb9-9b9d-3a93af491d1d&" \
                                         "strApp=hexi&" \
                                         "strTrackGuid=6bbfd0f1-f2fa-4e45-9300-fa5ff24a96a9&" \
                                         "strDistance=1000&" \
                                         "strDuration=3600&" \
                                         "strSpeed=25&" \
                                         "strTaskGuid=hexixunluo&" \
                                         "strLongitude=117.160707&" \
                                         "strLatitude=39.121024&" \
                                         "strAddress=天津市南开区白堤路靠近天津市非物质文化遗产馆&"
        print(self.url)
        self.headers = {"Content-Type":"application/json"}

        self.r = requests.get(url = self.url)
class test_endTrack(MyTest):
    '''测试接口:结束巡逻接口'''

    def test_endTrack(self):
        '''测试用例1：结束巡逻接口'''

#        ==================get请求==================================

        self.url =(config.TestPlanUrl) +"/publics/hx/taskTrack/endTrack.do?" \
                                         "strAccount=13820559247&" \
                                         "token=dc10feb8-39c2-48ee-9850-9f51aed3df1c&" \
                                         "strApp=hexi&" \
                                         "strTaskGuid=hexixunluo&" \
                                         "strTrackGuid=a523ab23-9fa3-489b-afb9-36d64e408be2"
        print(self.url)
        self.headers = {"Content-Type":"application/json"}

        self.r = requests.get(url = self.url)
class test_queryTrackPointList(MyTest):
    '''测试接口：巡逻历史轨迹接口'''

    def test_queryTrackPointList(self):
        '''测试用例1：巡逻历史轨迹接口'''

#        ==================get请求==================================

        self.url =(config.TestPlanUrl) +"/publics/hx/taskTrackPoint/queryTrackPointList.do?" \
                                         "strAccount=13820559247&" \
                                         "strApp=hexi&" \
                                         "token=9678d11a-33a1-4bb9-9b9d-3a93af491d1d&" \
                                         "strTrackGuid=6bbfd0f1-f2fa-4e45-9300-fa5ff24a96a9&"
        print(self.url)
        self.headers = {"Content-Type":"application/json"}

        self.r = requests.get(url = self.url)
class test_queryTrackList(MyTest):
    '''测试接口：巡逻历史列表接口'''

    def test_queryTrackList(self):
        '''测试用例1：巡逻历史列表接口'''

#        ==================get请求==================================

        self.url =(config.TestPlanUrl) +"/publics/hx/taskTrack/queryTrackList.do?" \
                                         "strAccount=13820559247&" \
                                         "token=9678d11a-33a1-4bb9-9b9d-3a93af491d1d&" \
                                         "strApp=hexi&"
        print(self.url)
        self.headers = {"Content-Type":"application/json"}

        self.r = requests.get(url = self.url)

        print(self.r)
        print(self.r.text)
        print(self.r.status_code)
        self.assertIn("200",self.r.text)

if __name__ =="__main__":
        unittest.main()