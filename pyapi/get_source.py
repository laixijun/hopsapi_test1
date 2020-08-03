# @Time ： 2020/6/20 21:23
# @Auth ： Yang Xiaobai
# @Email:  yangzhiyongtest@163.com
from utils.config_tool import ConfigParameter
from utils.config_tool.file_config_path import ExcelConfig
from utils.new_tools.common_tool import Common
from utils.new_tools.excel_tool import DealExcelTool, ExcelTool


class SourceGet:
	def __init__(self):
		pass

	# 获取Excel用例操作手柄
	def getExcelHandle(self):
		testFile = DealExcelTool().getTestFileName()
		testSheet = ExcelConfig.TESTCASEALLSHEET
		et=ExcelTool(excelFile=testFile,sheetName=testSheet)
		return et

	# 获取Excel参数操作手柄
	def getParameterExcelHandle(self):
		testFile = DealExcelTool().getTestFileName()
		testSheet = ExcelConfig.PARAMETERCASESHEET
		et = ExcelTool(excelFile=testFile, sheetName=testSheet)
		return et

	#获取用例表业务ID
	#{'KHGJ001': ['KHGJ001', 2, 3], 'list': ['KHGJ001']}
	def getOperateId(self):
		et=self.getExcelHandle()
		operateId=et.get_col_value(column=1,rowNum=2)
		operateDic=Common().itemListCount(operateId)
		return operateDic

	#获取参数表业务ID
	#{'KHGJ001': ['KHGJ001', 2, 3], 'list': ['KHGJ001']}
	def getParameterOperateId(self):
		testFile = DealExcelTool().getTestFileName()
		et = ExcelTool(excelFile=testFile, sheetName=ExcelConfig.PARAMETERCASESHEET)
		operateId = et.get_col_value(column=1, rowNum=2)
		operateDic = Common().itemListCount(operateId)
		return operateDic

	# 获取参数表业务执行ID
	def getTestExecuteID(self):
		testFile = DealExcelTool().getTestFileName()
		et = ExcelTool(excelFile=testFile, sheetName=ExcelConfig.PARAMETERCASESHEET)
		testExecuteID = et.get_col_value(column=2, rowNum=2)
		return testExecuteID

	# 获取业务下的测试用例
	def getIdOfTestOperate(self,lstNum):
		startNum= lstNum[2]+1-lstNum[1]
		endNum = lstNum[2]+1
		testCaseList = []
		for i in range(startNum,endNum):
			lsti=self.getExcelHandle().get_row_value(row=i)
			testCaseList.append(lsti)
		return testCaseList

	# 	# 获取业务下的测试参数
	def getIdOfParameterOperate(self,lstNum):
		startNum= lstNum[2]+1-lstNum[1]
		endNum = lstNum[2]+1
		testCaseList = []
		for i in range(startNum,endNum):
			lsti=self.getParameterExcelHandle().get_row_value(row=i)
			#数据清洗
			lsti = self.getIdOfParameterOperateValues(lsti)
			testCaseList.append(lsti)
		return testCaseList
	
	# 清洗数据为可以测试数据
	def getIdOfParameterOperateValues(self,lsti):
		flagApp = False
		lsti0 = ConfigParameter.WEBAPIDIC
		lsti3 = ConfigParameter.needRequestSetting
		for i in lsti0:
			if i in lsti:
				flagApp = True
		if flagApp:
			lsti3["isApp"] = "N"
		lsti1=ConfigParameter.needRequestParameter
		lsti1["paData"]["paramData"] = lsti[6]
		lsti[6] = lsti1
		lsti2 = ConfigParameter.needRequestSetting
		lsti2["isTransmit"]["transmitName"] = lsti[7]
		lsti[7] = lsti2
		return lsti

	# 判断是否APP接口
	def isAPPApi(self):
		pass
		

if __name__ == '__main__':
	lstid=[8, 3, 4]
	re=SourceGet().getIdOfParameterOperateValues().needRequestParameter
	print(re)