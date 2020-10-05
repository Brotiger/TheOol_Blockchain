import rsa
import os

class RSA:

    __priKeyPath = ""
    __pubKeyPath = ""

    __priFile = "rsa.pri"
    __pubFile = "rsa.pub"

    def __init__(self, priKeyPath = "./keys", pubKeyPath = "./keys"):
        self.__priKeyPath = priKeyPath
        self.__pubKeyPath = pubKeyPath
        if not os.path.exists(self.__priKeyPath + "/" + self.__priFile) or not os.path.exists(self.__pubKeyPath + "/" + self.__priFile):
            os.makedirs(self.__priKeyPath, exist_ok=True)
            os.makedirs(self.__pubKeyPath, exist_ok=True)
            self.__createKeys()

    def __loadPrivKey(self):
        with open(self.__priKeyPath + "/" + self.__priFile, mode='r') as privatefile:
            keydata = privatefile.read()
        return rsa.PrivateKey.load_pkcs1(keydata) #rsa.PrivateKey.load_pkcs1(keydata)

    def loadPubKey(self):
        with open(self.__pubKeyPath + "/" + self.__pubFile, mode='r') as pubfile:
            keydata = pubfile.read()
        return keydata

    def __createKeys(self):
        (pubkey, privkey) = rsa.newkeys(512, True, 8)
        with open(self.__pubKeyPath + "/" + self.__pubFile, "w") as text_file:
            text_file.write(pubkey.save_pkcs1().decode('ascii'))
        with open(self.__priKeyPath + "/" + self.__priFile, "w") as text_file:
            text_file.write(privkey.save_pkcs1().decode('ascii'))

    def decrypt(self, crypto):
        rsa.decrypt(crypto, self.__loadPrivKey())
        return bytes.decode(message)

