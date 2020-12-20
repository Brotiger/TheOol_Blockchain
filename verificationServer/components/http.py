import json
import string
import random

import ciphers.AES as AES

class http:

    def __init__(self, rsaObj):

        self.__aesObj = AES.aesCipher()
        self.__rsaObj = rsaObj

    def dataDecrypt(self, res):

        params = json.loads(res)

        AESPassword = params['aes_key']

        AESPassword = self.__rsaObj.decrypt(AESPassword)

        return json.loads(self.__aesObj.decrypt(params['data'], AESPassword))

    def createSign(self, data):
        new_data = {}
        for k in sorted(data.keys()):
            new_data[k] = data[k]

        sign = self.__rsaObj.createSign(new_data)

        return sign

    def dataEncrypt(self, data):
        data["sign"] = self.createSign(data)

        passwordAES = self.__randompassword()
        encryptedData = self.__aesObj.encrypt(data, passwordAES)

        passwordAES = self.__rsaObj.encrypt(passwordAES)

        dataPost = {
            "aes_key": passwordAES,
            "data": encryptedData
        }
            
        return dataPost

    def __randompassword(self):
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        size = 34
        return ''.join(random.choice(chars) for x in range(size))