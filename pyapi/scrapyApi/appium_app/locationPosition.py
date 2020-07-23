# @Time    : 7/23/2020 3:42 PM
# @Author  : Yang Xiaobai
# @Email   : yangzhiyongtest@163.com


class LocationPosition:
    def __init__(self):
        pass

    # Valid locator strategies for this request: xpath, id, class name, accessibility id, -android uiautomator
    # 1. 通过id定位  driver.find_element_by_id(id - string)
    def locationId(self,driverD,idD):
        eles=driverD.find_element_by_id(idD)
        return (driverD,eles)
    # 2.通过class name定位driver.find_element_by_class_name(class -name)
    def locationClassName(self,driverD,className):
        eles=driverD.find_element_by_class_name(className)
        return (driverD, eles)
    # 3.通过XPATH定位  driver.find_element_by_xpath(xpath)
    def locationXpath(self,driverD,xpathD):
        eles=driverD.find_element_by_xpath(xpathD)
        return (driverD, eles)
    # 4.通过 content-desc字段定位    driver.find_element_by_accessibility_id( content-desc）
    def locationContentDesc(self,driverD,contentDesc):
        eles=driverD.find_element_by_accessibility_id(contentDesc)
        return (driverD, eles)
    # 5. 通过 android uiautomator定位  基本语法：driver.find_element_by_android_uiautomator(xx)
    # 1）通过text定位
    # driver.find_element_by_android_uiautomator('new UiSelector().text("xx"))
    def locationAutoText(self,driverD,autoText):
        eles=driverD.find_element_by_android_uiautomator('new UiSelector().text(' + autoText + ')')
        return (driverD, eles)
    # 2)通过部分文本定位 driver.find_element_by_android_uiautomator('new UiSelector().textContains("部分text文本")')
    def locationAutoContainsText(self,driverD,autoText):
        eles=driverD.find_element_by_android_uiautomator('new UiSelector().textContains(' + autoText + ')')
        return (driverD, eles)
    # 3）通过文本开头定位
    # driver.fine_element_by_android_uiautormator(new UiSelector().textStartsWith("text文本开头"))
    def locationAutoStartsWithText(self,driverD,autoText):
        eles=driverD.find_element_by_android_uiautomator('new UiSelector().textStartsWith(' + autoText + ')')
        return (driverD, eles)
    # B.resource-id、class 、content-desc属性值
    # find_element_by_android_uiautomator(‘new
    # UiSelector().resourceId(“XXXX”)’).click()
    # find_element_by_android_uiautomator(‘new
    # UiSelector().className(“XXXX”)’).click()
    # find_element_by_android_uiautomator(‘new
    # UiSelector().description(“XXXX”)’).click()
    def locationAutoResourceId(self, driverD, autoText):
        eles = driverD.find_element_by_android_uiautomator('new UiSelector().resourceId(' + autoText + ')')
        return (driverD, eles)
    def locationAutoClassName(self, driverD, autoText):
        eles = driverD.find_element_by_android_uiautomator('new UiSelector().className(' + autoText + ')')
        return (driverD, eles)
    def locationAutoDescription(self, driverD, autoText):
        eles = driverD.find_element_by_android_uiautomator('new UiSelector().description(' + autoText + ')')
        return (driverD, eles)
    # 4)通过正则表达式匹配文本
    # driver.fine_element_by_android_uiautormator(new UiSelector().textMatches("正则表达式"))
    def locationAutoTextMatches(self, driverD, autoText):
        eles = driverD.find_element_by_android_uiautomator('new UiSelector().textMatches(' + autoText + ')')
        return (driverD, eles)
    # 6）id和text组合定位
    # id_text = 'resourceId("xx").text("xx")'
    # driver.find_element_by_android_uiautormator(id_text)
    def locationAutoTextMatches(self, driverD, autoId,autoText):
        id_text = 'resourceId('+ autoId +').text('+autoText+')'
        eles = driverD.find_element_by_android_uiautomator(id_text)
        return (driverD, eles)
    # class_text = 'className("xx").text("xx")'
    # driver.find_element_by_android_uiautormator(class_text)
    def locationAutoTextMatches(self, driverD, autoClass, autoText):
        id_text = 'className(' + autoClass + ').text(' + autoText + ')'
        eles = driverD.find_element_by_android_uiautomator(id_text)
        return (driverD, eles)
    # 7)关系定位
    # 父子定位
    # locator = 'resourceId("xx").childSelector(text("xx"))'
    # driver.find_element_by_android_uiautomator(locator)
    def locationAutoChildSelector(self, driverD, autoId,autoText):
        id_text = 'resourceId('+ autoId +').childSelector(text('+autoText+'))'
        eles = driverD.find_element_by_android_uiautomator(id_text)
        return (driverD, eles)
    # 同级元素定位
    # locator = 'resourceId("xx"""兄弟元素id"""").fromParent(text("xx"))'
    # driver.find_element_by_android_uiautomator(locator)
    def locationAutoTextMatches(self, driverD, autoId,autoText):
        id_text = 'resourceId('+ autoId +').fromParent(text('+autoText+'))'
        eles = driverD.find_element_by_android_uiautomator(id_text)
        return (driverD, eles)
    
class Model:
    def test_20a1(self):
        """通讯录-新的朋友"""
        self.driver.implicitly_wait(10)
        self.driver.find_elements_by_id(self.tongxunlu_id)[1].click()
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().text("%s")' % self.tongxunlu_xinde_text).click()
    
    def test_20a2(self):
        """通讯录-新的朋友"""
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")' % self.tongxunlu_text).click()
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().text("%s")' % self.tongxunlu_xinde_text).click()
    
    def test_20b(self):
        """通讯录-新的朋友"""
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().textContains("%s")' % self.tongxunlu_text2).click()
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().textContains("%s")' % self.tongxunlu_xinde_text2).click()
    
    def test_20c(self):
        """通讯录-新的朋友"""
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().textStartsWith("%s")' % self.tongxunlu_text2).click()
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().textStartsWith("%s")' % self.tongxunlu_xinde_text2).click()
    
    def test_20d(self):
        """通讯录-新的朋友"""
        self.driver.implicitly_wait(10)
        self.driver.find_elements_by_android_uiautomator('new UiSelector().resourceId("%s")' % self.tongxunlu_id)[
            1].click()
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().textStartsWith("%s")' % self.tongxunlu_xinde_text2).click()
    
    def test_20e(self):
        """通讯录-新的朋友"""
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("%s").text("%s")' % (self.tongxunlu_id, self.tongxunlu_text)).click()
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().text("%s")' % self.tongxunlu_xinde_text).click()
    
    def test_20f(self):
        """通讯录-新的朋友"""
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().text("%s").className("%s")' % (self.tongxunlu_text, self.tongxunlu_class)).click()
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().text("%s")' % self.tongxunlu_xinde_text).click()
    
    def test_20g(self):
        """通讯录-新的朋友"""
        # 注意！！！class 和 id 相同 其实很多！！！
        self.driver.implicitly_wait(10)
        self.driver.find_elements_by_android_uiautomator(
            'new UiSelector().resourceId("%s").className("%s")' % (self.tongxunlu_id, self.tongxunlu_class))[1].click()
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().text("%s")' % self.tongxunlu_xinde_text).click()
    
    def test_20h(self):
        """通讯录-新的朋友"""
        self.driver.implicitly_wait(10)
        self.driver.find_elements_by_android_uiautomator(
            'new UiSelector().resourceId("%s").className("%s")' % (self.tongxunlu_id, self.tongxunlu_class))[1].click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s").className("%s")' % (
        self.tongxunlu_xinde_text, self.tongxunlu_xinde_class)).click()
    
    def test_20i(self):
        """通讯录-新的朋友"""
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("%s").text("%s")' % (self.tongxunlu_id, self.tongxunlu_text)).click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s").className("%s")' % (
        self.tongxunlu_xinde_text, self.tongxunlu_xinde_class)).click()
    
    def test_21a(self):
        """通讯录-微信团队"""
        self.driver.implicitly_wait(10)
        self.driver.find_elements_by_android_uiautomator('new UiSelector().resourceId("%s")' % self.tongxunlu_id)[
            1].click()
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().description("%s")' % self.weixintuandui_dsec).click()
    
    def test_21b(self):
        """通讯录-微信团队"""
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().textStartsWith("%s")' % self.tongxunlu_text2).click()
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().description("%s")' % self.weixintuandui_dsec).click()
