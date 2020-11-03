import pymysql
import base64
import json

class Users:
    def __connect(self):
        con_info = json.loads(open('./config/connect_db.json', 'r').read())

        self.__con = pymysql.connect(
            host=con_info['host'],
            user=con_info['user'],
            password=con_info['password'],
            port=con_info['port'],
            db=con_info['db'],
            charset=con_info['charset']
        )
        self.__cur =  self.__con.cursor()
    
    def create(self, userData):
        sql_user = ""
        sql_user_left = "INSERT INTO Users ("
        sql_user_right = ") VALUES ("

        if('email' in userData):
            sql_user_left += "email" + ","
            sql_user_right += "'" + userData['email'] + "',"

        if('phone' in userData):
            sql_user_left += "phone" + ","
            sql_user_right += "'" + userData['phone'] + "',"

        if('first_name' in userData):
            sql_user_left += "first_name" + ","
            sql_user_right += "'" + userData['first_name'] + "',"

        if('last_name' in userData):
            sql_user_left += "last_name" + ","
            sql_user_right += "'" + userData['last_name'] + "',"

        if('middle_name' in userData):
            sql_user_left += "middle_name" + ","
            sql_user_right += "'" + userData['middle_name'] + "',"

        if('date_of_birth' in userData):
            sql_user_left += "date_of_birth" + ","
            sql_user_right += "'" + userData['date_of_birth'] + "',"
            
        if('country_and_place_of_birth' in userData):
            sql_user_left += "country_and_place_of_birth" + ","
            sql_user_right += "'" + userData['country_and_place_of_birth'] + "',"

        if('nationality' in userData):
            sql_user_left += "nationality" + ","
            sql_user_right += "'" + userData['nationality'] + "',"

        if('facebook' in userData):
            sql_user_left += "facebook" + ","
            sql_user_right += "'" + userData['facebook'] + "',"

        if('country_of_residence' in userData):
            sql_user_left += "country_of_residence" + ","
            sql_user_right += "'" + userData['country_of_residence'] + "',"

        if('address' in userData):
            sql_user_left += "address" + ","
            sql_user_right += "'" + userData['address'] + "',"

        if('zip_code' in userData):
            sql_user_left += "zip_code" + ","
            sql_user_right += "'" + userData['zip_code'] + "',"

        if('twitter' in userData):
            sql_user_left += "twitter" + ","

            if(userData["twitter"] == True):
                sql_user_right += "'1',"
            else:
                sql_user_right += "'0',"

        if('whatsapp' in userData):
            sql_user_left += "whatsapp" + ","

            if(userData["whatsapp"] == True):
                sql_user_right += "'1',"
            else:
                sql_user_right += "'0',"

        if('telegram' in userData):
            sql_user_left += "telegram" + ","

            if(userData["telegram"] == True):
                sql_user_right += "'1',"
            else:
                sql_user_right += "'0',"
            
        sql_user_left = sql_user_left[:-1]
        sql_user_right = sql_user_right[:-1]

        sql_user_right += ")"

        sql_user = sql_user_left + sql_user_right

        self.__connect()
        try:
            sql_result_user = self.__cur.execute(sql_user)     

            #id нового пользователя
            user_id = self.__cur.lastrowid

            sql_passport = "INSERT INTO Passport (name, ext, file) VALUES ( %s, %s, %s)"

            sql_result_passport = self.__cur.execute(sql_passport, (userData['passport']['name'], userData['passport']['ext'], base64.b64decode(userData['passport']['file'].encode('utf-8'))))

            passport_id = self.__cur.lastrowid

            sql_up = "INSERT INTO UP (user_id, passport_id) VALUES ( %s, %s)"
            
            sql_result_up = self.__cur.execute(sql_up, (user_id, passport_id))

            if (not sql_result_passport or not sql_result_user or not sql_result_up):
                raise Exception("Error - One of the requests was not fulfilled")

            self.__con.commit()
        except Exception as err:
            print(str(err))
            self.__con.rollback()
        finally:
            self.__close()

    def __close(self):
        self.__cur.close()
        self.__con.close()