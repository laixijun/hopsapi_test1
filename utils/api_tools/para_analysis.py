# @Time    : 6/18/2020 9:07 AM
# @Author  : Yang Xiaobai
# @Email   : yangzhiyongtest@163.com
import json

import jsonpath

from utils.config_tool.request_header import RequestHeader
from utils.logger import Log
from utils.new_tools.common_tool import Common
from utils.new_tools.txt_tool import TxtTool

logger = Log(logger='para_analysis').get_log()
class ParaAnalysis:
    def __init__(self):
        pass

    # 1、 将header中的token添加到header
    def tokenToHeader(self,responseValue,requestPara,envContentDic=None):
        requestPara=requestPara[7]
        logger.info(requestPara)
        # requestPara = json.dumps(requestPara,ensure_ascii=False)
        # if isinstance(requestPara,str):
        logger.info(type(requestPara))
        requestPara = json.loads(requestPara,encoding='utf-8')
        logger.info(requestPara["isTransmit"])
        header_tokenKey = requestPara["isTransmit"]["tokenName"]
        logger.info(header_tokenKey)
        if header_tokenKey != "" and ( not isinstance(header_tokenKey,list)):
            header_tokenKey = eval(header_tokenKey)
        listNum = Common().estimateList(header_tokenKey)
        if self.isAppRequest(isAppDic=requestPara):
            header_token = RequestHeader.APPHEADER
        else:
            header_token = RequestHeader.WEBHEADER
        ttr = TxtTool().readTxt()
        logger.info(ttr)
        if ttr:
            ttr = json.loads(ttr, encoding="utf-8")
        if listNum ==1 and responseValue != None :
            for list_item in header_tokenKey:
                logger.info(header_tokenKey)
                try:
                    logger.info(list_item)
                    header_tokenValue = responseValue[list_item[1]]
                    if list_item[0] == "Authorization" and header_token["User-Agent"] == RequestHeader.WEBHEADER["User-Agent"]:
                        header_tokenValue = "Bearer " + header_tokenValue
                        ttr["transmitData"]["webAuthorization"] = header_tokenValue
                    else:
                        ttr["transmitData"][list_item[1]]=header_tokenValue
                    header_token[list_item[0]]=header_tokenValue
                except:
                    try:
                        if list_item[0] == "Authorization" and header_token["User-Agent"] == RequestHeader.WEBHEADER[
                            "User-Agent"]:
                            header_tokenValue = "Bearer " + ttr["transmitData"]["applicationToken"]
                            header_token[list_item[0]] = header_tokenValue
                        else:
                            header_token[list_item[0]] = ttr["transmitData"][list_item[1]]
                    except:
                        header_token[list_item[0]] = "not found"
        elif listNum == 0 and responseValue != None:
            try:
                header_tokenValue = responseValue[header_tokenKey[1]]
                if header_tokenKey[0] == "Authorization" and header_token["User-Agent"] == RequestHeader.WEBHEADER[
                    "User-Agent"]:
                    header_tokenValue = "Bearer " + header_tokenValue
                    ttr["transmitData"]["webAuthorization"] = header_tokenValue
                else:
                    ttr["transmitData"][header_tokenKey[1]] = header_tokenValue
                header_token[header_tokenKey[0]] = header_tokenValue
            except:
                try:
                    if header_tokenKey[0] == "Authorization" and header_token["User-Agent"] == RequestHeader.WEBHEADER[
                        "User-Agent"]:
                        header_tokenValue = "Bearer " + ttr["transmitData"]["applicationToken"]
                        header_token[header_tokenKey[0]] = header_tokenValue
                    else:
                        header_token[header_tokenKey[0]] = ttr["transmitData"][header_tokenKey[1]]
                except:
                    header_token[header_tokenKey[0]] = "not fonnd"
        if not isinstance(ttr,str):
            ttr = json.dumps(ttr,ensure_ascii=False)
        logger.info(ttr)
        TxtTool().writeTxt(contents=ttr)
        return header_token

    # header处理选择
    def chooseHeader(self,caseList,responseValue=None):
        paraDic = caseList[7]
        # paraDic = json.loads(paraDic,encoding="utf-8")
        paraDic = json.loads(paraDic,encoding='utf-8')
        tokenlist = jsonpath.jsonpath(paraDic,'$.isTransmit.tokenName')
        # if responseValue != None:
        #     responseValue = json.loads(responseValue,encoding='utf-8')
        logger.info(tokenlist)
        if tokenlist == False:
            tokenlist = ""
        logger.info(paraDic)
        logger.info(type(paraDic))
        if tokenlist == '' and (paraDic['isApp'] == 'N' or paraDic['isApp'] == 'n'):
            return RequestHeader.WEBHEADER
        elif tokenlist == '' and (paraDic['isApp'] == 'Y' or paraDic['isApp'] == 'y'):
            return RequestHeader.APPHEADER
        elif tokenlist != '':
            headerdata=self.tokenToHeader(responseValue=responseValue, requestPara=caseList, envContentDic=None)
            return headerdata

    # 2、将需要传递的健值添加参数
    def paraToRequestData(self,requestPara,requestData,responseValue=None,parameterCase=None,envContentDic={}):
        # requestPara = requestPara[7]
        # requestData = json.loads(requestData,encoding='utf-8')
        # requestPara = json.loads(requestPara,encoding='urt-8')
        logger.info(requestData)
        logger.info(requestPara)
        logger.info(type(requestPara))
        logger.info(type(requestData))
        transmitKey = requestPara["isTransmit"]["transmitName"]
        requestDataJson = requestData["paData"]["paramData"]
        listNum = Common().estimateList(transmitKey)
        logger.info(listNum)
        ttr = TxtTool().readTxt()
        if ttr:
            ttr = json.loads(ttr, encoding="utf-8")
        requestDataJson = json.dumps(requestDataJson,ensure_ascii=False)
        if listNum ==1 and responseValue != None:
            for list_item in transmitKey:
                strKey = list_item[0]
                if not isinstance(list_item[1],str):
                    for k,v in list_item[1].items():
                        getValueFalseList = v.split("-")
                    strValue=Common().getJsonValue(mydict=responseValue, key=k, assitValue=getValueFalseList[1],assitKey=getValueFalseList[0])
                    valueKey=k
                else:
                    strValue = Common().getJsonValue(mydict=responseValue, key=list_item[1])
                    valueKey=list_item[1]
                if strValue != None:
                    ttr["transmitData"][valueKey] = strValue
                    envContentDic[strKey]=strValue
                else:
                    logger.info(ttr)
                    logger.info(type(ttr))
                    try:
                        strValue = ttr["transmitData"][valueKey]
                    except:
                        strValue = "not found"
                requestDataJson = Common().replaceStr(requestDataJson, strKey, strValue)
        elif listNum == 0  and responseValue != None:
            strKey = transmitKey[0]
            logger.info(strKey)
            if not isinstance(transmitKey[1], str):
                for k, v in transmitKey[1].items():
                    getValueFalseList = v.split("-")
                strValue = Common().getJsonValue(mydict=responseValue, key=k, assitValue=getValueFalseList[1],
                                                 assitKey=getValueFalseList[0])
                valueKey = k
            else:
                strValue = Common().getJsonValue(mydict=responseValue, key=transmitKey[1])
                valueKey = transmitKey[1]
            if strValue != None:
                ttr["transmitData"][valueKey] = strValue
                envContentDic[strKey] = strValue
            else:
                try:
                    strValue = ttr["transmitData"][strValue]
                except:
                    strValue = "not found"
            requestDataJson = Common().replaceStr(requestDataJson, strKey, strValue)
        if not isinstance(ttr,str):
            ttr = json.dumps(ttr,ensure_ascii=False)
        logger.info(ttr)
        TxtTool().writeTxt(contents=ttr)
        requestDataJson = json.loads(requestDataJson, encoding='utf-8')
        return {"requestDataJson":requestDataJson,"envContentDic":envContentDic}

    # 2、将需要参数化的健值添加参数
    def paraToRequestExchangeData(self,requestPara,requestData,responseValue=None,parameterCase=None,envContentDic={}):
        # requestData = requestData["requestDataJson"]
        # requestData = json.dumps(requestData,ensure_ascii=False)
        for para_item in requestPara.keys():
            strKey = para_item
            strValue = requestPara[strKey]
            requestDataJson = Common().replaceStr(requestData, strKey, strValue)
            requestData = requestDataJson
            # requestDataJson =json.loads(requestData,encoding='utf-8')
            logger.info(requestDataJson)
        logger.info(requestDataJson)
        return {"requestDataJson":requestData,"envContentDic":envContentDic}

    # 获取参数
    #parameterCase= {"testCaseId":{"parameterKey":"parameterValue"}}
    def choosePara(self,caseList,responseValue=None,parameterCase=None,envContentDic={}):
        testCaseId = caseList[1]
        paraRequestDict = caseList[7]
        logger.info(paraRequestDict)
        paraRequestDict = json.loads(paraRequestDict,encoding='utf-8')
        paraRequestJson = json.loads(caseList[6],encoding='utf-8')
        if responseValue != None:
            if isinstance(responseValue,str) and ('{' in responseValue[:2]):
                responseValue = json.loads(responseValue,encoding='utf-8')
        paraList = jsonpath.jsonpath(paraRequestDict,'$.isTransmit.transmitName')
        logger.info(paraList)
        if paraList == '':
            requestDataJson = paraRequestJson["PaData"]["paramData"]
            requestDataJson = json.loads(requestDataJson,encoding='utf-8')
            requestDataJson = {"requestDataJson":requestDataJson,"envContentDic":envContentDic}
        else:
            requestDataJson = self.paraToRequestData(requestPara=paraRequestDict,requestData=paraRequestJson,responseValue=responseValue,parameterCase=None)
        # {"BOHUI03":{"customerName":"王小王","customerPhone":"13712321234","customerSex":"0","arriveTime":"2020-06-27","isHiddenPhone":"isHiddenPhone"}}
        if parameterCase != None:
            parameterCase = parameterCase[2]
            parameterCase = json.loads(parameterCase,encoding='utf-8')
            for testCaseIdParameter in parameterCase.keys():
                if testCaseId == testCaseIdParameter:
                    parameterCasePara = parameterCase[testCaseIdParameter]
                    requestDataJson=self.paraToRequestExchangeData(requestPara=parameterCasePara, requestData=requestDataJson['requestDataJson'])
            logger.info(requestDataJson)
        logger.info(requestDataJson)
        return requestDataJson


    # 3、 获取Python脚本
    def acquirePython(self):
        pass
    # 4、 上下文的处理
    def envContent(self):
        pass
    # 5、判断是否是APP
    #{"isApp":"False","isTransmit":{"tokenName":"tokenKey","transmitName":"transmitKey"}}
    def isAppRequest(self,isAppDic):
        if isAppDic["isApp"] == 'Y' or isAppDic["isApp"] == 'y':
            return True
        else:
            return False



if __name__ == '__main__':
    pass
