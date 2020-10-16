# @Time    : 7/21/2020 5:13 PM
# @Author  : Yang Xiaobai
# @Email   : yangzhiyongtest@163.com
from appium import webdriver

from utils.logger import Log

logger = Log(logger='deal_source').get_log()
class GetDriver:
    def __init__(self):
        pass
    
    # Android data
    def getAndroidData(self):
        data ={
            "platformName": "Android",
            "platformVersion": "7.0",
            "deviceName": "Galaxy S6 edge+",
            "appPackage": "com.easylife.house.broker.test",
            "appActivity": "com.easylife.house.broker.ui.MainActivity",
            "resetKeyboard": "true"
        }
        return data
    
    # Android setData
    def setAndroidData(self,field,value):
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
    def chooseDriver(self,platform="ANDROID",field=None, value=None):
        if platform == "ios" or platform == "IOS":
            data = self.setIosData(field=field,value=value)
        elif platform == "android" or platform == "ANDROID":
            data = self.setIosData(field=field,value=value)
        else:
            logger.info("如果是Android平台请输入“ANDROID”，如果是ios平台请输入“IOS”")
        driver = webdriver.Remote('http://localhost:4723/wd/hub', data)
        return driver


if __name__ == "__main__":
    data=GetDriver().setAndroidData("platformVersion","9.0")
    print(data)
    