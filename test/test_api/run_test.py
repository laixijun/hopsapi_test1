# @Time ： 2020/6/24 00:15
# @Auth ： Yang Xiaobai
# @Email:  yangzhiyongtest@163.com
import json
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
	
def test103():
	a = "['a','b']"
	b={"c":1,"d":""}
	b["d"]=a
	e = json.dumps(b)
	f = json.loads(e)
	print(type(f["d"]))
	print(f["d"])
def test104():
	a="abc_bcd"
	a=a.split("_")
	print(a)
	
def test105():
	b={"a":1}
	for k,v in b.items():
		print(k)
		print(v)

def test107(*key,**kwargs):
	print(key)
	print(kwargs)


# test107((1,2,3),{"a":1},a=100,b=1000)

def test108():
	a=(1,2,3)
	b=len(a)
	print(b)
	
a="2.2"
if "." in a:
	a=float(a)
	b=int(a)
	
print(a,b)