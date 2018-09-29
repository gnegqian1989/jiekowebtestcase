#!usr/bin/python
#coding:utf-8

import called
def callback():
    print ("in callback")
def main():
    #called.test()
    called.test_call(callback)
    print ("in call.py")
main()