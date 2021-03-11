# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RON2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Registration(object):
    def setupUi(self, Registration):
        Registration.setObjectName("Registration")
        Registration.resize(640, 470)
        Registration.setMinimumSize(QtCore.QSize(640, 470))
        Registration.setMaximumSize(QtCore.QSize(640, 470))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./GUI/img/vectorpaint.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Registration.setWindowIcon(icon)
        self.groupBox = QtWidgets.QGroupBox(Registration)
        self.groupBox.setGeometry(QtCore.QRect(210, 181, 201, 121))
        self.groupBox.setStyleSheet("color: black")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(10, 30, 160, 83))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Twitter = QtWidgets.QCheckBox(self.verticalLayoutWidget_8)
        self.Twitter.setStyleSheet("color: black;")
        self.Twitter.setObjectName("Twitter")
        self.verticalLayout_8.addWidget(self.Twitter)
        self.Whatsapp = QtWidgets.QCheckBox(self.verticalLayoutWidget_8)
        self.Whatsapp.setStyleSheet("color: black")
        self.Whatsapp.setObjectName("Whatsapp")
        self.verticalLayout_8.addWidget(self.Whatsapp)
        self.Telegram = QtWidgets.QCheckBox(self.verticalLayoutWidget_8)
        self.Telegram.setStyleSheet("color: black")
        self.Telegram.setObjectName("Telegram")
        self.verticalLayout_8.addWidget(self.Telegram)
        self.groupBox_4 = QtWidgets.QGroupBox(Registration)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 71, 181, 341))
        self.groupBox_4.setStyleSheet("color: black")
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.groupBox_4)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(10, 30, 160, 306))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.WalletPassword = QtWidgets.QLineEdit(self.verticalLayoutWidget_9)
        self.WalletPassword.setStyleSheet("color: black")
        self.WalletPassword.setText("")
        self.WalletPassword.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.WalletPassword.setClearButtonEnabled(False)
        self.WalletPassword.setObjectName("WalletPassword")
        self.verticalLayout_9.addWidget(self.WalletPassword)
        self.FirstName = QtWidgets.QLineEdit(self.verticalLayoutWidget_9)
        self.FirstName.setStyleSheet("color: black")
        self.FirstName.setText("")
        self.FirstName.setObjectName("FirstName")
        self.verticalLayout_9.addWidget(self.FirstName)
        self.LastName = QtWidgets.QLineEdit(self.verticalLayoutWidget_9)
        self.LastName.setStyleSheet("color: black")
        self.LastName.setText("")
        self.LastName.setObjectName("LastName")
        self.verticalLayout_9.addWidget(self.LastName)
        self.MiddleName = QtWidgets.QLineEdit(self.verticalLayoutWidget_9)
        self.MiddleName.setStyleSheet("color: black")
        self.MiddleName.setText("")
        self.MiddleName.setObjectName("MiddleName")
        self.verticalLayout_9.addWidget(self.MiddleName)
        self.CountryOfResidence = QtWidgets.QLineEdit(self.verticalLayoutWidget_9)
        self.CountryOfResidence.setStyleSheet("color: black")
        self.CountryOfResidence.setText("")
        self.CountryOfResidence.setObjectName("CountryOfResidence")
        self.verticalLayout_9.addWidget(self.CountryOfResidence)
        self.ZipCode = QtWidgets.QLineEdit(self.verticalLayoutWidget_9)
        self.ZipCode.setStyleSheet("color: black")
        self.ZipCode.setText("")
        self.ZipCode.setObjectName("ZipCode")
        self.verticalLayout_9.addWidget(self.ZipCode)
        self.Address = QtWidgets.QLineEdit(self.verticalLayoutWidget_9)
        self.Address.setStyleSheet("color: black")
        self.Address.setText("")
        self.Address.setObjectName("Address")
        self.verticalLayout_9.addWidget(self.Address)
        self.Nationality = QtWidgets.QLineEdit(self.verticalLayoutWidget_9)
        self.Nationality.setStyleSheet("color: black")
        self.Nationality.setText("")
        self.Nationality.setObjectName("Nationality")
        self.verticalLayout_9.addWidget(self.Nationality)
        self.CountryAndPlaceOfBirth = QtWidgets.QLineEdit(self.verticalLayoutWidget_9)
        self.CountryAndPlaceOfBirth.setStyleSheet("color: black")
        self.CountryAndPlaceOfBirth.setText("")
        self.CountryAndPlaceOfBirth.setObjectName("CountryAndPlaceOfBirth")
        self.verticalLayout_9.addWidget(self.CountryAndPlaceOfBirth)
        self.PathToTHePdfFile = QtWidgets.QLineEdit(self.verticalLayoutWidget_9)
        self.PathToTHePdfFile.setStyleSheet("color: black")
        self.PathToTHePdfFile.setText("")
        self.PathToTHePdfFile.setObjectName("PathToTHePdfFile")
        self.verticalLayout_9.addWidget(self.PathToTHePdfFile)
        self.Register = QtWidgets.QPushButton(Registration)
        self.Register.setGeometry(QtCore.QRect(30, 421, 93, 28))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(False)
        font.setWeight(50)
        self.Register.setFont(font)
        self.Register.setStyleSheet("QPushButton{\n"
"background-color:#40167A;\n"
"color: #FFFFFF;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #442ABB;\n"
"}\n"
"")
        self.Register.setObjectName("Register")
        self.groupBox_5 = QtWidgets.QGroupBox(Registration)
        self.groupBox_5.setGeometry(QtCore.QRect(219, 320, 401, 131))
        self.groupBox_5.setStyleSheet("color: black")
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_12 = QtWidgets.QLabel(self.groupBox_5)
        self.label_12.setGeometry(QtCore.QRect(150, 20, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: black")
        self.label_12.setObjectName("label_12")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.groupBox_5)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(60, 50, 279, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lcdNumber_1 = QtWidgets.QLCDNumber(self.horizontalLayoutWidget_5)
        self.lcdNumber_1.setStyleSheet("")
        self.lcdNumber_1.setProperty("value", 158.0)
        self.lcdNumber_1.setProperty("intValue", 158)
        self.lcdNumber_1.setObjectName("lcdNumber_1")
        self.horizontalLayout_5.addWidget(self.lcdNumber_1)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.horizontalLayoutWidget_5)
        self.lcdNumber_2.setStyleSheet("")
        self.lcdNumber_2.setProperty("value", 22.0)
        self.lcdNumber_2.setProperty("intValue", 22)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.horizontalLayout_5.addWidget(self.lcdNumber_2)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.horizontalLayoutWidget_5)
        self.lcdNumber_3.setStyleSheet("")
        self.lcdNumber_3.setProperty("value", 10.0)
        self.lcdNumber_3.setProperty("intValue", 10)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.horizontalLayout_5.addWidget(self.lcdNumber_3)
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.horizontalLayoutWidget_5)
        self.lcdNumber_4.setStyleSheet("")
        self.lcdNumber_4.setProperty("value", 5.0)
        self.lcdNumber_4.setProperty("intValue", 5)
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.horizontalLayout_5.addWidget(self.lcdNumber_4)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.groupBox_5)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(60, 80, 281, 21))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_13.setStyleSheet("color: black")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_6.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_14.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_14.setStyleSheet("color: black")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_6.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_15.setStyleSheet("color: black")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_6.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_16.setStyleSheet("color: black")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_6.addWidget(self.label_16)
        self.groupBox_2 = QtWidgets.QGroupBox(Registration)
        self.groupBox_2.setGeometry(QtCore.QRect(430, 71, 191, 231))
        self.groupBox_2.setStyleSheet("color: black")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(10, 30, 160, 112))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.Email = QtWidgets.QLineEdit(self.verticalLayoutWidget_7)
        self.Email.setStyleSheet("color: black")
        self.Email.setText("")
        self.Email.setObjectName("Email")
        self.verticalLayout_7.addWidget(self.Email)
        self.FaceBook = QtWidgets.QLineEdit(self.verticalLayoutWidget_7)
        self.FaceBook.setStyleSheet("color: black")
        self.FaceBook.setText("")
        self.FaceBook.setObjectName("FaceBook")
        self.verticalLayout_7.addWidget(self.FaceBook)
        self.PhoneNumber = QtWidgets.QLineEdit(self.verticalLayoutWidget_7)
        self.PhoneNumber.setStyleSheet("color: black")
        self.PhoneNumber.setText("")
        self.PhoneNumber.setObjectName("PhoneNumber")
        self.verticalLayout_7.addWidget(self.PhoneNumber)
        self.groupBox_3 = QtWidgets.QGroupBox(Registration)
        self.groupBox_3.setGeometry(QtCore.QRect(210, 71, 201, 91))
        self.groupBox_3.setStyleSheet("color: black;")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 151, 16))
        self.label_2.setObjectName("label_2")
        self.month = QtWidgets.QSpinBox(self.groupBox_3)
        self.month.setGeometry(QtCore.QRect(60, 30, 42, 22))
        self.month.setMinimum(1)
        self.month.setMaximum(12)
        self.month.setObjectName("month")
        self.day = QtWidgets.QSpinBox(self.groupBox_3)
        self.day.setGeometry(QtCore.QRect(10, 30, 42, 22))
        self.day.setStyleSheet("")
        self.day.setMinimum(1)
        self.day.setMaximum(31)
        self.day.setObjectName("day")
        self.year = QtWidgets.QSpinBox(self.groupBox_3)
        self.year.setGeometry(QtCore.QRect(110, 30, 61, 22))
        self.year.setMinimum(1900)
        self.year.setMaximum(2021)
        self.year.setObjectName("year")
        self.Header = QtWidgets.QFrame(Registration)
        self.Header.setGeometry(QtCore.QRect(0, 0, 641, 51))
        self.Header.setStyleSheet("background-color:#40167A")
        self.Header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Header.setObjectName("Header")
        self.TextLogo_2 = QtWidgets.QLabel(self.Header)
        self.TextLogo_2.setGeometry(QtCore.QRect(20, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Serif Cond")
        font.setPointSize(18)
        font.setItalic(False)
        self.TextLogo_2.setFont(font)
        self.TextLogo_2.setStyleSheet("color: white")
        self.TextLogo_2.setObjectName("TextLogo_2")
        self.Logo_2 = QtWidgets.QLabel(self.Header)
        self.Logo_2.setEnabled(True)
        self.Logo_2.setGeometry(QtCore.QRect(520, -20, 161, 111))
        self.Logo_2.setStyleSheet("color: white")
        self.Logo_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Logo_2.setText("")
        self.Logo_2.setPixmap(QtGui.QPixmap("./GUI/img/vectorpaint.svg"))
        self.Logo_2.setScaledContents(True)
        self.Logo_2.setObjectName("Logo_2")

        self.retranslateUi(Registration)
        QtCore.QMetaObject.connectSlotsByName(Registration)

    def retranslateUi(self, Registration):
        _translate = QtCore.QCoreApplication.translate
        Registration.setWindowTitle(_translate("Registration", "Frame"))
        self.groupBox.setTitle(_translate("Registration", "Mark, if you have an account on:"))
        self.Twitter.setText(_translate("Registration", "Twitter"))
        self.Whatsapp.setText(_translate("Registration", "Whatsapp"))
        self.Telegram.setText(_translate("Registration", "Telegram"))
        self.groupBox_4.setTitle(_translate("Registration", "Personal information:"))
        self.WalletPassword.setPlaceholderText(_translate("Registration", "Wallet password*"))
        self.FirstName.setPlaceholderText(_translate("Registration", "FirstName*"))
        self.LastName.setPlaceholderText(_translate("Registration", "Last Name*"))
        self.MiddleName.setPlaceholderText(_translate("Registration", "Middle Name"))
        self.CountryOfResidence.setPlaceholderText(_translate("Registration", "Country of residence*"))
        self.ZipCode.setPlaceholderText(_translate("Registration", "Zip Code*"))
        self.Address.setPlaceholderText(_translate("Registration", "Address*"))
        self.Nationality.setPlaceholderText(_translate("Registration", "Nationality"))
        self.CountryAndPlaceOfBirth.setPlaceholderText(_translate("Registration", "Place of Birth"))
        self.PathToTHePdfFile.setPlaceholderText(_translate("Registration", "Path to the pdf file"))
        self.Register.setText(_translate("Registration", "Register"))
        self.groupBox_5.setTitle(_translate("Registration", "System information"))
        self.label_12.setText(_translate("Registration", "Time to sale:"))
        self.label_13.setText(_translate("Registration", "Days"))
        self.label_14.setText(_translate("Registration", "Hours"))
        self.label_15.setText(_translate("Registration", "Minuts"))
        self.label_16.setText(_translate("Registration", "Seconds"))
        self.groupBox_2.setTitle(_translate("Registration", "How to contact with you:"))
        self.Email.setPlaceholderText(_translate("Registration", "Email*"))
        self.FaceBook.setPlaceholderText(_translate("Registration", "FaceBook"))
        self.PhoneNumber.setPlaceholderText(_translate("Registration", "Phone number"))
        self.groupBox_3.setTitle(_translate("Registration", "Birth date:"))
        self.label_2.setText(_translate("Registration", " DD        MM        YYYY"))
        self.TextLogo_2.setText(_translate("Registration", "TheOol.net"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Registration = QtWidgets.QFrame()
    ui = Ui_Registration()
    ui.setupUi(Registration)
    Registration.show()
    sys.exit(app.exec_())
