# @Time    : 7/1/2020 3:20 PM
# @Author  : Yang Xiaobai
# @Email   : yangzhiyongtest@163.com
import json

import jsonpath
import requests

from utils.config_tool.request_header import RequestHeader
from utils.logger import Log

logger = Log(logger='deal_source').get_log()
class CmsLogin:
    def __init__(self,userPhone=None,userPassword=None):
        self.cmsUrl = "https://uat-pms-sso.hopsontong.com:11013/api/login"
        self.headers = RequestHeader.WEBHEADER
        if userPhone != None:
            self.userPhone = userPhone
        else:
            self.userPhone = '15718868478'
        if userPassword != None:
            self.userPassword = userPassword
        else:
            self.userPassword = "123456"
        
    # 请求获取参数
    def cmsLogin(self):
        requestData = self.inputData()
        inputData = json.dumps(requestData,ensure_ascii=False)
        httpMethod = 'post'
        logger.info(httpMethod)
        logger.info(inputData)
        logger.info(self.headers)
        resuntRequests = requests.post(url=self.cmsUrl,data=inputData,headers=self.headers, verify=False)
        logger.info(resuntRequests.text)
        if resuntRequests.status_code == 200:
            logger.info(type(resuntRequests.status_code))
            resuntRequestsData = json.loads(resuntRequests.text,encoding=False)
            return resuntRequestsData
        else:
            logger.info(resuntRequests)
            return "权限验证失败"
    
    # 生成入参
    def inputData(self):
        requestData = '{"mobile":'+ self.userPhone + ',"appFlag":"easylife-cms-api-gateway","afsSessionId":"WjFlCkIWDpHT9odN","afsSig":"QuAncgq0hrmAVNX0","afsToken":"FFFF0N00000000009184:1591688607383:0.9844042761792562","afsScene":"nc_login","password":"' + self.userPassword +'"}'
        # requestData='{"mobile":18600750013,"appFlag":null,"afsSessionId":"WjFlCkIWDpHT9odN","afsSig":"QuAncgq0hrmAVNX0","afsToken":"FFFF0N00000000009184:1591688607383:0.9844042761792562","afsScene":"nc_login","password":"qwer1234"}'
        requestData = json.loads(requestData,encoding=False)
        logger.info(requestData)
        return requestData

    
    # 获得需要的token
    # ntcms、nhcms、ncms
    def getToken(self,env=None):
        resultRequest = self.cmsLogin()
        tokenWeb = jsonpath.jsonpath(resultRequest,"$.data.token")
        applicationToken = jsonpath.jsonpath(resultRequest,"$.data.applicationToken")
        newCmsUrl =  jsonpath.jsonpath(resultRequest,"$.data.apps[0].appUrl")
        logger.info(newCmsUrl)
        logger.info(tokenWeb)
        if newCmsUrl:
            newCmsUrlList = newCmsUrl[0].split(",")
            logger.info(newCmsUrlList)
            newCmsUrldic = {}
            newCmsUrldic['ntcms'] = newCmsUrlList[2]
            newCmsUrldic['nhcms']=newCmsUrlList[3]
            newCmsUrldic['ncms'] =newCmsUrlList[4]
            self.headers["token"]=tokenWeb[0]
            self.headers["applicationToken"] = applicationToken[0]
            if env != None:
                env = newCmsUrldic['ntcms']
            else:
                env = newCmsUrldic[env]
            loginResult = {}
            loginResult["headers"]=self.headers
            loginResult["env"] = env
            return loginResult
        else:
            return {"code":0,"msg":"获取环境失败"}
    
    
if __name__ == "__main__":
    cg=CmsLogin().getToken(env='nhcms')
    print(cg)

        
        
        
        
    