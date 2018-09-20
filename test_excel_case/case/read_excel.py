#!/usr/bin/python
#coding:utf-8

import xlrd

class readExcel(object):
    def __init__(self,path):
        self.path = path

    @property
    def getsheet(self):
        #获取索引
        xl = xlrd.open_workbook(self.path)
        sheet = xl.sheet_by_index(1)
        # 打印所有sheet名字
        print(xl.sheet_names())
        #打印第3行第4列
        print (sheet.cell_value(2,3))
        return sheet

    @property
    def getRow(self):
        #获取行数
        row = self.getsheet.nrows
        return row

    @property
    def getcol(self):
        #获取列数
        row = self.getsheet.nrows
        return row

    #以下分别获取每一列的数值
    @property
    def getId(self):
        TestId = []
        for i in range(1,self.getRows):
            TestId.append(self.getsheet.cell_value(i,0))
        #print (TestName)
        return TestId

    @property
    def getName(self):
        TestName = []
        for i in range(1,self.getRows):
            TestName.append(self.getSheet.cell_value(i,1))
        #print(TestName)
        return TestName

    @property
    def getData(self):
        TestData = []
        for i in range(1,self.getRows):
            TestData.append(self.getsheet.cell_value(i,2))
        return TestData

    @property
    def getUrl(self):
        TestUrl = []
        for i in range(1,self.getRows):
            TestUrl.append(self.getsheet.cell_value(i,3))
        return TestUrl

    @property
    def getMethod(self):
        TestMethod = []
        for i in range(1,self.getRows):
            TestMethod.append(self.getsheet.cell_value(i,4))
        return TestMethod

    @property
    def getStatusCode(self):
        TestUid = []
        for i in range(1,self.getRows):
            TestUid.append(self.getsheet.getsheet.cell_value(i,5))
        return TestUid

    @property
    def getCode(self):
        TestCode = []
        for i in range(1,self.getRows):
            TestCode.append(self.getSheet.cell_value(i,6))
        return TestCode


