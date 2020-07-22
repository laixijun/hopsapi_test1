# @Time ： 2020/6/20 20:19
# @Auth ： Yang Xiaobai
# @Email:  yangzhiyongtest@163.com
import time


class ExcelConfig:
	PROJECTPATH = 'hopsapi_test1'
	TESTCASEALL = '/testCase/testCaseAll'
	REPORTPATH = '/report/excelReport'
	TESTCASEALLFile = 'testCase.xlsx'
	TESTCASEALLSHEET = 'testSheet'
	#参数化的sheet
	PARAMETERCASESHEET = 'parameterSheet'
	REPORTPATHFILE = 'testReport.xlsx'
	REPORTPATHSHEET = 'testReport'
	#临时存储文本
	TEMPDBFILEPATH = '/db_file/TempDB.txt'
	REPORTPATHFILECURRENT = 'testReport' + str(time.strftime('%Y-%m-%d%H%M%S',time.localtime(time.time()))) + '.xlsx'
	CONFIGTOOLPATH="/utils/config_tool/"
	

if __name__ == '__main__':
	print(ExcelConfig.REPORTPATHFILECURRENT)
