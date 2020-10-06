import re

class userValidator:

    __params = {}

    def __init__(self, userData):
        self.__params = userData

    def email(self, name):
        maxSize = 256
        reg = r"^[a-z]{1}[a-z0-9]*@[a-z]{1}[a-z0-9]*\.[a-z]+$"

        if (not name in self.__params) or (not len(self.__params[name])):
            return 'Email required'
        elif not (type(self.__params[name]) is str):
            return 'Invalid type'
        elif not re.match(reg, self.__params[name]):
            return 'Incorrect email'
        elif (len(self.__params[name]) > maxSize):
            return 'Max email size ' + str(maxSize) + ' characters'
        return False

    def password(self, name):
        minSize = 30

        if (not name in self.__params) or (not len(self.__params[name])):
            return 'Password required'
        elif not (type(self.__params[name]) is str):
            return 'Invalid type'
        elif (len(self.__params[name]) > minSize):
            return 'Min password size ' + str(minSize) + ' characters'
        return False

    def phone(self, name):
        maxSize = 15
        reg = r"^[0-9]+$"

        if (not name in self.__params) or (not len(self.__params[name])):
            return False
        elif not (type(self.__params[name]) is str):
            return 'Invalid type'
        elif not re.match(reg, self.__params[name]):
            return 'Incorrect phone'
        elif (len(self.__params[name]) > maxSize):
            return 'Max phone size ' + str(maxSize) + ' characters'
        return False

    def fName(self, name):
        maxSize = 30
        reg = r"^[A-ZА-Я]{1}[a-zа-я]+$"

        if (not name in self.__params) or (not len(self.__params[name])):
            return 'first name required'
        elif not (type(self.__params[name]) is str):
            return 'Invalid type'
        elif not re.match(reg, self.__params[name]):
            return 'Incorrect first name'
        elif (len(self.__params[name]) > maxSize):
            return 'Max first name size ' + str(maxSize) + ' characters'
        return False

    def lName(self, name):
        maxSize = 30
        reg = r"^[A-ZА-Я]{1}[a-zа-я]+$"

        if (not name in self.__params) or (not len(self.__params[name])):
            return 'last name required'
        elif not (type(self.__params[name]) is str):
            return 'Invalid type'
        elif not re.match(reg, self.__params[name]):
            return 'Incorrect last name'
        elif (len(self.__params[name]) > maxSize):
            return 'Max last name size ' + str(maxSize) + ' characters'
        return False

    def mName(self ,name):
        maxSize = 30
        reg = r"^[A-ZА-Я]{1}[a-zа-я]+$"

        if (not name in self.__params) or (not len(self.__params[name])):
            return False
        elif not (type(self.__params[name]) is str):
            return 'Invalid type'
        elif not re.match(reg, self.__params[name]):
            return 'Incorrect last name'
        elif (len(self.__params[name]) > maxSize):
            return 'Max last name size ' + str(maxSize) + ' characters'
        return False

    def dateOfBirth(self ,name):
        reg = r"^[0-9]+$"

        if (not name in self.__params) or (not len(self.__params[name])):
            return 'Date of birth required'
        elif not (type(self.__params[name]) is str):
            return 'Invalid type'
        elif not re.match(reg, self.__params[name]):
            return 'Incorrect date of birth'
        return False

    def countryAndPlaceOfBirth(self ,name):
        maxSize = 150
        reg = r"^[a-zA-Zа-яА-Я]+$"

        if (not name in self.__params) or (not len(self.__params[name])):
            return False
        elif not (type(self.__params[name]) is str):
            return 'Invalid type'
        elif not re.match(reg, self.__params[name]):
            return 'Incorrect country and place of birth'
        elif (len(self.__params[name]) > maxSize):
            return 'Max country and place of birth size ' + str(maxSize) + ' characters'
        return False

    def nationality(self ,name):
        maxSize = 30
        reg = r"^[A-ZА-Я]{1}[a-zа-я]+$"

        if (not name in self.__params) or (not len(self.__params[name])):
            return False
        elif not (type(self.__params[name]) is str):
            return 'Invalid type'
        elif not re.match(reg, self.__params[name]):
            return 'Incorrect nationality'
        elif (len(self.__params[name]) > maxSize):
            return 'Max nationality size ' + str(maxSize) + ' characters'
        return False

    def countryOfResidence(self ,name):
        maxSize = 30
        reg = r"^[A-ZА-Я]{1}[a-zа-я]+$"

        if (not name in self.__params) or (not len(self.__params[name])):
            return 'Country of residence required'
        elif not (type(self.__params[name]) is str):
            return 'Invalid type'
        elif not re.match(reg, self.__params[name]):
            return 'Incorrect country of residence'
        elif (len(self.__params[name]) > maxSize):
            return 'Max country of residence size ' + str(maxSize) + ' characters'
        return False
    
    def address(self ,name):
        maxSize = 30
        reg = r"^[A-Za-zА-Яа-я]+$"

        if (not name in self.__params) or (not len(self.__params[name])):
            return 'Address required'
        elif not (type(self.__params[name]) is str):
            return 'Invalid type'
        elif not re.match(reg, self.__params[name]):
            return 'Incorrect address'
        elif (len(self.__params[name]) > maxSize):
            return 'Max address size ' + str(maxSize) + ' characters'
        return False

    def zipCode(self ,name):
        maxSize = 9
        reg = r"^[0-9]+$"

        if (not name in self.__params) or (not len(self.__params[name])):
            return 'Zip code required'
        elif not (type(self.__params[name]) is str):
            return 'Invalid type'
        elif not re.match(reg, self.__params[name]):
            return 'Incorrect zip code'
        elif (len(self.__params[name]) > maxSize):
            return 'Max zip code size ' + str(maxSize) + ' characters'
        return False

    def faceBook(self ,name):
        maxSize = 50
        reg = r"^[a-zA-Z]{1}[a-zA-Z0-9]+$"

        if (not name in self.__params) or (not len(self.__params[name])):
            return False
        elif not (type(self.__params[name]) is str):
            return 'Invalid type'
        elif not re.match(reg, self.__params[name]):
            return 'Incorrect faceBook address'
        elif (len(self.__params[name]) > maxSize):
            return 'Max Facebook address size ' + str(maxSize) + ' characters'
        return False
    def messengers(self ,name):

        messengersType = ["Twitter", "WhatsApp", "Telegram"]

        if (not name in self.__params) or (not len(self.__params[name])):
            return False
        elif not (type(self.__params[name]) is list):
            return 'Incorrect messengers type'
        else:
            for key in self.__params[name]:
                if not key in messengersType:
                    return 'Incorrect messengers type'
        return False