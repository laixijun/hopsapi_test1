# @Time ： 2020/7/22 00:47
# @Auth ： Yang Xiaobai
# @Email:  yangzhiyongtest@163.com
import platform

from selenium import webdriver

from utils.new_tools.excel_tool import DealExcelTool


class GetDriver:
    def __init__(self):
        self.driver=self.getDriver()


    def getDriver(self):
        windowsOrMac = platform.platform()
        if "mac" in windowsOrMac:
            driverPath = DealExcelTool().getMacFirefoxDriver()
        elif "windows" in windowsOrMac:
            driverPath = DealExcelTool().getWindowsFirefoxDriver()
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
        driver.get(URL)  # 登陆web界面
        driver.maximize_window()  # 窗口最大化
        pageSource=driver.page_source
        print(pageSource)



if __name__ == "__main__":
    a= GetDriver()
    a.loginCms()