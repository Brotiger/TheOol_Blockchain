#!/usr/bin/env python

'''
	Название: verificationServer;
	Описание: Программа отвечает за регистрацию потенциального инвестора в очередь на верификацию;
	Автор: Берестнев Дмитрий Дмитриевич;
'''

from flask import Flask, make_response, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

import controllers.userController as userController
import ciphers.RSA as RSA

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mariadb://root:123456@db/users"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

rsaObj = RSA.rsaCipher()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(256), nullable=False)
    phone = db.Column(db.String(15), nullable=True)
    firstName = db.Column(db.String(30), nullable=False)
    lastName = db.Column(db.String(30), nullable=False)
    middleName = db.Column(db.String(30), nullable=True)
    dateOfBirth = db.Column(db.String(), nullable=False)
    countryAndPlaceOfBirth = db.Column(db.String(150), nullable=True)
    nationality = db.Column(db.String(30), nullable=True)
    countryOfResidence = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(30), nullable=False)
    zipCode = db.Column(db.String(9), nullable=False)
    facebook = db.Column(db.String(50), nullable=True)
    messengers = db.Column(db.String(50), nullable=True)

    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.id 

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
    app.run(debug=True,host='0.0.0.0')