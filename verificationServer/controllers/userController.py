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

            #newUser = {}

            #подготовка полей для записи в бд
           # newUser['password'] = userData['password'] if 'password' in userData else ''
           # newUser['email'] = userData['email'] if 'email' in userData else ''
           # newUser['phone'] = userData['phone'] if 'phone' in userData else ''
           # newUuser['firstName'] = userData['first_name'] if 'first_name' in userData else ''
           # newUser['lastName'] = userData['last_name'] if 'last_name' in userData else ''
           # newUser['middleName'] = userData['middle_name'] if 'middle_name' in userData else ''
           # newUser['dateOfBirth'] = userData['date_of_birth'] if 'date_of_birth' in userData else ''
           # newUser['country_and_place_of_birth'] = userData['country_and_place_of_birth'] if 'country_and_place_of_birth' in userData else ''
           # newUser['nationality'] = userData['nationality'] if 'nationality' in userData else ''
           # newUser['country_of_residence'] = userData['country_of_residence'] if 'country_of_residence' in userData else ''
           # newUser['address'] = userData['address'] if 'address' in userData else ''
           # newUser['zip_code'] = userData['zip_code'] if 'zip_code' in userData else ''
           # newUser['facebook'] = userData['facebook'] if 'facebook' in userData else ''
           # newUser['messengers'] = userData['messengers'] if 'messengers' in userData else ''

            resData = {
                'success': True
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