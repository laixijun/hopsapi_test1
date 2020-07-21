# @Time    : 7/21/2020 6:19 PM
# @Author  : Yang Xiaobai
# @Email   : yangzhiyongtest@163.com
from pyapi.scrapyApi.appium_app.get_driver import GetDriver


class SpiderDemo:
    def __init__(self):
        self.driver = GetDriver().chooseDriver()
    
    #点击始终允许
    def always(self):
        alwaysbutton=self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
        alwaysbutton.click()
        alwaysbutton = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
        alwaysbutton.click()
        
        


if __name__ == "__main__":
    SpiderDemo().always()
