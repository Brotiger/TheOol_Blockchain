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
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://server:v9bumEc1G9c8HBDO4QtHsFI8NNWcEh@192.168.99.100:3306/verification'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=True, nullable=False)
    last_name = db.Column(db.String(80), unique=True, nullable=False)

db.session.add(Users(first_name="asd", last_name=""))
db.session.commit()

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
    app.run(debug=True,host='0.0.0.0')