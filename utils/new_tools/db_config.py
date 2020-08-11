# @Time    : 8/6/2020 5:25 PM
# @Author  : Yang Xiaobai
# @Email   : yangzhiyongtest@163.com

# mysql
import re

import pymysql


from utils.config_tool.configurationEnv import DBSetting
from utils.logger import Log
from utils.new_tools.common_tool import Common

logger = Log(logger='db_config').get_log()
class MysqlSetting:
    def __init__(self,env):
        self.connect=self.getConnection(env)
        self.cursor=self.getCursor()
        
    def getConnection(self,env):
        if env == "h":
            listi = DBSetting.MYSQLSETTINGH
        elif env=="t":
            listi=DBSetting.MYSQLSETTINGT
        host=listi["host"]
        user=listi["user"]
        password=listi["password"]
        db=listi["db"]
        port=listi["port"]
        connection = pymysql.connect(host=host,
                                     user=user,
                                     password=password,
                                     port=port,
                                     db=db,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        return connection

    def getCursor(self):
        cursor=self.connect.cursor()
        return cursor
    # key 是一个元组，包括两个元组，第一个元组是键，第二个是值
    # 插入数据
    def insertData(self,*key,**kwargs):
        cursor= self.cursor
        # Create a new record
        print(key)
        key0=str(key[0])
        num=len(key[1])
        tableName=kwargs["tableName"]
        valueData=Common().getCValue(num)
        # sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        sql = "INSERT INTO "+ tableName + key0 +" VALUES "+valueData
        print(sql)
        print(key[1])
        # cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
        cursor.execute(sql, key[1])
        
    # 查询数据
    # 传入元组，第一个字符串"(key,key)",第二个传入元组（key),第三个传入值（value），第四个传入表名，tableName=Name,
    #get --[{'id': 2, 'code': '100', 'create_time': datetime.datetime(2020, 8, 10, 14, 8, 21)}]
    def selectData(self,*key,**kwargs):
        # Read a single record
        keyDPatterm=re.compile("\((.*?)\)")
        keyD=keyDPatterm.findall(key[0])[0]
        keyWhere=Common().getSValue(key[1])
        # sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        sql = "SELECT "+keyD+" FROM "+kwargs["tableName"]+" WHERE" + keyWhere
        logger.info(sql)
        logger.info(key[2])
        self.cursor.execute(sql, key[2])
        result = self.cursor.fetchall()
        return result

    # 1、 通过where定位查询到实际结果
    def selectDataBind(self,strDbKey,strDbValue):
        DicParameter=Common().expectDB(strDbKey,strDbValue)
        result=self.selectData(DicParameter["expectKey"],DicParameter["locationListKey"],DicParameter["locationListValue"],tableName=DicParameter["tableName"])
        resultD=Common().compareData(expectDic=DicParameter["expectValue"],actule=result[0])
        return resultD
        
    # 2、 通过sql语句查询

    def commitData(self):
        self.connect.commit()

    def closeConnect(self):
        self.connect.close()
    
    
    

# mangodb
class MangoDBSetting:
    pass




if __name__ == "__main__":
    ms=MysqlSetting(env="t")
    tuple1='(id,code,create_time)'
    tuple2=("id","status")
    tuple3=(2,1)
    tableName="table_name3"
    a=ms.selectData(tuple1,tuple2,tuple3,tableName=tableName)
    print(a)
    # key1='(code,status)'
    # value1=("100",1)
    # cs=ms.insertData(key1,value1,tableName="table_name3")
    # commit=ms.commitData()
    
    
    
