#!/usr/bin/env python

'''
	Название: verificationServer;
	Описание: Программа отвечает за регистрацию потенциального инвестора в очередь на верификацию;
	Автор: Берестнев Дмитрий Дмитриевич;
'''
from flask import Flask, make_response, request
from datetime import datetime

import controllers.userController as userController
import controllers.verifierController as verifierController
import ciphers.RSA as RSA

app = Flask(__name__)

@app.route('/api/users/reg', methods=['POST'])
def regUser():
    return userController.reg(request.data)

@app.route('/api/users/getBlockChainInfo', methods=['POST'])
def getBlockChainInfo():
    return userController.getBlockChainInfo(request.data)

@app.route('/api/verification/getOne', methods=['POST'])
def getOne():
    return verifierController.getOne(request.data)

@app.route('/api/verification/getAll', methods=['POST'])
def getAll():
    return verifierController.getAll(request.data)

@app.route('/api/verification/create', methods=['POST'])
def regVerifier():
    return verifierController.create(request.data)

@app.route('/api/verification/move', methods=['POST'])
def moveUser():
    return verifierController.moveUser(request.data)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')