import components.http as http
import os
import base64
from components.BlockChain import BlockChain
import re

class MainController:
    def __init__(self, wallet_priv = "./wallet/rsa.priv", wallet_pub = "./wallet/rsa.pub", blocksPath = "block", metaPath = "meta", BlockChainDir = "./BlockChain"):
        self.__wallet_priv = wallet_priv
        self.__wallet_pub = wallet_pub

        self.__blocksPath = blocksPath
        self.__metaPath = metaPath
        self.__BlockChainDir = BlockChainDir

        self.__httpObj = http.http()

        if (not os.environ.get('VER_SERVER_IP')):
            self.__verServerIP = "127.0.0.1"
        else:
            self.__verServerIP = os.environ.get('VER_SERVER_IP')

    def reg(self, data, walletPassword):
        response = self.__httpObj.sendData("http://" + self.__verServerIP + ":80/api/users/reg",data, walletPassword)

        if(response["success"] == False):
            os.remove(self.__wallet_priv)
            os.remove(self.__wallet_pub)
                        
        return response

    def checkReg(self):
        if(os.path.exists(self.__wallet_priv)):
            return True
        return False

    def __filterBlocks(self, file):
        if re.match(r'^data_file_[0-9]*\.block', file) is not None:
            return 1
        else:
            return 0

    def checkChain(self, walletPassword):
        try:
            data = {}

            if(not os.path.exists(self.__BlockChainDir + "/" + self.__blocksPath)):
                raise Exception("У вас отсутствует цепочка, запросите ее с сервера через соответствующий пункт меню")
            elif(not os.path.exists(self.__BlockChainDir + "/" + self.__metaPath + "/lastHash.meta")):
                raise Exception("У вас нету мета файла lastHash, для того что бы его получить пожалуйста обновите цепочку")
            elif(not os.path.exists(self.__BlockChainDir + "/" + self.__metaPath + "/lastFile.meta")):
                raise Exception("У вас нету мета файла lastFile, для того что бы его получить пожалуйста обновите цепочку")

            responseMeta = self.__httpObj.sendData("http://" + self.__verServerIP + ":80/api/users/getBlockChainInfo",data, walletPassword)

            successMeta = responseMeta["success"]

            if(not successMeta):
                raise Exception("Запрос к серверу выполнен не успешно")
                            
            with open(self.__BlockChainDir + "/" + self.__metaPath + "/lastFile.meta", mode='r') as text_file:
                lastFileLocal = int(text_file.read())

            with open(self.__BlockChainDir + "/" + self.__metaPath + "/lastHash.meta", mode='r') as text_file:
                lastHashLocal = text_file.read()

            blockfiles = os.listdir(self.__BlockChainDir + "/" + self.__blocksPath)
            clearBlockFiles = filter(self.__filterBlocks, blockfiles)
            listDirCount = len(list(clearBlockFiles))

            if(int(responseMeta["data"]["lastFile"]) > int(lastFileLocal) or int(responseMeta["data"]["lastFile"]) > listDirCount):
                data = {
                    "limit": listDirCount
                }
                                
                responseBlocks = self.__httpObj.sendData("http://" + self.__verServerIP + ":80/api/users/getBlocks",data, walletPassword)
                successBlocks = responseBlocks["success"]

                if(not successBlocks):
                    raise Exception("Новые блоки с сервера не получены")
                                
                i = listDirCount + 1

                for block in responseBlocks['data']['blocks']:
                    with open(self.__BlockChainDir + "/" + self.__blocksPath + "/data_file" + '_' + str(i) + ".block", "w") as write_file:
                        write_file.write(block)
                    i += 1

                with open(self.__BlockChainDir + "/" + self.__metaPath + "/lastHash.meta", "w") as write_file:
                    write_file.write(responseMeta["data"]["lastHash"])

                with open(self.__BlockChainDir + "/" + self.__metaPath + "/lastFile.meta", "w") as write_file:
                    write_file.write(responseMeta["data"]["lastFile"])
            elif(not responseMeta["data"]["lastHash"] == lastHashLocal):
                raise Exception("Целостность цепочки нарушена")

            BlockChainObj = BlockChain()
            verifyResult = BlockChainObj.verify()

            if(not verifyResult):
                raise Exception("Целостность цепочки нарушена")
                                
        except Exception as err:
            return err
        else:
            return "Ваша цепочка цела и актуальна"

    def updateChain(self, walletPassword):
        data = {
            "limit": 0
        }
        #Проверка существования всех необходимых директорий
        if(not os.path.exists(self.__BlockChainDir)):
            os.mkdir(self.__BlockChainDir)
        if(not os.path.exists(self.__BlockChainDir + "/" + self.__metaPath)):
            os.mkdir(self.__BlockChainDir + "/" + self.__metaPath)
        if(not os.path.exists(self.__BlockChainDir + "/" + self.__blocksPath)):
            os.mkdir(self.__BlockChainDir + "/" + self.__blocksPath)

        responseBlocks = self.__httpObj.sendData("http://" + self.__verServerIP + ":80/api/users/getBlocks",data, walletPassword)
        successBlocks = responseBlocks["success"]

        data = {}

        responseMeta = self.__httpObj.sendData("http://" + self.__verServerIP + ":80/api/users/getBlockChainInfo",data, walletPassword)
        successMeta = responseMeta["success"]

        if(successMeta and successBlocks):
            blockfiles = list(os.listdir(self.__BlockChainDir + "/" + self.__blocksPath))

            for block in blockfiles:
                os.remove(self.__BlockChainDir + "/" + self.__blocksPath + "/" + block)
            i = 1
            for block in responseBlocks['data']['blocks']:
                with open(self.__BlockChainDir + "/" + self.__blocksPath + "/data_file" + '_' + str(i) + ".block", "w") as write_file:
                    write_file.write(block)
                i += 1

            with open(self.__BlockChainDir + "/" + self.__metaPath + "/lastHash.meta", "w") as write_file:
                write_file.write(responseMeta["data"]["lastHash"])

            with open(self.__BlockChainDir + "/" + self.__metaPath + "/lastFile.meta", "w") as write_file:
                write_file.write(responseMeta["data"]["lastFile"])

        return "Цепочка обновлена"