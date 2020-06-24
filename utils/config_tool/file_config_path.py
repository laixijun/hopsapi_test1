# @Time ： 2020/6/20 20:19
# @Auth ： Yang Xiaobai
# @Email:  yangzhiyongtest@163.com
import time


class ExcelConfig:
	PROJECTPATH = 'hopsapi_test'
	TESTCASEALL = '/testCase/testCaseAll'
	REPORTPATH = '/report/excelReport'
	TESTCASEALLFile = 'testCase.xlsx'
	TESTCASEALLSHEET = 'testSheet'
	REPORTPATHFILE = 'testReport.xlsx'
	REPORTPATHSHEET = 'testReport'
	REPORTPATHSHEETCURRENT = 'testReport' + str(time.strftime('%Y-%m-%d',time.localtime(time.time()))) + '.xlsx'
	

if __name__ == '__main__':
	print(ExcelConfig.REPORTPATHSHEETCURRENT)
