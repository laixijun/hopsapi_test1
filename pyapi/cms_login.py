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
        self.tenantUrl = "https://uat-pms-sso.hopsontong.com:11013/api/selectTenant"
        self.tenantHeaders = RequestHeader.WEBHEADER
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
        dataR={}
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
            applicationToken = jsonpath.jsonpath(resuntRequestsData, "$.data.token")
            dataR["reaponse"] = resuntRequestsData
            dataR["token"] = applicationToken[0]
            return dataR
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

    # 选择租户的入参
    def tenantData(self,tokenTen):
        requestData='{"loginToken":"'+tokenTen+'","accessToken":null,"tenantId":28}'
        requestData = json.loads(requestData, encoding=False)
        return requestData
        

    # 获取租户token
    #response {"code":200,"msg":"成功","data":{"token":"eyJhbGciOiJIUzI1NiJ9.eyJ0ZW5hbnRfaWQiOiIyOCIsInVzZXJfaWQiOiI5NTEiLCJwbGF0Zm9ybV9pZCI6IjMiLCJpYXQiOjE1OTcxOTY2NjYsImV4cCI6MTU5NzIwMzg2MSwibmJmIjoxNTk3MTk2NjY2fQ.IrNhW5rDztZYTHGXWSTeHr50UWCWavOXwIz2yrWELjY","apps":[{"id":3,"appName":"新运营端管理系统","appIcon":"","appUrl":"http://localhost:8089/,https://ndcms.lifeat.cn:45788/cms/,https://ntcms.lifeat.cn:45788/cms/,https://nhcms.lifeat.cn:45788/cms/,https://hb-ncms.lifeat.cn/cms/"},{"id":0,"appName":"权限系统","appIcon":"https://kf-pms-cdn.hopsontong.com/1585129410411-10947/cms/permission-system-logo-258x86.png","appUrl":"https://uat-pms-tenant.hopsontong.com:11013/#/login"}]},"success":true}
    def getTenantToken(self,tokenTen):
        self.tenantHeaders["Authorization"]=tokenTen
        tenantData=self.tenantData(tokenTen)
        logger.info(tenantData)
        httpMethod = 'post'
        logger.info(httpMethod)
        logger.info(self.headers)
        tenantData=json.dumps(tenantData,ensure_ascii=False)
        resuntRequests = requests.post(url=self.tenantUrl, data=tenantData, headers=self.tenantHeaders, verify=False)
        r=json.loads(resuntRequests.text,encoding="utf-8")
        print(type(r))
        print(r)
        applicationToken = jsonpath.jsonpath(r, "$.data.token")
        print(type(applicationToken))
        print(applicationToken)
        tokenTenR="Bearer "+applicationToken[0]
        dataR={}
        dataR["reaponse"]=resuntRequests.text
        dataR["token"]=applicationToken[0]
        dataR["Authorization"]=tokenTenR
        return dataR
        
        
    # 获取token
    def getTenantTokenLeast(self):
        cl=CmsLogin()
        tokenJson=cl.cmsLogin()
        tokenTenant=tokenJson["token"]
        print(type(tokenTenant))
        print(tokenTenant)
        tokenTenant=cl.getTenantToken(tokenTenant)
        return tokenTenant
        
        
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
            authstr = "Bearer " + applicationToken[0]
            logger.info(authstr)
            self.headers["Authorization"] = authstr
            if env == None:
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
    cg=CmsLogin().getTenantTokenLeast()
    print(cg)

        
        
        
        
    