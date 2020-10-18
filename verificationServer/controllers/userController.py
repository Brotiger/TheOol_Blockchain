import validators.userValidator as validators
from flask import make_response
import components.http as http

#Передаем rsa объект для того что бы извлечь из него закрытый ключ
def Reg(userData, rsaObj):
    errorsObj = {}
    httpObj = http.http(rsaObj)

    try:
        userData = httpObj.dataDecrypt(userData)#дешифровка
    except:
        errorsObj['aes'] = 'Data spoofing'
        resData = {
            "success": False,
            "errors": errorsObj
        }
    else:
        #Создаем объект валидации и передаем в него расшифрованные данные из запроса
        userValidatorObj = validators.userValidator(userData)

        #Валидация
        passwordResult = userValidatorObj.password('password')
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
        messengersResult = userValidatorObj.messengers('messengers')

        #Формирование списка ошибок на основе результатов валидации
        if passwordResult:
            errorsObj['password'] = passwordResult
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
        if messengersResult:
            errorsObj['messengers'] = messengersResult

        #Если ошибок нет
        if not len(errorsObj):

            resData = {
                'success': True,
            }
            
        #Если ошибки есть
        else:
            resData ={
                'success': False,
                'errors': errorsObj
            }

    finally:
        rsaObj.setPubKeyClient(userData['rsa_key'])
        res = httpObj.dataEncrypt(resData)
        return make_response(res)