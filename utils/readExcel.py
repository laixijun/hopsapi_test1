#!/usr/bin/python
# coding=utf-8
import xlrd
import os


def cell_value(fp, sheet_name, row, col):
    """
    获取单元格的值
    """
    test_data = xlrd.open_workbook(fp)
    sheet_name = test_data.sheet_by_name(sheet_name)
    return sheet_name.cell_value(row-1, col-1)


def row_value(fp, sheet_name, case_name):
    """
    获取整行的值
    """
    test_data = xlrd.open_workbook(fp, 'br')
    sheet_name = test_data.sheet_by_name('%s' % sheet_name)
    cases = sheet_name.col_values(0)
    for case_i in range(len(cases)):
        if cases[case_i] == case_name:
            # print(sheet_name.row_values(case_i))
            row_value = sheet_name.row_values(case_i)
            for i in range(0, row_value.__len__()):
                if type(row_value[i]) == float:
                    row_value[i] = int(row_value[i])
            # print(row_value)
            return row_value


def col_value(fp, sheet_name, col):
    """
    获取整列的值
    """
    test_data = xlrd.open_workbook(fp)
    sheet_name = test_data.sheet_by_name('%s' % sheet_name)
    return sheet_name.col_values(col - 1)


def excel_path(filename):
    proj_path = str(os.path.dirname(__file__).split('/utils')[0])
    # proj_path = str(os.path.dirname(__file__))
    print(proj_path)
    proj_path = proj_path.replace('\\', '/')
    excel_path = proj_path + '/testcase/' + filename
    print(excel_path)
    return excel_path


def main():
    file = excel_path('test_datas.xlsx')
    rowvalue = row_value(file, 'cms_login', 'login_Sucess')
    for str in rowvalue:
        print(str)


if __name__ == '__main__':
    main()
