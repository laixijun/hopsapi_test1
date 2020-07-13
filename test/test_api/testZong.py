# @Time    : 6/23/2020 7:49 PM
# @Author  : Yang Xiaobai
# @Email   : yangzhiyongtest@163.com
from datetime import datetime
import json

import jsonpath

from pyapi.cms_login import CmsLogin
from test.test_api.httpTestTool import httpRequests
from utils.config_tool.request_header import RequestHeader
from utils.new_tools.common_tool import Common
from utils.new_tools.excel_tool import DealExcelTool, ExcelTool
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

def test100():
    b=DealExcelTool().getTestFileName()
    a=ExcelTool(excelFile=b,sheetName='testSheet').get_row_value(row=2)
    a= a[7]

    # a=json.dumps(a)
    # print(type(a))
    # print(a)
    a = json.dumps(a)
    a = json.loads(a)
    a = json.loads(a)


    # a=jsonpath.jsonpath(a,'$.isTransmit')
    print(type(a))
    print(a)

    # a = json.loads(a)
    # print(type(a))
    # print(a)

def test101():
    headers = '{"brokerPhone": "15718868478", "clientId": "77a8a4b9e5ba1c9b6a21ca1b839c3581", "password": "123456"}'
    # headers = json.dumps(headers)
    headers = json.loads(headers)
    print(headers,type(headers))
    a={"b":"$.brokerPhone"}
    c=jsonpath.jsonpath(headers,a["b"])
    d = jsonpath.jsonpath(headers, "$..clientId")
    print(c,d)

def test102():
    info ={'data': {'id': 163295, 'brokerCode': '866fce5e-95cd-11ea-ac1a-000c29af0c0c', 'brokerName': '羊小白经纪公司1',
              'brokerType': '5', 'brokerPhone': '15718868478', 'brokerCity': '110100', 'brokerEmail': '',
              'brokerWeixin': '', 'score': 0, 'level': 4, 'password': 'e10adc3949ba59abbe56e057f20f883e',
              'createTime': '2020-05-14', 'easylifeSalary': 0.0, 'delStatus': 0, 'checkStatus': 1,
              'token': '6ee017f6-4a8c-4745-8c62-52d518ad2387', 'brokerCityName': '北京市',
              'clientId': '77a8a4b9e5ba1c9b6a21ca1b839c3581', 'lastLoginTime': '2020-06-27', 'common': 0,
              'house': 100.0, 'insurance': 100.0, 'property': 100.0}, 'status': {'msg': '成功', 'code': '1000'}}

    getitem={"transmitName": [["brokerCode", {"valueKey": "brokerCode", "getValuePath": "$.data.brokerCode"}],
                     ["token", {"valueKey": "token", "getValuePath": "$.data.token"}],
                     ["brokerCity", {"valueKey": "brokerCity", "getValuePath": "$.data.brokerCity"}]]}

    info = json.dumps(info)
    info = json.loads(info)
    get01 = jsonpath.jsonpath(info,getitem["transmitName"][2][1]["getValuePath"])
    print(get01)

# def test103():
#     info = {'data': [{'devId': '11417', 'mTotalPrice': '0', 'packageCounts': 10, 'address': '', 'Time': '2020/04/01-2022/04/01', 'contentPhone': '13200000000', 'shareImg': 1, 'contentName': '联系人2', 'imgUrl': '', 'averPrice': '0.0', 'propertyType': '', 'name': '测试', 'share': 'https://tbroker.lifeat.cn/easylife/', 'packageName': '四个节点+奖励（听说这个是最大的）', 'projectId': 11414, 'status': '', 'hiddenPhone': '1'}, {'devId': '11392', 'mTotalPrice': '0', 'packageCounts': 0, 'address': '', 'Time': '2020/06/17-2020/06/30', 'contentPhone': '13123447899', 'shareImg': 0, 'contentName': '测试', 'imgUrl': '', 'averPrice': '0.0', 'propertyType': '', 'name': '大股东法国队', 'share': 'https://tbroker.lifeat.cn/easylife/', 'packageName': '', 'projectId': 10881, 'status': '', 'hiddenPhone': '0'}, {'devId': '11322', 'mTotalPrice': '0', 'packageCounts': 16, 'address': '朝阳区双井自动化专用楼盘', 'Time': '2019/12/19-2022/12/31', 'contentPhone': '13100000000', 'shareImg': 1, 'contentName': '专用', 'imgUrl': '', 'averPrice': '10000.0', 'propertyType': '住宅', 'name': '自动化专用楼盘-北京', 'share': 'https://tbroker.lifeat.cn/easylife/', 'packageName': '四个节点+奖励（听说这个是最大的）', 'projectId': 11317, 'status': '', 'hiddenPhone': '0'}, {'devId': '11304', 'mTotalPrice': '0', 'packageCounts': 35, 'address': '朝阳区双井双井', 'Time': '2019/12/06-2021/12/02', 'contentPhone': '13000000000', 'shareImg': 1, 'contentName': '测试', 'imgUrl': 'http://kfcdn.lifeat.cn/Fk54EBjUDzTVqVWasw92ZmIm5Dmb', 'averPrice': '100000.0', 'propertyType': '住宅', 'name': '陈芳霞测试楼盘2', 'share': 'https://tbroker.lifeat.cn/easylife/', 'packageName': '四个节点+奖励（听说这个是最大的）', 'projectId': 11264, 'status': '', 'hiddenPhone': '1'}, {'devId': '11244', 'mTotalPrice': '0', 'packageCounts': 23, 'address': '424554454545', 'Time': '2019/11/16-2023/11/23', 'contentPhone': '15678974815', 'shareImg': 1, 'contentName': 'fag', 'imgUrl': 'http://kfcdn.lifeat.cn/FqTpgEpNwlgW_rmPiX-jk7bFUrDJ', 'averPrice': '100.0', 'propertyType': '住宅', 'name': '森林半岛', 'share': 'https://tbroker.lifeat.cn/easylife/', 'packageName': '四个节点+奖励（听说这个是最大的）', 'projectId': 11087, 'status': '', 'hiddenPhone': '0'}, {'devId': '11202', 'mTotalPrice': '0', 'packageCounts': 14, 'address': '东城区121212', 'Time': '2019/09/19-2021/09/16', 'contentPhone': '15603904587', 'shareImg': 0, 'contentName': 'd', 'imgUrl': 'http://kfcdn.lifeat.cn/FvCb1VeWO5etULtRpZsqXnmVrWu9', 'averPrice': '100.0', 'propertyType': '别墅', 'name': '维多利亚港', 'share': 'https://tbroker.lifeat.cn/easylife/', 'packageName': '四个节点+奖励（听说这个是最大的）', 'projectId': 11201, 'status': '', 'hiddenPhone': '0'}, {'devId': '11094', 'mTotalPrice': '0', 'packageCounts': 20, 'address': '424554454545', 'Time': '2019/09/11-2022/09/09', 'contentPhone': '15678974815', 'shareImg': 1, 'contentName': 'fag', 'imgUrl': 'http://kfcdn.lifeat.cn/FqTpgEpNwlgW_rmPiX-jk7bFUrDJ', 'averPrice': '100.0', 'propertyType': '住宅', 'name': '未央宫', 'share': 'https://tbroker.lifeat.cn/easylife/', 'packageName': '四个节点+奖励（听说这个是最大的）', 'projectId': 11087, 'status': '', 'hiddenPhone': '0'}, {'devId': '11078', 'mTotalPrice': '0', 'packageCounts': 11, 'address': '朝阳区333333', 'Time': '2019/09/11-2022/10/01', 'contentPhone': '15789789444', 'shareImg': 0, 'contentName': 'sdhg', 'imgUrl': '', 'averPrice': '100.0', 'propertyType': '住宅', 'name': 'KP指标I考核', 'share': 'https://tbroker.lifeat.cn/easylife/', 'packageName': '四个节点+奖励（听说这个是最大的）', 'projectId': 11070, 'status': '', 'hiddenPhone': '0'}, {'devId': '11056', 'mTotalPrice': '0', 'packageCounts': 10, 'address': '东城区222', 'Time': '2019/09/10-2022/09/15', 'contentPhone': '13911564453', 'shareImg': 0, 'contentName': '王鹏', 'imgUrl': '', 'averPrice': '0.0', 'propertyType': '住宅', 'name': '外拓1', 'share': 'https://tbroker.lifeat.cn/easylife/', 'packageName': '四个节点+奖励（听说这个是最大的）', 'projectId': 11038, 'status': '', 'hiddenPhone': '0'}, {'devId': '11032', 'mTotalPrice': '0', 'packageCounts': 10, 'address': '朝阳区九龙山阳光财富大厦', 'Time': '2019/09/09-2023/10/13', 'contentPhone': '15801342357', 'shareImg': 0, 'contentName': '韩启川', 'imgUrl': '', 'averPrice': '50000.0', 'propertyType': '住宅', 'name': '外拓楼盘', 'share': 'https://tbroker.lifeat.cn/easylife/', 'packageName': '四个节点+奖励（听说这个是最大的）', 'projectId': 1308, 'status': '', 'hiddenPhone': '0'}], 'status': {'msg': '成功', 'code': '1000'}}
#     getitem = {"isApp":"Y","isTransmit":{"tokenName":[["token","token"],["brokerCode","brokerCode"]],"transmitName":[["estateProjectDevName",{"valueKey":"name","getValuePath":"$.data[?(@devId=\\'10881\\')].name"}],["estateProjectDevId",{"valueKey":"devId","getValuePath":"$.data[?(@name=\\'大股东法国队\\')].devId"}]]}}
#     get01 = jsonpath.jsonpath(info, getitem["isTransmit"]["transmitName"][1][1]["getValuePath"])
#     get02 = jsonpath.jsonpath(info, "$.data[0].devId")
#     print(get02)

def getValueFalse(lst,itemKey,itemValue,needKey):
    for i in lst:
        if i[itemKey] == itemValue:
            return i[needKey]

def test104():
    a = "1-2-3-4"
    a=a.split("-")
    print(a)

def test105():
    a ={'$.status.code': '1000'}
    b =jsonpath.jsonpath(a,"$")
    print(b)
    
def test106():
    a='{"$.status.code":"1000","estateProjectDevId":{"jsonExpectValue":"11392","getValuePath":{"threeListAll":"$.data","threeList":"name-大股东法国队-devId"}}}'
    a = json.loads(a)
    print("啊")
    
def test107():
    a= "https://docs.qq.com/sh{eet/DQk1Zc0Z0bXhSY2JT?tab=kumid1"
    if "{" in a:
        print("ok")
        
def test108():
    a_dict = {'$.status.code': '1000'}
    for k, v in a_dict.items():
        print(k, v)
        
def test109():
    ifnotest ='{"code":200,"msg":"成功","data":{"token":"eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMTU3MTg4Njg0NzgiLCJpYXQiOjE1OTM1OTQ4MzgsImV4cCI6MTU5MzYwMjAzOCwibmJmIjoxNTkzNTk0ODM4fQ.aYkCGFtqTR_Llanf0FwGJdY-R5RUCXTcMiroAaGWNoM","applicationToken":"eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiOTUxIiwiaWF0IjoxNTkzNTk0ODM4LCJleHAiOjE1OTM2MDIwMzgsIm5iZiI6MTU5MzU5NDgzOH0.5hnmlyab5a_LEVPCDysZuemsEFDj7ICRbmYe_77rXag","isDirectLogin":true,"tenants":null,"apps":[{"id":3,"appName":"新运营端管理系统","appIcon":"","appUrl":"http://localhost:8089/,https://ndcms.lifeat.cn:45788/cms/,https://ntcms.lifeat.cn:45788/cms/,https://nhcms.lifeat.cn:45788/cms/,https://hb-ncms.lifeat.cn/cms/"},{"id":0,"appName":"权限系统","appIcon":"https://kf-pms-cdn.hopsontong.com/1585129410411-10947/cms/permission-system-logo-258x86.png","appUrl":"https://uat-pms-tenant.hopsontong.com:11013/#/login"}]},"success":true}'
    ifnotest = json.loads(ifnotest,encoding=False)
    ifnotestlsit = jsonpath.jsonpath(ifnotest,"$.data.apps[?(@id = 3)].appUrl")
    print(ifnotestlsit)

def test10():
    urlData="https://tcmsapi.lifeat.cn:45788/sso/getUserAndMenuTree"
    dataData = {}
    dataData= json.dumps(dataData,ensure_ascii=False)
    headersData=CmsLogin().getToken()
    headersData=headersData["headers"]
    resultData = httpRequests(urlData=urlData, dataData=dataData, headersData=headersData)
    print(resultData)

def test101():
    info = {'headers': {'Content-Type': 'application/json;charset=UTF-8', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36', 'token': 'eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMTU3MTg4Njg0NzgiLCJpYXQiOjE1OTM2MTUwODIsImV4cCI6MTU5MzYyMjI4MiwibmJmIjoxNTkzNjE1MDgyfQ.CJtHOs2ki2P5Z5xCWhZpn9cY1_NnUaDL4tVHDP2k0yM', 'applicationToken': 'eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiOTUxIiwiaWF0IjoxNTkzNjE1MDgyLCJleHAiOjE1OTM2MjIyODIsIm5iZiI6MTU5MzYxNTA4Mn0.XRMwEiRoPMWOBUZZBX_PEFtc2dIu1mV2jUviDg1MHu0', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiOTUxIiwiaWF0IjoxNTkzNjE1MDgyLCJleHAiOjE1OTM2MjIyODIsIm5iZiI6MTU5MzYxNTA4Mn0.XRMwEiRoPMWOBUZZBX_PEFtc2dIu1mV2jUviDg1MHu0'}}

def test102():
    info = '{"isDefine":"","paData":{"urlData":"","paramData":{"mobile":"{userMobile}","appFlag":"easylife-cms-api-gateway","afsSessionId":"WjFlCkIWDpHT9odN","afsSig":"QuAncgq0hrmAVNX0","afsToken":"FFFF0N00000000009184:1591688607383:0.9844042761792562","afsScene":"nc_login","password":"{userPD}"}}}'
    info = json.loads(info,encoding='utf-8')
    print(info)


def test103():
    info = "{'Content-Type': 'application/json;charset=UTF-8','a':'{bb}'}"
    b="int(100)"
    print(b[:3])
    if b[:3] == "int":
        strValue = 100
    strValue = str(strValue)
    strKey = "bb"
    strKey1 = "'{" + strKey + "}'"
    strKey2 = '"{' + strKey + '}"'
    strRes1 = info.replace(strKey1, strValue)
    strRes1 = strRes1.replace(strKey2, strValue)
    print(strRes1)
    # print(info2)

def test104():
    strValue="23abdi9898987678878787878900909890"
    retest = strValue.isdigit()
    if retest:
        print(strValue)
    if strValue[:3] == "989":
        strValue = int(strValue[4:-1])
    # print(strValue)
    print(type(test104))
    
def test105():
    valuea={'mobile': '{userMobile}', 'appFlag': 'easylife-cms-api-gateway', 'afsSessionId': 'WjFlCkIWDpHT9odN', 'afsSig': 'QuAncgq0hrmAVNX0', 'afsToken': 'FFFF0N00000000009184:1591688607383:0.9844042761792562', 'afsScene': 'nc_login', 'password': '{userPD}'}
    # valuea = json.dumps(valuea,ensure_ascii=False)
    strKey = "userMobile"
    strValue = 15718868478
    
    strva=Common().replaceStr(valuea, strKey, strValue)
    print(strva)

def test106():
    valuea = {"isApp":"N","isTransmit":{"tokenName":[["token","token"],["Authorization","token"]],"transmitName":[["token",{"valueKey":"token","getValuePath":"$.data.token"}],["applicationToken",{"valueKey":"applicationToken","getValuePath":"$.data.applicationToken"}],["cityId",{"valueKey":"cityId","getValuePath":{"threeListAll":"$.data.cityList","threeList":"city-北京市-cityId"}}]]}}
    valuea = json.dumps(valuea)
    print(valuea)
# {"code":200,"msg":"成功","data":{"token":"eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMTU3MTg4Njg0NzgiLCJpYXQiOjE1OTM3NjA1OTYsImV4cCI6MTU5Mzc2Nzc5NiwibmJmIjoxNTkzNzYwNTk2fQ.su4C7DwOwdnxo3YzbTJgVs-R38LtC5i_wl6afbdz4J4","applicationToken":"eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiOTUxIiwiaWF0IjoxNTkzNzYwNTk2LCJleHAiOjE1OTM3Njc3OTYsIm5iZiI6MTU5Mzc2MDU5Nn0.HxBj8lXyc-zwQ0Pz4uqsX1ZBns710pFZb6_glxnUixc","isDirectLogin":true,"tenants":null,"apps":[{"id":3,"appName":"新运营端管理系统","appIcon":"","appUrl":"http://localhost:8089/,https://ndcms.lifeat.cn:45788/cms/,https://ntcms.lifeat.cn:45788/cms/,https://nhcms.lifeat.cn:45788/cms/,https://hb-ncms.lifeat.cn/cms/"},{"id":0,"appName":"权限系统","appIcon":"https://kf-pms-cdn.hopsontong.com/1585129410411-10947/cms/permission-system-logo-258x86.png","appUrl":"https://uat-pms-tenant.hopsontong.com:11013/#/login"}]},"success":true}
def test107():
    urlData = "https://uat-pms-sso.hopsontong.com:11013/api/login"
    dataData = {"mobile":15718868478,"appFlag":"easylife-cms-api-gateway","afsSessionId":"WjFlCkIWDpHT9odN","afsSig":"QuAncgq0hrmAVNX0","afsToken":"FFFF0N00000000009184:1591688607383:0.9844042761792562","afsScene":"nc_login","password":"123456"}
    dataData = json.dumps(dataData,ensure_ascii=False)
    headersData = RequestHeader.WEBHEADER
    valuea=httpRequests(urlData=urlData, dataData=dataData, headersData=headersData,)
    print(valuea)
    urlData = "https://uat-pms-sso.hopsontong.com:11013/api/checkToken"
    dataData={}
    dataData["token"]=headersData["token"] = valuea["data"]["token"]
    dataData["applicationToken"]=valuea["data"]["applicationToken"]
    dataData["appFlag"]="easylife-cms-api-gateway"
    # valueJson = json.loads(valuea.text,encoding=Fal
    # se)
    dataData =json.dumps(dataData,ensure_ascii=False)
    print(type(headersData))
    print(type(valuea))
    # headersData["token"] = valuea["data"]["token"]
    # headersData["Authorization"] = "Bearer " + valuea["data"]["token"]
    headersData1 = RequestHeader.WEBHEADER
    valuea1 = httpRequests(urlData=urlData, dataData=dataData, headersData=headersData1)
    print(valuea1)
    dataData = ""
    urlData = "https://tcmsapi.lifeat.cn:45788/city/cityList"
    headersData["token"] = valuea["data"]["applicationToken"]
    headersData["Authorization"] = "Bearer " + valuea["data"]["applicationToken"]
    valuea = httpRequests(urlData=urlData, dataData=dataData, headersData=headersData)
    print(valuea)

def test108():
    vainfo = {"isApp":"N","isTransmit":{"tokenName":[["token","applicationToken"],["Authorization","applicationToken"]],"transmitName":[["cityId",{"valueKey":"cityId","getValuePath":{"threeListAll":"$.data.cityList","threeList":"city-北京市-cityId"}}],["brokerageTypeId",{"valueKey":"brokerageTypeCode","getValuePath":{"threeListAll":"$.data.list","threeList":"brokerageTypeCode-YJ20200506000002-id"}}]]}}
    print(type(vainfo))

def test109():
    a = [1,2,3]
#     print(a[3])
# try:
#     test109()
# except:
#     print("ok")
def test110():
    dataData = {"mobile": 15718868478, "appFlag": "easylife-cms-api-gateway"}
    for k,v in dataData.items():
        print(k)
test110()