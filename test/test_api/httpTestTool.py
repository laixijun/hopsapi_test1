# @Time ： 2020/7/1 22:39
# @Auth ： Yang Xiaobai
# @Email:  yangzhiyongtest@163.com
import requests


def httpRequests(urlData=None,dataData=None,headersData=None):

	resultData = requests.post(url=urlData,data=dataData,headers=headersData)
	if resultData.status_code == 200:
		resultData = resultData.text
		return resultData
	else:
		return "请求失败"