import requests
import json

import ciphers.AES as AES

def main():
    data = {}

    passwordAES = input("Password: ")
    data['first_name'] = input("First name*: ")
    data['last_name'] = input("Last name*: ")
    data['middle_name'] = input("Middle name: ")
    data['date_of_birth'] = input("Date of birth: ")
    data['country_and_place_of_birth'] = input("Country and place of birth: ")
    data['nationality'] = input("Nationality: ")
    data['country_of_residence'] = input("Country of residence*: ")
    data['address'] = input("Address*: ")
    data['zip_code'] = input("Zip Code*: ")
    data['email'] = input("Email*: ")    
    data['phone'] = input("Phone: ")
    data['messengers'] = input("Messengers: ").split(', ')

    encryptedData = AES.encrypt(json.dumps(data), passwordAES)

    dataPost = {
        "aes_password": passwordAES,
        "data": encryptedData
    }
    
    response = requests.post('http://192.168.99.100:80/api/reg/user', json=dataPost)
    print(response.json())

main()