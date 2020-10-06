import json
import string
import random

import ciphers.AES as AES
import ciphers.RSA as RSA

class http:

   # __aesObj = {}
   # __rsaObj = {}

    def __init__(self, rsaObj):

        self.__aesObj = AES.aesCipher()
        self.__rsaObj = rsaObj

    def dataDecrypt(self, res):

        params = json.loads(res)

        AESPassword = params['aes_password']

        AESPassword = self.__rsaObj.decrypt(AESPassword)

        return json.loads(self.__aesObj.decrypt(params['data'], AESPassword))

    def dataEncrypt(self, data):

        passwordAES = self.__randompassword()
        encryptedData = self.__aesObj.encrypt(json.dumps(data), passwordAES)

        dataPost = {
            "aes_password": passwordAES,
            "data": encryptedData
        }
            
        return dataPost

    def __randompassword(self):
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        size = 34
        return ''.join(random.choice(chars) for x in range(size))