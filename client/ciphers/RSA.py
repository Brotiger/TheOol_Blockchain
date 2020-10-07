import rsa
import os
import base64

class rsaCipher:
    def setPubKeyServer(self, key):
        self.__pubkeyServer = rsa.PublicKey.load_pkcs1(key)

    def __getPrivKeyClient(self):
        return self.__privkeyClient

    def getPubKeyServer(self):
        return self.__pubkeyServer

    def getPubKeyClient(self):
        return self.__pubkeyClient.save_pkcs1().decode('ascii')

    def createKeys(self):
        (self.__pubkeyClient, self.__privkeyClient) = rsa.newkeys(512)

    def decrypt(self, message):
        message = base64.b64decode(message.encode('utf-8'))
        message = rsa.decrypt(message, self.__getPrivKeyClient())
        return bytes.decode(message)

    def encrypt(self, message):
        message = rsa.encrypt(message.encode('utf8'), self.getPubKeyServer())
        message = base64.b64encode(message).decode('utf-8')
        return message

