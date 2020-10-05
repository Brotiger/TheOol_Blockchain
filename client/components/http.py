import string
import random
import json
import requests
import ciphers.AES as AES

class http:

    __aesObj = {}

    def __init__(self):
        self.__aesObj = AES.aesCipher()
    def send(self, url, data):

        passwordAES = self.__randompassword()
        encryptedData = self.__aesObj.encrypt(json.dumps(data), passwordAES)

        dataPost = {
            "aes_password": passwordAES,
            "data": encryptedData
        }
            
        response = requests.post(url, json=dataPost)
        response = self.dataDecrypt(response)
        print(response)

    def __randompassword(self):
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        size = 34
        return ''.join(random.choice(chars) for x in range(size))

    def dataDecrypt(self, res):

        params = res.json()

        AESPassword = params['aes_password']

        return json.loads(self.__aesObj.decrypt(params['data'], AESPassword))