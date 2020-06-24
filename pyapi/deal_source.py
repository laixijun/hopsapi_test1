# @Time ： 2020/6/21 00:50
# @Auth ： Yang Xiaobai
# @Email:  yangzhiyongtest@163.com
from datetime import datetime
import json

from pyapi.get_source import SourceGet
from utils.api_tools.api_classfication import ApiClassification
from utils.api_tools.para_analysis import ParaAnalysis
from utils.api_tools.result_assert import ResultAssert
from utils.api_tools.url_classfication import UrlClassfication
from utils.config_tool.file_config_path import ExcelConfig
from utils.logger import Log
from utils.new_tools.excel_tool import ExcelTool, DealExcelTool

logger = Log(logger='deal_source').get_log()
class SourceDeal:
	def __init__(self):
		pass

	# 获取用例
	def dealTestCase(self):
		pass

	# 完成一次请求
	'''
	lstNum 业务编号用例
	'''
	def operationDeal(self,lstNum):
		testCaseList=SourceGet().getIdOfTestOperate(lstNum)
		responseValue= None
		resultList = []
		responseValue={}
		responseValue['headers']=None
		responseValue['text']=None
		testCaseDict = {}
		for testCaseListItem in testCaseList:
			resultCaseList = testCaseListItem[:3]
			resultList.append(resultCaseList)
			requestMethod = testCaseListItem[5]
			logger.info(requestMethod)
			requestUrl = UrlClassfication().estimateUrl(testCaseListItem)
			logger.info(requestUrl)
			requestHeader = ParaAnalysis().chooseHeader(caseList=testCaseListItem,responseValue=responseValue["headers"])
			logger.info(requestHeader)
			requestData = ParaAnalysis().choosePara(caseList=testCaseListItem,responseValue=responseValue['text'])
			logger.info(requestData)
			a = datetime.now()
			resultRequst=ApiClassification(headerData=requestHeader).requestEstimate(methodRequest=requestMethod, urlRequest=requestUrl, dataRequest=requestData)
			b = datetime.now()
			# 执行时间 durn
			durn = (b - a).seconds
			logger.info(resultRequst)
			# 是否执行通过 isPass
			isPass = None
			if resultRequst['status_code']==200:
				compareResults=ResultAssert().compareResult(jsonActual=resultRequst['text'],jsonExpect=testCaseListItem[8])
				if compareResults['reusltFinal'] == 'N':
					isPass = 'FAIL'
					failReason = compareResults['FAIL']
					# 失败response
					failResponse = resultRequst['text']
					# 失败request
					failRequests = requestData
				else:
					isPass = 'SUC'
			else:
				isPass = 'FAIL'
				# 失败原因 failReason
				failReason = resultRequst['text']
			resultList.append(durn)
			resultList.append(isPass)
			if isPass == "FAIL":
				resultList.append(failReason)
				resultList.append(failResponse)
				resultList.append(failRequests)
			resultList.append(isPass)
			responseValue=resultRequst
			testCaseDict[testCaseListItem[1]]=resultList
		return testCaseDict
	
	# 将业务编号循环执行
	def operationAllDeal(self):
		operateId = SourceGet().getOperateId()
		excelRow=None
		for operateIdKey in operateId.keys():
			resultDic=self.operationDeal(operateId[operateIdKey])
			resultDic = json.dumps(resultDic,ensure_ascii=False)
			resultDic = json.loads(resultDic,encoding='utf-8')
			rte=self.resultToExcel(testCaseDict=resultDic,excelRow=excelRow)
			excelRow=rte['excelRow']
		rte['et'].saveWorkbook(pathFile=ExcelConfig.REPORTPATHSHEETCURRENT)
	# 将测试结果写入到Excel
	def resultToExcel(self,testCaseDict,excelRow=None):
		rte={}
		et=ExcelTool(excelFile=DealExcelTool().getReportFileName(),sheetName=ExcelConfig.REPORTPATHSHEET)
		if excelRow != None:
			excelRow = excelRow
		else:
			excelRow=2
		for i in testCaseDict.keys:
			et.writeCellRow(list=testCaseDict[i],row=excelRow,column=1)
			excelRow += 1
		# et.saveWorkbook()
		rte['excelRow']=excelRow
		rte['et']=et
		return rte