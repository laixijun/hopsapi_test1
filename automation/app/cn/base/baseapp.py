#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2020/3/4 16:17
# @Author  : vivid
# @FileName: baseapp.py
# @Software: PyCharm
# @email    ：331597811@QQ.com
from automation.util.LoggerUtil import Log
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
class BaseApp:
    logger = Log().logger()
    def __init__(self,driver):
        self.driver = driver

    def implicitly_wait(self):
        time.sleep(2)
        self.driver.implicitly_wait(10)

    def getElementByElement(self, page_keyword, ui_keyword):
        """
        返回定位的单个元素
        :param page_keyword:
        :param ui_keyword:
        :return:
        """
        self.logger.info("点击【%s】的【%s】元素", page_keyword, ui_keyword)
        self.implicitly_wait()
        return self.driver.find_element(page_keyword,ui_keyword)

    def getElementByElements(self, page_keyword, ui_keyword):
        """
        返回定位的单个元素
        :param page_keyword:
        :param ui_keyword:
        :return:
        """
        self.logger.info("点击【%s】的【%s】元素", page_keyword, ui_keyword)
        self.implicitly_wait()
        return self.driver.find_elements(page_keyword,ui_keyword)

    def click(self, driver_ele):
        """
        点击方法
        :param page_keyword:
        :param ui_keyword:
        :return:
        """
        self.logger.info("点击【%s】元素",driver_ele)
        self.driver.implicitly_wait(5)
        self.highlight(driver_ele)
        driver_ele.click()

    def sendkeys(self,elements,ele_value):
        self.logger.info("通过【%s】的元素，录入信息为：【%s】",elements, ele_value)
        self.implicitly_wait()
        self.highlight(elements)
        elements.send_keys(ele_value)

    def save_img(self,img_path,time_stamp):
        """
        截图
        :img_path :图片路径
        :time_stamp: 获取时间格式
        :return:
        """
        self.implicitly_wait()
        self.driver.get_screenshot_as_file("%s/error%s.png" %(img_path,time_stamp))

    def get_text(self,driver_ele):
        """
        获取文本内容
        :param driver_ele:  driver_ele = self.driver.find_elements(page_keyword, ui_keyword)
        :return:
        """
        self.logger.info("获取文本内容【%s】", self.driver_ele.text)
        self.implicitly_wait()
        return self.driver_ele.text

    def get_size(self):
        """
        获取手机屏幕尺寸
        :return:
        """
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x,y

    def swipLeft(self):
        """
        左滑
        :return:
        """
        appsize = self.get_size()
        x1 = int(appsize[0]*0.9)
        y1 = int(appsize[1]*0.5)
        x2 = int(appsize[0]*0.1)
        self.driver.swipe(x1,y1,x2,y1,1000)

    def swipeUp(self):
        """
        上滑
        :return:
        """
        appsize = self.get_size()
        x1 = int(appsize[0] * 0.5)
        y1 = int(appsize[1] * 0.95)
        y2 = int(appsize[1] * 0.35)
        self.driver.swipe(x1, y1, x1, y2, 1000)

    def swipeDown(self):
        """
        下滑
        :return:
        """
        appsize = self.get_size()
        x1 = int(appsize[0] * 0.5)
        y1 = int(appsize[1] * 0.35)
        y2 = int(appsize[1] * 0.85)
        self.driver.swipe(x1, y1, x1, y2, 1000)

    def swipeRight(self):
        """
        右滑
        :return:
        """
        appsize = self.get_size()
        y1 = int(appsize[1] * 0.5)
        x1 = int(appsize[0] * 0.25)
        x2 = int(appsize[0] * 0.95)
        self.driver.swipe(x1, y1, x2, y1, 1000)


    def get_driver(self):
        """
        返回当前驱动
        :return:
        """
        self.logger.info("返回当前驱动")
        self.implicitly_wait()
        return self.driver