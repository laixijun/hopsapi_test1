# @Time    : 6/16/2020 3:53 PM
# @Author  : Yang Xiaobai
# @Email   : yangzhiyongtest@163.com
import json

from utils.logger import Log
from utils.new_tools.common_tool import Common
from utils.new_tools.txt_tool import TxtTool

logger = Log(logger='url_classfication').get_log()
class UrlClassfication:
    def __init__(self):
        pass
    # 4、 参数在URL中存在
    def havaVars(self,url_hava,param_dic,caseID=None,parameterCase=None):
        param_dic_items = param_dic.keys()
        ttr = TxtTool().readTxt()
        if ttr:
            ttr = json.loads(ttr, encoding="utf-8")
        if param_dic != {}:
            for param_dic_item in param_dic_items :
                urlParameter=param_dic[param_dic_item]
                try:
                    param_dic_value = ttr["transmitData"][urlParameter]
                except:
                    param_dic_value = param_dic[param_dic_item]
                param_dic_item_re = "{" + param_dic_item + "}"
                if not isinstance(param_dic[param_dic_item],str):
                    param_dic_value = str(param_dic_value)
                url_hava = url_hava.replace(param_dic_item_re,param_dic_value)
        if "{" in url_hava:
            if parameterCase != None:
                resultList = Common().getUrlReg(url_hava)
                for i in resultList:
                    param_dic_value=parameterCase[caseID][i]
                    param_dic_item_re = "{" + i + "}"
                    url_hava = url_hava.replace(param_dic_item_re, param_dic_value)
        logger.info(url_hava)
        return url_hava
    # 5、 参数在URL中不存在
    def noHaveVars(self,url_noHave):
        logger.info(url_noHave)
        return url_noHave
    #判断URL是否有参
    '''
    url_estimate URL
    param_dic  URL中的参数，字典类型
    '''
    def estimateUrl(self,testList,parameterCase=None):
        url_estimate=testList[4]
        if "{" in url_estimate:
            param_dic = testList[6]
            caseID = testList[1]
            param_dic = json.loads(param_dic,encoding='utf-8')
            try:
                param_dic=param_dic['PaData']['urlData']
            except:
                param_dic={}
            url_result = self.havaVars(url_hava = url_estimate,param_dic = param_dic,caseID=caseID,parameterCase=parameterCase)
        else:
            url_result = self.noHaveVars(url_noHave = url_estimate)
        logger.info(url_result)
        return url_result