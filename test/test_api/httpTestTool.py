# @Time ： 2020/7/1 22:39
# @Auth ： Yang Xiaobai
# @Email:  yangzhiyongtest@163.com
import json

import requests

from utils.config_tool.request_header import RequestHeader


def httpRequests(urlData=None,dataData=None,headersData=None):
	dataData = json.dumps(dataData, ensure_ascii=False)
	resultData = requests.post(url=urlData,data=dataData,headers=headersData,verify=False)
	if resultData.status_code == 200:
		resultData = resultData.text
		resultData = json.loads(resultData,encoding='utf-8')
		return resultData
	else:
		return "请求失败"
	
	
if __name__ == "__main__":
	urlData = "https://uat-pms-sso.hopsontong.com:11013/api/login"
	dataData = {"mobile":"15718868478","appFlag":"easylife-cms-api-gateway","afsSessionId":"WjFlCkIWDpHT9odN","afsSig":"QuAncgq0hrmAVNX0","afsToken":"FFFF0N00000000009184:1591688607383:0.9844042761792562","afsScene":"nc_login","password":"123456"}
	headersData = RequestHeader.WEBHEADER
	resultl=httpRequests(urlData=urlData, dataData=dataData, headersData=headersData)
	print(resultl)
	