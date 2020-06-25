# @Time    : 6/23/2020 7:49 PM
# @Author  : Yang Xiaobai
# @Email   : yangzhiyongtest@163.com
from datetime import datetime
import json

from utils.new_tools.excel_tool import DealExcelTool
from utils.new_tools.txt_tool import TxtTool


def historyTest():
    str = '{"isApp":"Y","isTransmit":{"tokenName":"[\'token\',\'token\']","transmitName":["brokerCode",{"valueKey":"brokerCode","getValuePath":"$.data.brokerCode"}]}}'
    strdic = json.loads(str)
    print(strdic['isTransmit']["transmitName"])


# isAppa='{"isApp":"Y","isTransmit":{"tokenName":"[\"token\",\"token\"]","transmitName":{"brokerCode":1 ,{"valueKey":"brokerCode","getValuePath":"$.data.brokerCode"}}}}'
# b=eval(a)
# print(b["isApp"])
def testDic():
    a = {"isApp": "Y", "isTransmit": {"tokenName": ["token", "token"], "transmitName": ["brokerCode",
                                                                                        {"valueKey": "brokerCode",
                                                                                         "getValuePath": "$.data.brokerCode"}]}}
    print(a["isTransmit"]["transmitName"])
    
    a = json.dumps(a)
    print(a)
    print(type(a))
    b = json.loads(a)
    print(b)
    print(type(b))
    c = json.dumps(b)
    d = json.dumps(c)
    e = json.dumps(d)
    f = json.loads(e)
    print(c)
    print(type(c))
    print(d)
    print(type(d))
    print(e)
    print(type(e))
    print(f)
    print(type(f))

    a = r"D:\zhy\haoshenghuo\autoproject\hopsapi_test\utils\api_tools\url_classfication.py"
    print(a)

def paraTest2():
    headers = {'brokerPhone': '15718868478', 'clientId': '77a8a4b9e5ba1c9b6a21ca1b839c3581', 'password': '123456'}
    tfn = DealExcelTool().getTempFileName()
    headers = json.dumps(headers, ensure_ascii=False)
    TxtTool().writeTxt(tfn, headers)
    result = TxtTool().readTxt(tfn)
    print(result)

def paraTest2():
    headers = {'brokerPhone': '15718868478', 'clientId': '77a8a4b9e5ba1c9b6a21ca1b839c3581', 'password': '123456'}
    headers['password']='098765'
    headers['defname']='wangxiaowang'
    print(headers)

paraTest2()