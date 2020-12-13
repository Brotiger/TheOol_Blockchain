import re
import base64
import sys

class validator:

    __params = {}

    def __init__(self, userData):
        self.__params = userData
    
    def rsaKey(self, name):
        if (not name in self.__params):
            return 'Rsa key required'
        elif not (type(self.__params[name]) is str):
            return 'Invalid type'
        return False
    
    def offset(self, name):
        if (not name in self.__params):
            return 'Offset required'
        elif not (type(self.__params[name]) is int):
            return 'Invalid type'
        elif(self.__params[name] < 0):
            return "Offset must be positive"
        return False

    def limit(self, name):
        if (not name in self.__params):
            return 'Limit required'
        elif not (type(self.__params[name]) is int):
            return 'Invalid type'
        elif(self.__params[name] < 0):
            return "Limit must be positive"
        elif (self.__params[name] > 100):
            return "Limit should not be more than 100"
        return False

    def id(self, name):
        if (not name in self.__params):
            return 'Id required'
        elif not (type(self.__params[name]) is int):
            return 'Invalid type'
        elif(self.__params[name] < 0):
            return "Id must be positive"
        return False

    def confirm(self, name):
        if (not name in self.__params):
            return 'Confirm required'
        elif not (type(self.__params[name]) is bool):
            return 'Invalid type'
        return False