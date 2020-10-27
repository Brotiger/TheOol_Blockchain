#!/usr/bin/env python

'''
	Название: verificationServer;
	Описание: Программа отвечает за регистрацию потенциального инвестора в очередь на верификацию;
	Автор: Берестнев Дмитрий Дмитриевич;
'''
from flask import Flask, make_response, request
from datetime import datetime

import controllers.userController as userController
import ciphers.RSA as RSA

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://server:v9bumEc1G9c8HBDO4QtHsFI8NNWcEh@db:3306/verification' #Добавляется по 2 записи, судя по всему стоит сменить mysql на sqllite или postegersql
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db = SQLAlchemy(app)

#class Users(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    first_name = db.Column(db.String(30), nullable=False)
#    last_name = db.Column(db.String(30), nullable=False)
#    middle_name = db.Column(db.String(30), nullable=True)
#    phone = db.Column(db.String(15), nullable=True, unique=True)
#    email = db.Column(db.String(256), nullable=False, unique=True)
#    password = db.Column(db.String(300), nullable=False)
#    date_of_birth = db.Column(db.String(30), nullable=False)
#    country_and_place_of_birth = db.Column(db.String(30), nullable=True)
#    nationality = db.Column(db.String(30), nullable=True)
#    country_of_residence = db.Column(db.String(30), nullable=False)
#    address = db.Column(db.String(30), nullable=False)
#    zip_code = db.Column(db.String(9), nullable=False)
#    facebook = db.Column(db.Integer, nullable=True)
#    messengers = db.Column(db.Integer, nullable=True)

#def createUser():
#    newUser = Users(
#        first_name="Dmitry",
#        last_name="Berestnev",
#        middle_name="Dmitrievich",
#        phone="899898967",
#        email="dimka@bdima.ru",
#        password="123",
#        date_of_birth="567456",
#        country_and_place_of_birth="Russia",
#        nationality="Russian",
#        country_of_residence="Russia",
#        address="Samara",
#        zip_code="123123",
#        facebook=0,
#        messengers=0,
#    )
#    db.session.add(newUser)
#    db.session.commit()

rsaObj = RSA.rsaCipher()

@app.route('/api/get/rsa', methods=['POST'])
def getRSA():
    rsaObj.createKeys()
    rsaKey = rsaObj.getPubKey()

    resData = {
            "rsa_key": rsaKey,
        }
    return make_response(resData)

@app.route('/api/reg/user', methods=['POST'])
def regUser():
    return userController.Reg(request.data, rsaObj)

if __name__ == '__main__':
    #createUser()
    app.run(debug=True,host='0.0.0.0')