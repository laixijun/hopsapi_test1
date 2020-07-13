# @Time ： 2020/6/22 00:25
# @Auth ： Yang Xiaobai
# @Email:  yangzhiyongtest@163.com
import json

import jsonpath

from utils.logger import Log
from utils.new_tools.common_tool import Common

logger = Log(logger='result_assert').get_log()
class ResultAssert:
	def __init__(self):
		pass

	def paraToExpectExchangeData(self, ExpectPara, ExpectData):
		for para_item in ExpectPara.keys():
			strKey = para_item
			strValue = ExpectPara[strKey]
			ExpectDataJson = Common().replaceStr(ExpectData, strKey, strValue)
			ExpectData = ExpectDataJson
			logger.info(ExpectDataJson)
		logger.info(ExpectDataJson)
		return ExpectDataJson

	# 编列预期结果与实际结果对比
	def compareResult(self,jsonActual,jsonExpect,testCaseID,parameterCase=None):
		compareResult = {}
		compareResults = {}
		compareResults['SUC']={}
		compareResults['FAIL']={}
		if parameterCase != None:
			try:
				parameterCase = parameterCase[3]
				parameterCase = json.loads(parameterCase, encoding='utf-8')
				for testCaseIdParameter in parameterCase.keys():
					if testCaseID == testCaseIdParameter:
						parameterCasePara = parameterCase[testCaseIdParameter]
						ExpectDataJson = self.paraToExpectExchangeData(ExpectPara=parameterCasePara,
																		ExpectData=jsonExpect)
				logger.info(ExpectDataJson)
				jsonExpect=ExpectDataJson
			except:
				jsonExpect=jsonExpect
		if isinstance(jsonActual,str):
			jsonActual = json.loads(jsonActual,encoding='utf-8')
		logger.info(jsonActual)
		logger.info(type(jsonActual))
		logger.info(jsonExpect)
		logger.info(type(jsonExpect))
		if isinstance(jsonExpect,str):
			jsonExpect = json.loads(jsonExpect,encoding='utf-8')
		logger.info(jsonExpect)
		logger.info(type(jsonExpect))
		for exItem in jsonExpect.keys():
			if not isinstance(jsonExpect[exItem],str):
				for k,v in jsonExpect[exItem].items():
					getValueFalseList = v.split("-")
					strValue = Common().getJsonValue(mydict=jsonActual, key=exItem,
													 assitValue=getValueFalseList[1], assitKey=getValueFalseList[0])
			else:
				strValue = Common().getJsonValue(mydict=jsonActual, key=exItem)
			actualResult = strValue
			expectValue=jsonExpect[exItem]["jsonExpectValue"]
			if not isinstance(actualResult,str):
				actualResult = str(actualResult)
			if actualResult == expectValue:
				compareResult['executeResult']='SUC'
				compareResults['SUC'][exItem]=compareResult
			else:
				compareResult['executeResult']='FAIL'
				compareResult['failField']=exItem
				compareResult['fieldExpect']=jsonExpect[exItem]
				compareResult['fieldActual']=actualResult

				compareResults['FAIL'][exItem]=compareResult
			compareResult = {}
		if compareResults['FAIL'] != {}:
			compareResults['reusltFinal']='N'
		else:
			compareResults['reusltFinal']='Y'
		return compareResults

