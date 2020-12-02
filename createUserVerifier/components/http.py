import string
import random
import json
import requests
import ciphers.AES as AES
import ciphers.RSA as RSA
import os
import hashlib
class http:
    def __init__(self):
        self.__aesObj = AES.aesCipher()
        self.__rsaObj = RSA.rsaCipher()
    def sendData(self, url):
        data = {}
        data["rsa_key"] = self.__rsaObj.getPubKeyClient()
        response = requests.post(url, json=data)
        return response.json()