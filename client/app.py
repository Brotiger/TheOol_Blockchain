# coding: utf8
import components.http as http
import os
import base64

def main():

    httpObj = http.http()

    data = {}

    data['first_name'] = input("First name*: ")
    data['last_name'] = input("Last name*: ")
    data['middle_name'] = input("Middle name: ")
    data['date_of_birth'] = input("Date of birth: ")
    data['country_and_place_of_birth'] = input("Country and place of birth: ")
    data['nationality'] = input("Nationality: ")
    data['country_of_residence'] = input("Country of residence*: ")
    data['address'] = input("Address*: ")
    data['zip_code'] = input("Zip Code*: ")
    data['facebook'] = input("facebook: ")
    data['email'] = input("Email*: ")    
    data['phone'] = input("Phone: ")

    twitter = input("Twitter (t/f): ")
    if(twitter == 't'):
        data['twitter'] = True
    elif(twitter == 'f'):
        data['twitter'] = False

    whatsapp = input("whatsapp (t/f): ")
    if(whatsapp == 't'):
        data['whatsapp'] = True
    elif(whatsapp == 'f'):
        data['whatsapp'] = False

    telegram = input("telegram (t/f): ")
    if(telegram == 't'):
        data['telegram'] = True
    elif(telegram == 'f'):
        data['telegram'] = False

    passportPwd = input("Введите путь до фотографии паспорта*: ")

    base = os.path.basename(passportPwd)
    fileName ,fileExt = os.path.splitext(base)

    fileExt = fileExt[1:]

    if os.path.exists(passportPwd):
        if os.path.isfile(passportPwd):
            passportByteString = open(passportPwd, 'rb').read()

            passportString = base64.b64encode(passportByteString).decode('utf-8')

            passport = {
                'ext': fileExt,
                'name': fileName,
                'file': passportString
            }

            data['passport'] = passport

    input("Для отправка введенных данных нажмите Enter")

    httpObj.sendData("http://" + os.environ.get('VER_SERVER_IP') + ":80/api/reg/user",data)

main()