import json

import jsonpath

from test.test_api.testZong import paraTest2
from utils.api_tools.api_classfication import ApiClassification
from utils.config_tool.ConfigParameter import TESTPARAMTER
from utils.config_tool.file_config_path import ExcelConfig
from utils.logger import Log
from utils.new_tools.common_tool import Common
from utils.new_tools.excel_tool import DealExcelTool, ExcelTool
from utils.new_tools.txt_tool import TxtTool

testDict = {}
testList =[["1",2,3,4],["2",2,3,4],["2",2,3,4]]
testBusinessNumBak = None
testDictItemList = []
for testListItem in testList:
    if testBusinessNumBak == None:
        testBusinessNumBak=testListItem[0]
    testBusinessNum = testListItem[0]
    if testBusinessNumBak == testBusinessNum:
        testDictItemList.append(testListItem[1:])
        testDict[testBusinessNum] = testDictItemList
    elif testBusinessNumBak != testBusinessNum:
        testBusinessNumBak = testListItem[0]
        testBusinessNum = testListItem[0]
        testDict[testBusinessNum] = testDictItemList
        testDictItemList = []
        testDictItemList.append(testListItem[1:])


def testCaseDic(testList):
    testDict = {}
    testBusinessNumBak = None
    testDictItemList = []
    for testListItem in testList:
        if testBusinessNumBak == None:
            testBusinessNumBak = testListItem[0]
        testBusinessNum = testListItem[0]
        if testBusinessNumBak == testBusinessNum:
            testDictItemList.append(testListItem[1:])
            testDict[testBusinessNum] = testDictItemList
        elif testBusinessNumBak != testBusinessNum:
            testBusinessNumBak = testListItem[0]
            testBusinessNum = testListItem[0]
            testDictItemList = []
            testDictItemList.append(testListItem[1:])
            testDict[testBusinessNum] = testDictItemList
    return testDict
testList =[["1",2,3,4],["2",2,3,4],["2",2,3,4]]
resulttestdict= testCaseDic(testList)


def estimateList(estimatelistValue):
    listNum = 0
    while isinstance(estimatelistValue, list):
        for item_list in estimatelistValue:
            if isinstance(item_list, list):
                listNum += 1
                estimatelistValue = item_list
                break
            else:
                estimatelistValue = item_list
                break
    return listNum
logger = Log(logger='para_analysis').get_log()
def paraToRequestData(responseValue,requestPara,requestData,envContentDic):
    transmitKey = requestPara["isTransmit"]["transmitName"]
    requestDataJson = requestData["paData"]["paramData"]
    listNum = Common().estimateList(transmitKey)
    logger.info(listNum)
    if listNum ==1:
        for list_item in transmitKey:
            strKey = list_item[0]
            logger.info(strKey)
            strValue=jsonpath.jsonpath(responseValue,list_item[1]["getValuePath"])[0]
            logger.info(strValue)
            envContentDic["transmitDic"][strKey]=strValue
            requestDataJson=Common().replaceStr(requestDataJson, strKey, strValue)
            logger.info(requestDataJson)
    elif listNum == 0:
        strKey = transmitKey[0]
        logger.info(strKey)
        strValue = jsonpath.jsonpath(responseValue, transmitKey[1]["getValuePath"])[0]
        logger.info(strValue)
        envContentDic["transmitDic"][strKey] = strValue
        requestDataJson=Common().replaceStr(requestDataJson, strKey, strValue)
        logger.info(requestDataJson)
    return {"requestDataJson":requestDataJson,"envContentDic":envContentDic}
envContentDic={"transmitDic":{"transmitKey":"transmitValue"},"definePara":{}}
requestPara={"isApp":"False","isTransmit":{"tokenName":"[tokenKey,valueKey]","transmitName":
    [["getValuePath",{"valueKey":"valueKey","getValuePath":"$.isTransmit.tokenName"}],["valueKey",{"valueKey":"valueKey","getValuePath":"$.isApp"}]]}}
requestData={"isDefine":{"keyName","print('python')"},"paData":{"urlData":{},"paramData":{"isApp":"False","isTransmit":{"tokenName":"[tokenKey,valueKey]","transmitName":
    ["transmitKey",{"valueKey":"{getValuePath}","getValuePath":"{valueKey}"}]}}}}
responseValue={"isApp":"False","isTransmit":{"tokenName":"[tokenKey,valueKey]","transmitName":
    ["transmitKey",{"valueKey":"valueKey","getValuePath":"getValuePath"}]}}
result=paraToRequestData(responseValue, requestPara, requestData, envContentDic)
# print(result)

def test():
    pass
# estimatelistValue=[["getValuePath",{"valueKey":"valueKey","getValuePath":"$.isTransmit.tokenName"}],["valueKey",{"valueKey":"valueKey","getValuePath":"$.isApp"}]]
# def estimateList(estimatelistValue):
#     listNum = 0
#     while isinstance(estimatelistValue, list):
#         for item_list in estimatelistValue:
#             if isinstance(item_list, list):
#                 listNum += 1
#                 estimatelistValue = item_list
#                 break
#             else:
#                 estimatelistValue = item_list
#                 break
#     return listNum
#
# num = estimateList(estimatelistValue)
# print(num)

def apiTest():
    data ={'brokerPhone': '15718868478', 'clientId': '77a8a4b9e5ba1c9b6a21ca1b839c3581', 'password': '123456'}
    headers = {'Content-Type': 'application/json', 'Connection': 'keep-alive', 'User-Agent': 'EasyLife.alpha/1.4.2 (iPhone; iOS 10.2.1; Scale/3.00)'}
    urldata = 'https://tbroker.lifeat.cn:45788/easylife/rest/broker/login'
    a=ApiClassification().post_request(url_post=urldata,post_data=data)

    print(a)

def paraTest():
    # headers = {'Content-Type': 'application/json', 'Connection': 'keep-alive',
    #            'User-Agent': 'EasyLife.alpha/1.4.2 (iPhone; iOS 10.2.1; Scale/3.00)'}
	#
    # tfn = DealExcelTool().getTempFileName()
    # headers = json.dumps(headers, ensure_ascii=False)
    ttr = TxtTool().readTxt()
    try:
        print(ttr['transmitData'])
    except:
        if ttr == None:
            print(1,ttr)

    # ttw=TxtTool().writeTxt(tfn, headers)
    # result = TxtTool().readTxt(tfn)
    # print(result)

def lenList():
    a= [1,2,3]
    if 1 in a:
        print(a)

def getTestExecuteID():
    testFile=DealExcelTool().getTestFileName()
    et=ExcelTool(excelFile=testFile,sheetName=ExcelConfig.PARAMETERCASESHEET)
    testExecuteID=et.get_col_value(column=1,rowNum=2)
    return testExecuteID

def estimateKey():
    d = {'name': 'Tom', 'age': 10, 'Tel': 110}
    if "name" in d:
        print(d)
    else:
        print(" Not in dic !")

def test100():
    d = {'name': 'Tom', 'age': 10, 'Tel': "{110}"}
    strKey = "110"
    strValue = 100
    if not isinstance(strValue,str):
        pass
    requestDataJson=json.dumps(d)
    requestDataJson=Common().replaceStr(requestDataJson, strKey, strValue)
    requestDataJson = json.loads(requestDataJson)
    print(requestDataJson)

def test101():
    d = {'name': 'Tom', 'age': 10, 'Tel': "{110}"}
    strKey = "110"
    strValue = {"a":1}
    if not isinstance(strValue,str):
        pass
    requestDataJson=json.dumps(d)
    # strValue=jsonpath.jsonpath(d,"")
    requestDataJson = Common().replaceStr(requestDataJson, strKey, strValue)
    print(requestDataJson)


def test102():
    dictest2 = '{"isApp":"Y","isTransmit":{"tokenName":[["token","token"],["brokerCode","brokerCode"]],' \
              '"transmitName":[["brokerCity",{"valueKey":"brokerCity","getValuePath":""}],' \
              '["estateProjectDevName",{"valueKey":"name","getValuePath":"$.data[?@devId=\'10881\'].name"}],' \
              '["estateProjectDevId",{"valueKey":"devId","getValuePath":"$.data[?@name=\'大股东法国队\'].devId"}]]}}'
    dictest = '{"isApp":"Y","isTransmit":{"tokenName":[["token","token"],["brokerCode","brokerCode"]],' \
               '"transmitName":[["brokerCity",{"valueKey":"brokerCity","getValuePath":""}],' \
               '["estateProjectDevName",{"valueKey":"name","getValuePath":"$.data[?@devId=\'10881\'].name"}],' \
               '["estateProjectDevId",{"valueKey":"devId","getValuePath":"$.data[?@name=\'大股东法国队\'].devId"}]]}}'
    # dictest = json.dumps(dictest,ensure_ascii=False)
    # dictest = json.loads(dictest,encoding='utf-8')
    print(dictest[236:])
    print(type(dictest))

def test03():
    a= {"transmitData": "", "parameterData": ""}
    a["transmitData"]["100"]=100
    print(a)

def test104():
    a={'transmitData': {}, 'parameterData': {}}
    a["transmitData"]["xuia"]=100
    a=json.dumps(a)
    a=json.loads(a)
    a=json.loads(a)
    print(a)

def test105():
    a=[
        'KHGJ001', 'BOHUI03', '客户跟进3', '驳回3', 'https://tbroker.lifeat.cn:45788/easylife/rest/broker/customer/user/follow', 'POST', '{"isDefine":"","paData":{"urlData":"","paramData":{"customerName":"{customerName}","customerPhone":"{customerPhone}","brokerCode":"{brokerCode}","customerSex":"{customerSex}","customerLook":{},"edition":"v1.3.0","followType":"1","estateProjectDevName":"{estateProjectDevName}","customerRerport":{"arriveTime":"{arriveTime}"},"customerPurchase":{"houseType":{}},"estateProjectDevId":"{estateProjectDevId}","isHiddenPhone":"{isHiddenPhone}"}}}', '{"isApp":"Y","isTransmit":{"tokenName":[["token","token"],["brokerCode","brokerCode"]],"transmitName":[["brokerCode",{"valueKey":"brokerCode","getValuePath":""}],["estateProjectDevName",{"valueKey":"name","getValuePath":"\n"}],["estateProjectDevId",{"valueKey":"devId","getValuePath":""}]]}}', '{"$.status.code":"1000"}']
    b= a[7]
    print(b[221:])



if __name__ == '__main__':
    test105()