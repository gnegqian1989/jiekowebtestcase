#!usr/bin/python
#coding:utf-8

import requests
from lxml import etree
import json


class TianYuan:

    def __init__(self):
       self.url = "http://www.tylaw.com.cn/CN/Team.aspx"
       self.headers ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
                     }
    def get_href(self):

        href_lists = []

            response = requests.post(self.url, data=tempdata, headers=self.headers)
             # 请求一次后currentPage＋１
            tempdata['currentPage'] += 1

            # 获取响应对象

            r = response.content.decode()
            h = etree.HTML(r)

            # print (r)
            # print (h)

             # 获取href
            href_list = h.xpath('//h3/a/@href')
            href_lists.append(href_list)
            return href_lists
            # print (href_list)

    def get_url_list(self, href_lists):
       print (href_lists)
       url_list = []
       for href_list in href_lists:
           for i in href_list:
            url = "http://www.tylaw.com.cn/CN/{}".format(i)
            url_list.append(url)
            print (i)
            print(url)
           return url_list


    def parse_url(self, url):
       response = requests.get(url, headers=self.headers)
       return etree.HTML(response.content.decode())



    def run(self):
        """run函数实现主逻辑"""
        id_list = self.get_href()
        url_list = self.get_url_list(id_list)
        for url in url_list:
            html = self.parse_url(url)
            content_list = self.get_content_list(html)
            self.save_content(content_list)

if __name__ == '__main__':
     tianyuan = TianYuan()
     tianyuan.run()

