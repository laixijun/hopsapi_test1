import unittest
from utils.httpUtil import HttpUtil
from utils import getParams
from utils.logger import Log
logger = Log(logger='LoginTest').get_log()


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.path = getParams.get_url('cms_login', 'login_Sucess')

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    # @unittest.skip
    def test01_login_Sucess(self):
        params = getParams.get_req_params('cms_login', 'login_Sucess')
        logger.info('params: %s' % params)
        resp_c = getParams.get_resp_params('cms_login', 'login_Sucess', 'code')
        resp_m = getParams.get_resp_params('cms_login', 'login_Sucess', 'msg')
        response = HttpUtil().do_post(self.path, params)
        accessToken = response['data']['token']
        HttpUtil.accessToken = accessToken
        logger.info(accessToken)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test02_login_PwdError(self):
        params = getParams.get_req_params('cms_login', 'login_PasswordError')
        logger.info('params: %s' % params)
        resp_c = getParams.get_resp_params('cms_login', 'login_PasswordError', 'code')
        response = HttpUtil().do_post(self.path, params)
        self.assertEqual(resp_c, response['code'])

    def test03_login_PhoneError(self):
        params = getParams.get_req_params('cms_login', 'login_PhoneError')
        logger.info('params: %s' % params)
        resp_c = getParams.get_resp_params('cms_login', 'login_PhoneError', 'code')
        response = HttpUtil().do_post(self.path, params)
        self.assertEqual(resp_c, response['code'])

    def test04_login_PhoneNull(self):
        params = getParams.get_req_params('cms_login', 'login_PhoneNull')
        logger.info('params: %s' % params)
        resp_c = getParams.get_resp_params('cms_login', 'login_PhoneNull', 'code')
        response = HttpUtil().do_post(self.path, params)
        self.assertEqual(resp_c, response['code'])

    def test05_login_PasswordNull(self):
        params = getParams.get_req_params('cms_login', 'login_PasswordNull')
        logger.info('params: %s' % params)
        resp_c = getParams.get_resp_params('cms_login', 'login_PasswordNull', 'code')
        response = HttpUtil().do_post(self.path, params)
        self.assertEqual(resp_c, response['code'])

    def test06_login_TypeError(self):
        params = getParams.get_req_params('cms_login', 'login_TypeError')
        logger.info('params: %s' % params)
        resp_c = getParams.get_resp_params('cms_login', 'login_TypeError', 'code')
        response = HttpUtil().do_post(self.path, params)
        self.assertEqual(resp_c, response['code'])
