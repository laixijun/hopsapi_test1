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
needRequestSetting = {"isApp": "Y", "isTransmit": {"tokenName": [["token","token"],["brokerCode","brokerCode"]], "transmitName": ""}}
WEBAPIDIC=("uat-pms-sso.hopsontong.com","cms.lifeat.cn")
LOGINWEBDIC={"mobile":"{userMobile}","appFlag":"easylife-cms-api-gateway","afsSessionId":"WjFlCkIWDpHT9odN",
			 "afsSig":"QuAncgq0hrmAVNX0","afsToken":"FFFF0N00000000009184:1591688607383:0.9844042761792562",
			 "afsScene":"nc_login","password":"{userPD}"}

class WebSelenium:
	WINDOWSFIREFOXDRIVER="geckodriver.exe"
	MACFIREFOXDRIVER="geckodriver"