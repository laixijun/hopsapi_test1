import unittest
from utils import getParams
from utils.httpUtil import HttpUtil
from utils.logger import Log
logger = Log(logger='cms_Members').get_log()


class MembersTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.path = getParams.get_url('members', 'getMemberList')
        HttpUtil.get_token()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test01_getMemberList(self):
        params = getParams.get_params('members', 'getMemberList')
        resp_c = getParams.get_resp_params('members', 'getMemberList', 'code')
        resp_m = getParams.get_resp_params('members', 'getMemberList', 'msg')
        response = HttpUtil().do_post(self.path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test02_getMemberInfo(self):
        params = getParams.get_params('members', 'getMemberInfo')
        path = getParams.get_url('members', 'getMemberInfo')+'/'+params
        resp_c = getParams.get_resp_params('members', 'getMemberInfo', 'code')
        resp_m = getParams.get_resp_params('members', 'getMemberInfo', 'msg')
        response = HttpUtil().do_get(path)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])

    def test03_getMemberVipBeyRecords(self):
        params = getParams.get_params('members', 'vipBeyRecords')
        path = getParams.get_url('members', 'vipBeyRecords')
        resp_c = getParams.get_resp_params('members', 'vipBeyRecords', 'code')
        resp_m = getParams.get_resp_params('members', 'vipBeyRecords', 'msg')
        response = HttpUtil().do_get_with_params(path, params)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])
