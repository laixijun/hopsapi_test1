# @Time    : 8/13/2020 2:47 PM
# @Author  : Yang Xiaobai
# @Email   : yangzhiyongtest@163.com


import asyncio
import os
#windows
from pyapi.scrapyApi.selenium_web.get_postion import GetPostion
from utils.new_tools.common_tool import Common

DEFAULT_DOWNLOAD_HOST = 'https://npm.taobao.org/mirrors'
#mac
# DEFAULT_DOWNLOAD_HOST = 'http://cdn.npm.taobao.org/mirrors'
os.environ["PYPPETEER_DOWNLOAD_HOST"] = DEFAULT_DOWNLOAD_HOST
from pyppeteer import launch

async def main():
    browser = await launch({'headless': False, 'args': ['--disable-infobars', '--window-size=1920,1080']})
    page = await browser.newPage()
    URL = "https://uat-pms-sso.hopsontong.com:11013/#/"
    width, height = Common().screen_size()
    await page.setViewport({'width': width, 'height': height})
    await page.goto(URL)
    await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
    await page.type('div.mobile > div.el-form-item__content > div.el-input.el-input--suffix > input.el-input__inner', '15718868478')  # 账号
    await page.type('div.password > div.el-form-item__content > div.el-input.el-input--suffix > input.el-input__inner', '123456')  # 密码
    await asyncio.sleep(2)
    dimensions = await page.evaluate('''() => {
                return {
                    width: document.documentElement.clientWidth,
                    height: document.documentElement.clientHeight,
                    deviceScaleFactor: window.devicePixelRatio,
                }
            }''')
    print(dimensions)
    '''
    属性值：
    
    top: 元素上边距离页面上边的距离
    left: 元素右边距离页面左边的距离
    right: 元素右边距离页面左边的距离
    bottom: 元素下边距离页面上边的距离
    width: 元素宽度
    height: 元素高度
    '''
    #{'top': 420.5, 'left': 523, 'right': 843, 'bottom': 454.5, 'width': 320, 'height': 34}
    dimensionsOne = await page.evaluate('''() => {
                    var myDate = new Date();
                    var div = document.getElementById('nc_1__scale_text');
                    var offset1 = div.tagName;
                    var reactObj = div.getBoundingClientRect();
                    var num = 0
                    while (reactObj=={} && num <10){
                        var reactObj = div.getBoundingClientRect();
                        num+=1
                        }
                    return{
                        top: reactObj.top,
                        left: reactObj.left,
                        right: reactObj.right,
                        bottom: reactObj.bottom,
                        width: reactObj.width,
                        height: reactObj.height,
                    }
                }''')
    #{'top': 420.5, 'left': 523, 'right': 565, 'bottom': 454.5, 'width': 42, 'height': 34}
    dimensionsTwo = await page.evaluate('''() => {
                        var myDate = new Date();
                        var div = document.getElementById('nc_1_n1z');
                        var offset1 = div.tagName;
                        var reactObj = div.getBoundingClientRect();
                        var num = 0
                        while (reactObj=={} && num <10){
                            var reactObj = div.getBoundingClientRect();
                            num+=1
                            }
                        return{
                            top: reactObj.top,
                            left: reactObj.left,
                            right: reactObj.right,
                            bottom: reactObj.bottom,
                            width: reactObj.width,
                            height: reactObj.height,
                        }
                    }''')
    
    # await page.evaluate(reactObj="document.getElementById('nc_1__scale_text')",force_expr=True)
    print(dimensionsOne,dimensionsTwo)
    slider = await page.Jeval('#nocaptcha', 'node => node.style')  # 是否有滑块，ps：试了好多次都没出滑块
    if slider:
        print('出现滑块')
    await page.click('#J_SubmitStatic')
    await asyncio.sleep(5)
    cookie = await page.cookies()
    print(cookie)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())