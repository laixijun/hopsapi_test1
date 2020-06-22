import json

import jsonpath

from utils.logger import Log
from utils.new_tools.common_tool import Common

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




