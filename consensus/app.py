from components.BlockChain import BlockChain
import socket
import subprocess
import pickle
from datetime import datetime
from select import select
import pickle
from threading import Timer
import json
import os
import re

class consensus:
    __socket_port = None
    __queue = None

    __to_monitor = []

    __client_socket = None
    __addr = None
    __metaPath = "./BlockChain/meta"
    __blocksPath = "./BlockChain/block"

    def __init__(self, socket_port = 9090, queue = 999, time = 1):
        if(type(socket_port is int) and type(queue is int) and type(time is int)):
            self.__time = time * 60
            self.__socket_port = socket_port
            self.__queue = queue
            self.__blockChain = BlockChain()
        else:
            raise Exception("metaServer - invalid types passed to the constructor")

    def start(self):
        #Создание блоков по таймеру
        self.set_interval()

        server_socket = socket.socket()
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(("",self.__socket_port))
        server_socket.listen(self.__queue)

        self.__to_monitor = [server_socket]

        print("socket start")

        while True:

            for s_err in self.__to_monitor:
                if s_err.fileno() == -1:
                    self.__to_monitor.remove(s_err)

            ready_to_read, _, _ = select(self.__to_monitor, [], [])

            for sock in ready_to_read:
                if sock is server_socket:
                    self.__accept_connection(sock)
                else:
                    self.__read_message(sock)

    def __read_message(self, client_socket):
        data = client_socket.recv(1024)
        result = {}
        result['success'] = True

        try:
            if not data:
                raise Exception("data read error")

            data_obj = pickle.loads(data)
            mType = data_obj.pop("type")

            if(mType == "createBlock"):
                dataResult = self.__blockChain.addData(data_obj)
                if not dataResult:
                    raise Exception("add info to block error")
            elif(mType == "getMeta"):
                with open(self.__metaPath + "/lastHash.meta", mode='r') as lastHashFile:
                    lastHash = lastHashFile.read()
            
                with open(self.__metaPath + "/lastFile.meta", mode='r') as lastFileFile:
                    lastFile = lastFileFile.read()

                result["lastHash"] = lastHash
                result["lastFile"] = lastFile

            elif(mType == "getBlocks"):
                blocksJson = []
                #путь до директории с блоками блокчейна
                blockfiles = list(os.listdir(self.__blocksPath))
                
                clearBlockFiles = filter(self.__filterBlocks, blockfiles)
                clearBlockFiles = list(clearBlockFiles)
                clearBlockFiles.sort(key=self.__sortBlocksByNumber)

                clearBlockFiles = clearBlockFiles[data_obj['limit']:]

                for block in clearBlockFiles:
                    with open(self.__blocksPath + "/" + block, mode='r') as blockfile:
                        blockInfo = blockfile.read()
                        blocksJson.append(blockInfo)
                result["blocks"] = blocksJson

            else:
                raise Exception("Unknown message type")
        except Exception as err:
            print(err)
            result = err
            print("Connection whith user: " + self.__addr + " is broken")
            
        finally:
            client_socket.send(pickle.dumps(result))
            client_socket.close()
            print("Data fron user: " + self.__addr + " received")

    def __accept_connection(self, server_socket):
        self.__client_socket, addr = server_socket.accept()
        self.__addr = addr[0]

        self.__to_monitor.append(self.__client_socket)

        print("Connection with user: " + self.__addr + " established")

    def setSocketPort(self, port):
        if(type(port is int)):
            self.__socket_port = port
            return True
        return False

    def setQueue(self, queue):
        if(type(queue is int)):
            self.__queue = queue
            return True
        return False

    def setQueue(self, time):
        if(type(time is int)):
            self.__time = time * 60
            return True
        return False

    def set_interval(self):
        try:
            self.__blockChain.createBlock()
            t = Timer(self.__time, self.set_interval)
            t.start()
        except Exception as err:
            print(str(err))

    def __filterBlocks(self, file):
        if re.match(r'^data_file_[0-9]*\.block', file) is not None:
            return 1
        else:
            return 0
    
    def __sortBlocksByNumber(self, inputStr):
        filterStr = int(inputStr[10:-6])
        return filterStr


consensus = consensus()
consensus.start()