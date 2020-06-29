# @Time : 6/16/2020 10:54 AM
# @Author  : YangXiaobai
# @Email   : yangzhiyongtest@163.com
import json

import requests

from utils.config_tool.request_header import RequestHeader
from utils.logger import Log

logger = Log(logger='api_classfication').get_log()
class ApiClassification:
    def __init__(self,headerData=None):
        self.url_post = "https://tbroker.lifeat.cn:45788/easylife/rest/broker/login"
        self.data = {\
                    "brokerPhone": "15718868478",\
                    "clientId": "8c82592b934908becdc2375e52dbbc6d",\
                    "password": "123456"\
                    }
        if headerData != None:
            self.header_app = headerData
            self.header_web = headerData
        else:
            self.header_app = RequestHeader.APPHEADER
            self.header_web = RequestHeader.WEBHEADER

    # 2、 对get的请求进行get处理
    def get_request(self, url_get, pydata = None):
        get_response_dic={}
        get_response_fail={}
        if pydata != None:
            pydata = pydata.encode("utf-8")
        get_response = requests.get(url=url_get, params=pydata,headers=self.header_app,verify=False)
        logger.info(get_response.status_code)
        if get_response.status_code == requests.codes.ok:
            get_response_dic["status_code"] = get_response.status_code
            get_response_dic["text"] = get_response.text
            get_response_dic["headers"] = get_response.headers
            logger.info(get_response_dic)
            return get_response_dic
        else:
            get_response_fail["status_code"] = get_response.status_code
            get_response_fail["text"] = get_response.text
            get_response_fail["headers"] = get_response.headers
            logger.info(get_response_fail)
            return get_response_fail
    # 3、 对post的请求进行post的处理
    def post_request(self, url_post, post_data):
        post_response_dic={}
        post_response_fail={}
        post_data_json = json.dumps(post_data,ensure_ascii=False)
        logger.info(post_data_json)
        logger.info(url_post)
        logger.info(self.header_app)
        post_data_json = post_data_json.encode("utf-8")
        post_response = requests.post(url=url_post, data=post_data_json, headers=self.header_app, verify=False)
        logger.info(post_response.status_code)
        if post_response.status_code == requests.codes.ok:
            post_response_dic["status_code"] = post_response.status_code
            post_response_dic["text"] = post_response.text
            post_response_dic["headers"] = post_response.headers
            logger.info(post_response_dic)
            return post_response_dic
        else:
            post_response_fail["status_code"] = post_response.status_code
            post_response_fail["text"] = post_response.text
            post_response_fail["headers"] = post_response.headers
            logger.info(post_response_fail)
            return post_response_fail
    # 如果需要处理token
    def requestToken(self,tokenStrDic):
        for tokenStr in tokenStrDic.keys():
            self.header_app
    # 判断需要使用的请求类型
    def requestEstimate(self,methodRequest,urlRequest,dataRequest=None):
        if methodRequest == "post" or methodRequest == "Post" or methodRequest == "POST":
            resultRequst=self.post_request(url_post = urlRequest, post_data = dataRequest)
        elif methodRequest == "get" or methodRequest == "Get" or methodRequest == "GET":
            resultRequst=self.get_request(url_get = urlRequest, pydata = dataRequest)

        return resultRequst

if __name__ == "__main__":
    ac = ApiClassification()
    logger.info(ac.header_post)
    result = ac.post_request(url_post=ac.url_post,post_data=ac.data)
    print(result.text)