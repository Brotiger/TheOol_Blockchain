from components.BlockChain import BlockChain
import socket
import subprocess
import pickle
from datetime import datetime
from select import select
import pickle
import threading

class metaServer:
    __class_types = ["A","B","C"]
    __socket_port = None
    __queue = None

    __to_monitor = []

    __client_socket = None
    __addr = None

    def __init__(self, socket_port = 9090, queue = 999, db_ip = "127.0.0.1", db_port = 27018, db_name = "meta-database-test", db_collection_name = "meta-collection-test", time_to_sort = 24):
        if(type(socket_port is int) and type(queue is int) and type(db_ip is str) and type(db_port is int) and type(db_name is str) and type(db_collection_name is str) and type(time_to_sort is int)):
            self.__socket_port = socket_port
            self.__queue = queue
            self.__db_ip = db_ip
            self.__db_port = db_port
            self.__db_name = db_name
            self.__db_collection_name = db_collection_name
            self.__time_to_sort = time_to_sort
            self.__blockChain = BlockChain()
        else:
            raise Exception("metaServer - invalid types passed to the constructor")

    def start(self):
        #Создание блоков по таймеру
        self.set_interval(self.__blockChain.createBlock(), 60)

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

        if data:
            data_obj = pickle.loads(data)
            self.__blockChain.addData(data_obj)

            client_socket.send("success".encode())

            print("Data fron user: " + self.__addr + " received")
        else:
            client_socket.close()

            print("Connection whith user: " + self.__addr + " is broken")

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

    def set_interval(self, func, sec):
        def func_wrapper():
            set_interval(func, sec) 
            func()  
        t = threading.Timer(sec, func_wrapper)
        t.start()
        return t

metaServer = metaServer()
metaServer.start()