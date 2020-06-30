# @Time    : 6/30/2020 9:26 AM
# @Author  : Yang Xiaobai
# @Email   : yangzhiyongtest@163.com
import sys


class ConfigurationEnv:
    def __init__(self):
        pass
    
    def getPath(self):
        getPath=sys.path
        for i in getPath:
            print(i)
        return getPath
    
    
if __name__ == "__main__":
    ce=ConfigurationEnv()
    ce.getPath()
    print(ce)
    # print(sys.executable)
    