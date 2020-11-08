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

rsaObj = RSA.rsaCipher()

@app.route('/api/reg/user', methods=['POST'])
def regUser():
    return userController.Reg(request.data, rsaObj)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')