# @Time ： 2020/6/24 00:15
# @Auth ： Yang Xiaobai
# @Email:  yangzhiyongtest@163.com
import json
import platform
import sys

from utils.new_tools.db_config import MysqlSetting


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
	

def get_track(distance):
	track = []
	current = 0
	mid = distance * 3 / 4
	t = 0.2
	v = 0
	while current < distance:
		if current < mid:
			a = 2
		else:
			a = -3
		v0 = v
		v = v0 + a * t
		move = v0 * t + 1 / 2 * a * t * t
		current += move
		track.append(round(move))
	return track

def update_sql(zId):
	env ={"host":"rm-2zeh739lme9f9hr08eo.mysql.rds.aliyuncs.com","user":"easylife","password":"root123HOPSON","db":"easylife","port":3306}
	mi=MysqlSetting(env=env)
	userID = 250825
	phoneD = 13503930411
	for i in range(301):
		userIDstr = str(userID)
		phoneDstr = str(phoneD)
		valueD = (zId,userIDstr,3,phoneDstr)
		key_value =('(id,user_id,user_type,phone)',valueD)
		mi.insertData01(key_value,tableName='easylife_live_room_user_record')
		phoneD += 1
		userID+=1
	mi.commitData()

# update_sql(zId='10261')

class A:
	def B(self):
		
		testC=100
		print('ok')
		

def test109():
	stra=" D:/zhy/haoshenghuo/autoproject/hopsapi_test1/pyapi/scrapyApi/appium_app\\report/logs"
	strb=stra.replace("\\","/")
	print(strb)
	
def test110():
	a=(1,2)
	print(a[0])
	print(a[1])
	
def test111():
	a= {"a":1}
	for k,v in a.items():
		print(k)
		print(v)
if __name__ in "__main__":
	test111()