#!/usr/bin/python
#coding:utf-8

import requests

# r=requests.post(
#     url='http://m.cyw.com/index.php?m=api&c=cookie&a=setcity',
#     data={'cityId':438})
# print (r.json())


# r=requests.get(
#     url=r'https://fresh.weijingyuan.com.cn/JinMen/main/login.do?account=admin&psw=23698741&strApp=hexi')
#     # data={'cityId':438})
# print (r.json())


import unittest
from lesson1.demo1 import add

class MyTestCase(unittest.TestCase):
    def test_add(self):
        x=3
        y=4
        z=add(x,y)
        self.assertEqual(z, 7,'method add test failed')

if __name__ == '__main__':
    unittest.main()
