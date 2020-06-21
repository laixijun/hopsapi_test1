# @Time ： 2020/6/21 00:50
# @Auth ： Yang Xiaobai
# @Email:  yangzhiyongtest@163.com
import datetime

from pyapi.get_source import SourceGet
from utils.api_tools.api_classfication import ApiClassification
from utils.api_tools.para_analysis import ParaAnalysis
from utils.api_tools.url_classfication import UrlClassfication
from utils.logger import Log

logger = Log(logger='deal_source').get_log()
class SourceDeal:
	def __init__(self):
		pass

	# 获取用例
	def dealTestCase(self):
		pass

	# 完成一次请求
	def operationDeal(self,lstNum):
		testCaseList=SourceGet().getIdOfTestOperate(lstNum)
		responseValue= None
		resultList = []
		for testCaseListItem in testCaseList:
			resultCaseList = testCaseListItem[:3]
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
			durn = (b - a).seconds
			logger.info(resultRequst)
			responseValue=resultRequst
			resultList.append(resultCaseList)