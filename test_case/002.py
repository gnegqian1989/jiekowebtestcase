# #!/usr/bin/python
# #coding:utf-8
#
# import requests
# import json
#
# def test_login():
#     # url = "https://fresh.weijingyuan.com.cn/JinMen/android/login/loginServerPath.do?"
#
#     url = "https://fresh.weijingyuan.com.cn/JinMen/android/user/registUser.do?"
#     # headers = {"Cookie: JSESSIONID=A5600A9BE0BC24DEF719D267B241E3E9"}
#     data ={
#          "strAccount":"15022744490",
# 	     "strApp":"hexi",
# 	     "strMobile":"15022744490",
# 	     "strPasswd":"11111111",
# 	     "strRePasswd":"11111111",
#     }
#
#     r = requests.get(url = url)
#     repones = r.text
#     print(r.text)
#     print(r.status_code)
#
# if __name__ =="__main__":
#     test_login()