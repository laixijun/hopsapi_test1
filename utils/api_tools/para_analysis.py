# @Time    : 6/18/2020 9:07 AM
# @Author  : Yang Xiaobai
# @Email   : yangzhiyongtest@163.com
import json

import jsonpath

from utils.config_tool.request_header import RequestHeader
from utils.logger import Log
from utils.new_tools.common_tool import Common

logger = Log(logger='para_analysis').get_log()
class ParaAnalysis:
    def __init__(self):
        pass

    # 1、 将header中的token添加到header
    def tokenToHeader(self,responseValue,requestPara,envContentDic=None):
        header_tokenKey = requestPara["isTransmit"]["tokenName"]
        listNum = Common().estimateList(header_tokenKey)
        if self.isAppRequest(isAppDic=requestPara):
            header_token = RequestHeader.APPHEADER
        else:
            header_token = RequestHeader.WEBHEADER
        if listNum ==1:
            for list_item in header_tokenKey:
                header_tokenValue = responseValue[list_item[1]]
                header_token[list_item[0]]=header_tokenValue
        elif listNum == 0:
            header_tokenValue = responseValue[header_tokenKey[1]]
            header_token[header_tokenKey[0]] = header_tokenValue
        return header_token

    # header处理选择
    def chooseHeader(self,caseList,responseValue=None):
        paraDic = caseList[7]
        paraDic = json.dumps(paraDic)
        tokenlist = jsonpath.jsonpath(paraDic,'$.isTransmit.tokenName')
        paraDic = json.loads(paraDic,encoding='utf-8')
        if tokenlist == '' and (paraDic['isApp'] == 'N' or paraDic['isApp'] == 'n'):
            return RequestHeader.WEBHEADER
        elif tokenlist == '' and (paraDic['isApp'] == 'Y' or paraDic['isApp'] == 'y'):
            return RequestHeader.APPHEADER
        elif tokenlist != '':
            headerdata=self.tokenToHeader(responseValue=responseValue, requestPara=caseList, envContentDic=None)
            return headerdata

    # 2、将需要传递的健值添加参数
    def paraToRequestData(self,responseValue,requestPara,requestData,envContentDic={}):
        transmitKey = requestPara["isTransmit"]["transmitName"]
        requestDataJson = requestData["paData"]["paramData"]
        listNum = Common().estimateList(transmitKey)
        if listNum ==1:
            for list_item in transmitKey:
                strKey = list_item[0]
                strValue=jsonpath.jsonpath(responseValue,list_item[1]["getValuePath"])[0]
                envContentDic["transmitDic"][strKey]=strValue
                requestDataJson=Common().replaceStr(requestDataJson, strKey, strValue)
        elif listNum == 0:
            strKey = transmitKey[0]
            logger.info(strKey)
            strValue = jsonpath.jsonpath(responseValue, transmitKey[1]["getValuePath"])[0]
            logger.info(strValue)
            envContentDic["transmitDic"][strKey] = strValue
            requestDataJson=Common().replaceStr(requestDataJson, strKey, strValue)
            logger.info(requestDataJson)
        return {"requestDataJson":requestDataJson,"envContentDic":envContentDic}

    # 获取参数
    def choosePara(self,caseList,responseValue=None):
        paraDic = caseList[7]
        paraJson = caseList[6]
        paraDic = json.dumps(paraDic)
        paraJson = json.dumps(paraJson)
        paraList = jsonpath.jsonpath(paraDic,'$.isTransmit.transmitName')
        if paraList == '':
            return paraJson["PaData"]["paramData"]
        else:
            return self.paraToRequestData(responseValue=responseValue,requestPara=paraDic,requestData=paraJson)


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




