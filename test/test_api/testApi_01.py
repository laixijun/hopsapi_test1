import json
import os

import requests

a=os.getcwd()
b=os.path.dirname(__file__)
# print(a,b)

dic_a={"a":1}
dic_a.update(b=10)
# print(dic_a)

def post_request(url_post, post_data):
    post_data_json = json.dump(post_data)
    post_response = requests.post(url=url_post, data=post_data_json)
    return post_response

dic_b={}
dic_b["static"]=100
dic_b["text"]="ok"
# for item_dic in dic_b.keys():
#     print("{"+item_dic+"}")
# print(dic_b)

param_dic={"a":1,"b":"c"}
url_hava="https://tbroker.lifeat.cn:45788/easylife/rest{b}/{a}/login"
param_dic_items = param_dic.keys()
for param_dic_item in param_dic_items :
    param_dic_item_re = "{" + param_dic_item + "}"
    param_dic_value=param_dic[param_dic_item]
    if not isinstance(param_dic[param_dic_item],str):
        param_dic_value=str(param_dic[param_dic_item])
        print(type(param_dic_value))
    url_hava=url_hava.replace(param_dic_item_re,param_dic_value)
    print(param_dic_item_re,type(param_dic_item_re))
    print(str(param_dic[param_dic_item]))
print(url_hava)


a="abc"
if isinstance(a,str):
    print(a,str(a))