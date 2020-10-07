# coding: utf8
import components.http as http

def main():

    httpObj = http.http()

    httpObj.getKey()

    data = {}

    data['password'] = input("Password: ")
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

    input("Для отправка введенных данных нажмите Enter")

    httpObj.sendData("http://192.168.99.100:80/api/reg/user",data)

main()