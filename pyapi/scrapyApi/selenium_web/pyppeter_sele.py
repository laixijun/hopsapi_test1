# @Time    : 8/13/2020 2:47 PM
# @Author  : Yang Xiaobai
# @Email   : yangzhiyongtest@163.com


import asyncio
import os
DEFAULT_DOWNLOAD_HOST = 'http://cdn.npm.taobao.org/dist'
os.environ["PYPPETEER_DOWNLOAD_HOST"] = DEFAULT_DOWNLOAD_HOST
from pyppeteer import launch

async def main():
    browser = await launch({'headless': False, 'args': ['--disable-infobars', '--window-size=1920,1080']})
    page = await browser.newPage()
    URL = "https://uat-pms-sso.hopsontong.com:11013/#/"
    URL1='https://login.taobao.com/member/login.jhtml'
    await page.setViewport({'width': 1920, 'height': 1080})
    await page.goto(URL)
    await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
    await page.waitForSelector('div.el-input.el-input--suffix > input', {'timeout': 3000})
    # await page.click('#J_QRCodeLogin > div.login-links > a.forget-pwd.J_Quick2Static')
    await page.type('//*[@id="app"]/div/div[1]/div/form/div[1]/div/div/input', '15718868478')  # 账号
    await page.type('#app > div > div.login-main > div > form > div.el-form-item.password.is-success > div > div > input', '123456')  # 密码
    await asyncio.sleep(5)
    slider = await page.Jeval('#nocaptcha', 'node => node.style')  # 是否有滑块，ps：试了好多次都没出滑块
    if slider:
        print('出现滑块')
    await page.click('#J_SubmitStatic')
    await asyncio.sleep(5)
    cookie = await page.cookies()
    print(cookie)
    await browser.close()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())