import pymysql
import base64
import json

class Users:
    def __connect(self, file):
        con_info = json.loads(open('./config/' + file, 'r').read())

        self.__con = pymysql.connect(
            host=con_info['host'],
            user=con_info['user'],
            password=con_info['password'],
            port=con_info['port'],
            db=con_info['db'],
            charset=con_info['charset']
        )
        self.__cur = self.__con.cursor()

    def createVerifier(self, data):
        self.__connect('connect_db.json')

        sql_result = {}

        sql = "INSERT INTO verifierUsers (rsa_pub) VALUES ( %s)"

        sql_verifier_result = self.__cur.execute(sql, data["rsa_key"])

        self.__con.commit()

        user_id = self.__cur.lastrowid

        sql_result["id"] = user_id

        self.__close()

        return sql_result

    def getAll(self, data):
        self.__connect('connect_db.json')

        sql_result = []

        sql_user_arr = [
            "id",
            "first_name",
            "last_name"
        ]

        sql_user = "SELECT "

        for sql_ell in sql_user_arr:
            sql_user += sql_ell + ","
        
        sql_user = sql_user[:-1]

        sql_user += " FROM Users LIMIT " + str(data["limit"]) + " OFFSET " + str(data["offset"])

        sql_result_user = self.__cur.execute(sql_user)
        sql_user_data = self.__cur.fetchall()

        q = 0
        user_data = {}

        while(q < len(sql_user_data)):
            i = 0
            while(i < len(sql_user_arr)):
                user_data[sql_user_arr[i]] = sql_user_data[q][i]
                i += 1
            sql_result.append(user_data)
            q += 1

        self.__close()

        return  sql_result

    def checkPermission(self, data):
        self.__connect('connect_db.json')

        sql = "SELECT rsa_pub FROM verifierUsers WHERE id=%s"

        sql_result = self.__cur.execute(sql, str(data))
        sql_data = self.__cur.fetchone()

        self.__close()

        return sql_data
        
    def getOne(self, data, move = False):
        try:
            self.__connect('connect_db.json')

            sql_result = {}

            #Массив данных для запроса
            sql_user_arr = [
                "id",
                "email",
                "phone",
                "first_name",
                "last_name",
                "middle_name",
                "date_of_birth",
                "country_and_place_of_birth",
                "nationality",
                "country_of_residence",
                "address",
                "zip_code"
            ]

            sql_move_user_arr = [
                "rsa_key",
                "facebook",
                "twitter",
                "whatsapp",
                "telegram",
                "email",
                "phone",
                "first_name",
                "last_name",
                "middle_name",
                "date_of_birth",
                "country_and_place_of_birth",
                "nationality",
                "country_of_residence",
                "address",
                "zip_code"
            ]

            sql_passport_arr = [
                "file",
                "ext",
                "name"
            ]

            sql_user = "SELECT "

            if(move):
                for sql_ell in sql_move_user_arr:
                    sql_user += sql_ell + ","
            else:
                for sql_ell in sql_user_arr:
                    sql_user += sql_ell + ","

            sql_user = sql_user[:-1]

            sql_user += " FROM Users WHERE id=" + str(data["id"])

            sql_result_user = self.__cur.execute(sql_user)
            sql_user_data = self.__cur.fetchone()

            i = 0

            if(move):
                while(i < len(sql_move_user_arr)):
                    sql_result[sql_move_user_arr[i]] = sql_user_data[i]
                    i += 1
            else:
                while(i < len(sql_user_arr)):
                    sql_result[sql_user_arr[i]] = sql_user_data[i]
                    i += 1

            passport_id_sql = "SELECT passport_id FROM UP WHERE user_id=" + str(data["id"])

            sql_result_passport_id = self.__cur.execute(passport_id_sql)
            sql_passport_id_data = self.__cur.fetchone()
            sql_passport_id_data = str(sql_passport_id_data[0])

            sql_passport = "SELECT "

            for sql_ell in sql_passport_arr:
                sql_passport += sql_ell + ","

            sql_passport = sql_passport[:-1]

            sql_passport += " FROM Passport WHERE id=" + sql_passport_id_data

            sql_result_passport = self.__cur.execute(sql_passport)
            sql_passport_data = self.__cur.fetchone()

            sql_file_result = {}

            q = 0

            while(q < len(sql_passport_arr)):
                sql_file_result[sql_passport_arr[q]] = sql_passport_data[q]
                q += 1

            sql_file_result["file"] = base64.b64encode(sql_file_result["file"]).decode('utf-8')

            sql_result["file"] = sql_file_result
        except:
            return False
        finally:
            self.__close()

        return sql_result

    def create(self, userData, move = False):
        sql_user = ""
        sql_user_left = "INSERT INTO Users ("
        sql_user_right = ") VALUES ("
        sql_values = ()

        if('rsa_key' in userData):
            sql_user_left += "rsa_key" + ","
            sql_user_right += "%s,"
            sql_values = sql_values + (userData['rsa_key'],)

        if('email' in userData):
            sql_user_left += "email" + ","
            sql_user_right += "%s,"
            sql_values = sql_values + (userData['email'],)

        if('phone' in userData):
            sql_user_left += "phone" + ","
            sql_user_right += "%s,"
            sql_values = sql_values + (userData['phone'],)

        if('first_name' in userData):
            sql_user_left += "first_name" + ","
            sql_user_right += "%s,"
            sql_values = sql_values + (userData['first_name'],)

        if('last_name' in userData):
            sql_user_left += "last_name" + ","
            sql_user_right += "%s,"
            sql_values = sql_values + (userData['last_name'],)

        if('middle_name' in userData):
            sql_user_left += "middle_name" + ","
            sql_user_right += "%s,"
            sql_values = sql_values + (userData['middle_name'],)

        if('date_of_birth' in userData):
            sql_user_left += "date_of_birth" + ","
            sql_user_right += "%s,"
            sql_values = sql_values + (userData['date_of_birth'],)
            
        if('country_and_place_of_birth' in userData):
            sql_user_left += "country_and_place_of_birth" + ","
            sql_user_right += "%s,"
            sql_values = sql_values + (userData['country_and_place_of_birth'],)

        if('nationality' in userData):
            sql_user_left += "nationality" + ","
            sql_user_right += "%s,"
            sql_values = sql_values + (userData['nationality'],)

        if('facebook' in userData):
            sql_user_left += "facebook" + ","
            sql_user_right += "%s,"
            sql_values = sql_values + (userData['facebook'],)

        if('country_of_residence' in userData):
            sql_user_left += "country_of_residence" + ","
            sql_user_right += "%s,"
            sql_values = sql_values + (userData['country_of_residence'],)

        if('address' in userData):
            sql_user_left += "address" + ","
            sql_user_right += "%s,"
            sql_values = sql_values + (userData['address'],)

        if('zip_code' in userData):
            sql_user_left += "zip_code" + ","
            sql_user_right += "%s,"
            sql_values = sql_values + (userData['zip_code'],)

        if('twitter' in userData):
            sql_user_left += "twitter" + ","
            sql_user_right += "%s,"

            if(userData["twitter"] == True):
                sql_values = sql_values + ("1",)
            else:
                sql_values = sql_values + ("0",)

        if('whatsapp' in userData):
            sql_user_left += "whatsapp" + ","
            sql_user_right += "%s,"

            if(userData["whatsapp"] == True):
                sql_values = sql_values + ("1",)
            else:
                sql_values = sql_values + ("0",)

        if('telegram' in userData):
            sql_user_left += "telegram" + ","
            sql_user_right += "%s,"

            if(userData["telegram"] == True):
                sql_values = sql_values + ("1",)
            else:
                sql_values = sql_values + ("0",)

        sql_user_left = sql_user_left[:-1]
        sql_user_right = sql_user_right[:-1]

        sql_user_right += ")"

        sql_user = sql_user_left + sql_user_right

        if(move):
            self.__connect('connect_ver_db.json')
        else:
            self.__connect('connect_db.json')
        try:
            sql_result_user = self.__cur.execute(sql_user, sql_values)

            #id нового пользователя
            user_id = self.__cur.lastrowid

            sql_passport = "INSERT INTO Passport (name, ext, file) VALUES ( %s, %s, %s)"

            sql_result_passport = self.__cur.execute(sql_passport, (userData['file']['name'], userData['file']['ext'], base64.b64decode(userData['file']['file'].encode('utf-8'))))

            passport_id = self.__cur.lastrowid

            sql_up = "INSERT INTO UP (user_id, passport_id) VALUES ( %s, %s)"
            
            sql_result_up = self.__cur.execute(sql_up, (user_id, passport_id))

            if (not sql_result_passport or not sql_result_user or not sql_result_up):
                raise Exception("Error - One of the requests was not fulfilled")

            self.__con.commit()
        except Exception as err:
            
            print(str(err))
            self.__con.rollback()
            return False

        finally:
            self.__close()

        return True

    def delete(self, data):
        self.__connect('connect_db.json')
        try:
            sql_up_arr = [
                "id",
                "passport_id"
            ]

            sql_up = "SELECT "

            for sql_ell in sql_up_arr:
                    sql_up += sql_ell + ","

            sql_up = sql_up[:-1]
            
            sql_up += " FROM UP WHERE user_id=" + str(data["id"])

            sql_result_up =  self.__cur.execute(sql_up)

            sql_up_data = self.__cur.fetchone()

            i = 0
            up_data = {}

            while(i < len(sql_up_arr)):
                up_data[sql_up_arr[i]] = sql_up_data[i]
                i += 1

            sql_delete_up = "DELETE FROM UP WHERE id=" + str(up_data["id"])
            sql_result_delete_up = self.__cur.execute(sql_delete_up)

            sql_delete_passport = "DELETE FROM Passport WHERE id=" + str(up_data["passport_id"])
            sql_result_delete_passport = self.__cur.execute(sql_delete_passport)

            sql_delete_user = "DELETE FROM Users WHERE id=" + str(data["id"])

            sql_result_delete_user = self.__cur.execute(sql_delete_user)

            if (not sql_result_delete_user or not sql_result_delete_passport or not sql_result_delete_up):
                raise Exception("Error - One of the requests was not fulfilled")

            self.__con.commit()
        
        except Exception as err:
            
            print(str(err))
            self.__con.rollback()
            return False

        finally:
            self.__close()

        return True
    
    def moveUser(self, data):
        user = self.getOne(data, True)

        if(user):
            move_result = self.create(user, True)

            if(move_result):    #проверяем удалось ли перенести пользователя
                delete_result = self.delete(data)
                if(delete_result):  #проверяем удалось ли удалить пользователя из временной
                    return True

        return False

    def __close(self):
        self.__cur.close()
        self.__con.close()