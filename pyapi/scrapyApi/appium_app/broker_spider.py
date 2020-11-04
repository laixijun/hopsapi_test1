# @Time    : 7/21/2020 6:19 PM
# @Author  : Yang Xiaobai
# @Email   : yangzhiyongtest@163.com
import os
from time import sleep
import logging
import time
import pymysql


# from utils.config_tool.configurationEnv import DBSetting
# from utils.logger import Log
# from utils.new_tools.common_tool import Common
# from pyapi.scrapyApi.appium_app.get_driver import GetDriver
# from utils.spider_tool.time_wait import TimeWait
from appium import webdriver
import platform
import re
import openpyxl

# from utils.config_tool.ConfigParameter import WebSelenium
# from utils.config_tool.file_config_path import ExcelConfig

class Log(object):
    """编写日志类，供其他模块调用"""
    def __init__(self, logger):
        # 拼接日志文件夹，如果不存在则自动创建
        report_path = str(os.path.dirname(__file__).split('utils')[0])
        # D:/zhy/haoshenghuo/autoproject/hopsapi_test1/pyapi/scrapyApi/appium_app\\report/logs
        log_path = os.path.join(report_path, 'logs')
        log_path = log_path.replace("\\", "/")
        if not os.path.exists(log_path):
            os.mkdir(log_path)

        # 设置日志文件名称格式及日志等级
        self.log_name = os.path.join(log_path, '%s.log' % time.strftime('%Y-%m-%d'))
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，将日志写入日志文件
        fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')
        fh.setLevel(logging.INFO)

        # 再创建一个handler，将日志输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义日志输出格式
        self.formatter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
        ch.setFormatter(self.formatter)
        fh.setFormatter(self.formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def get_log(self):
        return self.logger
logger = Log(logger='deal_source').get_log()
class SpiderDemo:
    def __init__(self):
        self.driver = GetDriver().chooseDriver()
        # self.tm = TimeWait()
    #启动APP，在首页
    def startApp(self):
        driver=self.driver
        driver.implicitly_wait(10)
        el1 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
        el1.click()
        el2 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
        el2.click()
        sleep(5)
        el3 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvAgreement")
        el3.click()
        return driver
    # 登录APP,登录后在我的界面
    def loginApp(self,driver,phone="15517655129"):
        # driver = self.driver
        el4 = driver.find_element_by_id("com.easylife.house.broker.test:id/tabMine")
        el4.click()
        elementExist = ToolsAppium().is_element_exist(driver=driver, element='常驻城市')
        if elementExist:
            el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/sure")
            el1.click()
        el5 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvlogin")
        el5.click()
        sleep(5)
        el6 = driver.find_element_by_id("com.easylife.house.broker.test:id/edphone")
        el6.send_keys(phone)
        el7 = driver.find_element_by_id("com.easylife.house.broker.test:id/btnLogin")
        el7.click()
        sleep(5)
        elementExist=ToolsAppium().is_element_exist(driver=driver,element='常驻城市')
        if elementExist:
            el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/sure")
            el1.click()
        sleep(3)
        return driver
    # 我的回到首页
    def mineGoHome(self,driver):
        el8 = driver.find_element_by_id("com.easylife.house.broker.test:id/tabIndex")
        el8.click()
        return driver
    # 首页回到我的界面
    def homeGoMine(self,driver):
        sleep(2)
        el9 = driver.find_element_by_id("com.easylife.house.broker.test:id/tabMine")
        el9.click()
        return driver
    
    # 首页进入我的店铺的二维码
    def myStoreQR(self,driver):
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/imgQRCode")
        el1.click()
        return driver
    # 我的钱包、关键数据立即提现、我的界面的待结佣、现金奖励、购物卡奖励入口
    def myCommission(self,driver):
        #我的界面进入首页
        driver = self.mineGoHome(driver)
        #我的钱包进入
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvIndexVolley")
        el1.click()
        sleep(5)
        el2 = driver.find_element_by_id("com.easylife.house.broker.test:id/title")
        el2.click()
        # 结佣记录
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/tv_brokerage_record")
        el1.click()
        el2 = driver.find_element_by_id("com.easylife.house.broker.test:id/action_bar_left_btn")
        el2.click()
        #我的钱包回到首页
        el3 = driver.find_element_by_id("com.easylife.house.broker.test:id/back")
        el3.click()
        sleep(5)
        # 关键输入立即提现进入
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvRedraw")
        el1.click()
        sleep(5)
        # 结佣记录
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/tv_brokerage_record")
        el1.click()
        el2 = driver.find_element_by_id("com.easylife.house.broker.test:id/action_bar_left_btn")
        el2.click()
        # 关键输入立即提现回到首页
        el2 = driver.find_element_by_id("com.easylife.house.broker.test:id/back")
        el2.click()
        sleep(5)
        # 进入我的界面
        driver = self.homeGoMine(driver)
        # 我的界面的待结佣进入
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/llWite")
        el1.click()
        sleep(5)
        # 结佣记录
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/tv_brokerage_record")
        el1.click()
        el2 = driver.find_element_by_id("com.easylife.house.broker.test:id/action_bar_left_btn")
        el2.click()
        # 我的界面待结佣退出
        el2 = driver.find_element_by_id("com.easylife.house.broker.test:id/back")
        el2.click()
        sleep(5)
        # 我的界面现金奖励进入
        el1 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView[2]")
        el1.click()
        sleep(5)
        # 结佣记录
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/tv_brokerage_record")
        el1.click()
        el2 = driver.find_element_by_id("com.easylife.house.broker.test:id/action_bar_left_btn")
        el2.click()
        # 我的界面现金奖励出来
        el2 = driver.find_element_by_id("com.easylife.house.broker.test:id/back")
        el2.click()
        sleep(5)
        # 我的购物卡奖励进入
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/llCard")
        el1.click()
        sleep(5)
        # 结佣记录
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/tv_brokerage_record")
        el1.click()
        el2 = driver.find_element_by_id("com.easylife.house.broker.test:id/action_bar_left_btn")
        el2.click()
        # 我的购物卡奖励退出
        el2 = driver.find_element_by_id("com.easylife.house.broker.test:id/back")
        el2.click()
        sleep(5)
        # 我的界面回到首页
        driver=self.mineGoHome(driver)
        return driver
    # 牵头人佣金
    def lookCommissionData(self,driver):
        # 进入牵头人佣金
        el6 = driver.find_element_by_id("com.easylife.house.broker.test:id/tv_channel")
        el6.click()
        # 结佣记录
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/tv_brokerage_record")
        el1.click()
        el2 = driver.find_element_by_id("com.easylife.house.broker.test:id/action_bar_left_btn")
        el2.click()
        # 退出牵头人佣金，返回我的界面
        el7 = driver.find_element_by_id("com.easylife.house.broker.test:id/action_bar_left_btn")
        el7.click()
        return driver
    # 查看结佣记录(在进入我的佣金已查看)
    def lookCommissionRecord(self):
        pass
    # 企业认证
    def companyAuthencition(self,driver,xinTax):
        driver = self.companyIdentify(driver,xinTax)
        driver = self.bankAccount(driver)
        driver = self.receiveFund(driver)
        driver = self.administratorEntry(driver)
        return driver
        
    
    # 管理员信息录入
    def administratorEntry(self,driver):
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/imgIDCardFront")
        el1.click()
        sleep(3)
        if ToolsAppium().is_element_exist(driver, element='拒绝'):
            el1 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
            el1.click()
            sleep(3)
        el2 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[10]/android.view.View")
        el2.click()
        sleep(3)
        el3 = driver.find_element_by_id("com.easylife.house.broker.test:id/button_apply")
        el3.click()
        sleep(3)
        el4 = driver.find_element_by_id("com.easylife.house.broker.test:id/imgIDCardSide")
        el4.click()
        sleep(3)
        el5 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[12]/android.view.View")
        el5.click()
        sleep(3)
        el6 = driver.find_element_by_id("com.easylife.house.broker.test:id/button_apply")
        el6.click()
        el7 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvOwnerName")
        el7.send_keys("薛业乔")
        el8 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvOwnerIdCardNum")
        el8.send_keys("44010319900822244x")
        # 滑动界面
        ta = ToolsAppium()
        driver = ta.swipeUp(driver)
        sleep(3)
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvOwnerIDCardValidDate")
        el1.click()
        # 证件有效期
        driver = ta.legalSwipeUp(driver)
        sleep(3)
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvOwnerPhone")
        el1.send_keys("15700000006")
        el2 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvOwnerEmail")
        el2.send_keys("15700000006@163.com")
        el3 = driver.find_element_by_id("com.easylife.house.broker.test:id/imgAttorney")
        el3.click()
        sleep(3)
        el4 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[9]/android.view.View")
        el4.click()
        sleep(3)
        el5 = driver.find_element_by_id("com.easylife.house.broker.test:id/button_apply")
        el5.click()
        el6 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvSubmit")
        el6.click()
        sleep(3)
        return driver
    # 收款金额验证
    def receiveFund(self,driver):
        el2 = driver.find_element_by_id("com.easylife.house.broker.test:id/edMoney")
        el2.send_keys("11")
        el3 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvSubmit")
        el3.click()
        sleep(3)
        return driver
    # 企业认证企业信息录入
    def companyIdentify(self,driver,xinTax='911101085636363795'):
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvAuthState")
        el1.click()
        sleep(3)
        el2 = driver.find_element_by_id("com.easylife.house.broker.test:id/btnApply")
        el2.click()
        sleep(3)
        # ToolsAppium().waitWait(driver, idContent='com.easylife.house.broker.test:id/imgBusinessv')
        el3 = driver.find_element_by_id("com.easylife.house.broker.test:id/imgBusiness")
        el3.click()
        sleep(3)
        if ToolsAppium().is_element_exist(driver,element='拒绝'):
            el4 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
            el4.click()
            sleep(3)
        el5 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[9]/android.view.View")
        el5.click()
        sleep(3)
        el6 = driver.find_element_by_id("com.easylife.house.broker.test:id/button_apply")
        el6.click()
        sleep(3)
        el7 = driver.find_element_by_id("com.easylife.house.broker.test:id/edIDCardNum")
        el7.clear()
        sleep(3)
        el7.send_keys(xinTax)
        el8 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvSubmit")
        el8.click()
        sleep(3)
        el9 = driver.find_element_by_id("com.easylife.house.broker.test:id/imgBusiness")
        el9.click()
        sleep(3)
        el10 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[6]/android.view.View")
        el10.click()
        sleep(3)
        el11 = driver.find_element_by_id("com.easylife.house.broker.test:id/button_apply")
        el11.click()
        sleep(3)
        el12 = driver.find_element_by_id("com.easylife.house.broker.test:id/edIDCardNum")
        el12.clear()
        sleep(3)
        el12.send_keys(xinTax)
        # 滑动界面
        ta = ToolsAppium()
        driver=ta.swipeUp(driver)
        driver=ta.dateSwipeUp(driver)
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/edAddress")
        el1.click()
        el2 = driver.find_element_by_id("com.easylife.house.broker.test:id/edAddress")
        el2.send_keys("北京朝阳区")
        driver.hide_keyboard()
        ta.industrySwipeUp(driver)
        ta.scaleSwipeUp(driver)
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/edRegisterMoney")
        el1.click()
        el1.clear()
        el1.send_keys("100000")
        driver.hide_keyboard()
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/edBusinessScope")
        el1.clear()
        el1.send_keys("计算机技术")
        # 法人身份证上传
        driver = ta.swipeUp(driver)
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/imgIDCardFront")
        el1.click()
        sleep(3)
        el2 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[6]/android.view.View")
        el2.click()
        sleep(3)
        el3 = driver.find_element_by_id("com.easylife.house.broker.test:id/button_apply")
        el3.click()
        sleep(3)
        el4 = driver.find_element_by_id("com.easylife.house.broker.test:id/imgIDCardSide")
        el4.click()
        sleep(3)
        el5 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[9]/android.view.View")
        el5.click()
        sleep(3)
        el6 = driver.find_element_by_id("com.easylife.house.broker.test:id/button_apply")
        el6.click()
        sleep(3)
        el2 = driver.find_element_by_id("com.easylife.house.broker.test:id/edOwnerName")
        el2.clear()
        el2.send_keys("薛业乔")
        el3 = driver.find_element_by_id("com.easylife.house.broker.test:id/edOwnerIdCardNum")
        el3.send_keys("44010319900822244x")
        el4 = driver.find_element_by_id("com.easylife.house.broker.test:id/edOwnerPhone")
        el4.send_keys("15700000012")
        sleep(3)
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvOwnerIDCardValidDate")
        el1.click()
        ta.legalSwipeUp(driver)
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvSubmit")
        el1.click()
        sleep(3)
        return driver
    # 银行账号录入
    def bankAccount(self,driver):
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/imgAddBankCard")
        el1.click()
        sleep(3)
        el2 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[6]/android.view.View")
        el2.click()
        sleep(3)
        el3 = driver.find_element_by_id("com.easylife.house.broker.test:id/button_apply")
        el3.click()
        sleep(3)
        el4 = driver.find_element_by_id("com.easylife.house.broker.test:id/edBankCardOwnerName")
        el4.send_keys("工商银行")
        sleep(3)
        el5 = driver.find_element_by_id("com.easylife.house.broker.test:id/edBankCardNum")
        el5.send_keys("12323234")
        sleep(1)
        # 滑动界面
        ta = ToolsAppium()
        driver = ta.swipeUp(driver)
        driver = ta.bankBranchChoose(driver)
        driver = ta.areaChoose(driver)
        driver = ta.bankChoose(driver)
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvSubmit")
        el1.click()
        sleep(3)
        return driver
    # 认证中
    def rezhen(self,driver):
        sleep(3)
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/rl_company_auth")
        el1.click()
        sleep(3)
        el2 = driver.find_element_by_id("com.easylife.house.broker.test:id/btnApply")
        el2.click()
        sleep(3)
        # 滑动界面
        ta = ToolsAppium()
        driver = ta.swipeUp(driver)
        driver = ta.bankBranchChoose(driver)
        driver = ta.areaChoose(driver)
        driver = ta.bankChoose(driver)
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvSubmit")
        el1.click()
        sleep(3)
        # el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvBankCardOpenBankName")
        # el1.click()
        # el2 = driver.find_element_by_id("com.easylife.house.broker.test:id/edSearch")
        # el2.click()
        # el3 = driver.find_element_by_id("com.easylife.house.broker.test:id/edSearch")
        # el3.click()
        # el3.send_keys("工")
        # # ToolsAppium().keyCode(type='Sougou')
        # sleep(3)
        # driver.keyevent(66)
    # 认证3
    def rezhen3(self,driver):
        sleep(3)
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/rl_company_auth")
        el1.click()
        sleep(3)
        el2 = driver.find_element_by_id("com.easylife.house.broker.test:id/btnApply")
        el2.click()
        sleep(3)
        driver = self.administratorEntry(driver)

    #点击始终允许
    def always(self):
        alwaysbutton=self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
        alwaysbutton.click()
        self.driver.implicitly_wait(30)
        alwaysbutton = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
        alwaysbutton.click()
        # self.tm.WebDriverWaitW(driverDR=alwaysbutton,needFind="yes",someId="com.easylife.house.broker.test:id/tvNewHouse")
        self.driver.implicitly_wait(10)
        # alwaysbutton = self.driver.find_element_by_class_name("android.widget.TextView")
        # 新房点击
        # alwaysbutton = self.driver.find_element_by_id("com.easylife.house.broker.test:id/tvNewHouse")
        # 客户点击
        alwaysbutton = self.driver.find_element_by_id("com.easylife.house.broker.test:id/tabCustomer")
        logger.info(alwaysbutton.text)
        alwaysbutton.click()
        self.driver.implicitly_wait(30)
        alwaysbutton = self.driver.find_elements_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout")
        xml1 = self.driver.page_source
        logger.info(xml1)
        xml2 = self.driver.find_element_by_css_selector("android.widget.EditText")
        print(xml2)

# 获取Excel用例
# 报告写入Excel

#封装工具
class ToolsAppium:
    def __init__(self):
        pass

    from appium import webdriver
    import time
    '''
    #封装翻页类
    class SwipepMethod:
        def __init__(self,driver=None):
            self.pm_size=self.swipSize()

        #获取屏幕尺寸
        def swipSize(self):
            return driver.get_window_size()
    '''
    # 解析校验数据
    def assertExpect(self,expectList,driver):
        sleep(3)
        expectListDic = {}
        itemResult=True
        driverData = driver.page_source
        for item in expectList:
            if item in driverData:
                expectListDic[expectList][item]="Success"
            else:
                expectListDic[expectList][item]['result']="Fail"
                # {"driver":driver,"filename":filename}
                screenShot=self.take_screenShot(driver,item)
                driver = screenShot["driver"]
                expectListDic[expectList][item]['filepath']=screenShot["filename"]
                itemResult = False
        if itemResult == True:
            expectListDic[expectList]["result"]="Success"
        else:
            expectListDic[expectList]["result"] = "Fail"
        return expectListDic
        
    # 截图工具
    def take_screenShot(self, driver,name="takeShot"):
        '''
        
        :param name:
        :return:
        ''''''
        method
        explain: 获取当前屏幕的截图
        parameter
        explain：【name】 截图的名称
        Usage:
        device.take_screenShot(u"个人主页")  # 实际截图保存的结果为：2018-01-13_17_10_58_个人主页.png
        '''
        day = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        fq = "./screenShots/" + day
        # fq =os.getcwd()[:-4] +‘screenShots\\‘+day    根据获取的路径，然后截取路径保存到自己想存放的目录下
        tm = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
        type = '.png'
        filename = ""
        if os.path.exists(fq):
            filename = fq + "/" + tm + "_" + name + type
        else:
            os.makedirs(fq)
            filename = fq + "/" + tm + "_" + name + type
        # c = os.getcwd()
        # r"\\".join(c.split("\\"))     #此2行注销实现的功能为将路径中的\替换为\\
        driver.get_screenshot_as_file(filename)
        return {"driver":driver,"filename":filename}
    
    # 判断元素是否存在
    def is_element_exist(self, driver,element):
        source = driver.page_source
        print(source)
        if element in source:
            return True
        else:
            return False
    
    # 选择开户地区
    def areaChoose(self,driver):
        sleep(3)
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvBankCardOpenBankAddress")
        el1.click()
        eleArea = driver.find_element_by_id("com.easylife.house.broker.test:id/wheelProvince")
        #滑动5分
        driver = self.swipeUp1(driver, ele=eleArea, t=1000, n=1, startRate=0.4, endRate=0.25)
        eleAreaCity = driver.find_element_by_id("com.easylife.house.broker.test:id/wheelCity")
        driver = self.swipeUp1(driver, ele=eleAreaCity, t=1000, n=1, startRate=0.4, endRate=0.25)
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvOk")
        el1.click()
        sleep(3)
        return driver

    # 开户行选择
    def bankChoose(self,driver):
        el2 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvBankCardOpenBankSubName")
        el2.click()
        sleep(3)
        el3 = driver.find_element_by_id("com.easylife.house.broker.test:id/edSearch")
        el3.click()
        sleep(3)
        el4 = driver.find_element_by_id("com.easylife.house.broker.test:id/edSearch")
        el4.send_keys("工")
        sleep(3)
        # self.keyCode(type='Sougou')
        driver.keyevent(66)
        driver.hide_keyboard()
        el5 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvName")
        el5.click()
        sleep(3)
        return driver
        
    # 开户行支行选择
    def bankBranchChoose(self,driver):
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvBankCardOpenBankName")
        el1.click()
        sleep(3)
        el2 = driver.find_element_by_id("com.easylife.house.broker.test:id/edSearch")
        el2.click()
        sleep(3)
        el3 = driver.find_element_by_id("com.easylife.house.broker.test:id/edSearch")
        el3.send_keys("工")
        # self.keyCode(type='Sougou')
        driver.keyevent(66)
        driver.hide_keyboard()
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvName")
        el1.click()
        sleep(3)
        return driver
    
    # 企业规模（7分）
    def scaleSwipeUp(self,driver):
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvCompanyScale")
        el1.click()
        sleep(3)
        eleScale = driver.find_element_by_id("com.easylife.house.broker.test:id/wheeView_center")
        driver = self.swipeUp1(driver, ele=eleScale, t=1000, n=1)
        el3 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvok")
        el3.click()
        sleep(3)
        return driver
    # 法人信息日期控件
    def legalSwipeUp(self,driver):
        # el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvOwnerIDCardValidDate")
        # el1.click()
        eleyear = driver.find_elements_by_id('com.easylife.house.broker.test:id/year')[0]  # 当前年份元素
        driver = self.swipeUp1(driver, ele=eleyear, t=1000, n=1)
        elemonth = driver.find_element_by_id("com.easylife.house.broker.test:id/month")
        driver = self.swipeUp1(driver, ele=elemonth, t=1000, n=1)
        eleday = driver.find_element_by_id("com.easylife.house.broker.test:id/day")
        driver = self.swipeUp1(driver, ele=eleday, t=1000, n=1)
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/btnSubmit")
        el1.click()
        sleep(3)
        return driver
    # 所属行业滑动选择（5分）
    def industrySwipeUp(self,driver):
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvIndustry")
        el1.click()
        sleep(3)
        eleIndustry = driver.find_element_by_id("com.easylife.house.broker.test:id/wheeView_center")
        driver = self.swipeUp1(driver, ele=eleIndustry, t=1000, n=1,startRate=0.4,endRate=0.25)
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvSubmit")
        el1.click()
        sleep(3)
        eleIndustry = driver.find_element_by_id("com.easylife.house.broker.test:id/wheeView_center")
        driver = self.swipeUp1(driver, ele=eleIndustry, t=1000, n=1, startRate=0.4, endRate=0.25)
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvSubmit")
        el1.click()
        sleep(3)
        eleIndustry = driver.find_element_by_id("com.easylife.house.broker.test:id/wheeView_center")
        driver = self.swipeUp1(driver, ele=eleIndustry, t=1000, n=1, startRate=0.4, endRate=0.25)
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvSubmit")
        el1.click()
        sleep(3)
        eleIndustry = driver.find_element_by_id("com.easylife.house.broker.test:id/wheeView_center")
        driver = self.swipeUp1(driver, ele=eleIndustry, t=1000, n=1, startRate=0.4, endRate=0.25)
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvSubmit")
        el1.click()
        sleep(3)
        return driver
        
    # 通过抓取到时间控件的元素滑动选择日期
    def dateSwipeUp(self,driver,):
        # 选择日期
        driver.find_element_by_id('com.easylife.house.broker.test:id/tvCompanyValidityDate').click()  # 点击日期选择
        eleyear = driver.find_elements_by_id('com.easylife.house.broker.test:id/year')[0]  # 当前年份元素
        print(eleyear)
        driver=self.swipeUp1(driver, ele=eleyear, t=1000, n=1)
        elemonth = driver.find_element_by_id("com.easylife.house.broker.test:id/month")
        driver = self.swipeUp1(driver, ele=elemonth, t=1000, n=1)
        eleday = driver.find_element_by_id("com.easylife.house.broker.test:id/day")
        driver = self.swipeUp1(driver, ele=eleday, t=1000, n=1)
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/btnSubmit")
        el1.click()
        # 选择城市
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvProvince")
        el1.click()
        sleep(3)
        elePrivince = driver.find_element_by_id("com.easylife.house.broker.test:id/wheelProvince")
        driver = self.swipeUp1(driver, ele=elePrivince, t=1000, n=1,startRate=0.4,endRate=0.25)
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvOk")
        el1.click()
        return driver

    # 调用输入法解决输入
    def keyCode(self,type='Sougou'):
        command2='adb shell ime set com.sohu.inputmethod.sogou/.SogouIME'
        command3='adb shell ime set io.appium.android.ime/.UnicodeIME'
        
        # 列出系统现在所安装的所有输入法 os.system(command0)
        # 打印系统当前默认的输入法 os.system(command1)
        # 切换华为输入法为当前输入法 os.system(command2)
        # 切换appnium输入法为当前输入法 os.system(command3)
        if type == 'Sougou':
            os.system(command2)
        elif type == 'Appium':
            os.system(command3)

    # 向上滑动屏幕
    def swipeUp(self,driver, t=1000, n=1):
        l = driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.75  # 起始y坐标
        y2 = l['height'] * 0.25  # 终点y坐标
        for i in range(n):
            driver.swipe(x1, y1, x1, y2, t)
        return driver

    # 向上滑动屏幕(时间控件)(城市控件推荐0.40,0.25)
    def swipeUp1(self, driver,ele=None, t=1000, n=1,startRate=0.35,endRate=0.25):
        loctionD = ele.location
        sizeD=ele.size
        sizeDD = sizeD['width'] * 0.5  # x坐标
        x1=loctionD["x"]+sizeDD
        y1 = loctionD['y']+sizeD['height'] * startRate  # 起始y坐标
        y2 = loctionD['y']+sizeD['height'] * endRate  # 终点y坐标
        for i in range(n):
            driver.swipe(x1, y1, x1, y2, t)
        return driver

    # 向下滑动屏幕
    def swipeDown(self,driver, t=500, n=1):
        l = driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.25  # 起始y坐标
        y2 = l['height'] * 0.75  # 终点y坐标
        for i in range(n):
            driver.swipe(x1, y1, x1, y2, t)
        return driver

    # 向左滑动屏幕
    def swipeLeft(self,driver, t=500, n=1):
        l = driver.get_window_size()
        x1 = l['width'] * 0.75
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.05
        for i in range(n):
            driver.swipe(x1, y1, x2, y1, t)
        return driver

    # 向右滑动屏幕
    def swipRight(self,driver, t=500, n=1):
        l = driver.get_window_size()
        x1 = l['width'] * 0.05
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.75
        for i in range(n):
            driver.swipe(x1, y1, x2, y1, t)
        return driver
        
    # 显式等待
    def waitWait(self,driver,idContent):
        # 引入WebDriverWait
        from selenium.webdriver.support.ui import WebDriverWait
        # 引入expected_conditions类，并重命名为EC
        from selenium.webdriver.support import expected_conditions as EC
        # 引入By类
        from selenium.webdriver.common.by import By
        # 设置等待
        wait = WebDriverWait(driver, 10, 0.5)
        wait.until(EC.presence_of_element_located((By.ID, idContent)))
        return driver

# 断言 log
class AssertResult:
    def __init__(self):
        pass
    
    # unittest断言
    def assertUnittest(self,isUnittest="unittest",expectData=None,actualData=None):
        if isUnittest != None:
            isUnittest.assertEqual(expectData, actualData)
            return True
        else:
            return False
            
    # 自定义断言
    def assertCostom(self,isCustom="custom",expectData=None,actualData=None):
        if not isinstance(expectData,str):
            expectData = str(expectData)
        if not isinstance(actualData,str):
            actualData = str(actualData)
        if isCustom != None:
            try:
                if expectData == actualData:
                    msg = "预期 " + expectData + "实际 " + actualData + ",对比结果为相同"
                    return {"code":1,"msg":msg}
                elif expectData != actualData:
                    msg = "预期 " + expectData + "实际 " + actualData + ",对比结果为不相同"
                    return {"code": 0, "msg": msg}
            except:
                msg = "预期 " + expectData + "实际 " + actualData + ",对比结果为不相同"
                return {"code": 0, "msg": msg}
    # 打印日志
    def assertLog(self,contentData):
        logger.info(contentData)

# 获取driver
class GetDriver:
    def __init__(self):
        pass
    
    # Android data
    def getAndroidData(self):
        data = {
            "platformName": "Android",
            "platformVersion": "7.0",
            "deviceName": "Galaxy S6 edge+",
            "appPackage": "com.easylife.house.broker.test",
            "appActivity": "com.easylife.house.broker.ui.MainActivity",
            "resetKeyboard": "true"
        }
        return data
    
    # Android setData
    def setAndroidData(self, field, value):
        initNum = 0
        if field != None:
            for i in field:
                data = self.getAndroidData()
                data[i] = value[initNum]
                initNum += 1
        else:
            data = self.getAndroidData()
        return data
    
    # ios data
    def getIosData(self):
        data = {
            "platformName": "Android",
            "platformVersion": "7.0",
            "deviceName": "Galaxy S6 edge+",
            "appPackage": "com.easylife.house.broker.test",
            "appActivity": "com.easylife.house.broker.ui.MainActivity",
            "resetKeyboard": "true"
        }
        return data
    
    # ios setData
    def setIosData(self, field=None, value=None):
        initNum = 0
        if field != None:
            for i in field:
                data = self.getAndroidData()
                data[i] = value[initNum]
                initNum += 1
        else:
            data = self.getAndroidData()
        return data
    
    # 返回driver
    def chooseDriver(self, platform="ANDROID", field=None, value=None):
        if platform == "ios" or platform == "IOS":
            data = self.setIosData(field=field, value=value)
        elif platform == "android" or platform == "ANDROID":
            data = self.setIosData(field=field, value=value)
        else:
            logger.info("如果是Android平台请输入“ANDROID”，如果是ios平台请输入“IOS”")
        driver = webdriver.Remote('http://localhost:4723/wd/hub', data)
        return driver
class ExcelTool:
    def __init__(self, excelFile, sheetName=None):
        self.excelFile = excelFile
        if sheetName != None:
            self.sheetName = sheetName
        else:
            self.sheetName = "Sheet1"
        self.work_book = openpyxl.load_workbook(self.excelFile)
    
    # 获取工作表
    def getSheetValue(self):
        sheet = self.work_book[self.sheetName]
        return sheet
    
    # row = xl_sheet.max_row 获取行数
    def getMaxRows(self):
        maxNum = self.getSheetValue().max_row
        return maxNum
    
    # column = xl_sheet.max_column 获取列数
    def getMaxColumn(self):
        maxColumnNum = self.getSheetValue().max_column
        return maxColumnNum
    
    # 获取表格的总行数和总列数
    def get_row_clo_num(self):
        rows = self.getSheetValue().max_row
        columns = self.getSheetValue().max_column
        return rows, columns
    
    # 获取某列的所有值
    def get_col_value(self, column, rowNum=1):
        rows = self.getSheetValue().max_row
        column_data = []
        for i in range(rowNum, rows + 1):
            cell_value = self.getSheetValue().cell(row=i, column=column).value
            if cell_value != None:
                column_data.append(cell_value)
            else:
                break
        return column_data
    
    # 获取某行所有值
    def get_row_value(self, row, columnNum=1):
        columns = self.getSheetValue().max_column
        row_data = []
        for i in range(columnNum, columns + 1):
            cell_value = self.getSheetValue().cell(row=row, column=i).value
            if cell_value != None:
                row_data.append(cell_value)
            else:
                break
        return row_data
    
    # 获取

    # 读取指定位置的值
    def getCellValue(self, row, column):
        cellValue = self.getSheetValue().cell(row, column).value
        return cellValue

    # 获取所有行
    def getAllRowDataToTuple(self):
        rows = self.getSheetValue().rows
        cases = []
        for row in rows:
            row_cases = []
            for cell in row:
                row_cases.append(cell.value)
            cases.append(tuple(row_cases))
        return cases

    # 向指定位置写入数据
    def writeCellValue(self, row, column, rcValue):
        cellIndex = self.getSheetValue().cell(row, column)
        if not isinstance(rcValue, str):
            rcValue = str(rcValue)
        cellIndex.value = rcValue
    
    # 向一行写入一条list
    def writeCellRow(self, list, row, column=1):
        column = column
        for i in list:
            self.writeCellValue(row=row, column=column, rcValue=i)
            column += 1

    # 将工作簿保存
    def saveWorkbook(self, pathFile):
        self.work_book.save(pathFile)
        self.work_book.close()
class DealExcelTool:
    def __init__(self):
        pass
    
    # 读取数据的业务ID数据存放入列表
    def readOpretion(self, idOp, startPostition, endPosition):
        pass
    
    # 获取用例文件的全路径
    def getTestFileName(self):
        testFileName = self.getFilePath() + '/' + ExcelConfig.TESTCASEALLFile
        testFileName = testFileName.replace('\\', '/')
        return testFileName
    
    # 获取报告文件的全路径
    def getReportFileName(self):
        reportFileName = self.getFileReport() + '/' + ExcelConfig.REPORTPATHFILECURRENT
        reportFileName = reportFileName.replace('\\', '/')
        return reportFileName
    
    # 获取报告文件的全路径复制前
    def getReportFilePreName(self):
        reportFileName = self.getFileReport() + '/' + ExcelConfig.REPORTPATHFILE
        reportFileName = reportFileName.replace('\\', '/')
        return reportFileName
    
    # 获取临时存储文件的全路径
    def getTempFileName(self):
        tempDBFileName = self.getProjectPath() + ExcelConfig.TEMPDBFILEPATH
        tempDBFileName = tempDBFileName.replace('\\', '/')
        return tempDBFileName
    
    # 获取mac的Firefox driver的全路径
    def getMacFirefoxDriver(self, name=None):
        if name == "firefox":
            macFirefoxDriver = self.getProjectPath() + ExcelConfig.CONFIGTOOLPATH + WebSelenium.MACFIREFOXDRIVER
        else:
            macFirefoxDriver = self.getProjectPath() + ExcelConfig.CONFIGTOOLPATH + WebSelenium.MACCHROMEDRIVER
        macFirefoxDriver = macFirefoxDriver.replace('\\', '/')
        return macFirefoxDriver
    
    # 获取windows的Firefox driver的全路径
    def getWindowsFirefoxDriver(self, name=None):
        if name == "firefox":
            windowsFirefoxDriver = self.getProjectPath() + ExcelConfig.CONFIGTOOLPATH + WebSelenium.WINDOWSFIREFOXDRIVER
        else:
            windowsFirefoxDriver = self.getProjectPath() + ExcelConfig.CONFIGTOOLPATH + WebSelenium.WINDOWSCHROMEDRIVER
        windowsFirefoxDriver = windowsFirefoxDriver.replace('\\', '/')
        return windowsFirefoxDriver
    
    # 获取用例文件的路径
    def getFilePath(self):
        testCaseFilePath = self.getProjectPath() + ExcelConfig.TESTCASEALL
        return testCaseFilePath
    
    # 获取报告文件的路径
    def getFileReport(self):
        reportFilePath = self.getProjectPath() + ExcelConfig.REPORTPATH
        return reportFilePath
    
    # 获取项目路径
    def getProjectPath(self):
        projectPath = ExcelConfig.PROJECTPATH
        root_path = os.path.abspath(os.path.dirname(__file__))
        root_path = self.changeProjectPath(root_path)
        reform = re.compile("/(.*?)/utils/new_tools", re.S)
        projectPath = reform.findall(root_path)[0]
        root_path = root_path.split(projectPath)[0]
        # proPath = root_path[0]
        # logger.info(proPath)
        proPath = root_path + projectPath
        return proPath

    # 适配不同的系统，获取项目路径
    def changeProjectPath(self, pathGet=None):
        sysPlat = platform.system()
        print(type(sysPlat))
        print(sysPlat)
        if "Windows" in sysPlat:
            print("here")
            pathGet = pathGet.replace('\\', '/')
            print(pathGet)
        return pathGet
class WebSelenium:
	WINDOWSFIREFOXDRIVER="geckodriver.exe"
	MACFIREFOXDRIVER="geckodriver"
	WINDOWSCHROMEDRIVER = "chromedriver84.exe"
	MACCHROMEDRIVER = "chromedriver84"
class ExcelConfig:
    PROJECTPATH = 'hopsapi_test1'
    TESTCASEALL = '/testCase/testCaseAll'
    REPORTPATH = '/report/excelReport'
    TESTCASEALLFile = 'testCase.xlsx'
    TESTCASEALLSHEET = 'testSheet'
    # 参数化的sheet
    PARAMETERCASESHEET = 'parameterSheet'
    REPORTPATHFILE = 'testReport.xlsx'
    REPORTPATHSHEET = 'testReport'
    # 临时存储文本
    TEMPDBFILEPATH = '/db_file/TempDB.txt'
    REPORTPATHFILECURRENT = 'testReport' + str(time.strftime('%Y-%m-%d%H%M%S', time.localtime(time.time()))) + '.xlsx'
    CONFIGTOOLPATH = "/utils/config_tool/"


class MysqlSetting:
    def __init__(self, env):
        self.connect = self.getConnection(env)
        self.cursor = self.getCursor()
    
    def getConnection(self, env):
        if env == "h":
            listi = DBSetting.MYSQLSETTINGH
        elif env == "t":
            listi = DBSetting.MYSQLSETTINGT
        else:
            listi = env
        host = listi["host"]
        user = listi["user"]
        password = listi["password"]
        db = listi["db"]
        port = listi["port"]
        connection = pymysql.connect(host=host,
                                     user=user,
                                     password=password,
                                     port=port,
                                     db=db,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        return connection
    
    def getCursor(self):
        cursor = self.connect.cursor()
        return cursor
    
    # key 是一个元组，包括两个元组，第一个元组是键，第二个是值
    # 插入数据
    def insertData(self, *key, **kwargs):
        cursor = self.cursor
        # Create a new record
        print(key)
        key0 = str(key[0])
        num = len(key[1])
        tableName = kwargs["tableName"]
        valueData = Common().getCValue(num)
        # sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        sql = "INSERT INTO " + tableName + key0 + " VALUES " + valueData
        print(sql)
        print(key[1])
        # cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
        cursor.execute(sql, key[1])
    
    # key 是一个元组，包括两个元组，第一个元组是键，第二个是值
    # 插入数据
    def insertData01(self, *key, **kwargs):
        cursor = self.cursor
        # Create a new record
        print(key)
        key0 = str(key[0][0])
        num = len(key[0][1])
        tableName = kwargs["tableName"]
        valueData = Common().getCValue(num)
        # sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        sql = "INSERT INTO " + tableName + key0 + " VALUES " + valueData
        print(sql)
        print(key[0][1])
        # cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
        cursor.execute(sql, key[0][1])
    
    # 查询数据
    # 传入元组，第一个字符串"(key,key)",第二个传入元组（key),第三个传入值（value），第四个传入表名，tableName=Name,
    # get --[{'id': 2, 'code': '100', 'create_time': datetime.datetime(2020, 8, 10, 14, 8, 21)}]
    def selectData(self, *key, **kwargs):
        # Read a single record
        keyDPatterm = re.compile("\((.*?)\)")
        keyD = keyDPatterm.findall(key[0])[0]
        keyWhere = Common().getSValue(key[1])
        # sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        sql = "SELECT " + keyD + " FROM " + kwargs["tableName"] + " WHERE" + keyWhere
        logger.info(sql)
        logger.info(key[2])
        self.cursor.execute(sql, key[2])
        result = self.cursor.fetchall()
        return result
    
    # 1、 通过where定位查询到实际结果
    def selectDataBind(self, strDbKey, strDbValue):
        DicParameter = Common().expectDB(strDbKey, strDbValue)
        result = self.selectData(DicParameter["expectKey"], DicParameter["locationListKey"],
                                 DicParameter["locationListValue"], tableName=DicParameter["tableName"])
        resultD = Common().compareData(expectDic=DicParameter["expectValue"], actule=result[0])
        return resultD
    
    # 2、 通过sql语句查询
    
    def commitData(self):
        self.connect.commit()
    
    def closeConnect(self):
        self.connect.close()
class Common:
    def __init__(self):
        pass
    # 生成（%s,%s）
    def getCValue(self, num):
        numList = []
        for i in range(num):
            numList.append(1)
        numListStr = str(tuple(numList))
        numListStr = numListStr.replace("1", "%s")
        return numListStr

    # 生成键=值  键=%s
    def getSValue(self, listTu):
        keyWhere = ""
        for key in listTu:
            keyWhere = keyWhere + " and " + key + " = %s "
        # anda = % sandb = % s
        keyWhere = keyWhere[4:]
        return keyWhere
class DBSetting:
    MYSQLSETTINGH={"host":"rm-2zeh739lme9f9hr08eo.mysql.rds.aliyuncs.com","user":"easylife","password":"root123HOPSON","db":"easylife_test","port":3306}
    MYSQLSETTINGT ={"host":"124.127.103.190","user":"root","password":"root123HOPSON","db":"easylife_test","port":40003}
# mangodb
class MangoDBSetting:
    pass


if __name__ == "__main__":
    sd=SpiderDemo()
    driver=sd.startApp()
    # ta=ToolsAppium()
    # driver=ta.take_screenShot(driver,"takeshot")
    # driver=sd.loginApp(driver,phone='15231285090')
    a=driver.page_source
    print(a)
    # sleep(5)
    # # driver= sd.rezhen(driver)
    # # driver= sd.rezhen3(driver)
    # driver = sd.companyAuthencition(driver,xinTax='91110000710933809D')
    # ar=AssertResult()
    # a=ar.assertCostom("custom",2,1)
    # print(a)
    # ar.assertLog("hahaha")
    

