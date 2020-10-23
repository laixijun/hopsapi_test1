# @Time    : 7/21/2020 6:19 PM
# @Author  : Yang Xiaobai
# @Email   : yangzhiyongtest@163.com
import os
from time import sleep

from pyapi.scrapyApi.appium_app.get_driver import GetDriver
from utils.logger import Log
from utils.spider_tool.time_wait import TimeWait

logger = Log(logger='deal_source').get_log()
class SpiderDemo:
    def __init__(self):
        self.driver = GetDriver().chooseDriver()
        self.tm = TimeWait()
    #启动APP
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
    # 登录APP
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
        el2 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[10]/android.view.View")
        el2.click()
        sleep(3)
        el3 = driver.find_element_by_id("com.easylife.house.broker.test:id/button_apply")
        el3.click()
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
        el1 = driver.find_element_by_id("com.easylife.house.broker:id/tvOwnerPhone")
        el1.send_keys("15700000006")
        el2 = driver.find_element_by_id("com.easylife.house.broker:id/tvOwnerEmail")
        el2.send_keys("15700000006@163.com")
        el3 = driver.find_element_by_id("com.easylife.house.broker:id/imgAttorney")
        el3.click()
        sleep(3)
        el4 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[9]/android.view.View")
        el4.click()
        sleep(3)
        el5 = driver.find_element_by_id("com.easylife.house.broker:id/button_apply")
        el5.click()
        el6 = driver.find_element_by_id("com.easylife.house.broker:id/tvSubmit")
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
        driver = ta.bankChoose(driver)
        driver = ta.bankBranchChoose(driver)
        driver = ta.areaChoose(driver)
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
        driver = ta.bankChoose(driver)
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
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvBankCardOpenBankAddress")
        el1.click()
        eleArea = driver.find_element_by_id("com.easylife.house.broker.test:id/wheelProvince")
        #滑动5分
        driver = self.swipeUp1(driver, ele=eleArea, t=1000, n=1, startRate=0.4, endRate=0.25)
        eleAreaCity = driver.find_element_by_id("com.easylife.house.broker.test:id/wheelCity")
        driver = self.swipeUp1(driver, ele=eleAreaCity, t=1000, n=1, startRate=0.4, endRate=0.25)
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvOk")
        el1.click()
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
        el1 = driver.find_element_by_id("com.easylife.house.broker.test:id/tvOwnerIDCardValidDate")
        el1.click()
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


if __name__ == "__main__":
    sd=SpiderDemo()
    driver=sd.startApp()
    driver=sd.loginApp(driver,phone='13025896542')
    sleep(5)
    driver= sd.rezhen(driver)
    # driver = sd.companyAuthencition(driver,xinTax='911000001000013428')
    # ta=ToolsAppium()
    # ta.swipeUp(driver)
    # ta.swipeUp(driver)
    # ta.swipeDown(driver)
    

    # sd.myCommission(driver)

