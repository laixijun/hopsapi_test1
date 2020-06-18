import openpyxl


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

	#将工作簿保存
	def saveWorkbook(self,pathFile):
		self.work_book.save(pathFile)
		self.work_book.close()