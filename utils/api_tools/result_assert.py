# @Time ： 2020/6/22 00:25
# @Auth ： Yang Xiaobai
# @Email:  yangzhiyongtest@163.com
import json

import jsonpath

from utils.logger import Log

logger = Log(logger='result_assert').get_log()
class ResultAssert:
	def __init__(self):
		pass

	# 编列预期结果与实际结果对比
	def compareResult(self,jsonActual,jsonExpect):
		compareResult = {}
		compareResults = {}
		compareResults['SUC']={}
		compareResults['FAIL']={}
		if isinstance(jsonActual,str):
			jsonActual = json.loads(jsonActual,encoding='utf-8')
		logger.info(jsonActual)
		logger.info(type(jsonActual))
		if isinstance(jsonExpect,str):
			jsonExpect = json.loads(jsonExpect,encoding='utf-8')
		logger.info(jsonExpect)
		logger.info(type(jsonExpect))
		for exItem in jsonExpect.keys():
			actualResult = jsonpath.jsonpath(jsonActual,exItem)
			actualResult = actualResult[0]
			if not isinstance(actualResult,str):
				actualResult = str(actualResult)
			if actualResult == jsonExpect[exItem]:
				compareResult['executeResult']='SUC'
				compareResults['SUC'][exItem]=compareResult
			else:
				compareResult['executeResult']='FAIL'
				compareResult['failField']='exItem'
				compareResult['fieldExpect']=jsonExpect[exItem]
				compareResult['fieldActual']=actualResult

				compareResults['FAIL'][exItem]=compareResult
			compareResult = {}
		if compareResults['FAIL'] != {}:
			compareResults['reusltFinal']='N'
		else:
			compareResults['reusltFinal']='Y'
		return compareResults

