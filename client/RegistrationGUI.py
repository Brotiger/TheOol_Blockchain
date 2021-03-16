import components.http as http
import os
import base64
import sys
from PyQt5 import QtCore, QtGui,QtWidgets 
from PyQt5.QtGui import QIcon
import GUI.RON2 as RON2
from datetime import datetime
import time

#RON - RegisterOolNet

class GUIWindow(QtWidgets.QMainWindow):
    data = {}
    day = 1
    month = 1
    year = 1900
    pathToThePdfFile= None
    walletPassword = None

    def __init__(self):
        super().__init__()
        self.RON2 = RON2.Ui_Registration()
        self.RON2.setupUi(self)
        self.show()
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('TheOolNet registration')
        self.setWindowIcon(QIcon('./GUI/img/vectorpaint.svg'))
        self.RON2.Register.clicked.connect(self.buttonClicked) 
    
    def buttonClicked(self):
        self.data = {}
        sender = self.sender()
        self.sysInput()
        wallet_priv = "./wallet/rsa.priv"
        wallet_pub = "./wallet/rsa.pub"
        if (not os.environ.get('VER_SERVER_IP')):
            verServerIP = "127.0.0.1"
        else:
            verServerIP = os.environ.get('VER_SERVER_IP')

        httpObj = http.http()

        base = os.path.basename(self.pathToThePdfFile)
        fileName ,fileExt = os.path.splitext(base)

        fileExt = fileExt[1:]

        if os.path.exists(self.pathToThePdfFile):
            if os.path.isfile(self.pathToThePdfFile):
                fileByteString = open(self.pathToThePdfFile, 'rb').read()

                fileString = base64.b64encode(fileByteString).decode('utf-8')

                infoFile = {
                    "ext": fileExt,
                    "name": fileName,
                    "file": fileString
                }

                self.data["file"] = infoFile
        response = httpObj.sendData("http://" + verServerIP + ":80/api/users/reg",self.data, self.walletPassword)
        
        if(response["success"] == False):
            os.remove(wallet_priv)
            os.remove(wallet_pub)                              

        try:
            if(response["errors"]["email"]!=None):
                self.RON2.Email.setStyleSheet("color:red;")
        except KeyError:
            self.RON2.Email.setStyleSheet("color:black;")
        except TypeError:
            self.RON2.Email.setStyleSheet("color:black;")
            
        try:
            if(response["errors"]["first_name"]!=None):
                self.RON2.FirstName.setStyleSheet("color:red;")
        except KeyError:
            self.RON2.FirstName.setStyleSheet("color:black;")
        except TypeError:
            self.RON2.FirstName.setStyleSheet("color:black;")

        try:
            if(response["errors"]["last_name"]!=None):
                self.RON2.LastName.setStyleSheet("color:red;")
        except KeyError:
            self.RON2.LastName.setStyleSheet("color:black;")
        except TypeError:
            self.RON2.LastName.setStyleSheet("color:black;")


        try:
            if(response["errors"]["zip_code"]!=None):
                self.RON2.ZipCode.setStyleSheet("color:red;")
        except KeyError:
            self.RON2.ZipCode.setStyleSheet("color:black;")
        except TypeError:
            self.RON2.ZipCode.setStyleSheet("color:black;")
            
        try:
            if(response["errors"]["country_of_residence"]!=None):
                self.RON2.CountryOfResidence.setStyleSheet("color:red;")
        except KeyError:
            self.RON2.CountryOfResidence.setStyleSheet("color:black;")
        except TypeError:
            self.RON2.CountryOfResidence.setStyleSheet("color:black;")

        try:
            if(response["errors"]["address"]!=None):
                self.RON2.Address.setStyleSheet("color:red;")
        except KeyError:
            self.RON2.Address.setStyleSheet("color:black;")
        except TypeError:
            self.RON2.Address.setStyleSheet("color:black;")
        #self.close()

        
# уточнить по поводу номера телефона (формат записи , инт неподходит для записи типа: +7..........)

# в блоке переменным присваиваются значения полей, затем на необхоимых к заполнению полях происходит проверка, если они незаполнены они выделяются красным
# метка времени для даты рождения
    def sysInput(self):
        self.data = {}
        self.walletPassword = self.RON2.WalletPassword.text() 
        self.data["first_name"] = self.RON2.FirstName.text()
        self.data["last_name"] = self.RON2.LastName.text()
        self.data["middle_name"]= self.RON2.MiddleName.text()
        self.data["country_and_place_of_birth"] = self.RON2.CountryOfResidence.text()
        self.data["zip_code"] = self.RON2.ZipCode.text()
        self.data["address"] = self.RON2.Address.text()
        self.data["nationality"] = self.RON2.Nationality.text()
        self.data["country_of_residence"] = self.RON2.CountryOfResidence.text()
        self.pathToThePdfFile = self.RON2.PathToTHePdfFile.text()
        self.data["email"] = self.RON2.Email.text()
        self.data["facebook"] = self.RON2.FaceBook.text()
        day = self.RON2.day.value()
        month = self.RON2.month.value()
        year = self.RON2.year.value()
        time_tuple = (year , month,  day,0,0,0,0,0,0)
        timestamp = str(int(time.mktime(time_tuple)))
        print(timestamp)
        self.data["date_of_birth"] = timestamp
        self.data["phone"] = self.RON2.PhoneNumber.text()
        if self.RON2.Telegram.isChecked():
            self.data["telegram"]=True
        else:
            self.data["telegram"] = False

        if self.RON2.Twitter.isChecked():
            self.data["twitter"] = True
        else:
            self.data["twitter"] = False

        if self.RON2.Whatsapp.isChecked():
            self.data["whatsapp"] = True
        else:
            self.data["whatsapp"] = False

app = QtWidgets.QApplication([])
window = GUIWindow()
window.show()
sys.exit(app.exec())


      

