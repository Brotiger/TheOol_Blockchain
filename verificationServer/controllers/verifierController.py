import validators.validatorUserVerifier as validators
from flask import make_response
import components.http as http
import models.Users as mUsers
import json
import ciphers.RSA as RSA

rsaObj = RSA.rsaCipher()

objUsers = mUsers.Users()

def getAll(userData):
    errorsObj = {}
    successType = False
    statusCode = 400
    resData = {}

    httpObj = http.http(rsaObj)

    try:
        userData = httpObj.dataDecrypt(userData)#дешифровка
    except:
        errorsObj['aes'] = 'Data spoofing'
        successType = False
        statusCode = 400
    else:
        validatorObj = validators.validator(userData)
        userIdResult = validatorObj.id('user_id')

        if(not userIdResult):
            pubVerifirekey = objUsers.getVerifier(userData)["rsa_pub"]

        rsaObj.setPubKeyClient(pubVerifirekey)#сюда надо передать публичный ключ

        sign = userData.pop("sign")

        signResult = rsaObj.verifySign(userData, sign)

        #Если подпись не настоящая дальше ничег оне проверяем и генерируем ошибку
        if not signResult:
            errorsObj['sign'] = 'Data spoofing'
            successType = False
            statusCode = 400
        else:
            offsetResult = validatorObj.offset('offset')
            limitResult = validatorObj.limit('limit')

            user_id = userData.pop("user_id")

            if userIdResult:
                errorsObj['user_id'] = userIdResult
            if offsetResult:
                errorsObj['offset'] = offsetResult
            if limitResult:
                errorsObj['limit'] = limitResult

            if not len(errorsObj):
                db_result = False
                rsa_pub = objUsers.checkPermission(user_id)

                if(rsa_pub):
                    db_result = objUsers.getAll(userData)

                if (db_result):
                    resData['data'] = db_result if bool(db_result) else None
                    successType = True
                    statusCode = 201
                else:
                    errorsObj['db'] = "Unstable connection"
                    successType = False
                    statusCode = 500
            else:
                successType = False
                statusCode = 400

    finally:
        resData['success'] = successType
        resData['errors'] = errorsObj if bool(errorsObj) else None
        res = httpObj.dataEncrypt(resData)
        return make_response(res, statusCode)

def getOne(data):
    errorsObj = {}
    successType = False
    statusCode = 400
    resData = {}

    data = json.loads(data)

    validatorObj = validators.validator(data)

    idResult = validatorObj.id('id')
    userIdResult = validatorObj.id('user_id')

    user_id = data.pop("user_id")

    if idResult:
        errorsObj['id'] = idResult
    if userIdResult:
        errorsObj['user_id'] = userIdResult

    if not len(errorsObj):
        db_result = False
        rsa_pub = objUsers.checkPermission(user_id)
        if(rsa_pub):
            db_result = objUsers.getOne(data)

        if (db_result):
            resData['data'] = db_result if bool(db_result) else None
            successType = True
            statusCode = 201
        else:
            errorsObj['db'] = "Unstable connection"
            successType = False
            statusCode = 500
    else:
        successType = False
        statusCode = 400

    resData['success'] = successType
    resData['errors'] = errorsObj if bool(errorsObj) else None

    return make_response(resData, statusCode)

def create(data):
    errorsObj = {}
    successType = False
    statusCode = 400
    resData = {}

    data = json.loads(data)

    validatorObj = validators.validator(data)
    rsaResult = validatorObj.rsaKey('rsa_key')

    if rsaResult:
        errorsObj['rsa_key'] = rsaResult

    if not len(errorsObj):
        objUsers = mUsers.Users()
        db_result = objUsers.createVerifier(data)

        if (db_result):
            resData['data'] = db_result if bool(db_result) else None
            successType = True
            statusCode = 201
        else:
            errorsObj['db'] = "Not connection"
            successType = False
            statusCode = 500
    else:
        successType = False
        statusCode = 400

    resData['success'] = successType
    resData['errors'] = errorsObj if bool(errorsObj) else None

    return make_response(resData, statusCode)

def moveUser(data):
    errorsObj = {}
    successType = False
    statusCode = 400
    resData = {}

    data = json.loads(data)

    validatorObj = validators.validator(data)

    idResult = validatorObj.id('id')
    userIdResult = validatorObj.id('user_id')

    user_id = data.pop("user_id")

    if idResult:
        errorsObj['id'] = idResult
    if userIdResult:
        errorsObj['user_id'] = userIdResult

    if not len(errorsObj):
        db_result = False
        rsa_pub = objUsers.checkPermission(user_id)
        if(rsa_pub):
            db_result = objUsers.moveUser(data)

        if (db_result):
            successType = True
            statusCode = 201
        else:
            errorsObj['db'] = "Transfer failed"
            successType = False
            statusCode = 500
    else:
        successType = False
        statusCode = 400

    resData['success'] = successType
    resData['errors'] = errorsObj if bool(errorsObj) else None

    return make_response(resData, statusCode)