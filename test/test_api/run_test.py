# @Time ： 2020/6/24 00:15
# @Auth ： Yang Xiaobai
# @Email:  yangzhiyongtest@163.com
import json
import platform
import sys

from test.test_api.runTest import DataParamter
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
def test112():
	a=('(id, organization_id, used_ebill_flag)', ('account_num', 'account_name'), ('1231255', '北京'))
	print(a[2])
	
def test113():
	import time
	return time.strftime("%Y-%m-%d")


def getDateStr():
	import time
	timeStr = time.strftime("%Y-%m-%d")
	timeList = timeStr.split("-")
	return timeList

def test114():
	a={"a":1,"b":2}
	for k,v in a.items():
		print(k,v)
		
def test115():
	('< appium.webdriver.webdriver.WebDriver (session="d0c4c0f6-33a0-48a5-a317-ea08ff5b69b2") >', {'company_name': '公司名称',
																								 'base_status': '认证成功',
																								 'certificate_type': '统一信用社会代码',
																								 'social_credit_code': '911103026605015136',
																								 'province_name': '天津市 天津市 和平区',
																								 'company_address': '北京朝阳区',
																								 'industry_name': '海洋天然气及可燃冰开采',
																								 'customer_scale': '中型',
																								 'biz_scope': '计算机技术',
																								 'corporation_id_card_name': '薛业乔',
																								 'authenticate_status': '认证成功',
																								 'corporation_id_card_type': '中国居民身份证',
																								 'corporation_id_card_num': '44010319900822244x',
																								 'corporation_id_card_expiry_date': '2021-12-10',
																								 'corporation_phone': '15700000006',
																								 'account_name': '工商银行',
																								 'bank_authenticate_status': '认证成功',
																								 'account_num': '12323234',
																								 'bank_name': '中国工商银行',
																								 'city_name': '天津市 天津市',
																								 'bank_branch_name': '中国工商银行股份有限公司天津玫瑰湾支行',
																								 'used_ebill_flag': '否',
																								 'admin_id_card_name': '薛业乔',
																								 'admin_status': '认证成功',
																								 'admin_id_card_type': '中国居民身份证',
																								 'admin_id_card_num': '44010319900822244x',
																								 'admin_id_card_expiry_date': '2021-12-10',
																								 'admin_phone': '15700000006',
																								 'admin_email': '15700000006@163.com'})

def test116():
	a={"a":1}
	a["b"]["c"]=2
	print(a)


def test117():
    DataParamter.dp=100
    DataParamter.dp += 1
def test118():
    print(DataParamter.dp)
def test119():
    test117()
    test118()
def test120():
    operationCodeValuesdic = {}
    operationCodeValuesdic["list"]=[]
    operationCodeValuesdic["listDetail"] = []
    operationCodeValue=[]
    i_num=1
    i_num_offSet=1
    a=[1,1,1,2,2,4,4,3]
    for i in a:
        if i in operationCodeValuesdic["list"]:
            i_num += 1
            # 每个业务编号，用例数量，用例开始位置
            operationCodeValue=[i,i_num,i_num_offSet]
        else:
            if operationCodeValue != [] or i_num_offSet==len(a)-1:
                operationCodeValuesdic["listDetail"].append(operationCodeValue)
            operationCodeValuesdic["list"].append(i)
            i_num = 1
            operationCodeValue = [i, i_num, i_num_offSet]
        i_num_offSet +=1
    print(operationCodeValuesdic)
def test121():
    operationCodeValuesdic = {}
    operationCodeValuesdic["list"]=[]
    operationCodeValuesdic["listDetail"] = []
    operationCodeValueBn=False
    operationCodeValue=[]
    i_num=1
    i_num_offSet=1
    a=[1,1,1,2,2,4,4,3]
    for i in a:
        if i in operationCodeValuesdic["list"]:
            i_num += 1
            # 每个业务编号，用例数量，用例开始位置
            operationCodeValue = [i, i_num, i_num_offSet]
        else:
            if i ==3:
                print(i_num_offSet)
                print(len(a))
                print(operationCodeValue)
            if operationCodeValue != [] and (operationCodeValue[0] in operationCodeValuesdic["list"]):
                operationCodeValuesdic["listDetail"].append(operationCodeValue)
                operationCodeValue=[]
            if operationCodeValue == [] and i_num_offSet == len(a):
                i_num = 1
                # 每个业务编号，用例数量，用例开始位置
                operationCodeValue = [i, i_num, i_num_offSet]
                operationCodeValuesdic["listDetail"].append(operationCodeValue)
            operationCodeValuesdic["list"].append(i)
            i_num = 1
        i_num_offSet +=1
    return operationCodeValuesdic
if __name__ in "__main__":
	a=test121()
	print(a)