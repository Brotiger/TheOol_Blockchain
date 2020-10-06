import rsa
import os
import base64

class rsaCipher:
    def __getPrivKey(self):
        return self.__privkey

    def getPubKey(self):
        return self.__pubkey.save_pkcs1().decode('ascii')

    def createKeys(self):
        (self.__pubkey, self.__privkey) = rsa.newkeys(512, True, 8)

    def decrypt(self, message):
        message = base64.b64decode(message.encode('utf-8'))
        message = rsa.decrypt(message, self.__getPrivKey())
        return bytes.decode(message)

    def encrypt(self, message):
        message = rsa.encrypt(message, self.getPubKey())
        return bytes.decode(message)
