#!/usr/bin/env python
from flask import Flask, make_response, request

import json

import validators.user as validators
import ciphers.AES as AES

app = Flask(__name__)

@app.route('/api/reg/user', methods=['POST'])
def regUser():
    errorsObj = {}

    params = json.loads(request.data)

    try:
        userData = json.loads(AES.decrypt(params['data'], params['aes_password']))
    except:
        errorsObj['aes'] = 'Data spoofing'
        
        return make_response({
            "success": False,
            "errors": errorsObj
        }, 406)

    userValidatorObj = validators.userValidator(userData)

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

    if not len(errorsObj):
        res = make_response({
            'success': True
        }, 201)
    else:
        res = make_response({
            'success': False,
            'errors': errorsObj
        }, 406)
    return res

@app.route('/api/reg/company', methods=['POST'])
def regCompany():
    return "company"

@app.route('/api/auth/', methods=['POST'])
def auth():
    return "auth"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')