# @Time ： 2020/6/26 01:10
# @Auth ： Yang Xiaobai
# @Email:  yangzhiyongtest@163.com
import json

from utils.new_tools.excel_tool import DealExcelTool


class TxtTool:
	def __init__(self):
		pass

	# 写入TXT
	def readTxt(self,filename):
		with open(filename) as f:  # 默认模式为‘r’，只读模式
			contents = f.read()  # 读取文件全部内容
		return contents

	# 读取TXT
	def writeTxt(self,filename,contents):
		with open(filename, 'w') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
			f.write(contents)

	#  增加新数据
	def appendTxt(self,filename,contents):
		with open(filename, 'a') as f:  # 'a'表示append,即在原来文件内容后继续写数据（不清楚原有数据）
			f.write(contents)





if __name__ == '__main__':
	headers = {'Content-Type': 'application/json', 'Connection': 'keep-alive',
			   'User-Agent': 'EasyLife.alpha/1.4.2 (iPhone; iOS 10.2.1; Scale/3.00)'}

	tfn = DealExcelTool().getTempFileName()
	headers = json.dumps(headers,ensure_ascii=False)
	TxtTool().writeTxt(tfn,headers)
	result = TxtTool().readTxt(tfn)
	print(result)