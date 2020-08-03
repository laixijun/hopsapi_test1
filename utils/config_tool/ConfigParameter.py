# @Time ： 2020/6/26 00:23
# @Auth ： Yang Xiaobai
# @Email:  yangzhiyongtest@163.com

# 参数测试
TESTPARAMTER = None
TRANSMITPARAMETER_MODLE = {"transmitData":{"transmitKey":{"transmitValue":"value","transmitDescribe":"describe"}},
					 "parameterData":{"testExecuteID":{"testCaseId":{"parameterValue":{"getValuePath":"value"},"requestData":"data"}}}}
TRANSMITPARAMETER = {"transmitData": {}, "parameterData": {}}
needRequestParameter = {"isDefine": "", "paData": {"urlData": "", "paramData": {
	"brokerPhone": "15718868478",
	"clientId": "8c82592b934908becdc2374e52dbbc7d",
	"password": "123456"
}}}
needRequestSetting = {"isApp": "Y", "isTransmit": {"tokenName": "", "transmitName": ""}}


class WebSelenium:
	WINDOWSFIREFOXDRIVER="geckodriver.exe"
	MACFIREFOXDRIVER="geckodriver"