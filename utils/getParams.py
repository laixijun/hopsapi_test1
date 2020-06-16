#!/usr/bin/python
# coding=utf-8
from utils.readExcel import *
import json
from utils.logger import Log
from json.decoder import JSONDecodeError
# fp = '/Users/rasule/PycharmProjects/hopsapi_test/testcase/test_datas.xlsx'
fp = excel_path('test_datas.xlsx')
logger = Log(logger='get_params').get_log()


def get_params(sheet, case):
    """
    获取请求参数
    :param sheet: sheet name
    :param case: 用例名
    :return:
    """
    index = 0
    # 获取当前用例所在行下标
    col_case = col_value(fp, sheet, 1)
    for i in range(len(col_case)):
        if col_case[i] == case:
            index = i
            break
    params = cell_value(fp, sheet, index+1, 3)
    # print(params)
    # print(type(params))
    # if type(params) == str or type(params) == bytes or type(params) == bytearray:
    try:
        params = json.loads(params)
    finally:
        return params


def get_req_params(sheet, case):
    """
    获取请求参数
    :param sheet: sheet name
    :param case: 用例名
    :return:
    """
    index = 0
    param_key = row_value(fp, sheet, 'case_name')
    param_value = row_value(fp, sheet, case)
    # 获取 result 列的下标
    for i in range(len(param_key)):
        # if param_key[i] == 'Response':
        if param_key[i] == 'result':
            index = i
            break
    params = dict()
    for key_i in range(2, index):
        # if param_key[key_i] == 'password':
        #     params['password'] = Encryption().aspire_aes_crypt(param_value[key_i])
        # elif param_key[key_i] in ('user_id', 'teacher_id') and param_value[key_i] == 'uid_from_tb_user':
        #     params[param_key[key_i]] = DB().execute_sql('select', cf.get('SQL', 'sel_tb_user'))[0][0]
        # else:
            params[param_key[key_i]] = param_value[key_i]
    # params['sign'] = Encryption().sign(params)
    return params


def get_resp_params(sheet, case, resp_key):
    """
    获取响应参数
    :param resp_key: 响应名
    :param sheet: sheet name
    :param case: 用例名
    :return:
    """
    index = 0
    param_key = row_value(fp, sheet, 'case_name')
    param_value = row_value(fp, sheet, case)
    for i in range(len(param_key)):
        if param_key[i] == resp_key:
            index = i
            break
    return param_value[index]


def get_url(sheet, case):
    """
    获取响应参数
    :param url_key: 字段名
    :param sheet: sheet name
    :param case: 用例名
    :return:
    """
    index = 0
    param_key = row_value(fp, sheet, 'case_name')
    param_value = row_value(fp, sheet, case)
    # 获取 url 列的下标
    for i in range(len(param_key)):
        if param_key[i] == 'url':
            index = i
            break
    return param_value[index]


if __name__ == '__main__':

    # req = get_req_params('cms_login', 'login_Sucess')
    # resp_c = get_resp_params('cms_login', 'login_Sucess', 'code')
    # resp_m = get_resp_params('cms_login', 'login_Sucess', 'msg')
    # print(req)
    # print(resp_c, resp_m)
    # url = get_url('cms_login', 'login_Sucess')
    # print(url)
    a = get_params('members', 'vipBeyRecords')
    print(a)
    print(type(a))
