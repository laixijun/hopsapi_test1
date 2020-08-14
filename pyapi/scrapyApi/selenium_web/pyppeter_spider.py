# @Time ： 2020/8/14 00:11
# @Auth ： Yang Xiaobai
# @Email:  yangzhiyongtest@163.com

'''
https://miyakogi.github.io/pyppeteer/reference.html  api

'''

import asyncio
import os
DEFAULT_DOWNLOAD_HOST = 'https://npm.taobao.org/mirrors/'
os.environ["PYPPETEER_DOWNLOAD_HOST"] = DEFAULT_DOWNLOAD_HOST
from pyppeteer import launch

width, height = 1366, 768

async def main():
    browser = await launch(headless=False,
                           args=[f'--window-size={width},{height}'])
    page = await browser.newPage()
    await page.setViewport({'width': width, 'height': height})
    await page.goto('https://www.taobao.com')
    await page.evaluate(
        '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
    await asyncio.sleep(100)

asyncio.get_event_loop().run_until_complete(main())
