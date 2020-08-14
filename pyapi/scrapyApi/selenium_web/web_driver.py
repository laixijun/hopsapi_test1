# @Time ： 2020/7/22 00:47
# @Auth ： Yang Xiaobai
# @Email:  yangzhiyongtest@163.com
import json
import platform
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

from pyapi.scrapyApi.selenium_web.get_postion import GetPostion
from utils.logger import Log
from utils.new_tools.common_tool import Common
from utils.new_tools.excel_tool import DealExcelTool

logger = Log(logger='web_driver').get_log()
class GetDriver:
    def __init__(self,brower=None):
        self.driver=self.getDriver(brower)

    # fireofx 浏览器
    def getDriver(self,brower=None):
        windowsOrMac = platform.platform()

        print(windowsOrMac)
        if "mac" in windowsOrMac:
            driverPath = DealExcelTool().getMacFirefoxDriver(brower)
        elif ("windows" in windowsOrMac) or ("Windows" in windowsOrMac):
            driverPath = DealExcelTool().getWindowsFirefoxDriver(brower)
            print(driverPath)
        if brower=="firefox":
            driver = webdriver.Firefox(executable_path=driverPath)
        else:
            driver = webdriver.Chrome(executable_path=driverPath)
        return driver
    # chrome 浏览器
    def getDriver1(self):
        windowsOrMac = platform.platform()

        print(windowsOrMac)
        if "mac" in windowsOrMac:
            driverPath = DealExcelTool().getMacFirefoxDriver()
        elif ("windows" in windowsOrMac) or ("Windows" in windowsOrMac):
            driverPath = DealExcelTool().getWindowsFirefoxDriver()
            print(driverPath)
        driver = webdriver.Firefox(executable_path=driverPath)
        return driver

    #获取当前界面的URL
    def getUrl(self):
        now_url = self.driver.current_url
        print('当前页面的url为：{0}'.format(now_url))
        return now_url

    def loginCms(self):
        driver=self.driver
        URL="https://uat-pms-sso.hopsontong.com:11013/#/"
        obj={"mobile":15718868478,"appFlag":None,"afsSessionId":"WjFlCkIWDpHT9odN","afsSig":"QuAncgq0hrmAVNX0","afsToken":"FFFF0N00000000009184:1591688607383:0.9844042761792562","afsScene":"nc_login","password":"123456"}
        driver.get(URL)  # 登陆web界面
        driver.maximize_window()  # 窗口最大化
        pageSource=driver.page_source
        obj=json.dumps(obj,ensure_ascii=False)
        jsData = GetPostion().jsLogin(url=URL,obj=obj)
        a=driver.execute_script(jsData)
        print(a)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/form/div[1]/div/div/input').send_keys("15718868478")
        driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/form/div[2]/div/div/input').send_keys("123456")
        button=driver.find_element_by_xpath('//*[@id="nc_1_n1z"]')
        langDiv=driver.find_element_by_xpath('//*[@id="nc_1__scale_text"]')
        jsData=GetPostion().jsLocation()
        a=driver.execute_script(jsData)
        print(a)
        divLang=langDiv.size
        buttonLang=button.size
        langH=divLang["width"]-buttonLang["width"]
        langH=int(langH)
        logger.info(divLang,buttonLang)
        flag = 0
        distance = 195
        offset = 5
        times = 0
        while 1:
            action = ActionChains(driver)
            action.click_and_hold(button).perform()
            action.reset_actions()  # 清除之前的action
            logger.info(distance)
            # track = Common().get_track(distance)
            for i in range(langH,langH+1):
                # action.move_by_offset(xoffset=1, yoffset=0).perform()
                action.move_by_offset(xoffset=i, yoffset=0).perform()
                sleep(0.5)
                action.release().perform()
                try:
                    alert = driver.find_element_by_xpath('//*[@id="nc_1__scale_text"]/span/b').text
                    sleep(0.5)
                    action.release().perform()
                    if "通过" in alert:
                        logger.info("ok")
                except:
                    try:
                        alert = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/form/div[3]/div/div/span/a[1]").text
                        if "刷新" in alert:
                            driver.find_element_by_xpath("/html/body/div/div/div[1]/div/form/div[3]/div/div/span/a[1]").click()
                    except:
                        action.reset_actions()
                sleep(0.5)
                action.release().perform()
            sleep(5)
    
            # 判断某元素是否被加载到DOM树里，并不代表该元素一定可见
            try:
                alert = driver.find_element_by_xpath('//*[@id="nc_1__scale_text"]/span/b').text
                logger.info(alert)
            except Exception as e:
                logger.info('get alert error: %s' % e)
                alert = ''
            if alert:
                logger.info(u'滑块位移需要调整: %s' % alert)
                distance -= offset
                times += 1
                sleep(5)
            else:
                logger.info('滑块验证通过')
                flag = 1
                # driver.switch_to.parent_frame()  # 验证成功后跳回最外层页面
                break

        sleep(2)
        driver.quit()
        logger.info("finish~~")
        return flag

        print(pageSource)



if __name__ == "__main__":
    a= GetDriver()
    a.loginCms()