import os
def root_path():
	root_path = os.path.abspath(os.path.dirname(__file__)).split('hopsapi_test1')
	print(root_path)


def count():
	lst_dic = {}
	lst = [8, 8,8,9,9,12,12]


# 对列表中的数据进行计数
def itemListCount(lst):
	itemDic = {}
	lstSet = set(lst)
	lstSet = list(lstSet)
	countEnd = 1
	for item in lstSet:
		countGap = 0
		for compareItem in lst:
			if item == compareItem:
				countGap += 1
		countEnd = countEnd + countGap
		itemDic[item] = [item, countGap, countEnd]
	return itemDic


def dicNext():
	a={'a':1,'b':2}
	for i in a.keys():
		print(i)
		print(a[i])
if __name__ == '__main__':
	lst = [8, 8, 8, 9, 9, 12, 12]
	a=itemListCount(lst)
	# print(a)
	dicNext()