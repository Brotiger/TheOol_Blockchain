import rsa
import base64
import os

class Generator:

    __rsaFolder = "./keys/"

    def createRsaKeys(self):
        (pubkey, privkey) = rsa.newkeys(512)

        if(not os.path.exists(self.__rsaFolder)):
            os.mkdir(self.__rsaFolder)

        with open(self.__rsaFolder + "rsa.pub", "w") as text_file:
            text_file.write(pubkey.save_pkcs1().decode('utf-8'))

        with open(self.__rsaFolder + "rsa.priv", "w") as text_file:
            text_file.write(privkey.save_pkcs1().decode('utf-8'))

GeneratorObj = Generator()
GeneratorObj.createRsaKeys()