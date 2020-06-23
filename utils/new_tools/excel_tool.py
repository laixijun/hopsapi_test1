import os

import openpyxl

from utils.config_tool.file_config_path import ExcelConfig


class ExcelTool:
	def __init__(self,excelFile,sheetName=None):
		self.excelFile=excelFile
		if sheetName != None:
			self.sheetName = sheetName
		else:
			self.sheetName = "Sheet1"
	#获取工作表
	def getSheetValue(self):
		self.work_book = openpyxl.load_workbook(self.excelFile)
		sheet = self.work_book[self.sheetName]
		return sheet

	# row = xl_sheet.max_row 获取行数
	def  getMaxRows(self):
		maxNum=self.getSheetValue().max_row
		return maxNum
	# column = xl_sheet.max_column 获取列数
	def getMaxColumn(self):
		maxColumnNum = self.getSheetValue().max_column
		return maxColumnNum

	# 获取表格的总行数和总列数
	def get_row_clo_num(self):
		rows = self.getSheetValue().max_row
		columns = self.getSheetValue().max_column
		return rows, columns

	# 获取某列的所有值
	def get_col_value(self, column, rowNum=1):
		rows = self.getSheetValue().max_row
		column_data = []
		for i in range(rowNum, rows + 1):
			cell_value = self.getSheetValue().cell(row=i, column=column).value
			column_data.append(cell_value)
		return column_data

	# 获取某行所有值
	def get_row_value(self, row, columnNum=1):
		columns = self.getSheetValue().max_column
		row_data = []
		for i in range(columnNum, columns + 1):
			cell_value = self.getSheetValue().cell(row=row, column=i).value
			row_data.append(cell_value)
		return row_data

	# 获取

	#读取指定位置的值
	def getCellValue(self,row,column):
		cellValue=self.getSheetValue().cell(row,column).value
		return cellValue

	#获取所有行
	def getAllRowDataToTuple(self):
		rows = self.getSheetValue().rows
		cases=[]
		for row in rows:
			row_cases=[]
			for cell in row:
				row_cases.append(cell.value)
			cases.append(tuple(row_cases))
		return cases

	#向指定位置写入数据
	def writeCellValue(self,row,column,rcValue):
		cellIndex=self.getSheetValue().cell(row,column)
		cellIndex.value=rcValue

	# 向一行写入一条list
	def writeCellRow(self,list,row,column=1):
		column = column
		for i in list:
			self.writeCellValue(row=row,column=column,rcValue=i)
			column += 1

	#将工作簿保存
	def saveWorkbook(self,pathFile):
		self.work_book.save(pathFile)
		self.work_book.close()

class DealExcelTool:
	def __init__(self):
		pass
	# 读取数据的业务ID数据存放入列表
	def readOpretion(self,idOp,startPostition,endPosition):
		pass

	# 获取用例文件的全路径
	def getTestFileName(self):
		testFileName=self.getFilePath()+'/'+ ExcelConfig.TESTCASEALLFile
		return testFileName
	# 获取报告文件的全路径
	def getReportFileName(self):
		reportFileName=self.getFileReport() + '/' + ExcelConfig.REPORTPATHFILE
		return reportFileName
	# 获取用例文件的路径
	def getFilePath(self):
		testCaseFilePath = self.getProjectPath()+ ExcelConfig.TESTCASEALL
		return testCaseFilePath
	# 获取报告文件的路径
	def getFileReport(self):
		reportFilePath=self.getProjectPath() + ExcelConfig.REPORTPATH
		return reportFilePath
	# 获取项目路径
	def getProjectPath(self):
		projectPath=ExcelConfig.PROJECTPATH
		root_path = os.path.abspath(os.path.dirname(__file__)).split(projectPath)
		proPath = root_path[0]+ projectPath
		return proPath


if __name__ == '__main__':
	proPath=DealExcelTool().getProjectPath()
	print(proPath)
	getfilepath=DealExcelTool().getFilePath()
	print(getfilepath)
	filename = DealExcelTool().getTestFileName()
	print(filename)
	value=ExcelTool(excelFile=filename,sheetName='testCasejModle').get_col_value(1)
	print(value)