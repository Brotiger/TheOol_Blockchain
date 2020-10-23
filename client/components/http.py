import string
import random
import json
import requests
import ciphers.AES as AES
import ciphers.RSA as RSA
import os

class http:
    def __init__(self):
        self.__aesObj = AES.aesCipher()
        self.__rsaObj = RSA.rsaCipher()

    def sendData(self, url, data):

        self.__getKey()
        self.__rsaObj.createKeys()
        data["rsa_key"] = self.__rsaObj.getPubKeyClient()

        passwordAES = self.__randompassword()

        encryptedData = self.__aesObj.encrypt(json.dumps(data), passwordAES)

        passwordAES = self.__rsaObj.encrypt(passwordAES)

        dataPost = {
            "aes_key": passwordAES,
            "data": encryptedData
        }
        response = requests.post(url, json=dataPost)
        
        response = self.dataDecrypt(response)
        print(response)
    
    def __getKey(self):
        
        response = requests.post("http://" + os.environ.get('VER_SERVER_IP') + ":80/api/get/rsa")
        self.__rsaObj.setPubKeyServer(response.json()['rsa_key'])

    def __randompassword(self):
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        size = 34
        return ''.join(random.choice(chars) for x in range(size))

    def dataDecrypt(self, res):

        params = res.json()
        
        AESPassword = params['aes_key']

        AESPassword = self.__rsaObj.decrypt(AESPassword)

        return json.loads(self.__aesObj.decrypt(params['data'], AESPassword))