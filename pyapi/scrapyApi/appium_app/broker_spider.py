# @Time    : 7/21/2020 6:19 PM
# @Author  : Yang Xiaobai
# @Email   : yangzhiyongtest@163.com
from pyapi.scrapyApi.appium_app.get_driver import GetDriver
from utils.logger import Log
from utils.spider_tool.time_wait import TimeWait

logger = Log(logger='deal_source').get_log()
class SpiderDemo:
    def __init__(self):
        self.driver = GetDriver().chooseDriver()
        self.tm = TimeWait()
    
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
        xml = self.driver.dump_hierarchy()
        # alwaysbutton=alwaysbutton.
        # alwaysbutton= self.driver.
        logger.info(alwaysbutton)
        logger.info(xml)
        
        
        


if __name__ == "__main__":
    SpiderDemo().always()
