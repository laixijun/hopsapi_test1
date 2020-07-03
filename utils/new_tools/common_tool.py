# @Time    : 6/18/2020 9:16 AM
# @Author  : Yang Xiaobai
# @Email   : yangzhiyongtest@163.com
import json
import re

from utils.logger import Log

logger = Log(logger='para_analysis').get_log()

class ApiCommon:
    def __init__(self):
        pass
    # 将值替换字符串中的内容

class Common:
    def __init__(self):
        pass
    # 判断是否为list，list有几级
    def estimateList(self,estimatelistValue):
        listNum=0
        while isinstance(estimatelistValue, list):
                for item_list in estimatelistValue:
                    if isinstance(item_list,list):
                        listNum+=1
                        estimatelistValue=item_list
                        break
                    else:
                        estimatelistValue = item_list
                        break
        return listNum

    # 替换字符串中指定的字符
    def replaceStr_1(self,strRes,strKey,strValue):
        strKey="{" + strKey + "}"
        strRes = json.dumps(strRes,ensure_ascii=False)
        if isinstance(strValue,int):
            strValue = str(strValue)
            strKey1 = "'{" + strKey + "}'"
            strKey2 = '"{' + strKey + '}"'
            strRes = strRes.replace(strKey1, strValue)
            strRes = strRes.replace(strKey1, strValue)
        elif not isinstance(strValue,str):
            strValue=str(strValue)
        strRes = strRes.replace(strKey,strValue)
        strRes = json.loads(strRes)
        return strRes

    def replaceStr(self,mydict, key, value):
        mydict = json.loads(mydict,encoding="utf-8")
        if isinstance(mydict, dict):  # 使用isinstance检测数据类型，如果是字典
            if key in mydict.keys():  # 替换字典第一层中所有key与传参一致的key
                mydict[key] = value
            for k in mydict.keys():  # 遍历字典的所有子层级，将子层级赋值为变量chdict，分别替换子层级第一层中所有key对应的value，最后在把替换后的子层级赋值给当前处理的key
                chdict = mydict[k]
                self.replaceStr(chdict, key, value)
                mydict[k] = chdict
        elif isinstance(mydict, list):  # 如是list
            for element in mydict:  # 遍历list元素，以下重复上面的操作
                if isinstance(element, dict):
                    if key in element.keys():
                        element[key] = value
                    for k in element.keys():
                        chdict = element[k]
                        self.replaceStr(chdict, key, value)
                        element[k] = chdict

    # 对列表中的数据进行计数
    def itemListCount(self,lst):
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
        itemDic['list']=lstSet
        return itemDic
    #itemKey, itemValue, needKey
    def getValueFalse(self,lst, itemKey, itemValue, needKey):
        for i in lst:
            try:
                if i[itemKey] == itemValue:
                    return i[needKey]
            except:
                return False

    # 正则内容对比返回true
    def getConpareResult(self,strData,regular,value):
        prog = re.compile(regular)
        result = prog.findall(strData)
        logger.info(result)
        if result == value:
            return True
        else:
            return False




if __name__ == "__main__":
    strData="outerOrgId"
    regular = "ou(^.*?)rgId"
    value= "terO"
    result = Common().getConpareResult(strData,regular,value)
    print(result)