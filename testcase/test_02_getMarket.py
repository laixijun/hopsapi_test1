import unittest
from utils import getParams
from utils.httpUtil import HttpUtil
from utils.logger import Log
logger = Log(logger='cms_getMarket').get_log()


class NavTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = getParams.get_url('cms_getMarket', 'getMarket')
        HttpUtil.get_token()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test01_getMarket(self):
        resp_c = getParams.get_resp_params('cms_getMarket', 'getMarket', 'code')
        resp_m = getParams.get_resp_params('cms_getMarket', 'getMarket', 'msg')
        response = HttpUtil().do_get(self.url)
        self.assertEqual(resp_c, response['code'])
        self.assertEqual(resp_m, response['msg'])
