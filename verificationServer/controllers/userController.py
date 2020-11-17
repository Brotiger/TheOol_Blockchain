import validators.userValidator as validators
from flask import make_response
import components.http as http
import models.Users as mUsers
import json

#Передаем rsa объект для того что бы извлечь из него закрытый ключ
def Reg(userData, rsaObj):

    errorsObj = {}
    successType = False
    statusCode = 200

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
            userValidatorObj = validators.userValidator(userData)

            #Валидация
            emailResult = userValidatorObj.email('email')
            phoneResult = userValidatorObj.phone('phone')
            fNameResult = userValidatorObj.fName('first_name')
            lNameResult = userValidatorObj.lName('last_name')
            mNameResult = userValidatorObj.mName('middle_name')
            dateOfBirthResult = userValidatorObj.dateOfBirth('date_of_birth')
            countryAndPlaceOfBirthResult = userValidatorObj.countryAndPlaceOfBirth('country_and_place_of_birth')
            nationalityResult = userValidatorObj.nationality('nationality')
            countryOfResidenceResult = userValidatorObj.countryOfResidence('country_of_residence')
            addressResult = userValidatorObj.address('address')
            zipCodeResult = userValidatorObj.zipCode('zip_code')
            facebookResult = userValidatorObj.faceBook('facebook')
            twitterResult = userValidatorObj.twitter('twitter')
            whatsappResult = userValidatorObj.whatsapp('whatsapp')
            telegramResult = userValidatorObj.telegram('telegram')
            fileResult = userValidatorObj.tFile('file')

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
                objUsers = mUsers.Users()
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