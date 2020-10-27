import pymysql

class Users:
    def __connect(self):
        self.__con = pymysql.connect(
            host='db',
            user='server',
            password='v9bumEc1G9c8HBDO4QtHsFI8NNWcEh',
            port=3306,
            db='verification',
            charset='utf8mb4'
        )
        self.__cur =  self.__con.cursor()
    
    def add(self, sql):
        self.__connect()
        self.__cur.execute(sql)        
        self.__con.commit()
        self.__cur.close()
        self.__con.close()