from utils.logger import Log
from utils import getParams
import configparser as cparser
import requests
import json
import os
logger = Log(logger='HttpUtil').get_log()

# 读取配置
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + '/db_file.ini'
cf = cparser.ConfigParser()
cf.read(file_path)


class HttpUtil:
    accessToken = ''

    def __init__(self):
        self.headers = {'Accept': 'application/json, text/plain, */*', 'Content-Type': 'application/json;charset=UTF-8',
                        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0',
                        'Authorization': self.accessToken}
        print(self.headers)
        self.base_url = cf.get('URL', 'base_url')
        self.sso_url = cf.get('URL', 'sso_url')
        self.port = cf.get('URL', 'port')
        if self.port:
            self.url = "https://" + self.base_url + ":" + self.port
            self.sso_url = "https://" + self.sso_url + ":" + self.port
        else:
            self.url = "https://" + self.base_url
            self.sso_url = "https://" + self.sso_url

    @classmethod
    def get_token(self):
        path = getParams.get_url('cms_login', 'login_Sucess')
        params = getParams.get_req_params('cms_login', 'login_Sucess')
        logger.info('params: %s' % params)
        response = HttpUtil().do_post(path, params)
        # 登录sso,获取sso返回的token
        accessToken = response['data']['token']
        self.accessToken = accessToken
        logger.info(accessToken)
        # 调用sso checkToken接口校验token有效性
        c_path = '/api/checkToken'
        c_params = dict()
        c_params['token'] = accessToken
        c_params['appFlag'] = ''
        c_params['applicationToken'] = ''
        logger.info('c_params: %s' % c_params)
        c_response = HttpUtil().do_post(c_path, c_params)
        logger.info('c_response: %s' % c_response)
        # 调用sso selectTenant接口,获取applicationToken
        selectTenant_path = '/api/selectTenant'
        selectTenant_params = dict()
        selectTenant_params['accessToken'] = ''
        selectTenant_params['loginToken'] = accessToken
        selectTenant_params['tenantId'] = 6
        selectTenant_response = HttpUtil().do_post(selectTenant_path, selectTenant_params)
        self.accessToken = selectTenant_response['data']['token']

    def do_get(self, path):
        url = self.url + path
        logger.info('>>>request url is: %s' % url)
        try:
            r = requests.get(url=url, headers=self.headers)
            logger.info('>>>header: %s' % self.headers)
            r.encoding = 'UTF-8'
            json_response = r.json()
            logger.info('>>>response: %s' % json_response)
            return json_response
        except Exception as e:
            return {'code': 1, 'result': 'get请求出错，出错原因:%s' % e}

    def do_get_with_params(self, path, params):
        url = self.url + path
        logger.info('>>>request url is: %s' % url)
        try:
            r = requests.get(url=url, params=params, headers=self.headers)
            r.encoding = 'UTF-8'
            json_response = r.json()
            logger.info('>>>response: %s' % json_response)
            return json_response
        except Exception as e:
            logger.info(e)
            return {'code': 1, 'result': 'get请求出错，出错原因:%s' % e}

    def do_post(self, path, params):
        if path == '/api/login' or path == '/api/checkToken' or path == '/api/selectTenant':
            url = self.sso_url + path
        else:
            url = self.url + path
        logger.info('>>>request url %s' % url)
        params = json.dumps(params)
        logger.info('>>>params %s' % params)
        try:
            r = requests.post(url=url, data=params, headers=self.headers)
            json_response = r.json()
            logger.info('>>>response: %s' % json_response)
            if 200 == r.status_code:
                return json_response
        except Exception as e:
            logger.info(e)
            return {'code': 1, 'result': 'post请求出错，出错原因: %s' % e}

    def del_file(self, path, params):
        url = self.url + path
        try:
            del_word = requests.delete(url=url, data=params, headers=self.headers)
            json_response = del_word.json()
            return {'code': 0, 'result': json_response}
        except Exception as e:
            return {'code': 1, 'result': 'del请求出错，出错原因:%s' % e}

    def put_file(self, path, params):
        url = self.url + path
        try:
            params = json.dumps(params)
            me = requests.put(url=url, data=params)
            json_response = me.json()
            return {'code': 0, 'result': json_response}
        except Exception as e:
            return {'code': 1, 'result': 'put请求出错，出错原因:%s' % e}