testDict = {}
testList =[["1",2,3,4],["2",2,3,4],["2",2,3,4]]
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
        testDict[testBusinessNum] = testDictItemList
        testDictItemList = []
        testDictItemList.append(testListItem[1:])


def testCaseDic(testList):
    testDict = {}
    testBusinessNumBak = None
    testDictItemList = []
    for testListItem in testList:
        if testBusinessNumBak == None:
            testBusinessNumBak = testListItem[0]
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
testList =[["1",2,3,4],["2",2,3,4],["2",2,3,4]]
resulttestdict= testCaseDic(testList)
print(resulttestdict)