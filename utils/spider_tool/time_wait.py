# @Time    : 7/22/2020 9:35 AM
# @Author  : Yang Xiaobai
# @Email   : yangzhiyongtest@163.com
import time

from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.wait import WebDriverWait


class TimeWait:
    def __init__(self):
        pass
    
    # sleep
    def sleepWait(self,timeW):
        time.sleep(timeW)
        
    # 隐式等待固定时间
    def implicitlyWait(self,timeW,driver):
        driver.implicitly_wait(timeW)
        return driver
    
    # 隐式等待，元素出现
    def WebDriverWaitW(self,driverDR,needFind='yes',someId = None,lambdaform= None,timeoutNum=10,pollFrequency=0.5):
        '''
        driver - 浏览器驱动
        timeout - 超时前的秒数
        poll_frequency - 时间隔间的秒数，默认0.5s
        ignored_exceptions - 调用期间忽略的异常类的可迭代结构。默认情况下，它仅包含NoSuchElementException
        :return:
        '''
        if needFind == "yes":
            if lambdaform != None:
                elementData = lambdaform
            else:
                elementData=lambda x: x.find_element_by_id(someId)
            element = WebDriverWait(driverDR, timeoutNum,pollFrequency).until(elementData)
            return element
        #是消失的
        elif needFind == 'no':
            if lambdaform != None:
                elementDisapeared = lambdaform
            else:
                elementDisapeared=lambda x: x.find_element_by_id(someId).is_displayed()
            is_disappeared = WebDriverWait(driverDR, timeoutNum, pollFrequency, (ElementNotVisibleException)).until_not(elementDisapeared)
            return is_disappeared
        
        
        
if __name__ == "__main__":
    tw=TimeWait()
    # tw.sleepWait(10)
    # print(1)
    # dr = tw.implicitlyWait()implicitlyWait