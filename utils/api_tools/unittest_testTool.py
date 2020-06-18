# @Time    : 6/17/2020 12:27 PM
# @Author  : Yang Xiaobai
# @Email   : yangzhiyongtest@163.com
from utils.api_tools.api_classfication import ApiClassification
from utils.logger import Log

logger = Log(logger='api_classfication').get_log()
class UnittestTestTool:
    def __init__(self):
        pass
    # 1、 根据业务编号将一组用例添加到字典
    # return {'1': [[2, 3, 4]], '2': [[2, 3, 4], [2, 3, 4]]}
    def testCaseDic(self,testList):
        testDict = {}
        testBusinessNumBak = None
        testDictItemList = []
        for testListItem in testList:
            if testBusinessNumBak == None:
                testBusinessNumBak=testListItem[0]
            testBusinessNum = testListItem[0]
            if testBusinessNumBak == testBusinessNum:
                testDictItemList.append(testListItem[1:])
                testDict[testBusinessNum] = testDictItemList
            elif testBusinessNumBak != testBusinessNum:
                testBusinessNumBak = testListItem[0]
                testBusinessNum = testListItem[0]
                testDictItemList = []
                testDictItemList.append(testListItem[1:])
                testDict[testBusinessNum] = testDictItemList
        return testDict

    # 2、 循环执行业务内的接口生成测试结果
    def loopApiTest(self,testDict):
        pass
    # 3、 unittest 展示业务的成功与失败，可以查看失败详情，是否需要人工校验
    def estimateResult(self,resultDic):
        pass