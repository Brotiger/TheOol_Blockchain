import rsa
import base64
import json

class rsaCipher:
    def __init__(self):

        with open("./keys/server_rsa.priv", mode='rb') as privatefile:
            privKeyData = privatefile.read()
        self.__privkey = rsa.PrivateKey.load_pkcs1(privKeyData) 

    def getPrivKey(self):
        return self.__privkey

    def getPubKeyClient(self):
        return self.__pubKeyClient

    def decrypt(self, message):
        message = base64.b64decode(message.encode('utf-8'))
        message = rsa.decrypt(message, self.getPrivKey())
        return bytes.decode(message)

    def encrypt(self, message):
        message = rsa.encrypt(message.encode('utf8'), self.getPubKeyClient())
        message = base64.b64encode(message).decode('utf-8')
        return message

    def setPubKeyClient(self, key):
        self.__pubKeyClient = rsa.PublicKey.load_pkcs1(key)

    def verifySign(self, message, sign):
        new_message = {}
        for k in sorted(message.keys()):
            new_message[k] = message[k]

        sign = base64.b64decode(sign.encode('utf-8'))
        new_message = json.dumps(new_message)
        new_message = new_message.encode('utf-8')
        try:
            rsa.verify(new_message, sign, self.getPubKeyClient())
        except:
            return False
        return True

    def createSign(self, message):
        new_message = {}
        for k in sorted(message.keys()):
            new_message[k] = message[k]

        new_message = json.dumps(new_message)
        new_message = new_message.encode('utf-8')
        sign = rsa.sign(new_message, self.getPrivKey(), 'SHA-1')
        sign = base64.b64encode(sign).decode('utf-8')
        return sign
