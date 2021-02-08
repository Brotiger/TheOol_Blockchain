'''
    Название: BlockChain;
    Описание: Программа отвечает за создания и верификацию блоков в блокчейн цепочке, а так же поиск иниформации в данной цепочке;
    Автор: Берестнев Петр Дмитриевич, Берестнев Дмитрий Дмитриевич;
    Версия: 1.0.0;
'''

import hashlib
import json 
import os.path
import time

class BlockChain : 
    __adres = "./"
    __blockChain = "BlockChain"
    __metaDir = "meta"
    __blockDir = "block"
    __data = []

    def __init__(self, adres = None):
        if(adres):
            self.__adres = adres

        self.__adres += self.__blockChain + '/'

        if(not os.path.exists(self.__adres)):
            os.mkdir(self.__adres)
            os.mkdir(self.__adres + self.__metaDir)
            os.mkdir(self.__adres + self.__blockDir)
    
    def lastFile(self):
        statment=0

        if(os.path.exists(self.__adres + self.__metaDir + "/lastFile.meta")):
            f= open(self.__adres + self.__metaDir + "/lastFile.meta", "r")
            statment = int(f.read())
            f.close()

        return statment
        
    def changeLastFile(self, i, dataHash):
        file = open(self.__adres + self.__metaDir + "/lastFile.meta", "w")
        file.write(str(i))
        file.close()
        f = open(self.__adres + self.__metaDir + "/lastHash.meta", "w")
        f.write(dataHash)
        f.close()

    def getPrevHash(self):
        
        statment=str("")
        prev_hash=str("")
        i = str(self.lastFile())
        
        if(os.path.exists(self.__adres + self.__metaDir + "/lastHash.meta")):
            f1= open(self.__adres + self.__metaDir + "/lastHash.meta","r")
            prev_hash=f1.read()
            f1.close()
        else:
            prev_hash=None

        return prev_hash

    def __getFiles(self, path):
        for root, dirs, files in os.walk(path):
            files.sort()
        return files

    def verify(self):
        i = self.lastFile()
        prevHash = ""

        path = self.__adres + self.__blockDir
        if(os.path.exists(path)):
            files = self.__getFiles(path)
            for fileName in files:
                fileInfo= (open(path + "/" + fileName, "r")).read()
                fileArr = fileInfo.split("\n")

                if(fileArr[0] != prevHash):
                    return False

                prevHash = hashlib.sha256(fileInfo.encode()).hexdigest()

        return True

    def select(self, fieldName = '', fieldValue = '', exists = False):
        path = self.__adres + self.__blockDir

        resultArr = []

        if(os.path.exists(path)):
            files = self.__getFiles(path)

            for fileName in files:
                fileInfo= (open(path + "/" + fileName, "r")).read()
                fileArr = fileInfo.split("\n")

                blockData = json.loads(fileArr[2])

                for data in blockData:
                    if(fieldName == '' and fieldValue == ''):
                        resultArr.append(data)
                    elif(fieldName and fieldValue == '' and fieldName in data):
                        resultArr.append(data[fieldName])
                    else:
                        if(fieldName in data):
                            if(data[fieldName] == fieldValue):
                                if(exists):
                                    return True
                                resultArr.append(data)

        if(not resultArr):
            return False
            
        return resultArr