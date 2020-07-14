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
    def replaceStr(self,strRes,strKey,strValue):
        strRes = json.dumps(strRes,ensure_ascii=False)
        logger.info(strValue)
        if not isinstance(strValue,str):
            strValue = str(strValue)
            strKey1 = "'{" + strKey + "}'"
            strKey2 = '"{' + strKey + '}"'
            strRes1 = strRes.replace(strKey1, strValue)
            strRes2 = strRes1.replace(strKey2, strValue)
        else:
            strKey = "{" + strKey + "}"
            strRes2 = strRes.replace(strKey,strValue)
        strRes3 = json.loads(strRes2,encoding='utf-8')
        return strRes3

    def getJsonValue(self,mydict, key, assitValue=None,assitKey=None):
        # mydict = json.loads(mydict,encoding="utf-8")
        if isinstance(mydict, dict):  # 使用isinstance检测数据类型，如果是字典
            if key in mydict.keys():  # 替换字典第一层中所有key与传参一致的key
                if assitValue == None:
                    needValue=mydict[key]
                    return needValue
                elif  assitValue == mydict[assitKey]:
                    needValue = mydict[key]
                    return needValue
            for k in mydict.keys():  # 遍历字典的所有子层级，将子层级赋值为变量chdict，分别替换子层级第一层中所有key对应的value，最后在把替换后的子层级赋值给当前处理的key
                chdict = mydict[k]
                if self.getJsonValue(chdict, key, assitValue=assitValue,assitKey=assitKey):
                    return self.getJsonValue(chdict, key, assitValue=assitValue,assitKey=assitKey)
        elif isinstance(mydict, list):  # 如是list
            for element in mydict:  # 遍历list元素，以下重复上面的操作
                if isinstance(element, dict):
                    if key in element.keys():
                        if assitValue == None:
                            needValue = element[key]
                            return needValue
                        elif assitValue == element[assitKey]:
                            needValue = element[key]
                            return needValue
                    for k in element.keys():
                        chdict = element[k]
                        if self.getJsonValue(chdict, key, assitValue=assitValue,assitKey=assitKey):
                            return self.getJsonValue(chdict, key, assitValue=assitValue, assitKey=assitKey)
                else:
                    for elementItem in element:
                        chdict = elementItem
                        if self.getJsonValue(chdict, key, assitValue=assitValue,assitKey=assitKey):
                            return self.getJsonValue(chdict, key, assitValue=assitValue, assitKey=assitKey)

        else:
            return False

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
                elif itemValue.isdigit():
                    if i[itemKey] == int(itemValue):
                        return i[needKey]
                else:
                    return False
            except:
                return False

    def getUrlReg(self,urla):
        urla = "https://tbroker.lifeat.cn:45788/easylife/{rest}/{broker}/login"
        regex = re.compile("{(.*?)}", re.I)
        resultlist = regex.findall(urla)
        return resultlist

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
    valuea = {"isApp":"N","isTransmit":{"tokenName":[["token","token"],["Authorization","token"]],"transmitName":[["token",{"valueKey":"token","getValuePath":"$.data.token"}],["applicationToken",{"valueKey":"applicationToken","getValuePath":"$.data.applicationToken"}],["cityId",{"valueKey":"cityId","getValuePath":{"threeListAll":"$.data.cityList","threeList":"city-北京市-cityId"}}]]}}
    assitValue={"threeListAll": "$.data.cityList", "threeList": "city-北京市-cityId"}
    assitKey="getValuePath"
    valueab=Common().getJsonValue(mydict=valuea, key="valueKey1", assitValue=assitValue,assitKey=assitKey)
    print(valueab)