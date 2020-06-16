#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2019/6/14 13:43
# @Author  : vivid
# @FileName: ExcelUtil.py
# @Software: PyCharm
# @email    ：331597811@QQ.com
import xlsxwriter
import xlrd
import re
from automation.util.RandomUtil import TestRamdom
from automation.util.SystemOsUtil import SystemOs
class xlsxoper():
    """
    操作excel文件,文件写入即覆盖，不支持追加操作
    """
    def __init__(self,path):
        self.path = path
    def writeXLS(self,headings,data=None,datanums=20,sheet1='Sheet1'):
        """
        对文件是否存在进行判断,当文件不存在时自动创建文件
        :param headings:    #headings = ['Number', 'testA', 'testB']
        :param datanums:    默认循环次数，如果数据为None将循环20次
        :param sheet1:      页表
        :param data:
        #42-51行 ：判断是否采用随机数操作写入文件
        :return:
        """
        testos = SystemOs()
        if testos.is_file(self.path):
            try:
                workbook = xlsxwriter.Workbook(self.path)
                worksheet = workbook.add_worksheet(sheet1)
                # data = [
                #     ['2017-9-1', '2017-9-2', '2017-9-3', '2017-9-4', '2017-9-5', '2017-9-6'],
                #     [10, 40, 50, 20, 10, 50]
                # ]
                # worksheet.write_row('A1', headings)
                # worksheet.write_column('A2', data[0])
                # worksheet.write_column('B2', data[1])
                # worksheet.write_column('C2', data[2])
                if data is None:
                    data=[]
                    for j in range(len(headings)):
                        lists=[]
                        for i in range(datanums):
                            trandom = TestRamdom()
                            lists.append(trandom.RandomTest())
                        data.append(lists)
                else:
                    pass

                worksheet.write_row('A1', headings)
                column=[
                        'A2','B2','C2','D2','E2','F2',
                        'G2','H2','I2','J2','K2','L2',
                        'M2','N2','O2','P2','Q2','R2','S2',
                        'T2','U2','V2','W2','X2','Y2','Z2',
                        ]
                for i in range(len(headings)):
                    #print(data[i])
                    worksheet.write_column(column[i], data[i])
            except Exception as e:
                print(e)
            finally:
                workbook.close()
        else:
            msg = "文件不存在,创建新excel文件"
            import time
            time.sleep(5)
            try:
                # 新建一个excel文件
                workbook = xlsxwriter.Workbook(self.path)
                # 创建一个worksheet
                sheet = sheet1
                worksheet = workbook.add_worksheet(sheet)
                title = headings
                #向A1单元格写入title列表，列表中每一个字段对应一个内容
                worksheet.write_row(0,0,title)
                #关闭文件
                workbook.close()
                #重新写入文件
                datas = data
                datasnum = datanums
                self.writeXLS(title,datas,datasnum,sheet)
            except Exception as e:
                msg = "创建文件失败！"

            return msg

    def readerXLS(self,sheet1='Sheet1'):
        """
        将文件中的所有数据读取出来，放入list中，返回数据[['a','b'],['c','d']]
        :param sheet1: 页表
        :return:
        """
        testos = SystemOs()
        if testos.is_file(self.path):
            workbook = xlrd.open_workbook(self.path)
            booksheet = workbook.sheet_by_name(sheet1)
            # print(booksheet.nrows)
            # print(booksheet.ncols)
            p = list()
            for row in range(booksheet.nrows):
                row_data = []
                for col in range(booksheet.ncols):
                    cel = booksheet.cell(row, col)
                    val = cel.value
                    try:
                        val = cel.value
                        val = re.sub(r'\s+', '', val)
                    except:
                        pass
                    if type(val) == float:
                        val = int(val)
                    else:
                        val = str(val)
                    row_data.append(val)
                p.append(row_data)
            return p
        else:
            msg = "文件不存在"
            return msg


    def cell_value(fp, sheet_name, row, col):
        """
        @Author  : ranshuang
        获取单元格的值，获取某一行某一列的值
        """
        test_data = xlrd.open_workbook(fp)
        sheet_name = test_data.sheet_by_name(sheet_name)
        return sheet_name.cell_value(row-1, col-1)


    def row_value(fp, sheet_name, case_name):
        """
        @Author  : ranshuang
        通过第一列信息内容，获取整行的值
        """
        test_data = xlrd.open_workbook(fp, 'br')
        sheet_name = test_data.sheet_by_name('%s' % sheet_name)
        cases = sheet_name.col_values(0)
        for case_i in range(len(cases)):
            if cases[case_i] == case_name:
                row_value = sheet_name.row_values(case_i)
                for i in range(0, row_value.__len__()):
                    if type(row_value[i]) == float:
                        row_value[i] = int(row_value[i])
                return row_value


    def col_value(fp, sheet_name, col):
        """
        @Author  : ranshuang
        指定列数，获取列信息，列数从1开始
        """
        test_data = xlrd.open_workbook(fp)
        sheet_name = test_data.sheet_by_name('%s' % sheet_name)
        return sheet_name.col_values(col - 1)

if __name__=='__main__':
    #DestroyerRobot/automation/datas_template/test_data.xlsx|C:\Users\vivid\PycharmProjects\untitled\DestroyerRobot\automation\datas_template\test_data.xlsx
    file_addrec = 'C:\\Users\\vivid\\PycharmProjects\\untitled\\DestroyerRobot\\automation\\datas_template\\test_data.xlsx'
    xls=xlsxoper(file_addrec)
    # p=xls.writeXLS('test_data')
    # print(p)
    # for i in p:
    #     print(i)
    #     for j in i:
    #         #print(j)
    #         pass

#    xls.do_excel()

    # data = [
    #     ['2017-9-1', '2017-9-2', '2017-9-3', '2017-9-4', '2017-9-5', '2017-9-6'],
    #     [10, 40, 50, 20, 10, 1000]
    # ]
    # p=xls.writeXLS(['序列号', '兑换码'],data)
    # print(p)

    ls=xls.readerXLS("test_data")
    print(ls)




