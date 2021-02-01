# coding: utf8
import components.http as http
import os
import base64
import json

def main():
    user_id_path = "./wallet/user_id.id"

    httpObj = http.http()

    if (not os.environ.get('VER_SERVER_IP')):
        verServerIP = "127.0.0.1"
    else:
        verServerIP = os.environ.get('VER_SERVER_IP')

    postType = ''

    choice = ''
    
    while(choice != 'q'):

        data = {}

        print("1 - Весь список пользователей")
        print("2 - Информация о конкретном пользователем")
        print("3 - Верефицировать пользователя")
        print("q - Выход")

        print('\n')
        
        choice = input("Ваше действие: ")

        print('\n')

        with open(user_id_path, "r") as text_file:
            data["user_id"] = int(text_file.read())

        if(choice == "q"):
            break
        elif(choice == "1"):
            data["limit"] = int(input("Количество записей: "))
            data["offset"] = int(input("Сдвиг: "))
            postType = "/api/verification/getAll"
        elif(choice == "2"):
            data["id"] = int(input("Введите id пользователя информацию о котором хотите получить: "))
            postType = "/api/verification/getOne"
        elif(choice == "3"):
            data["id"] = int(input("Введите id пользователя которого хотите верефицировать: "))
            postType = "/api/verification/move"

        print('\n')
        input("Для отправка введенных данных нажмите Enter")

        response = httpObj.sendData("http://" + verServerIP + ":80" + postType,data)
        
        print('\n')
        print(response)
        print('\n')

main()