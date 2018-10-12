#!usr/bin/python
#coding:utf-8

import requests
from lxml import etree
import json
import requests
import json
import unittest
import json

import sys
sys.path.append(r'D:\shuo-huahua\Public_number_jieko_0919\Public_number_jieko\config')
import config

class MyTest(unittest.TestCase):
    def setUp(self):
        print('start test')
        pass
    def tearDown(self):
        print('end test')
        pass

class test_startTrack(MyTest):

    def test_startTrack(self):
        href_lists = []
        self.url = (config.TestPlanUrl) + "/publics/hx/taskTrack/startTrack.do?" \
                                          "strAccount=13820559247&" \
                                          "token=9678d11a-33a1-4bb9-9b9d-3a93af491d1d&" \
                                          "strApp=hexi&" \
                                          "strTaskGuid=hexixunluo&"
        print(self.url)
        self.headers = {"Content-Type": "application/json"}
        self.r = requests.get(url=self.url)
        # print(self.r)
        a = self.r.text
        # print(a)
        print(self.r.status_code)
        self.assertIn("200", a)

        # json 提取返回结果
        hjson = json.loads(a)
        # strTrackGuid1 = hjson['resultData']
        strTrackGuid  = hjson['resultData']['strTrackGuid']
        print(strTrackGuid)
        href_lists.append(strTrackGuid)
        return href_lists
        print(href_lists)

    def test_saveTrackPoint(self, href_lists):
        print(href_lists)
        # list转化为字符串
        a = ','.join(href_lists)
        print(a)

        url_list = []

        self.url = (config.TestPlanUrl) + '/publics/hx/taskTrackPoint/saveTrackPoint.do?' \
                                                  'strAccount=13820559247&' \
                                                  'token=9678d11a-33a1-4bb9-9b9d-3a93af491d1d&' \
                                                  'strApp=hexi&' \
                                                  'strDistance=1000&' \
                                                  'strDuration=3600&' \
                                                  'strSpeed=25&' \
                                                  'strTaskGuid=hexixunluo&' \
                                                  'strLongitude=117.160707&' \
                                                  'strLatitude=39.121024&' \
                                                  'strAddress=天津市南开区白堤路靠近天津市非物质文化遗产馆&' \
                                                  'strTrackGuid={}'.format(a)
        url_list.append(self.url)
        # print(i)
        print(self.url)
        return url_list

    def parse_url(self, url):
            headers = {"Content-Type": "application/json"}
            r = requests.get(url=url)
            print(r)
            print(r.text)
            print(r.status_code)
            self.assertIn("200", r.text)

    def run(self):
        """run函数实现主逻辑"""
        id_list = self.test_startTrack()
        url_list = self.test_saveTrackPoint(id_list)
        for url in url_list:
            html = self.parse_url(url)



if __name__ == '__main__':
     tianyuan = test_startTrack()
     tianyuan.run()



# if __name__ == "__main__":
#     # unittest.main()
#     test_startTrack.test_startTrack()
#     test_startTrack.test_saveTrackPoint()