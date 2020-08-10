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
    
class DBSetting:
    MYSQLSETTINGH={"host":"rm-2zeh739lme9f9hr08eo.mysql.rds.aliyuncs.com","user":"easylife","password":"root123HOPSON","db":"easylife_test","port":3306}
    MYSQLSETTINGT ={"host":"124.127.103.190","user":"root","password":"root123HOPSON","db":"easylife_test","port":40003}
    
if __name__ == "__main__":
    ce=ConfigurationEnv()
    ce.getPath()
    print(ce)
    # print(sys.executable)
    