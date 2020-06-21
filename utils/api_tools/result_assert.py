# @Time ： 2020/6/22 00:25
# @Auth ： Yang Xiaobai
# @Email:  yangzhiyongtest@163.com
import json

import jsonpath


class ResultAssert:
	def __init__(self):
		pass

	# 编列预期结果与实际结果对比
	def compareResult(self,jsonActual,jsonExpect):
		compareResult = {}
		compareResults = {}
		compareResults['SUC']={}
		compareResults['FAIL']={}
		jsonActual = json.dumps(jsonActual,ensure_ascii=False)
		for exItem in jsonExpect.keys:
			actualResult = jsonpath.jsonpath(jsonActual,exItem)
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

