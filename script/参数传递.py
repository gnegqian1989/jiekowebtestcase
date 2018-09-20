#!/usr/bin/python
#coding:utf-8

import requests

# def login():
#     r= requests.post(url = 'https://fresh.weijingyuan.com.cn/JinMen/main/login.do?account=admin&psw=23698741&strApp=hexi',
#                      )
#     # print (r.status_code)
#     # print (r.text)
#     return r.cookies.get_dict()
# print (login())
# if __name__ =="__main__":
#     login()


def getSession():
    # 登陆后获取session
    r = requests.get(url = "https://fresh.weijingyuan.com.cn/JinMen/main/login.do?account=admin&psw=23698741&strApp=hexi")
    # 获取cookies
    return r.cookies.get_dict()
a = getSession()
print (a)
def test_access_datas():
    # 测试返回数据
    r = requests.get(
        url = 'https://fresh.weijingyuan.com.cn/JinMen/pc/information/queryCollectList.do?',
        data ={
            "strApp": "hexi", "token": "1000000",
            "strTypeGuid": "b7aea750-d42f-4c09-b06b-907d4b74a311,6c9f83c2-593b-4c0d-bb8a-74eb0bc787de,031e3a3e-a233-4df1-b1ba-bddc4f07844d",
            "strCreatorName": "", "strPoliceName": "", "strUnitGuid": "", "strQueryType": "report",
            "strType": "collect", "intPageIndex": 1, "intPageSize": 10},

        cookies = {'JSESSIONID': 'DAF2EC76DFD0C82B9F42ADC50457C2FF'})
    print (r.status_code)
    print(r.json)

if __name__ == '__main__':
    test_access_datas()

    # {
    # "intPageIndex": 1,
    #  "intPageSize": 10,
    #  "strApp": "hexi",
    #  "strQueryType": "report",
    #  "strType": "collect",
    #  "strTypeGuid": "b7aea750-d42f-4c09-b06b-907d4b74a311,6c9f83c2-593b-4c0d-bb8a-74eb0bc787de,031e3a3e-a233-4df1-b1ba-bddc4f07844d",
    #  "token": "1000000"
    #  },