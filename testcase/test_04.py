# @Time    : 6/18/2020 5:53 PM
# @Author  : Yang Xiaobai
# @Email   : yangzhiyongtest@163.com
import unittest

from utils.logger import Log

logger = Log(logger='LoginTest').get_log()

class BatchDeal(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass