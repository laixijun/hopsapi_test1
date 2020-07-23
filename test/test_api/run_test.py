# @Time ： 2020/6/24 00:15
# @Auth ： Yang Xiaobai
# @Email:  yangzhiyongtest@163.com
import platform
import sys


def test01():
	a=platform.platform()
	print(a)
	if "mac" in a:
		print("mac")
	elif "windows" in a:
		print("windows")

def test102():
	a=(1,2)
	print(a[1])
test102()
