# @Time ： 2020/6/20 21:23
# @Auth ： Yang Xiaobai
# @Email:  yangzhiyongtest@163.com
from utils.config_tool.file_config_path import ExcelConfig
from utils.new_tools.common_tool import Common
from utils.new_tools.excel_tool import DealExcelTool, ExcelTool


class SourceGet:
	def __init__(self):
		pass

	# 获取Excel操作手柄
	def getExcelHandle(self):
		testFile = DealExcelTool().getTestFileName()
		testSheet = ExcelConfig.TESTCASEALLSHEET
		et=ExcelTool(excelFile=testFile,sheetName=testSheet)
		return et

	#获取业务ID
	def getOperateId(self):
		et=self.getExcelHandle()
		operateId=et.get_col_value(column=1)
		operateDic=Common().itemListCount(operateId)
		return operateDic

	# 获取业务下的测试用例
	def getIdOfTestOperate(self,lstNum):
		startNum= lstNum[2]+1-lstNum[1]
		endNum = lstNum[2]+1
		testCaseList = []
		for i in range(startNum,endNum):
			lsti=self.getExcelHandle().get_row_value(row=i)
			testCaseList.append(lsti)
		return testCaseList


if __name__ == '__main__':
	lstid=[8, 3, 4]
	re=SourceGet().getIdOfTestOperate(lstid)
	print(re)