#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2020/3/8
# @Author  : vivid-XIEMENG
# @FileName: test_test.py
# @Software: PyCharm
# @email    ：331597811@QQ.com

from appium import  webdriver
from BeautifulReport import BeautifulReport
from automation.util.YamlUtil import  yamlUtil
from automation.util.ConfigUtil import Config
from automation.app.cn.base.capability import Capability
from automation.util.SystemOsUtil import SystemOs
import  unittest

class test_login(unittest.TestCase):
    """
     实现unittest操作，到 run目录运行对应脚本操作
     BeautifulReport记录操作失败截图报告
     """
    def setUp(self):
        conf1 = Config("YamlFile")
        confFile = conf1.get_configPath("borkeryaml")
        brokeryaml = SystemOs().sys_path(confFile)
        data = yamlUtil(brokeryaml).get_yalm()
        # print(data)
        self.driver = Capability(data).app_driver()



    def tearDown(self):
        self.driver.quit()





if __name__=='__main__':
    unittest.main()