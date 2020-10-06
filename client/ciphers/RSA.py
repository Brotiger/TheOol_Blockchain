import rsa
import os
import base64

class rsaCipher:
    def setPubKey(self, key):
        self.__pubkey = rsa.PublicKey.load_pkcs1(key)

    def __getPrivKey(self):
        return self.__privkey

    def getPubKey(self):
        return self.__pubkey

    def createKeys(self):
        (self.__pubkey, self.__privkey) = rsa.newkeys(512, True, 8)

    def decrypt(self, message):
        message = rsa.decrypt(message, self.__getPrivKey())
        return bytes.decode(message)

    def encrypt(self, message):
        message = rsa.encrypt(message.encode('utf8'), self.getPubKey())
        message = base64.b64encode(message).decode('utf-8')
        return message

