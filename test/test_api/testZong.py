# @Time    : 6/23/2020 7:49 PM
# @Author  : Yang Xiaobai
# @Email   : yangzhiyongtest@163.com
from datetime import datetime
import json

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


a = datetime.now()
print(a)
