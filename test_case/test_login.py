#!/usr/bin/python
#coding:utf-8

# 人力情报 pc端登录接口  https://fresh.weijingyuan.com.cn/JinMen/main/login.do?account=admin&psw=23698741&strApp=hexi

import requests
import json

def test_login():
    url = "https://fresh.weijingyuan.com.cn/JinMen/main/login.do?account=admin&psw=23698741&strApp=hexi"
    # headers = {"Cookie: JSESSIONID=A5600A9BE0BC24DEF719D267B241E3E9"}

    r = requests.get(url = url)
    repones = r.text
    print(r.text)
    print(r.status_code)

if __name__ =="__main__":
    test_login()

