# coding: utf8
import components.http as http
import os
import base64
from components.BlockChain import BlockChain
import re

def main():

    choice = ''
    wallet_priv = "./wallet/rsa.priv"
    wallet_pub = "./wallet/rsa.pub"

    blocksPath = "block"
    metaPath = "meta"
    BlockChainDir = "./BlockChain"

    httpObj = http.http()

    while(choice != 'q'):
        print("1 - Регистрация")
        print("2 - Проверить и обновить цепочку")
        print("3 - Запросить цепочку сервера")
        print("q - Выход")

        print('\n')
            
        choice = input("Ваше действие: ")

        print('\n')

        data = {}

        if (not os.environ.get('VER_SERVER_IP')):
            verServerIP = "127.0.0.1"
        else:
            verServerIP = os.environ.get('VER_SERVER_IP')

        try:
            if(choice == "q"):
                continue
            elif(choice == "1"):
                if(os.path.exists(wallet_priv)):
                    print("Вы уже зарегистрированы")
                    print("\n")
                else:
                    walletPassword = input("Wallet password*: ")
                    data["first_name"] = input("First name*: ")
                    data["last_name"] = input("Last name*: ")
                    data["middle_name"] = input("Middle name: ")
                    data["date_of_birth"] = input("Date of birth: ")
                    data["country_and_place_of_birth"] = input("Country and place of birth: ")
                    data["nationality"] = input("Nationality: ")
                    data["country_of_residence"] = input("Country of residence*: ")
                    data["address"] = input("Address*: ")
                    data["zip_code"] = input("Zip Code*: ")
                    data["facebook"] = input("facebook: ")
                    data["email"] = input("Email*: ")    
                    data["phone"] = input("Phone: ")

                    twitter = input("Twitter (t/f): ")
                    if(twitter == 't'):
                        data["twitter"] = True
                    elif(twitter == 'f'):
                        data["twitter"] = False

                    whatsapp = input("whatsapp (t/f): ")
                    if(whatsapp == 't'):
                        data["whatsapp"] = True
                    elif(whatsapp == 'f'):
                        data["whatsapp"] = False

                    telegram = input("telegram (t/f): ")
                    if(telegram == 't'):
                        data["telegram"] = True
                    elif(telegram == 'f'):
                        data["telegram"] = False

                    filePwd = input("Введите путь до pdf файла*: ")

                    base = os.path.basename(filePwd)
                    fileName ,fileExt = os.path.splitext(base)

                    fileExt = fileExt[1:]

                    if os.path.exists(filePwd):
                        if os.path.isfile(filePwd):
                            fileByteString = open(filePwd, 'rb').read()

                            fileString = base64.b64encode(fileByteString).decode('utf-8')

                            infoFile = {
                                "ext": fileExt,
                                "name": fileName,
                                "file": fileString
                            }

                            data["file"] = infoFile

                    print("\n")
                    input("Для отправка введенных данных нажмите Enter")
                    print("\n")

                    response = httpObj.sendData("http://" + verServerIP + ":80/api/users/reg",data, walletPassword)

                    if(response["success"] == False):
                        os.remove(wallet_priv)
                        os.remove(wallet_pub)
                        
                    print(response)
            elif(choice == "2"):

                if(not os.path.exists(wallet_priv)):
                    print("Сначала вам необходимо зарегистрироваться")
                else:
                    data = {}
                    try:
                        if(not os.path.exists(BlockChainDir + "/" + blocksPath)):
                            raise Exception("У вас отсутствует цепочка, запросите ее с сервера через соответствующий пункт меню")
                        if(not os.path.exists(BlockChainDir + "/" + metaPath + "/lastHash.meta")):
                            raise Exception("У вас нету мета файла lastHash, для того что бы его получить пожалуйста обновите цепочку")
                        if(not os.path.exists(BlockChainDir + "/" + metaPath + "/lastFile.meta")):
                            raise Exception("У вас нету мета файла lastFile, для того что бы его получить пожалуйста обновите цепочку")

                        walletPassword = input("Wallet password*: ")
                        responseMeta = httpObj.sendData("http://" + verServerIP + ":80/api/users/getBlockChainInfo",data, walletPassword)
                        successMeta = responseMeta["success"]

                        if(not successMeta):
                            print(responseMeta["errors"])
                            raise Exception("Запрос к серверу выполнен не успешно")
                        
                        with open(BlockChainDir + "/" + metaPath + "/lastFile.meta", mode='r') as text_file:
                            lastFileLocal = int(text_file.read())

                        with open(BlockChainDir + "/" + metaPath + "/lastHash.meta", mode='r') as text_file:
                            lastHashLocal = text_file.read()

                        blockfiles = os.listdir(BlockChainDir + "/" + blocksPath)
                        clearBlockFiles = filter(filterBlocks, blockfiles)
                        listDirCount = len(list(clearBlockFiles))
                        

                        if(int(responseMeta["data"]["lastFile"]) > int(lastFileLocal) or int(responseMeta["data"]["lastFile"]) > listDirCount):
                            data = {
                                "limit": listDirCount
                            }
                            
                            responseBlocks = httpObj.sendData("http://" + verServerIP + ":80/api/users/getBlocks",data, walletPassword)
                            successBlocks = responseBlocks["success"]

                            if(not successBlocks):
                                raise Exception("Новые блоки с сервера не получены")
                            
                            i = listDirCount + 1

                            for block in responseBlocks['data']['blocks']:
                                with open(BlockChainDir + "/" + blocksPath + "/data_file" + '_' + str(i) + ".block", "w") as write_file:
                                    write_file.write(block)
                                i += 1

                            with open(BlockChainDir + "/" + metaPath + "/lastHash.meta", "w") as write_file:
                                write_file.write(responseMeta["data"]["lastHash"])

                            with open(BlockChainDir + "/" + metaPath + "/lastFile.meta", "w") as write_file:
                                write_file.write(responseMeta["data"]["lastFile"])
                        elif(not responseMeta["data"]["lastHash"] == lastHashLocal):
                            raise Exception("Целостность цепочки нарушена")

                        BlockChainObj = BlockChain()
                        verifyResult = BlockChainObj.verify()

                        if(not verifyResult):
                            raise Exception("Целостность цепочки нарушена")
                            
                    except Exception as err:
                        print(err)
                    else:
                        print("Ваша цепочка цела и актуальна")
                    
            elif(choice == "3"):
                data = {
                    "limit": 0
                }
                if(not os.path.exists(wallet_priv)):
                    print("Сначала вам необходимо зарегистрироваться")
                else:

                    #Проверка существования всех необходимых директорий
                    if(not os.path.exists(BlockChainDir)):
                        os.mkdir(BlockChainDir)
                    if(not os.path.exists(BlockChainDir + "/" + metaPath)):
                        os.mkdir(BlockChainDir + "/" + metaPath)
                    if(not os.path.exists(BlockChainDir + "/" + blocksPath)):
                        os.mkdir(BlockChainDir + "/" + blocksPath)

                    walletPassword = input("Wallet password*: ")
                    responseBlocks = httpObj.sendData("http://" + verServerIP + ":80/api/users/getBlocks",data, walletPassword)
                    successBlocks = responseBlocks["success"]

                    data = {}

                    responseMeta = httpObj.sendData("http://" + verServerIP + ":80/api/users/getBlockChainInfo",data, walletPassword)
                    successMeta = responseMeta["success"]

                    if(successMeta and successBlocks):
                        blockfiles = list(os.listdir(BlockChainDir + "/" + blocksPath))

                        for block in blockfiles:
                            os.remove(BlockChainDir + "/" + blocksPath + "/" + block)
                        i = 1
                        for block in responseBlocks['data']['blocks']:
                            with open(BlockChainDir + "/" + blocksPath + "/data_file" + '_' + str(i) + ".block", "w") as write_file:
                                write_file.write(block)
                            i += 1

                        with open(BlockChainDir + "/" + metaPath + "/lastHash.meta", "w") as write_file:
                            write_file.write(responseMeta["data"]["lastHash"])

                        with open(BlockChainDir + "/" + metaPath + "/lastFile.meta", "w") as write_file:
                            write_file.write(responseMeta["data"]["lastFile"])

                    print("Цепочка обновлена")
            else:
                print("Неверный ввод, выбирите что то другое")
                print("\n")
                continue
        except Exception as err:
            print(err)
            print("\n")
            print("Ошибка, попробуйте еще раз")
            print("\n")
            continue

def filterBlocks(file):
    if re.match(r'^data_file_[0-9]*\.block', file) is not None:
        return 1
    else:
        return 0

main()