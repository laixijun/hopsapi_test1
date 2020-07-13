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
from utils.config_tool.ConfigParameter import TRANSMITPARAMETER
from utils.config_tool.file_config_path import ExcelConfig
from utils.logger import Log
from utils.new_tools.excel_tool import ExcelTool, DealExcelTool
from utils.new_tools.txt_tool import TxtTool

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
	def operationDeal(self,lstNum,parameterCase=None):
		try:
			testCaseList=SourceGet().getIdOfTestOperate(lstNum)
		except:
			logger.info("错误传参",lstNum)
		responseValue= None
		resultList = []
		responseValue={}
		responseValue['headers']=None
		responseValue['text']=None
		testCaseDict = {}
		for testCaseListItem in testCaseList:
			if testCaseListItem[0] == None:
				break
			resultCaseList = testCaseListItem[:4]
			testCaseID = testCaseListItem[1]
			logger.info(testCaseListItem)
			# resultList.append(resultCaseList)
			resultList = resultCaseList
			requestMethod = testCaseListItem[5]
			logger.info(requestMethod)
			logger.info(responseValue['headers'])
			logger.info(responseValue['text'])
			requestData = ParaAnalysis().choosePara(caseList=testCaseListItem, responseValue=responseValue['text'],
													parameterCase=parameterCase)
			# requestData = json.dumps(requestData['requestDataJson'],ensure_ascii=False)
			requestData = requestData['requestDataJson']
			logger.info(requestData)
			logger.info(type(requestData))
			requestHeader = ParaAnalysis().chooseHeader(caseList=testCaseListItem,responseValue=responseValue["headers"])
			logger.info(requestHeader)
			requestUrl = UrlClassfication().estimateUrl(testCaseListItem)
			logger.info(requestUrl)
			a = datetime.now()
			resultRequst=ApiClassification(headerData=requestHeader).requestEstimate(methodRequest=requestMethod, urlRequest=requestUrl, dataRequest=requestData)
			b = datetime.now()
			# 执行时间 durn
			durn = (b - a).microseconds/1000000
			logger.info(resultRequst)
			# 是否执行通过 isPass
			isTwo = None
			if resultRequst['status_code']==200:
				compareResults=ResultAssert().compareResult(jsonActual=resultRequst['text'],jsonExpect=testCaseListItem[8],testCaseID=testCaseID,parameterCase=parameterCase)
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
				if resultRequst['status_code']==200:
					resultList.append(failResponse)
					resultList.append(failRequests)
			# resultList.append(isPass)
			responseValue=resultRequst
			testCaseDict[testCaseListItem[1]]=resultList
		return testCaseDict
	
	# 将业务编号循环执行
	def operationAllDeal(self):
		ttr = TRANSMITPARAMETER
		if not isinstance(ttr, str):
			ttr = json.dumps(ttr, ensure_ascii=False)
		TxtTool().writeTxt(contents=ttr)
		# {'KHGJ002': ['KHGJ002', 3, 4], 'list': ['KHGJ002']}
		operateId = SourceGet().getOperateId()
		# {'KHGJ001': ['KHGJ001', 1, 2], 'KHGJ002': ['KHGJ002', 1, 3], 'list': ['KHGJ001', 'KHGJ002']}
		parameterOperateId = SourceGet().getParameterOperateId()
		excelRow=None
		fileName = None
		fileBool = True
		savaFile = DealExcelTool().getReportFileName()
		logger.info(operateId)
		for operateIdKey in operateId.keys():
			if operateIdKey == "list":
				break
			if operateIdKey in parameterOperateId['list']:
				parameterCaseList=SourceGet().getIdOfParameterOperate(parameterOperateId[operateIdKey])
				for parameterCase in parameterCaseList:
					resultDic = self.operationDeal(lstNum=operateId[operateIdKey],parameterCase=parameterCase)
					# if isinstance(resultDic, str):
					# 	resultDic = json.loads(resultDic, encoding='utf-8')
					logger.info(resultDic)
					logger.info(type(resultDic))
					rte = self.resultToExcel(testCaseDict=resultDic, excelRow=excelRow,fileName=fileName)
					excelRow = rte['excelRow']
					fileName = rte['fileName']
					if fileBool:
						fileName = savaFile
						fileBool = False
					ttr = json.dumps(TRANSMITPARAMETER,ensure_ascii=False)
					TxtTool().writeTxt(contents=ttr)
					rte['et'].saveWorkbook(pathFile=fileName)
			else:
				resultDic=self.operationDeal(operateId[operateIdKey])
				# resultDic = json.dumps(resultDic,ensure_ascii=False)
				if isinstance(resultDic,str):
					resultDic = json.loads(resultDic,encoding='utf-8')
				logger.info(resultDic)
				logger.info(type(resultDic))
				rte=self.resultToExcel(testCaseDict=resultDic,excelRow=excelRow,fileName=fileName)
				excelRow=rte['excelRow']
				fileName = rte['fileName']
				if fileBool:
					fileName = savaFile
					fileBool = False
				ttr = TRANSMITPARAMETER
				if not isinstance(ttr,str):
					ttr = json.dumps(ttr,ensure_ascii=False)
				TxtTool().writeTxt(contents=ttr)
				rte['et'].saveWorkbook(pathFile=fileName)

	# 将测试结果写入到Excel
	def resultToExcel(self,testCaseDict,excelRow=None,fileName=None):
		rte={}
		if fileName == None:
			excelFile = DealExcelTool().getReportFilePreName()
		else:
			excelFile=fileName
		et=ExcelTool(excelFile=excelFile,sheetName=ExcelConfig.REPORTPATHSHEET)
		if excelRow != None:
			excelRow = excelRow
		else:
			excelRow=2
		for i in testCaseDict.keys():
			et.writeCellRow(list=testCaseDict[i],row=excelRow,column=1)
			excelRow += 1
		# et.saveWorkbook()
		rte['excelRow']=excelRow
		rte['et']=et
		rte["fileName"] = excelFile
		return rte

	# 判断用例表业务ID是否在参数表业务ID中
	def estimateOperateID(self):
		pass
