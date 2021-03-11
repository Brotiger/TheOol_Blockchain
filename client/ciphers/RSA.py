import rsa
import os
import base64
import re
import json
import ciphers.AES as AES

class rsaCipher:

    __folder = "./wallet/"
    __privRSA = "rsa.priv"
    __pubRSA = "rsa.pub"

    def __init__(self, walletPassword):
        self.__aesObj = AES.aesCipher()

        with open("./keys/rsa.pub", mode='rb') as text_file:
            pubKeyData = text_file.read()
        self.__pubKeyServer = rsa.PublicKey.load_pkcs1(pubKeyData)
        if(self.checkKeys()):
            self.getKeys(walletPassword)
        else:
            self.createKeys(walletPassword)

    def __getPrivKeyClient(self):
        return self.__privKeyClient

    def getPubKeyServer(self):
        return self.__pubKeyServer

    def getPubKeyClient(self):
        return self.__pubKeyClient.save_pkcs1().decode('utf-8')

    def createKeys(self, walletPassword):
        (self.__pubKeyClient, self.__privKeyClient) = rsa.newkeys(512)

        with open(self.__folder + self.__privRSA, "w") as text_file:
            #print(self.__privKeyClient.save_pkcs1().decode('utf-8'))
            text_file.write(json.dumps(self.__aesObj.encrypt(self.__privKeyClient.save_pkcs1().decode('utf-8'), walletPassword)))

        with open(self.__folder + self.__pubRSA, "w") as text_file:
            text_file.write(self.__pubKeyClient.save_pkcs1().decode('utf-8'))

    def getKeys(self, walletPassword):
        with open(self.__folder + self.__privRSA, "rb") as text_file:
            privKeyData = self.__aesObj.decrypt(json.loads(text_file.read()), walletPassword)
            privKeyData = privKeyData[1:]
            privKeyData = privKeyData[:-1]
            privKeyData = privKeyData.replace(r"\n", "\n")#могут быть проблемы
        self.__privKeyClient = rsa.PrivateKey.load_pkcs1(privKeyData)

        with open(self.__folder + self.__pubRSA, "rb") as text_file:
            pubKeyData = text_file.read()
        self.__pubKeyClient = rsa.PublicKey.load_pkcs1(pubKeyData)
    
    def checkKeys(self):
        if(os.path.exists(self.__folder + self.__pubRSA) and os.path.exists(self.__folder + self.__privRSA)):
            return True
        return False

    def decrypt(self, message):
        message = base64.b64decode(message.encode('utf-8'))
        message = rsa.decrypt(message, self.__privKeyClient)
        return bytes.decode(message)

    def encrypt(self, message):
        message = rsa.encrypt(message.encode('utf8'), self.getPubKeyServer())
        message = base64.b64encode(message).decode('utf-8')
        return message

    def createSign(self, message):
        new_message = {}
        for k in sorted(message.keys()):
            new_message[k] = message[k]

        new_message = json.dumps(new_message)
        new_message = new_message.encode('utf-8')
        sign = rsa.sign(new_message, self.__privKeyClient, 'SHA-1')
        sign = base64.b64encode(sign).decode('utf-8')
        return sign

    def verifySign(self, message, sign):
        new_message = {}
        for k in sorted(message.keys()):
            new_message[k] = message[k]

        sign = base64.b64decode(sign.encode('utf-8'))
        new_message = json.dumps(new_message)
        new_message = new_message.encode('utf-8')
        try:
            rsa.verify(new_message, sign, self.getPubKeyServer())
        except:
            return False
        return True