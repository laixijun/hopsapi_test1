import json

import jsonpath

from test.test_api.testZong import paraTest2
from utils.api_tools.api_classfication import ApiClassification
from utils.config_tool.ConfigParameter import TESTPARAMTER
from utils.logger import Log
from utils.new_tools.common_tool import Common
from utils.new_tools.excel_tool import DealExcelTool
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
print(result)

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
    headers = {'Content-Type': 'application/json', 'Connection': 'keep-alive',
               'User-Agent': 'EasyLife.alpha/1.4.2 (iPhone; iOS 10.2.1; Scale/3.00)'}

    tfn = DealExcelTool().getTempFileName()
    headers = json.dumps(headers, ensure_ascii=False)
    TxtTool().writeTxt(tfn, headers)
    result = TxtTool().readTxt(tfn)
    print(result)


if __name__ == '__main__':

    paraTest()
    paraTest2()