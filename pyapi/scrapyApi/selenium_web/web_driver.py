# @Time ： 2020/7/22 00:47
# @Auth ： Yang Xiaobai
# @Email:  yangzhiyongtest@163.com
import platform

from selenium import webdriver

from utils.new_tools.excel_tool import DealExcelTool


class GetDriver:
    def __init__(self):
        pass


    def getDriver(self):
        windowsOrMac = platform.platform()
        if "mac" in windowsOrMac:
            driverPath = DealExcelTool().getMacFirefoxDriver()
        elif "windows" in windowsOrMac:
            driverPath = DealExcelTool().getWindowsFirefoxDriver()
        driver = webdriver.Firefox(executable_path=driverPath)
        return driver




if __name__ == "__main__":
    a= GetDriver().getDriver()
    print(a)