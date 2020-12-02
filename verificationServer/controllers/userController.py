import validators.validator as validators
from flask import make_response
import components.http as http
import models.Users as mUsers
import json
import ciphers.RSA as RSA

rsaObj = RSA.rsaCipher()

objUsers = mUsers.Users()

#Передаем rsa объект для того что бы извлечь из него закрытый ключ
def reg(userData):

    errorsObj = {}
    successType = False
    statusCode = 400

    httpObj = http.http(rsaObj)

    try:
        userData = httpObj.dataDecrypt(userData)#дешифровка
    except:
        errorsObj['aes'] = 'Data spoofing'
        successType = False
        statusCode = 400
    else:
        rsaObj.setPubKeyClient(userData['rsa_key'])

        sign = userData.pop("sign")

        signResult = rsaObj.verifySign(userData,sign)

        #Если подпись не настоящая дальше ничег оне проверяем и генерируем ошибку
        if not signResult:
            errorsObj['sign'] = 'Data spoofing'
            successType = False
            statusCode = 400
        else:
            #Создаем объект валидации и передаем в него расшифрованные данные из запроса
            validatorObj = validators.validator(userData)

            #Валидация
            emailResult = validatorObj.email('email')
            phoneResult = validatorObj.phone('phone')
            fNameResult = validatorObj.fName('first_name')
            lNameResult = validatorObj.lName('last_name')
            mNameResult = validatorObj.mName('middle_name')
            dateOfBirthResult = validatorObj.dateOfBirth('date_of_birth')
            countryAndPlaceOfBirthResult = validatorObj.countryAndPlaceOfBirth('country_and_place_of_birth')
            nationalityResult = validatorObj.nationality('nationality')
            countryOfResidenceResult = validatorObj.countryOfResidence('country_of_residence')
            addressResult = validatorObj.address('address')
            zipCodeResult = validatorObj.zipCode('zip_code')
            facebookResult = validatorObj.faceBook('facebook')
            twitterResult = validatorObj.twitter('twitter')
            whatsappResult = validatorObj.whatsapp('whatsapp')
            telegramResult = validatorObj.telegram('telegram')
            fileResult = validatorObj.tFile('file')

            #Формирование списка ошибок на основе результатов валидации
            if emailResult:
                errorsObj['email'] = emailResult
            if phoneResult:
                errorsObj['phone'] = phoneResult
            if fNameResult:
                errorsObj['first_name'] = fNameResult
            if lNameResult:
                errorsObj['last_name'] = lNameResult
            if mNameResult:
                errorsObj['middle_name'] = mNameResult
            if dateOfBirthResult:
                errorsObj['date_of_birth'] = dateOfBirthResult
            if countryAndPlaceOfBirthResult:
                errorsObj['country_and_place_of_birth'] = countryAndPlaceOfBirthResult
            if nationalityResult:
                errorsObj['nationality'] = nationalityResult
            if countryOfResidenceResult:
                errorsObj['country_of_residence'] = countryOfResidenceResult
            if addressResult:
                errorsObj['address'] = addressResult
            if zipCodeResult:
                errorsObj['zip_code'] = zipCodeResult
            if facebookResult:
                errorsObj['facebook'] = facebookResult
            if twitterResult:
                errorsObj['twitter'] = twitterResult
            if telegramResult:
                errorsObj['telegram'] = telegramResult
            if whatsappResult:
                errorsObj['whatsapp'] = whatsappResult
            if fileResult:
                errorsObj['file'] = fileResult

            #Если ошибок нет
            if not len(errorsObj):
                db_result = objUsers.create(userData)

                if (db_result): 
                    successType = True
                    statusCode = 201
                else:
                    errorsObj['db'] = "Not recorded"
                    successType = False
                    statusCode = 500
                
            #Если ошибки есть
            else:
                successType = False
                statusCode = 400

    finally:
        resData = {
            'success': successType,
            'errors': errorsObj if bool(errorsObj) else None
        }
        res = httpObj.dataEncrypt(resData)
        return make_response(res, statusCode)