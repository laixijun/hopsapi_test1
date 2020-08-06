# @Time    : 8/6/2020 5:25 PM
# @Author  : Yang Xiaobai
# @Email   : yangzhiyongtest@163.com

# mysql
import pymysql


class MysqlSetting:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                     user='user',
                                     password='passwd',
                                     db='db',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
    
    

# mangodb
class MangoDBSetting:
    pass