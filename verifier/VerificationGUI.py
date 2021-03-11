import os
import base64
import sys
import components.http as http
import json
from PyQt5 import QtCore, QtGui,QtWidgets 
from PyQt5.QtGui import QIcon
import GUI.Verification as Verification
from datetime import datetime
from PyQt5.QtCore import (Qt, QTimer)
import GUI.VerificationSecondWindow3 as VerificationSecondWindow3
from pdf2image import  convert_from_bytes
from PIL import Image 
from PIL.ImageQt import ImageQt
import PIL  
import webbrowser

class Verification_window(QtWidgets.QMainWindow):
    
    Number = "num"
    Li = 10
    Of = 0
    j = 1
    def __init__(self):
        super().__init__()
        self.setParams()
        self.show()
        self.init_UI()

    def init_UI(self):
        self.Verification.pushButton1.clicked.connect(self.button1Clicked)
        self.Verification.pushButton2.clicked.connect(self.button2Clicked)
        self.Verification.pushButton3.clicked.connect(self.button3Clicked)
        self.Verification.pushButton4.clicked.connect(self.button4Clicked)
        self.Verification.pushButton5.clicked.connect(self.button5Clicked)
        self.Verification.pushButton6.clicked.connect(self.button6Clicked)
        self.Verification.pushButton7.clicked.connect(self.button7Clicked)
        self.Verification.pushButton8.clicked.connect(self.button8Clicked)
        self.Verification.pushButton9.clicked.connect(self.button9Clicked)
        self.Verification.pushButton10.clicked.connect(self.button10Clicked)
        self.Verification.right.clicked.connect(self.buttonRightClicked)
        self.Verification.left.clicked.connect(self.buttonLeftClicked)
        self.Verification.maxLeft.clicked.connect(self.buttonMaxLeftClicked)
        self.Verification.slideButton1.clicked.connect(self.buttonSlideButton1)
        self.Verification.slideButton2.clicked.connect(self.buttonSlideButton2)
        self.Verification.slideButton3.clicked.connect(self.buttonSlideButton3)
        self.Verification.slideButton4.clicked.connect(self.buttonSlideButton4)
        self.Verification.slideButton5.clicked.connect(self.buttonSlideButton5)

    def setParams(self):
        print(self.Li)
        user_id_path = "./wallet/user_id.id"
        postType = "/api/verification/getAll"
        httpObj = http.http()

        if (not os.environ.get('VER_SERVER_IP')):
            verServerIP = "127.0.0.1"
        else:
            verServerIP = os.environ.get('VER_SERVER_IP')
        
        data = {}
        
        with open(user_id_path, "r") as text_file:
            data["user_id"] = int(text_file.read())
        
        data["limit"] = self.Li
        data["offset"] = self.Of

        response = httpObj.sendData("http://" + verServerIP + ":80" + postType,data)    
        i = 0
        self.Verification = Verification.Ui_Verification()
        self.Verification.setupUi(self)
        # Установка полей согласно массивву, автоматизировать не удаётся, нарушается лексика языка, стараюсь организовать на массиве из 10 эл-тов
        # Поле номера
        try:
            string = response["data"][i]["id"]
            self.Verification.num1.setText(str(self.Of+1))
            i=i+1
        except IndexError:
            self.Verification.num1.setText("")
        except KeyError:
            self.Verification.num1.setText("")

        try:
            string = response["data"][i]["id"]
            self.Verification.num2.setText(str(self.Of+2))
            i=i+1
        except IndexError:
            self.Verification.num2.setText("")
        except KeyError:
            self.Verification.num2.setText("")

        try:
            string = response["data"][i]["id"]
            self.Verification.num3.setText(str(self.Of+3))
            i=i+1
        except IndexError:
            self.Verification.num3.setText("")
        except KeyError:
            self.Verification.num3.setText("")

        try:
            string = response["data"][i]["id"]
            self.Verification.num4.setText(str(self.Of+4))
            i=i+1
        except IndexError:
            self.Verification.num4.setText("")
        except KeyError:
            self.Verification.num4.setText("")

        try:
            string = response["data"][i]["id"]
            self.Verification.num5.setText(str(self.Of+5))
            i=i+1
        except IndexError:
            self.Verification.num5.setText("")
        except KeyError:
            self.Verification.num5.setText("")

        try:
            string = response["data"][i]["id"]
            self.Verification.num6.setText(str(self.Of+6))
            i=i+1
        except IndexError:
            self.Verification.num6.setText("")
        except KeyError:
            self.Verification.num6.setText("")

        try:
            string = response["data"][i]["id"]
            self.Verification.num7.setText(str(self.Of+7))
            i=i+1
        except IndexError:
            self.Verification.num7.setText("")
        except KeyError:
            self.Verification.num7.setText("")

        try:
            string = response["data"][i]["id"]
            self.Verification.num8.setText(str(self.Of+8))
            i=i+1
        except IndexError:
            self.Verification.num8.setText("")
        except KeyError:
            self.Verification.num8.setText("")

        try:
            string = response["data"][i]["id"]
            self.Verification.num9.setText(str(self.Of+9))
            i=i+1
        except IndexError:
            self.Verification.num9.setText("")
        except KeyError:
            self.Verification.num9.setText("")

        try:
            string = response["data"][i]["id"]
            self.Verification.num10.setText(str(self.Of+10))
            i=i+1
        except IndexError:
            self.Verification.num10.setText("")
        except KeyError:
            self.Verification.num10.setText("")
        # Поле имени
        i = 0

        try:
            self.Verification.name1.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name1.setText("")
        except KeyError:
            self.Verification.name1.setText("")

        try:
            self.Verification.name2.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name2.setText("")
        except KeyError:
            self.Verification.name2.setText("")

        try:
            self.Verification.name3.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name3.setText("")
        except KeyError:
            self.Verification.name3.setText("")

        try:
            self.Verification.name4.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name4.setText("")
        except KeyError:
            self.Verification.name4.setText("")

        try:
            self.Verification.name5.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name5.setText("")
        except KeyError:
            self.Verification.name5.setText("")

        try:
            self.Verification.name6.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name6.setText("")
        except KeyError:
            self.Verification.name6.setText("")

        try:
            self.Verification.name7.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name7.setText("")
        except KeyError:
            self.Verification.name7.setText("")

        try:
            self.Verification.name8.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name8.setText("")
        except KeyError:
            self.Verification.name8.setText("")

        try:
            self.Verification.name9.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name9.setText("")
        except KeyError:
            self.Verification.name9.setText("")

        try:
            self.Verification.name10.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name10.setText("")
        except KeyError:
            self.Verification.name10.setText("")
        
        # Поле фамилии
        i = 0
        try:
            self.Verification.lastName1.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName1.setText("")
        except KeyError:
            self.Verification.lastName1.setText("")

        try:
            self.Verification.lastName2.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName2.setText("")
        except KeyError:
            self.Verification.lastName2.setText("")

        try:
            self.Verification.lastName3.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName3.setText("")
        except KeyError:
            self.Verification.lastName3.setText("")

        try:
            self.Verification.lastName4.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName4.setText("")
        except KeyError:
            self.Verification.lastName4.setText("")

        try:
            self.Verification.lastName5.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName5.setText("")
        except KeyError:
            self.Verification.lastName5.setText("")

        try:
            self.Verification.lastName6.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName6.setText("")
        except KeyError:
            self.Verification.lastName6.setText("")

        try:
            self.Verification.lastName7.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName7.setText("")
        except KeyError:
            self.Verification.lastName7.setText("")

        try:
            self.Verification.lastName8.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName8.setText("")
        except KeyError:
            self.Verification.lastName8.setText("")

        try:
            self.Verification.lastName9.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName9.setText("")
        except KeyError:
            self.Verification.lastName9.setText("")

        try:
            self.Verification.lastName10.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName10.setText("")
        except KeyError:
            self.Verification.lastName10.setText("")

    def buttonMaxLeftClicked(self):
        self.Verification.pushButton1.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton2.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton3.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton4.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton5.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton6.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton7.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton8.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton9.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton10.setStyleSheet("background-color: #E5E7F5")
        self.Of=0
        self.j = 1
        self.Verification.slideButton1.setText(str(self.j))
        self.Verification.slideButton2.setText(str(self.j+1))
        self.Verification.slideButton3.setText(str(self.j+2))
        self.Verification.slideButton4.setText(str(self.j+3))
        self.Verification.slideButton5.setText(str(self.j+4))
        #self.setParams()
        user_id_path = "./wallet/user_id.id"
        postType = "/api/verification/getAll"
        httpObj = http.http()

        if (not os.environ.get('VER_SERVER_IP')):
            verServerIP = "127.0.0.1"
        else:
            verServerIP = os.environ.get('VER_SERVER_IP')
        
        data = {}
        
        with open(user_id_path, "r") as text_file:
            data["user_id"] = int(text_file.read())
        
        data["limit"] = self.Li
        data["offset"] = self.Of

        response = httpObj.sendData("http://" + verServerIP + ":80" + postType,data)    
        print(response)
        i=0
        try:
            string = response["data"][i]["id"]
            self.Verification.num1.setText(str(self.Of+1))
            i=i+1
        except IndexError:
            self.Verification.num1.setText("")
        except KeyError:
            self.Verification.num1.setText("")

        try:
            string = response["data"][i]["id"]
            self.Verification.num2.setText(str(self.Of+2))
            i=i+1
        except IndexError:
            self.Verification.num2.setText("")
        except KeyError:
            self.Verification.num2.setText("")

        try:
            string = response["data"][i]["id"]
            self.Verification.num3.setText(str(self.Of+3))
            i=i+1
        except IndexError:
            self.Verification.num3.setText("")
        except KeyError:
            self.Verification.num3.setText("")

        try:
            string = response["data"][i]["id"]
            self.Verification.num4.setText(str(self.Of+4))
            i=i+1
        except IndexError:
            self.Verification.num4.setText("")
        except KeyError:
            self.Verification.num4.setText("")

        try:
            string = response["data"][i]["id"]
            self.Verification.num5.setText(str(self.Of+5))
            i=i+1
        except IndexError:
            self.Verification.num5.setText("")
        except KeyError:
            self.Verification.num5.setText("")

        try:
            string = response["data"][i]["id"]
            self.Verification.num6.setText(str(self.Of+6))
            i=i+1
        except IndexError:
            self.Verification.num6.setText("")
        except KeyError:
            self.Verification.num6.setText("")

        try:
            string = response["data"][i]["id"]
            self.Verification.num7.setText(str(self.Of+7))
            i=i+1
        except IndexError:
            self.Verification.num7.setText("")
        except KeyError:
            self.Verification.num7.setText("")

        try:
            string = response["data"][i]["id"]
            self.Verification.num8.setText(str(self.Of+8))
            i=i+1
        except IndexError:
            self.Verification.num8.setText("")
        except KeyError:
            self.Verification.num8.setText("")

        try:
            string = response["data"][i]["id"]
            self.Verification.num9.setText(str(self.Of+9))
            i=i+1
        except IndexError:
            self.Verification.num9.setText("")
        except KeyError:
            self.Verification.num9.setText("")

        try:
            string = response["data"][i]["id"]
            self.Verification.num10.setText(str(self.Of+10))
            i=i+1
        except IndexError:
            self.Verification.num10.setText("")
        except KeyError:
            self.Verification.num10.setText("")
        # Поле имени
        i = 0

        try:
            self.Verification.name1.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name1.setText("")
        except KeyError:
            self.Verification.name1.setText("")

        try:
            self.Verification.name2.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name2.setText("")
        except KeyError:
            self.Verification.name2.setText("")

        try:
            self.Verification.name3.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name3.setText("")
        except KeyError:
            self.Verification.name3.setText("")

        try:
            self.Verification.name4.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name4.setText("")
        except KeyError:
            self.Verification.name4.setText("")

        try:
            self.Verification.name5.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name5.setText("")
        except KeyError:
            self.Verification.name5.setText("")

        try:
            self.Verification.name6.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name6.setText("")
        except KeyError:
            self.Verification.name6.setText("")

        try:
            self.Verification.name7.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name7.setText("")
        except KeyError:
            self.Verification.name7.setText("")

        try:
            self.Verification.name8.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name8.setText("")
        except KeyError:
            self.Verification.name8.setText("")

        try:
            self.Verification.name9.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name9.setText("")
        except KeyError:
            self.Verification.name9.setText("")

        try:
            self.Verification.name10.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name10.setText("")
        except KeyError:
            self.Verification.name10.setText("")
        
        # Поле фамилии
        i = 0
        try:
            self.Verification.lastName1.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName1.setText("")
        except KeyError:
            self.Verification.lastName1.setText("")

        try:
            self.Verification.lastName2.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName2.setText("")
        except KeyError:
            self.Verification.lastName2.setText("")

        try:
            self.Verification.lastName3.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName3.setText("")
        except KeyError:
            self.Verification.lastName3.setText("")

        try:
            self.Verification.lastName4.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName4.setText("")
        except KeyError:
            self.Verification.lastName4.setText("")

        try:
            self.Verification.lastName5.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName5.setText("")
        except KeyError:
            self.Verification.lastName5.setText("")

        try:
            self.Verification.lastName6.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName6.setText("")
        except KeyError:
            self.Verification.lastName6.setText("")

        try:
            self.Verification.lastName7.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName7.setText("")
        except KeyError:
            self.Verification.lastName7.setText("")

        try:
            self.Verification.lastName8.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName8.setText("")
        except KeyError:
            self.Verification.lastName8.setText("")

        try:
            self.Verification.lastName9.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName9.setText("")
        except KeyError:
            self.Verification.lastName9.setText("")

        try:
            self.Verification.lastName10.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName10.setText("")
        except KeyError:
            self.Verification.lastName9.setText("")
 
    def buttonRightClicked(self):
        self.Verification.pushButton1.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton2.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton3.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton4.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton5.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton6.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton7.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton8.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton9.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton10.setStyleSheet("background-color: #E5E7F5")
        self.Of=self.Of+10
        self.j = self.j+1
        self.Verification.slideButton1.setText(str(self.j))
        self.Verification.slideButton2.setText(str(self.j+1))
        self.Verification.slideButton3.setText(str(self.j+2))
        self.Verification.slideButton4.setText(str(self.j+3))
        self.Verification.slideButton5.setText(str(self.j+4))
        #self.setParams()
        user_id_path = "./wallet/user_id.id"
        postType = "/api/verification/getAll"
        httpObj = http.http()

        if (not os.environ.get('VER_SERVER_IP')):
            verServerIP = "127.0.0.1"
        else:
            verServerIP = os.environ.get('VER_SERVER_IP')
        
        data = {}
        
        with open(user_id_path, "r") as text_file:
            data["user_id"] = int(text_file.read())
        
        data["limit"] = self.Li
        data["offset"] = self.Of

        response = httpObj.sendData("http://" + verServerIP + ":80" + postType,data)    
        print(response)
        i=0
        try:
            string = response["data"][i]["id"]
            self.Verification.num1.setText(str(self.Of+1))
            i=i+1
        except IndexError:
            self.Verification.num1.setText("")
        except KeyError:
            self.Verification.num1.setText("")

        try:
            string = response["data"][i]["id"]
            self.Verification.num2.setText(str(self.Of+2))
            i=i+1
        except IndexError:
            self.Verification.num2.setText("")
        except KeyError:
            self.Verification.num2.setText("")

        try:
            string = response["data"][i]["id"]
            self.Verification.num3.setText(str(self.Of+3))
            i=i+1
        except IndexError:
            self.Verification.num3.setText("")
        except KeyError:
            self.Verification.num3.setText("")

        try:
            string = response["data"][i]["id"]
            self.Verification.num4.setText(str(self.Of+4))
            i=i+1
        except IndexError:
            self.Verification.num4.setText("")
        except KeyError:
            self.Verification.num4.setText("")

        try:
            string = response["data"][i]["id"]
            self.Verification.num5.setText(str(self.Of+5))
            i=i+1
        except IndexError:
            self.Verification.num5.setText("")
        except KeyError:
            self.Verification.num5.setText("")

        try:
            string = response["data"][i]["id"]
            self.Verification.num6.setText(str(self.Of+6))
            i=i+1
        except IndexError:
            self.Verification.num6.setText("")
        except KeyError:
            self.Verification.num6.setText("")

        try:
            string = response["data"][i]["id"]
            self.Verification.num7.setText(str(self.Of+7))
            i=i+1
        except IndexError:
            self.Verification.num7.setText("")
        except KeyError:
            self.Verification.num7.setText("")

        try:
            string = response["data"][i]["id"]
            self.Verification.num8.setText(str(self.Of+8))
            i=i+1
        except IndexError:
            self.Verification.num8.setText("")
        except KeyError:
            self.Verification.num8.setText("")

        try:
            string = response["data"][i]["id"]
            self.Verification.num9.setText(str(self.Of+9))
            i=i+1
        except IndexError:
            self.Verification.num9.setText("")
        except KeyError:
            self.Verification.num9.setText("")

        try:
            string = response["data"][i]["id"]
            self.Verification.num10.setText(str(self.Of+10))
            i=i+1
        except IndexError:
            self.Verification.num10.setText("")
        except KeyError:
            self.Verification.num10.setText("")
        # Поле имени
        i = 0

        try:
            self.Verification.name1.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name1.setText("")
        except KeyError:
            self.Verification.name1.setText("")

        try:
            self.Verification.name2.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name2.setText("")
        except KeyError:
            self.Verification.name2.setText("")

        try:
            self.Verification.name3.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name3.setText("")
        except KeyError:
            self.Verification.name3.setText("")

        try:
            self.Verification.name4.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name4.setText("")
        except KeyError:
            self.Verification.name4.setText("")

        try:
            self.Verification.name5.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name5.setText("")
        except KeyError:
            self.Verification.name5.setText("")

        try:
            self.Verification.name6.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name6.setText("")
        except KeyError:
            self.Verification.name6.setText("")

        try:
            self.Verification.name7.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name7.setText("")
        except KeyError:
            self.Verification.name7.setText("")

        try:
            self.Verification.name8.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name8.setText("")
        except KeyError:
            self.Verification.name8.setText("")

        try:
            self.Verification.name9.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name9.setText("")
        except KeyError:
            self.Verification.name9.setText("")

        try:
            self.Verification.name10.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name10.setText("")
        except KeyError:
            self.Verification.name10.setText("")
        
        # Поле фамилии
        i = 0
        try:
            self.Verification.lastName1.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName1.setText("")
        except KeyError:
            self.Verification.lastName1.setText("")

        try:
            self.Verification.lastName2.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName2.setText("")
        except KeyError:
            self.Verification.lastName2.setText("")

        try:
            self.Verification.lastName3.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName3.setText("")
        except KeyError:
            self.Verification.lastName3.setText("")

        try:
            self.Verification.lastName4.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName4.setText("")
        except KeyError:
            self.Verification.lastName4.setText("")

        try:
            self.Verification.lastName5.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName5.setText("")
        except KeyError:
            self.Verification.lastName5.setText("")

        try:
            self.Verification.lastName6.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName6.setText("")
        except KeyError:
            self.Verification.lastName6.setText("")

        try:
            self.Verification.lastName7.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName7.setText("")
        except KeyError:
            self.Verification.lastName7.setText("")

        try:
            self.Verification.lastName8.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName8.setText("")
        except KeyError:
            self.Verification.lastName8.setText("")

        try:
            self.Verification.lastName9.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName9.setText("")
        except KeyError:
            self.Verification.lastName9.setText("")

        try:
            self.Verification.lastName10.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName10.setText("")
        except KeyError:
            self.Verification.lastName9.setText("")

    def buttonLeftClicked(self):
        if (self.Of>=10):
            self.Verification.pushButton1.setStyleSheet("background-color: #E5E7F5")
            self.Verification.pushButton2.setStyleSheet("background-color: #E5E7F5")
            self.Verification.pushButton3.setStyleSheet("background-color: #E5E7F5")
            self.Verification.pushButton4.setStyleSheet("background-color: #E5E7F5")
            self.Verification.pushButton5.setStyleSheet("background-color: #E5E7F5")
            self.Verification.pushButton6.setStyleSheet("background-color: #E5E7F5")
            self.Verification.pushButton7.setStyleSheet("background-color: #E5E7F5")
            self.Verification.pushButton8.setStyleSheet("background-color: #E5E7F5")
            self.Verification.pushButton9.setStyleSheet("background-color: #E5E7F5")
            self.Verification.pushButton10.setStyleSheet("background-color: #E5E7F5")
            self.Of=self.Of-10
            self.j = self.j-1
            self.Verification.slideButton1.setText(str(self.j))
            self.Verification.slideButton2.setText(str(self.j+1))
            self.Verification.slideButton3.setText(str(self.j+2))
            self.Verification.slideButton4.setText(str(self.j+3))
            self.Verification.slideButton5.setText(str(self.j+4))
            #self.setParams()
            user_id_path = "./wallet/user_id.id"
            postType = "/api/verification/getAll"
            httpObj = http.http()

            if (not os.environ.get('VER_SERVER_IP')):
                verServerIP = "127.0.0.1"
            else:
                verServerIP = os.environ.get('VER_SERVER_IP')
            
            data = {}
            
            with open(user_id_path, "r") as text_file:
                data["user_id"] = int(text_file.read())
            
            data["limit"] = self.Li
            data["offset"] = self.Of

            response = httpObj.sendData("http://" + verServerIP + ":80" + postType,data)    
            print(response)
            i=0
            try:
                string = response["data"][i]["id"]
                self.Verification.num1.setText(str(self.Of+1))
                i=i+1
            except IndexError:
                self.Verification.num1.setText("")
            except KeyError:
                self.Verification.num1.setText("")

            try:
                string = response["data"][i]["id"]
                self.Verification.num2.setText(str(self.Of+2))
                i=i+1
            except IndexError:
                self.Verification.num2.setText("")
            except KeyError:
                self.Verification.num2.setText("")

            try:
                string = response["data"][i]["id"]
                self.Verification.num3.setText(str(self.Of+3))
                i=i+1
            except IndexError:
                self.Verification.num3.setText("")
            except KeyError:
                self.Verification.num3.setText("")

            try:
                string = response["data"][i]["id"]
                self.Verification.num4.setText(str(self.Of+4))
                i=i+1
            except IndexError:
                self.Verification.num4.setText("")
            except KeyError:
                self.Verification.num4.setText("")

            try:
                string = response["data"][i]["id"]
                self.Verification.num5.setText(str(self.Of+5))
                i=i+1
            except IndexError:
                self.Verification.num5.setText("")
            except KeyError:
                self.Verification.num5.setText("")

            try:
                string = response["data"][i]["id"]
                self.Verification.num6.setText(str(self.Of+6))
                i=i+1
            except IndexError:
                self.Verification.num6.setText("")
            except KeyError:
                self.Verification.num6.setText("")

            try:
                string = response["data"][i]["id"]
                self.Verification.num7.setText(str(self.Of+7))
                i=i+1
            except IndexError:
                self.Verification.num7.setText("")
            except KeyError:
                self.Verification.num7.setText("")

            try:
                string = response["data"][i]["id"]
                self.Verification.num8.setText(str(self.Of+8))
                i=i+1
            except IndexError:
                self.Verification.num8.setText("")
            except KeyError:
                self.Verification.num8.setText("")

            try:
                string = response["data"][i]["id"]
                self.Verification.num9.setText(str(self.Of+9))
                i=i+1
            except IndexError:
                self.Verification.num9.setText("")
            except KeyError:
                self.Verification.num9.setText("")

            try:
                string = response["data"][i]["id"]
                self.Verification.num10.setText(str(self.Of+10))
                i=i+1
            except IndexError:
                self.Verification.num10.setText("")
            except KeyError:
                self.Verification.num10.setText("")
                # Поле имени
                i = 0

            try:
                self.Verification.name1.setText(response["data"][i]["first_name"])
                i=i+1
            except IndexError:
                self.Verification.name1.setText("")
            except KeyError:
                self.Verification.name1.setText("")

            try:
                self.Verification.name2.setText(response["data"][i]["first_name"])
                i=i+1
            except IndexError:
                self.Verification.name2.setText("")
            except KeyError:
                self.Verification.name2.setText("")

            try:
                self.Verification.name3.setText(response["data"][i]["first_name"])
                i=i+1
            except IndexError:
                self.Verification.name3.setText("")
            except KeyError:
                self.Verification.name3.setText("")

            try:
                self.Verification.name4.setText(response["data"][i]["first_name"])
                i=i+1
            except IndexError:
                self.Verification.name4.setText("")
            except KeyError:
                self.Verification.name4.setText("")

            try:
                self.Verification.name5.setText(response["data"][i]["first_name"])
                i=i+1
            except IndexError:
                self.Verification.name5.setText("")
            except KeyError:
                self.Verification.name5.setText("")

            try:
                self.Verification.name6.setText(response["data"][i]["first_name"])
                i=i+1
            except IndexError:
                self.Verification.name6.setText("")
            except KeyError:
                self.Verification.name6.setText("")

            try:
                self.Verification.name7.setText(response["data"][i]["first_name"])
                i=i+1
            except IndexError:
                self.Verification.name7.setText("")
            except KeyError:
                self.Verification.name7.setText("")

            try:
                self.Verification.name8.setText(response["data"][i]["first_name"])
                i=i+1
            except IndexError:
                self.Verification.name8.setText("")
            except KeyError:
                self.Verification.name8.setText("")

            try:
                self.Verification.name9.setText(response["data"][i]["first_name"])
                i=i+1
            except IndexError:
                self.Verification.name9.setText("")
            except KeyError:
                self.Verification.name9.setText("")

            try:
                self.Verification.name10.setText(response["data"][i]["first_name"])
                i=i+1
            except IndexError:
                self.Verification.name10.setText("")
            except KeyError:
                self.Verification.name10.setText("")
            
            # Поле фамилии
            i = 0
            try:
                self.Verification.lastName1.setText(response["data"][i]["last_name"])
                i=i+1
            except IndexError:
                self.Verification.lastName1.setText("")
            except KeyError:
                self.Verification.lastName1.setText("")

            try:
                self.Verification.lastName2.setText(response["data"][i]["last_name"])
                i=i+1
            except IndexError:
                self.Verification.lastName2.setText("")
            except KeyError:
                self.Verification.lastName2.setText("")

            try:
                self.Verification.lastName3.setText(response["data"][i]["last_name"])
                i=i+1
            except IndexError:
                self.Verification.lastName3.setText("")
            except KeyError:
                self.Verification.lastName3.setText("")

            try:
                self.Verification.lastName4.setText(response["data"][i]["last_name"])
                i=i+1
            except IndexError:
                self.Verification.lastName4.setText("")
            except KeyError:
                self.Verification.lastName4.setText("")

            try:
                self.Verification.lastName5.setText(response["data"][i]["last_name"])
                i=i+1
            except IndexError:
                self.Verification.lastName5.setText("")
            except KeyError:
                self.Verification.lastName5.setText("")

            try:
                self.Verification.lastName6.setText(response["data"][i]["last_name"])
                i=i+1
            except IndexError:
                self.Verification.lastName6.setText("")
            except KeyError:
                self.Verification.lastName6.setText("")

            try:
                self.Verification.lastName7.setText(response["data"][i]["last_name"])
                i=i+1
            except IndexError:
                self.Verification.lastName7.setText("")
            except KeyError:
                self.Verification.lastName7.setText("")

            try:
                self.Verification.lastName8.setText(response["data"][i]["last_name"])
                i=i+1
            except IndexError:
                self.Verification.lastName8.setText("")
            except KeyError:
                self.Verification.lastName8.setText("")

            try:
                self.Verification.lastName9.setText(response["data"][i]["last_name"])
                i=i+1
            except IndexError:
                self.Verification.lastName9.setText("")
            except KeyError:
                self.Verification.lastName9.setText("")

            try:
                self.Verification.lastName10.setText(response["data"][i]["last_name"])
                i=i+1
            except IndexError:
                self.Verification.lastName10.setText("")
            except KeyError:
                self.Verification.lastName9.setText("")

    def button1Clicked(self):
        try:

            self.Verification.pushButton1.setStyleSheet("background-color: #E5E7F5")

            user_id_path = "./wallet/user_id.id"
            
            postType = "/api/verification/getOne"

            if (not os.environ.get('VER_SERVER_IP')):
                verServerIP = "127.0.0.1"
            else:
                verServerIP = os.environ.get('VER_SERVER_IP')

            httpObj = http.http()

            data = {}

            data["id"] = self.Of+1

            with open(user_id_path, "r") as text_file:
                data["user_id"] = int(text_file.read())


            response = httpObj.sendData("http://" + verServerIP + ":80" + postType,data)    
            
            Personal_Card(response["data"]["first_name"],response["data"]["last_name"],response["data"]["middle_name"],response["data"]["address"],response["data"]["country_of_residence"],response["data"]["country_and_place_of_birth"],response["data"]["nationality"],response["data"]["date_of_birth"],response["data"]["email"],response["data"]["phone"],response["data"]["zip_code"],response["data"]["file"],self.Of+1)
        except KeyError:
            self.fade(self.Verification.pushButton1)  

    def button2Clicked(self):
        try:

            self.Verification.pushButton2.setStyleSheet("background-color: #2e3436")

            user_id_path = "./wallet/user_id.id"
            
            postType = "/api/verification/getOne"

            if (not os.environ.get('VER_SERVER_IP')):
                verServerIP = "127.0.0.1"
            else:
                verServerIP = os.environ.get('VER_SERVER_IP')

            httpObj = http.http()

            data = {}
            data["id"] = self.Of+2

            with open(user_id_path, "r") as text_file:
                data["user_id"] = int(text_file.read())

            response = httpObj.sendData("http://" + verServerIP + ":80" + postType,data)    
        
            Personal_Card(response["data"]["first_name"],response["data"]["last_name"],response["data"]["middle_name"],response["data"]["address"],response["data"]["country_of_residence"],response["data"]["country_and_place_of_birth"],response["data"]["nationality"],response["data"]["date_of_birth"],response["data"]["email"],response["data"]["phone"],response["data"]["zip_code"],response["data"]["file"],self.Of+2)   
        except KeyError:
            self.fade(self.Verification.pushButton2)      

    def button3Clicked(self):
        try:

            self.Verification.pushButton3.setStyleSheet("background-color: #2e3436")

            user_id_path = "./wallet/user_id.id"
            
            postType = "/api/verification/getOne"

            if (not os.environ.get('VER_SERVER_IP')):
                verServerIP = "127.0.0.1"
            else:
                verServerIP = os.environ.get('VER_SERVER_IP')

            httpObj = http.http()

            data = {}
            data["id"] = self.Of+3

            with open(user_id_path, "r") as text_file:
                data["user_id"] = int(text_file.read())

            response = httpObj.sendData("http://" + verServerIP + ":80" + postType,data)    
        
            Personal_Card(response["data"]["first_name"],response["data"]["last_name"],response["data"]["middle_name"],response["data"]["address"],response["data"]["country_of_residence"],response["data"]["country_and_place_of_birth"],response["data"]["nationality"],response["data"]["date_of_birth"],response["data"]["email"],response["data"]["phone"],response["data"]["zip_code"],response["data"]["file"],self.Of+3)   
        except KeyError:
            self.fade(self.Verification.pushButton3)      

    def button4Clicked(self):
        try:

            self.Verification.pushButton4.setStyleSheet("background-color: #2e3436")

            user_id_path = "./wallet/user_id.id"
            
            postType = "/api/verification/getOne"

            if (not os.environ.get('VER_SERVER_IP')):
                verServerIP = "127.0.0.1"
            else:
                verServerIP = os.environ.get('VER_SERVER_IP')

            httpObj = http.http()

            data = {}
            data["id"] = self.Of+4

            with open(user_id_path, "r") as text_file:
                data["user_id"] = int(text_file.read())

            response = httpObj.sendData("http://" + verServerIP + ":80" + postType,data)    
        
            Personal_Card(response["data"]["first_name"],response["data"]["last_name"],response["data"]["middle_name"],response["data"]["address"],response["data"]["country_of_residence"],response["data"]["country_and_place_of_birth"],response["data"]["nationality"],response["data"]["date_of_birth"],response["data"]["email"],response["data"]["phone"],response["data"]["zip_code"],response["data"]["file"],self.Of+4)   
        except KeyError:
            self.fade(self.Verification.pushButton4)

    def button5Clicked(self):
        try:

            self.Verification.pushButton5.setStyleSheet("background-color: #2e3436")

            user_id_path = "./wallet/user_id.id"
            
            postType = "/api/verification/getOne"

            if (not os.environ.get('VER_SERVER_IP')):
                verServerIP = "127.0.0.1"
            else:
                verServerIP = os.environ.get('VER_SERVER_IP')

            httpObj = http.http()

            data = {}
            data["id"] = self.Of+5

            with open(user_id_path, "r") as text_file:
                data["user_id"] = int(text_file.read())

            response = httpObj.sendData("http://" + verServerIP + ":80" + postType,data)    
        
            Personal_Card(response["data"]["first_name"],response["data"]["last_name"],response["data"]["middle_name"],response["data"]["address"],response["data"]["country_of_residence"],response["data"]["country_and_place_of_birth"],response["data"]["nationality"],response["data"]["date_of_birth"],response["data"]["email"],response["data"]["phone"],response["data"]["zip_code"],response["data"]["file"],self.Of+5)   
        except KeyError:
            self.fade(self.Verification.pushButton5)

    def button6Clicked(self):
        try:

            self.Verification.pushButton6.setStyleSheet("background-color: #2e3436")
            
            user_id_path = "./wallet/user_id.id"
            
            postType = "/api/verification/getOne"

            if (not os.environ.get('VER_SERVER_IP')):
                verServerIP = "127.0.0.1"
            else:
                verServerIP = os.environ.get('VER_SERVER_IP')

            httpObj = http.http()

            data = {}
            data["id"] = self.Of+6

            with open(user_id_path, "r") as text_file:
                data["user_id"] = int(text_file.read())

            response = httpObj.sendData("http://" + verServerIP + ":80" + postType,data)    
        
            Personal_Card(response["data"]["first_name"],response["data"]["last_name"],response["data"]["middle_name"],response["data"]["address"],response["data"]["country_of_residence"],response["data"]["country_and_place_of_birth"],response["data"]["nationality"],response["data"]["date_of_birth"],response["data"]["email"],response["data"]["phone"],response["data"]["zip_code"],response["data"]["file"],self.Of+6)   
        except KeyError:
            self.fade(self.Verification.pushButton6)

    def button7Clicked(self):
        try:

            self.Verification.pushButton7.setStyleSheet("background-color: #2e3436")

            user_id_path = "./wallet/user_id.id"
            
            postType = "/api/verification/getOne"

            if (not os.environ.get('VER_SERVER_IP')):
                verServerIP = "127.0.0.1"
            else:
                verServerIP = os.environ.get('VER_SERVER_IP')

            httpObj = http.http()

            data = {}
            data["id"] = self.Of+7

            with open(user_id_path, "r") as text_file:
                data["user_id"] = int(text_file.read())

            response = httpObj.sendData("http://" + verServerIP + ":80" + postType,data)    
        
            Personal_Card(response["data"]["first_name"],response["data"]["last_name"],response["data"]["middle_name"],response["data"]["address"],response["data"]["country_of_residence"],response["data"]["country_and_place_of_birth"],response["data"]["nationality"],response["data"]["date_of_birth"],response["data"]["email"],response["data"]["phone"],response["data"]["zip_code"],response["data"]["file"],self.Of+7)   
        except KeyError:
            self.fade(self.Verification.pushButton7)

    def button8Clicked(self):
        try:

            self.Verification.pushButton8.setStyleSheet("background-color: #2e3436")

            user_id_path = "./wallet/user_id.id"
            
            postType = "/api/verification/getOne"

            if (not os.environ.get('VER_SERVER_IP')):
                verServerIP = "127.0.0.1"
            else:
                verServerIP = os.environ.get('VER_SERVER_IP')

            httpObj = http.http()

            data = {}
            data["id"] = self.Of+8

            with open(user_id_path, "r") as text_file:
                data["user_id"] = int(text_file.read())

            response = httpObj.sendData("http://" + verServerIP + ":80" + postType,data)    
        
            Personal_Card(response["data"]["first_name"],response["data"]["last_name"],response["data"]["middle_name"],response["data"]["address"],response["data"]["country_of_residence"],response["data"]["country_and_place_of_birth"],response["data"]["nationality"],response["data"]["date_of_birth"],response["data"]["email"],response["data"]["phone"],response["data"]["zip_code"],response["data"]["file"],self.Of+8)   
        except KeyError:
            self.fade(self.Verification.pushButton8)          

    def button9Clicked(self):
        try:
            self.Verification.pushButton9.setStyleSheet("background-color: #2e3436")

            user_id_path = "./wallet/user_id.id"
            
            postType = "/api/verification/getOne"

            if (not os.environ.get('VER_SERVER_IP')):
                verServerIP = "127.0.0.1"
            else:
                verServerIP = os.environ.get('VER_SERVER_IP')

            httpObj = http.http()

            data = {}
            data["id"] = self.Of+9

            with open(user_id_path, "r") as text_file:
                data["user_id"] = int(text_file.read())

            response = httpObj.sendData("http://" + verServerIP + ":80" + postType,data)    
        
            Personal_Card(response["data"]["first_name"],response["data"]["last_name"],response["data"]["middle_name"],response["data"]["address"],response["data"]["country_of_residence"],response["data"]["country_and_place_of_birth"],response["data"]["nationality"],response["data"]["date_of_birth"],response["data"]["email"],response["data"]["phone"],response["data"]["zip_code"],response["data"]["file"],self.Of+9)   
        except KeyError:
            self.fade(self.Verification.pushButton9)

    def button10Clicked(self):
        try:

            self.Verification.pushButton10.setStyleSheet("background-color: #2e3436")

            user_id_path = "./wallet/user_id.id"
            
            postType = "/api/verification/getOne"

            if (not os.environ.get('VER_SERVER_IP')):
                verServerIP = "127.0.0.1"
            else:
                verServerIP = os.environ.get('VER_SERVER_IP')

            httpObj = http.http()

            data = {}
            data["id"] = self.Of+10

            with open(user_id_path, "r") as text_file:
                data["user_id"] = int(text_file.read())

            response = httpObj.sendData("http://" + verServerIP + ":80" + postType,data)    
        
            Personal_Card(response["data"]["first_name"],response["data"]["last_name"],response["data"]["middle_name"],response["data"]["address"],response["data"]["country_of_residence"],response["data"]["country_and_place_of_birth"],response["data"]["nationality"],response["data"]["date_of_birth"],response["data"]["email"],response["data"]["phone"],response["data"]["zip_code"],response["data"]["file"],self.Of+10)   
        except KeyError:
            self.fade(self.Verification.pushButton10)

    def buttonSlideButton1(self):
        self.Verification.pushButton1.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton2.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton3.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton4.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton5.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton6.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton7.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton8.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton9.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton10.setStyleSheet("background-color: #E5E7F5")
        self.Of=self.j*10-10
        user_id_path = "./wallet/user_id.id"
        postType = "/api/verification/getAll"
        httpObj = http.http()

        if (not os.environ.get('VER_SERVER_IP')):
            verServerIP = "127.0.0.1"
        else:
            verServerIP = os.environ.get('VER_SERVER_IP')
        
        data = {}
        
        with open(user_id_path, "r") as text_file:
            data["user_id"] = int(text_file.read())
        
        data["limit"] = self.Li
        data["offset"] = self.Of

        response = httpObj.sendData("http://" + verServerIP + ":80" + postType,data)    
        print(response)
        i=0
        try:
            self.Verification.num1.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num1.setText("")
        except KeyError:
            self.Verification.num1.setText("")

        try:
            self.Verification.num2.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num2.setText("")
        except KeyError:
            self.Verification.num2.setText("")

        try:
            self.Verification.num3.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num3.setText("")
        except KeyError:
            self.Verification.num3.setText("")

        try:
            self.Verification.num4.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num4.setText("")
        except KeyError:
            self.Verification.num4.setText("")

        try:
            self.Verification.num5.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num5.setText("")
        except KeyError:
            self.Verification.num5.setText("")

        try:
            self.Verification.num6.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num6.setText("")
        except KeyError:
            self.Verification.num6.setText("")

        try:
            self.Verification.num7.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num7.setText("")
        except KeyError:
            self.Verification.num7.setText("")

        try:
            self.Verification.num8.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num8.setText("")
        except KeyError:
            self.Verification.num8.setText("")

        try:
            self.Verification.num9.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num9.setText("")
        except KeyError:
            self.Verification.num9.setText("")

        try:
            self.Verification.num10.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num10.setText("")
        except KeyError:
            self.Verification.num10.setText("")
        # Поле имени
        i = 0

        try:
            self.Verification.name1.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name1.setText("")
        except KeyError:
            self.Verification.name1.setText("")

        try:
            self.Verification.name2.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name2.setText("")
        except KeyError:
            self.Verification.name2.setText("")

        try:
            self.Verification.name3.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name3.setText("")
        except KeyError:
            self.Verification.name3.setText("")

        try:
            self.Verification.name4.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name4.setText("")
        except KeyError:
            self.Verification.name4.setText("")

        try:
            self.Verification.name5.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name5.setText("")
        except KeyError:
            self.Verification.name5.setText("")

        try:
            self.Verification.name6.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name6.setText("")
        except KeyError:
            self.Verification.name6.setText("")

        try:
            self.Verification.name7.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name7.setText("")
        except KeyError:
            self.Verification.name7.setText("")

        try:
            self.Verification.name8.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name8.setText("")
        except KeyError:
            self.Verification.name8.setText("")

        try:
            self.Verification.name9.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name9.setText("")
        except KeyError:
            self.Verification.name9.setText("")

        try:
            self.Verification.name10.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name10.setText("")
        except KeyError:
            self.Verification.name10.setText("")
        
        # Поле фамилии
        i = 0
        try:
            self.Verification.lastName1.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName1.setText("")
        except KeyError:
            self.Verification.lastName1.setText("")

        try:
            self.Verification.lastName2.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName2.setText("")
        except KeyError:
            self.Verification.lastName2.setText("")

        try:
            self.Verification.lastName3.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName3.setText("")
        except KeyError:
            self.Verification.lastName3.setText("")

        try:
            self.Verification.lastName4.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName4.setText("")
        except KeyError:
            self.Verification.lastName4.setText("")

        try:
            self.Verification.lastName5.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName5.setText("")
        except KeyError:
            self.Verification.lastName5.setText("")

        try:
            self.Verification.lastName6.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName6.setText("")
        except KeyError:
            self.Verification.lastName6.setText("")

        try:
            self.Verification.lastName7.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName7.setText("")
        except KeyError:
            self.Verification.lastName7.setText("")

        try:
            self.Verification.lastName8.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName8.setText("")
        except KeyError:
            self.Verification.lastName8.setText("")

        try:
            self.Verification.lastName9.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName9.setText("")
        except KeyError:
            self.Verification.lastName9.setText("")

        try:
            self.Verification.lastName10.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName10.setText("")
        except KeyError:
            self.Verification.lastName9.setText("")
    
        #self.setPara

    def buttonSlideButton2(self):
        self.Verification.pushButton1.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton2.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton3.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton4.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton5.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton6.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton7.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton8.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton9.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton10.setStyleSheet("background-color: #E5E7F5")
        self.Of=(self.j+1)*10-10
        user_id_path = "./wallet/user_id.id"
        postType = "/api/verification/getAll"
        httpObj = http.http()

        if (not os.environ.get('VER_SERVER_IP')):
            verServerIP = "127.0.0.1"
        else:
            verServerIP = os.environ.get('VER_SERVER_IP')
        
        data = {}
        
        with open(user_id_path, "r") as text_file:
            data["user_id"] = int(text_file.read())
        
        data["limit"] = self.Li
        data["offset"] = self.Of

        response = httpObj.sendData("http://" + verServerIP + ":80" + postType,data)    
        print(response)
        i=0
        try:
            self.Verification.num1.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num1.setText("")
        except KeyError:
            self.Verification.num1.setText("")

        try:
            self.Verification.num2.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num2.setText("")
        except KeyError:
            self.Verification.num2.setText("")

        try:
            self.Verification.num3.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num3.setText("")
        except KeyError:
            self.Verification.num3.setText("")

        try:
            self.Verification.num4.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num4.setText("")
        except KeyError:
            self.Verification.num4.setText("")

        try:
            self.Verification.num5.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num5.setText("")
        except KeyError:
            self.Verification.num5.setText("")

        try:
            self.Verification.num6.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num6.setText("")
        except KeyError:
            self.Verification.num6.setText("")

        try:
            self.Verification.num7.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num7.setText("")
        except KeyError:
            self.Verification.num7.setText("")

        try:
            self.Verification.num8.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num8.setText("")
        except KeyError:
            self.Verification.num8.setText("")

        try:
            self.Verification.num9.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num9.setText("")
        except KeyError:
            self.Verification.num9.setText("")

        try:
            self.Verification.num10.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num10.setText("")
        except KeyError:
            self.Verification.num10.setText("")
        # Поле имени
        i = 0

        try:
            self.Verification.name1.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name1.setText("")
        except KeyError:
            self.Verification.name1.setText("")

        try:
            self.Verification.name2.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name2.setText("")
        except KeyError:
            self.Verification.name2.setText("")

        try:
            self.Verification.name3.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name3.setText("")
        except KeyError:
            self.Verification.name3.setText("")

        try:
            self.Verification.name4.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name4.setText("")
        except KeyError:
            self.Verification.name4.setText("")

        try:
            self.Verification.name5.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name5.setText("")
        except KeyError:
            self.Verification.name5.setText("")

        try:
            self.Verification.name6.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name6.setText("")
        except KeyError:
            self.Verification.name6.setText("")

        try:
            self.Verification.name7.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name7.setText("")
        except KeyError:
            self.Verification.name7.setText("")

        try:
            self.Verification.name8.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name8.setText("")
        except KeyError:
            self.Verification.name8.setText("")

        try:
            self.Verification.name9.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name9.setText("")
        except KeyError:
            self.Verification.name9.setText("")

        try:
            self.Verification.name10.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name10.setText("")
        except KeyError:
            self.Verification.name10.setText("")
        
        # Поле фамилии
        i = 0
        try:
            self.Verification.lastName1.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName1.setText("")
        except KeyError:
            self.Verification.lastName1.setText("")

        try:
            self.Verification.lastName2.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName2.setText("")
        except KeyError:
            self.Verification.lastName2.setText("")

        try:
            self.Verification.lastName3.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName3.setText("")
        except KeyError:
            self.Verification.lastName3.setText("")

        try:
            self.Verification.lastName4.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName4.setText("")
        except KeyError:
            self.Verification.lastName4.setText("")

        try:
            self.Verification.lastName5.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName5.setText("")
        except KeyError:
            self.Verification.lastName5.setText("")

        try:
            self.Verification.lastName6.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName6.setText("")
        except KeyError:
            self.Verification.lastName6.setText("")

        try:
            self.Verification.lastName7.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName7.setText("")
        except KeyError:
            self.Verification.lastName7.setText("")

        try:
            self.Verification.lastName8.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName8.setText("")
        except KeyError:
            self.Verification.lastName8.setText("")

        try:
            self.Verification.lastName9.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName9.setText("")
        except KeyError:
            self.Verification.lastName9.setText("")

        try:
            self.Verification.lastName10.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName10.setText("")
        except KeyError:
            self.Verification.lastName9.setText("")
    
    def buttonSlideButton3(self):
        self.Verification.pushButton1.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton2.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton3.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton4.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton5.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton6.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton7.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton8.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton9.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton10.setStyleSheet("background-color: #E5E7F5")
        self.Of=(self.j+2)*10-10
        user_id_path = "./wallet/user_id.id"
        postType = "/api/verification/getAll"
        httpObj = http.http()

        if (not os.environ.get('VER_SERVER_IP')):
            verServerIP = "127.0.0.1"
        else:
            verServerIP = os.environ.get('VER_SERVER_IP')
        
        data = {}
        
        with open(user_id_path, "r") as text_file:
            data["user_id"] = int(text_file.read())
        
        data["limit"] = self.Li
        data["offset"] = self.Of

        response = httpObj.sendData("http://" + verServerIP + ":80" + postType,data)    
        print(response)
        i=0
        try:
            self.Verification.num1.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num1.setText("")
        except KeyError:
            self.Verification.num1.setText("")

        try:
            self.Verification.num2.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num2.setText("")
        except KeyError:
            self.Verification.num2.setText("")

        try:
            self.Verification.num3.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num3.setText("")
        except KeyError:
            self.Verification.num3.setText("")

        try:
            self.Verification.num4.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num4.setText("")
        except KeyError:
            self.Verification.num4.setText("")

        try:
            self.Verification.num5.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num5.setText("")
        except KeyError:
            self.Verification.num5.setText("")

        try:
            self.Verification.num6.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num6.setText("")
        except KeyError:
            self.Verification.num6.setText("")

        try:
            self.Verification.num7.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num7.setText("")
        except KeyError:
            self.Verification.num7.setText("")

        try:
            self.Verification.num8.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num8.setText("")
        except KeyError:
            self.Verification.num8.setText("")

        try:
            self.Verification.num9.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num9.setText("")
        except KeyError:
            self.Verification.num9.setText("")

        try:
            self.Verification.num10.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num10.setText("")
        except KeyError:
            self.Verification.num10.setText("")
        # Поле имени
        i = 0

        try:
            self.Verification.name1.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name1.setText("")
        except KeyError:
            self.Verification.name1.setText("")

        try:
            self.Verification.name2.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name2.setText("")
        except KeyError:
            self.Verification.name2.setText("")

        try:
            self.Verification.name3.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name3.setText("")
        except KeyError:
            self.Verification.name3.setText("")

        try:
            self.Verification.name4.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name4.setText("")
        except KeyError:
            self.Verification.name4.setText("")

        try:
            self.Verification.name5.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name5.setText("")
        except KeyError:
            self.Verification.name5.setText("")

        try:
            self.Verification.name6.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name6.setText("")
        except KeyError:
            self.Verification.name6.setText("")

        try:
            self.Verification.name7.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name7.setText("")
        except KeyError:
            self.Verification.name7.setText("")

        try:
            self.Verification.name8.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name8.setText("")
        except KeyError:
            self.Verification.name8.setText("")

        try:
            self.Verification.name9.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name9.setText("")
        except KeyError:
            self.Verification.name9.setText("")

        try:
            self.Verification.name10.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name10.setText("")
        except KeyError:
            self.Verification.name10.setText("")
        
        # Поле фамилии
        i = 0
        try:
            self.Verification.lastName1.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName1.setText("")
        except KeyError:
            self.Verification.lastName1.setText("")

        try:
            self.Verification.lastName2.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName2.setText("")
        except KeyError:
            self.Verification.lastName2.setText("")

        try:
            self.Verification.lastName3.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName3.setText("")
        except KeyError:
            self.Verification.lastName3.setText("")

        try:
            self.Verification.lastName4.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName4.setText("")
        except KeyError:
            self.Verification.lastName4.setText("")

        try:
            self.Verification.lastName5.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName5.setText("")
        except KeyError:
            self.Verification.lastName5.setText("")

        try:
            self.Verification.lastName6.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName6.setText("")
        except KeyError:
            self.Verification.lastName6.setText("")

        try:
            self.Verification.lastName7.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName7.setText("")
        except KeyError:
            self.Verification.lastName7.setText("")

        try:
            self.Verification.lastName8.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName8.setText("")
        except KeyError:
            self.Verification.lastName8.setText("")

        try:
            self.Verification.lastName9.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName9.setText("")
        except KeyError:
            self.Verification.lastName9.setText("")

        try:
            self.Verification.lastName10.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName10.setText("")
        except KeyError:
            self.Verification.lastName9.setText("")

    def buttonSlideButton4(self):
        self.Verification.pushButton1.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton2.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton3.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton4.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton5.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton6.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton7.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton8.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton9.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton10.setStyleSheet("background-color: #E5E7F5")
        self.Of=(self.j+3)*10-10
        user_id_path = "./wallet/user_id.id"
        postType = "/api/verification/getAll"
        httpObj = http.http()

        if (not os.environ.get('VER_SERVER_IP')):
            verServerIP = "127.0.0.1"
        else:
            verServerIP = os.environ.get('VER_SERVER_IP')
        
        data = {}
        
        with open(user_id_path, "r") as text_file:
            data["user_id"] = int(text_file.read())
        
        data["limit"] = self.Li
        data["offset"] = self.Of

        response = httpObj.sendData("http://" + verServerIP + ":80" + postType,data)    
        print(response)
        i=0
        try:
            self.Verification.num1.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num1.setText("")
        except KeyError:
            self.Verification.num1.setText("")

        try:
            self.Verification.num2.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num2.setText("")
        except KeyError:
            self.Verification.num2.setText("")

        try:
            self.Verification.num3.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num3.setText("")
        except KeyError:
            self.Verification.num3.setText("")

        try:
            self.Verification.num4.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num4.setText("")
        except KeyError:
            self.Verification.num4.setText("")

        try:
            self.Verification.num5.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num5.setText("")
        except KeyError:
            self.Verification.num5.setText("")

        try:
            self.Verification.num6.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num6.setText("")
        except KeyError:
            self.Verification.num6.setText("")

        try:
            self.Verification.num7.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num7.setText("")
        except KeyError:
            self.Verification.num7.setText("")

        try:
            self.Verification.num8.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num8.setText("")
        except KeyError:
            self.Verification.num8.setText("")

        try:
            self.Verification.num9.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num9.setText("")
        except KeyError:
            self.Verification.num9.setText("")

        try:
            self.Verification.num10.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num10.setText("")
        except KeyError:
            self.Verification.num10.setText("")
        # Поле имени
        i = 0

        try:
            self.Verification.name1.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name1.setText("")
        except KeyError:
            self.Verification.name1.setText("")

        try:
            self.Verification.name2.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name2.setText("")
        except KeyError:
            self.Verification.name2.setText("")

        try:
            self.Verification.name3.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name3.setText("")
        except KeyError:
            self.Verification.name3.setText("")

        try:
            self.Verification.name4.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name4.setText("")
        except KeyError:
            self.Verification.name4.setText("")

        try:
            self.Verification.name5.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name5.setText("")
        except KeyError:
            self.Verification.name5.setText("")

        try:
            self.Verification.name6.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name6.setText("")
        except KeyError:
            self.Verification.name6.setText("")

        try:
            self.Verification.name7.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name7.setText("")
        except KeyError:
            self.Verification.name7.setText("")

        try:
            self.Verification.name8.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name8.setText("")
        except KeyError:
            self.Verification.name8.setText("")

        try:
            self.Verification.name9.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name9.setText("")
        except KeyError:
            self.Verification.name9.setText("")

        try:
            self.Verification.name10.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name10.setText("")
        except KeyError:
            self.Verification.name10.setText("")
        
        # Поле фамилии
        i = 0
        try:
            self.Verification.lastName1.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName1.setText("")
        except KeyError:
            self.Verification.lastName1.setText("")

        try:
            self.Verification.lastName2.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName2.setText("")
        except KeyError:
            self.Verification.lastName2.setText("")

        try:
            self.Verification.lastName3.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName3.setText("")
        except KeyError:
            self.Verification.lastName3.setText("")

        try:
            self.Verification.lastName4.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName4.setText("")
        except KeyError:
            self.Verification.lastName4.setText("")

        try:
            self.Verification.lastName5.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName5.setText("")
        except KeyError:
            self.Verification.lastName5.setText("")

        try:
            self.Verification.lastName6.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName6.setText("")
        except KeyError:
            self.Verification.lastName6.setText("")

        try:
            self.Verification.lastName7.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName7.setText("")
        except KeyError:
            self.Verification.lastName7.setText("")

        try:
            self.Verification.lastName8.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName8.setText("")
        except KeyError:
            self.Verification.lastName8.setText("")

        try:
            self.Verification.lastName9.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName9.setText("")
        except KeyError:
            self.Verification.lastName9.setText("")

        try:
            self.Verification.lastName10.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName10.setText("")
        except KeyError:
            self.Verification.lastName9.setText("")
        
    def buttonSlideButton5(self):
        self.Verification.pushButton1.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton2.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton3.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton4.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton5.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton6.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton7.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton8.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton9.setStyleSheet("background-color: #E5E7F5")
        self.Verification.pushButton10.setStyleSheet("background-color: #E5E7F5")
        self.Of=(self.j+4)*10-10
        user_id_path = "./wallet/user_id.id"
        postType = "/api/verification/getAll"
        httpObj = http.http()

        if (not os.environ.get('VER_SERVER_IP')):
            verServerIP = "127.0.0.1"
        else:
            verServerIP = os.environ.get('VER_SERVER_IP')
        
        data = {}
        
        with open(user_id_path, "r") as text_file:
            data["user_id"] = int(text_file.read())
        
        data["limit"] = self.Li
        data["offset"] = self.Of

        response = httpObj.sendData("http://" + verServerIP + ":80" + postType,data)    
        print(response)
        i=0
        try:
            self.Verification.num1.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num1.setText("")
        except KeyError:
            self.Verification.num1.setText("")

        try:
            self.Verification.num2.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num2.setText("")
        except KeyError:
            self.Verification.num2.setText("")

        try:
            self.Verification.num3.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num3.setText("")
        except KeyError:
            self.Verification.num3.setText("")

        try:
            self.Verification.num4.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num4.setText("")
        except KeyError:
            self.Verification.num4.setText("")

        try:
            self.Verification.num5.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num5.setText("")
        except KeyError:
            self.Verification.num5.setText("")

        try:
            self.Verification.num6.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num6.setText("")
        except KeyError:
            self.Verification.num6.setText("")

        try:
            self.Verification.num7.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num7.setText("")
        except KeyError:
            self.Verification.num7.setText("")

        try:
            self.Verification.num8.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num8.setText("")
        except KeyError:
            self.Verification.num8.setText("")

        try:
            self.Verification.num9.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num9.setText("")
        except KeyError:
            self.Verification.num9.setText("")

        try:
            self.Verification.num10.setText(str(response["data"][i]["id"]))
            i=i+1
        except IndexError:
            self.Verification.num10.setText("")
        except KeyError:
            self.Verification.num10.setText("")
        # Поле имени
        i = 0

        try:
            self.Verification.name1.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name1.setText("")
        except KeyError:
            self.Verification.name1.setText("")

        try:
            self.Verification.name2.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name2.setText("")
        except KeyError:
            self.Verification.name2.setText("")

        try:
            self.Verification.name3.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name3.setText("")
        except KeyError:
            self.Verification.name3.setText("")

        try:
            self.Verification.name4.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name4.setText("")
        except KeyError:
            self.Verification.name4.setText("")

        try:
            self.Verification.name5.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name5.setText("")
        except KeyError:
            self.Verification.name5.setText("")

        try:
            self.Verification.name6.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name6.setText("")
        except KeyError:
            self.Verification.name6.setText("")

        try:
            self.Verification.name7.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name7.setText("")
        except KeyError:
            self.Verification.name7.setText("")

        try:
            self.Verification.name8.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name8.setText("")
        except KeyError:
            self.Verification.name8.setText("")

        try:
            self.Verification.name9.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name9.setText("")
        except KeyError:
            self.Verification.name9.setText("")

        try:
            self.Verification.name10.setText(response["data"][i]["first_name"])
            i=i+1
        except IndexError:
            self.Verification.name10.setText("")
        except KeyError:
            self.Verification.name10.setText("")
        
        # Поле фамилии
        i = 0
        try:
            self.Verification.lastName1.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName1.setText("")
        except KeyError:
            self.Verification.lastName1.setText("")

        try:
            self.Verification.lastName2.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName2.setText("")
        except KeyError:
            self.Verification.lastName2.setText("")

        try:
            self.Verification.lastName3.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName3.setText("")
        except KeyError:
            self.Verification.lastName3.setText("")

        try:
            self.Verification.lastName4.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName4.setText("")
        except KeyError:
            self.Verification.lastName4.setText("")

        try:
            self.Verification.lastName5.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName5.setText("")
        except KeyError:
            self.Verification.lastName5.setText("")

        try:
            self.Verification.lastName6.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName6.setText("")
        except KeyError:
            self.Verification.lastName6.setText("")

        try:
            self.Verification.lastName7.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName7.setText("")
        except KeyError:
            self.Verification.lastName7.setText("")

        try:
            self.Verification.lastName8.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName8.setText("")
        except KeyError:
            self.Verification.lastName8.setText("")

        try:
            self.Verification.lastName9.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName9.setText("")
        except KeyError:
            self.Verification.lastName9.setText("")

        try:
            self.Verification.lastName10.setText(response["data"][i]["last_name"])
            i=i+1
        except IndexError:
            self.Verification.lastName10.setText("")
        except KeyError:
            self.Verification.lastName9.setText("")
    

    def fade(self,__fading_button):
        self.__fading_button = self.sender()  # enter the "fading button" state
        self.__fading_button.setWindowOpacity(1)
        self.__fading_button.setStyleSheet("background-color: #2e3436")
        self.__fading_button = None  # exit the "fading button" state


class Personal_Card(QtWidgets.QMainWindow):

    num = None

    def __init__(self,fN,lN,mN,ad,COR,CAPOB,Na,DOB,Em,Ph,zC,fl,num):
        super().__init__()
        pdfFile = open("./pdfCard.pdf","wb")
        fl['file'] = base64.b64decode(fl['file'].encode('utf-8'))
        pdfFile.write(fl['file'])
        pdfFile.close()
        self.num = num
        self.VerificationSecondWindow3 = VerificationSecondWindow3.Ui_PersonalCard()
        self.VerificationSecondWindow3.setupUi(self)
        self.VerificationSecondWindow3.First_Name.setText(fN)
        self.VerificationSecondWindow3.Last_Name.setText(lN)
        self.VerificationSecondWindow3.Midle_Name.setText(mN)
        self.VerificationSecondWindow3.Address.setText(ad)
        self.VerificationSecondWindow3.CountryOfResidence.setText(COR)
        self.VerificationSecondWindow3.CountryAndPlaceOfBirth.setText(CAPOB)
        self.VerificationSecondWindow3.Nationality.setText(Na)
        self.VerificationSecondWindow3.DateOfBirth.setText(DOB)
        self.VerificationSecondWindow3.Email.setText(Em)
        self.VerificationSecondWindow3.PhoneNumber.setText(Ph)
        self.VerificationSecondWindow3.ZIpCode.setText(zC)
        PDF = convert_from_bytes(open("./pdfCard.pdf","rb").read())
        PDF[0].thumbnail((481, 621), Image.ANTIALIAS)
        self.VerificationSecondWindow3.pdf.setPixmap(self.pil2pixmap(PDF[0]))
        self.show()
        if(os.path.exists("./pdfCard.pdf")):
            os.remove("./pdfCard.pdf")
        self.VerificationSecondWindow3.Verify.clicked.connect(self.verifyButton)
        self.init_UI()

        
    def pil2pixmap(self, im):

        if im.mode == "RGB":
            r, g, b = im.split()
            im = Image.merge("RGB", (b, g, r))
        elif  im.mode == "RGBA":
            r, g, b, a = im.split()
            im = Image.merge("RGBA", (b, g, r, a))
        elif im.mode == "L":
            im = im.convert("RGBA")
        # Bild in RGBA konvertieren, falls nicht bereits passiert
        im2 = im.convert("RGBA")
        data = im2.tobytes("raw", "RGBA")
        qim = QtGui.QImage(data, im.size[0], im.size[1], QtGui.QImage.Format_ARGB32)
        pixmap = QtGui.QPixmap.fromImage(qim)
        return pixmap 

    def verifyButton(self):

        user_id_path = "./wallet/user_id.id"
            
        postType = "/api/verification/move"

        if (not os.environ.get('VER_SERVER_IP')):
            verServerIP = "127.0.0.1"
        else:
            verServerIP = os.environ.get('VER_SERVER_IP')

        httpObj = http.http()

        data = {}

        data["id"] = self.num

        with open(user_id_path, "r") as text_file:
            data["user_id"] = int(text_file.read())

        response = httpObj.sendData("http://" + verServerIP + ":80" + postType,data)   
        


app = QtWidgets.QApplication([])
window = Verification_window()
window.show()
sys.exit(app.exec())
