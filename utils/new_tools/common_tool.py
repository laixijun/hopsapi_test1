# @Time    : 6/18/2020 9:16 AM
# @Author  : Yang Xiaobai
# @Email   : yangzhiyongtest@163.com
import datetime
import json
import re

import requests

from utils.config_tool import ConfigParameter
from utils.config_tool.request_header import RequestHeader
from utils.logger import Log
from utils.new_tools.excel_tool import DealExcelTool

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
    
    # 判断是否是APP
    def isAppAssert(self,lsti):
        flagApp = False
        lsti0 = ConfigParameter.WEBAPIDIC
        lsti3 = ConfigParameter.needRequestSetting
        for i in lsti0:
            if i in lsti:
                flagApp = True
        return flagApp
    
    # 获取header图片
    def getHeaderImage(self,url):
        header = {}
        header["authority"] = "upload-z1.qiniup.com"
        isWebApi=self.isAppAssert(url)
        if isWebApi:
            header["content-type"] = "multipart/form-data; boundary=----WebKitFormBoundaryPdEjbkHRVcjoWRVS"
            header[
                "user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
            return header
        else:
            header["content-type"] = "multipart/form-data; boundary=werghnvt54wef654rjuhgb56trtg34tweuyrgf"
            header[
                "user-agent"] = "QiniuObject-C/7.2.5 (iPhone; iOS 12.2; D5525AE8-3362-4E8C-9BE2-A604B651C1BF; m1qdTqGcH54NLtQrE2j0MRnvKf8LaJBu1A7omyfe)"
            return header
    
    # pass
    def test_upload(self,fileName,headersD,url):
        """
        test case
        :return:
        """
        header=self.getHeaderImage(url)
        isWebApi = self.isAppAssert(url)
        url = 'https://upload-z1.qiniup.com/'
        tailFile = self.getTailFile(fileName)
        tailType = 'image/' + tailFile
        filepath = DealExcelTool().getFilePath() + "/" + fileName
        fo = self.getFilesBin(fileName=filepath)
        crc32Value=self.crc32Get(fo)
        tokenFilesJson=self.getQiNiuToken(headersD)
        tokenFiles=tokenFilesJson["data"]["imgToken"]
        qiniuUrl=tokenFilesJson["data"]["qiniuUrl"]
        logger.info(crc32Value)
        keyName=self.getTimeHMS()+ "." + tailFile
        if isWebApi:
            data={
                'token': tokenFiles,
                "key" : keyName,
                "fname" : fileName
            }
            qiNiuName=keyName
        else:
            data={ 'token':tokenFiles,
                'crc32': crc32Value}
        files = [
            # 'token': (None, tokenFiles),
            # 'crc32': (None, crc32Value),
            ('file',(fileName, open(filepath,"rb"),tailType))
        ]
        r = requests.post(url=url, files=files, data=data, verify=False)
        response=json.loads(r.text)
        if isWebApi:
            qiNiuUrl = qiniuUrl + response["key"]
        else:
            qiNiuUrl=qiniuUrl+response["hash"]
            qiNiuName=self.getFileName(tailFile)
        qiNiuUrl=qiNiuUrl.replace("/","\/")
        return {"qiNiuUrl":qiNiuUrl,"qiNiuName":qiNiuName}
    # 返回文件名称
    def getFileName(self,tailFile):
        import time
        ticks=time.time()
        fileName = "follow0-"+ticks+"."+tailFile
        return fileName
    
    # 获取时间格式
    def getTimeHMS(self):
        now_time = datetime.datetime.now()
        time1 = datetime.datetime.strftime(now_time, '%Y%m%d%H%M%S')
        return time1
        
        
    
    # 计算图片crc32
    def crc32Get(self,valueD):
        import zlib
        valueE=zlib.crc32(valueD)
        return valueE

    # 获取文件的二进制内容
    def getFilesBin(self,fileName):
        # 打开文件
        with open(fileName, 'rb') as file:
            fo = file.read()
        file.close()
        return fo

    # 获取文件的后缀
    def getTailFile(self,fileName):
        patternD=re.compile("\.(.*)")
        tailFile=patternD.findall(fileName)[0]
        return tailFile

    # 获取图片qiniu的token
    def getQiNiuToken(self,headersD,endPoint):
        data=json.dumps({},ensure_ascii=False)
        # urlD="https://tapi.lifeat.cn:45788/checkin/upload/uploadToken"
        urlD = "https://"+endPoint+".lifeat.cn:45788/checkin/upload/uploadToken"
        r=requests.post(url=urlD,data=data,headers=headersD,verify=False)
        response=json.loads(r.text,encoding="utf-8")
        return response
    
    # 获取端URL节点
    def getEndPont(self,url):
        urlD = re.compile("https://(.*?)\.")
        urlP = urlD.findall(url)[0]
        return urlP


    # 生成（%s,%s）
    def getCValue(self,num):
        numList=[]
        for i in range(num):
            numList.append(1)
        numListStr=str(tuple(numList))
        numListStr=numListStr.replace("1","%s")
        return numListStr
    
    # 生成键=值  键=%s
    def getSValue(self,listTu):
        keyWhere=""
        for key in listTu:
            keyWhere=keyWhere + " and " + key + " = %s "
        # anda = % sandb = % s
        keyWhere=keyWhere[4:]
        return keyWhere
    
    def formatTrans(self):
        # tuple1 = '(id,code,create_time)'
        # tuple2 = ("id", "status")
        # tuple3 = (2, 1)
        # tableName = "table_name3"
        pass

    # 预期结果：字段名 = 值_字段名 = 值_字段名 = 值：字段名 = 值_字段名 = 值
    #  如果是int 或者浮点类型  值的前面加一个！
    def expectDB(self,strDbKey,strDbValue):
        expectDic={}
        expectList=[]
        locationListKey=[]
        locationListValue=[]
        # strDbList = strDb.split(":")
        strDbListExpect=strDbKey.split("_")
        for i in strDbListExpect:
            i= i.split("=")
            expectDic[i[0]]=i[1]
            expectList.append(i[0])
        strDbListLocation=strDbValue.split("_")
        for i in strDbListLocation:
            i = i.split("=")
            if i[0]!="tableName":
                locationListKey.append(i[0])
                valueD=self.transTupleToNoStr(i[1])
                locationListValue.append(valueD)
            else:
                tableName=i[1]
        locationListKey=tuple(locationListKey)
        locationListValue=tuple(locationListValue)
        expectList=tuple(expectList)
        expectList=self.transTupleToStr(expectList)
        return {"expectValue":expectDic,"expectKey":expectList,"locationListKey":locationListKey,"locationListValue":locationListValue,"tableName":tableName}
        
    def transTupleToStr(self,liti):
        liti=str(liti)
        liti=liti.replace("'","")
        liti = liti.replace("'", "")
        liti = liti.replace('"', "")
        return liti
    def transTupleToNoStr(self,keyD):
        if "!" in keyD:
            keyD=keyD[1:]
            if "." in keyD:
                keyD=float(keyD)
            else:
                keyD=int(keyD)
        return keyD
    
    # 字典数据对比
    def compareData(self,expectDic,actule):
        compareResult={}
        compareResult["FAIL"]={}
        compareResult["SUC"] = {}
        try:
            for k,v in expectDic.items():
                if actule[k]==v:
                    compareResult["SUC"][k]="PASS"
                else:
                    compareResult["FAIL"][k] = actule[k]
        except:
            compareResult["FAIL"]="FAIL"
        return compareResult
    

if __name__ == "__main__":
    com = Common()
    
    # a= "!2.2"
    # b=com.transTupleToNoStr(a)
    # print(b)
    a="字段名=值_字段名=值_字段名=值:字段名=值_字段名=值_字段名=!2.2_tableName=abc"
    b=com.expectDB(a)
    print(b)
    # listTu=("a","b")
    # a=com.getSValue(listTu)
    # print(a)
    # urlD="https://tapi.lifeat.cn:45788/checkin/upload/uploadToken"
    # a=com.getCValue(10)
    # print(a)
    # a=com.getTimeHMS()
    # print(a)
    # a=com.getEndPont(urlD)
    # print(a)
    # b= com.isAppAssert(urlD)
    # print(b)
    
  
  
    # fileName="timg.png"
    # header=RequestHeader.APPHEADER
    # header["Authorization"]="nJoTBfnirWaUISt7znl4fg"
    # r=com.test_upload(fileName=fileName,headersD=header)
    # print(r)
    
    # a=com.getTailFile(fileName)
    # print(a)
    #
    
    # valuea = {"isApp":"N","isTransmit":{"tokenName":[["token","token"],["Authorization","token"]],"transmitName":[["token",{"valueKey":"token","getValuePath":"$.data.token"}],["applicationToken",{"valueKey":"applicationToken","getValuePath":"$.data.applicationToken"}],["cityId",{"valueKey":"cityId","getValuePath":{"threeListAll":"$.data.cityList","threeList":"city-北京市-cityId"}}]]}}
    # assitValue={"threeListAll": "$.data.cityList", "threeList": "city-北京市-cityId"}
    # assitKey="getValuePath"
    # valueab=Common().getJsonValue(mydict=valuea, key="valueKey1", assitValue=assitValue,assitKey=assitKey)
    # print(valueab)
    # a=DealExcelTool().getFilePath()
    # print(a)
    
    # com=Common()
    # binData=com.getFilesBin("timg.jpeg")
    # print(binData)
    # crcData=com.crc32Get(binData)
    # print(crcData)
    # qiNiuUrl="https://www.runoob.com/python/att-string-replace.html"
    # qiNiuUrl = qiNiuUrl.replace("/", "\/")
    # print(qiNiuUrl)