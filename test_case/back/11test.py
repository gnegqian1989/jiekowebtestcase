#!/usr/bin/python
#coading:utf-8

import requests
import json
import unittest


class MyTest(unittest.TestCase):  # 封装测试环境的初始化和还原的类
    def setUp(self):  # 放对数据可操作的代码，如对mysql、momgodb的初始化等,这里不对数据库进行操作！
        print("start test")
        pass

    def tearDown(self):  # 与setUp()相对
        print("end test")
        pass


class test_login_get(MyTest):  # 把这个接口封装一个类，下面的方法是具体的测试用例
    '''接口名称：获取资质'''  # 这个描述接口名称

    def test_login_get(self):
        '''测试用例1：哈哈'''  # 这个描述接口用例名称
        self.url = "https://fresh.weijingyuan.com.cn/JinMen/main/login.do?account=admin&psw=23698741&strApp=hexi"  # 请求url
        # self.headers = {"Cookie: JSESSIONID=A5600A9BE0BC24DEF719D267B241E3E9"}
        # # self.data ={
        #     "account" = "admin",
        #     "psw" = "23698741" ,
        #     "strApp" = "hexi"
        #     } # self.用在方法属性中，表示是该方法的属性，不会影响其他方法的属性。
        r = requests.post(url=self.url)
        return r.json()
        print (self.r.text)
        print (self.r.status_code)
        self.assertIn("true", self.r.text)  # 断言判断接口返回是否符合要求，可以写多个断言！


if __name__ == "__main__":
    unittest.main()