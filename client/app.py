# coding: utf8
import components.http as http
import os
import base64

def main():

    choice = ''
    wallet_priv = "./wallet/client_rsa.priv"
    wallet_pub = "./wallet/client_rsa.pub"

    httpObj = http.http()

    while(choice != 'q'):
        print("1 - Регистрация")
        print("2 - Проверить цепочку")
        print("3 - Обновить цепочку")
        print("q - Выход")

        print('\n')
            
        choice = input("Ваше действие: ")

        print('\n')

        data = {}

        if (not os.environ.get('VER_SERVER_IP')):
            verServerIP = "127.0.0.1"
        else:
            verServerIP = os.environ.get('VER_SERVER_IP')

        try:
            if(choice == "q"):
                continue
            elif(choice == "1"):
                if(os.path.exists(wallet_priv)):
                    print("Вы уже зарегистрированы")
                else:
                    walletPassword = input("Wallet password*: ")
                    data["first_name"] = input("First name*: ")
                    data["last_name"] = input("Last name*: ")
                    data["middle_name"] = input("Middle name: ")
                    data["date_of_birth"] = input("Date of birth: ")
                    data["country_and_place_of_birth"] = input("Country and place of birth: ")
                    data["nationality"] = input("Nationality: ")
                    data["country_of_residence"] = input("Country of residence*: ")
                    data["address"] = input("Address*: ")
                    data["zip_code"] = input("Zip Code*: ")
                    data["facebook"] = input("facebook: ")
                    data["email"] = input("Email*: ")    
                    data["phone"] = input("Phone: ")

                    twitter = input("Twitter (t/f): ")
                    if(twitter == 't'):
                        data["twitter"] = True
                    elif(twitter == 'f'):
                        data["twitter"] = False

                    whatsapp = input("whatsapp (t/f): ")
                    if(whatsapp == 't'):
                        data["whatsapp"] = True
                    elif(whatsapp == 'f'):
                        data["whatsapp"] = False

                    telegram = input("telegram (t/f): ")
                    if(telegram == 't'):
                        data["telegram"] = True
                    elif(telegram == 'f'):
                        data["telegram"] = False

                    filePwd = input("Введите путь до pdf файла*: ")

                    base = os.path.basename(filePwd)
                    fileName ,fileExt = os.path.splitext(base)

                    fileExt = fileExt[1:]

                    if os.path.exists(filePwd):
                        if os.path.isfile(filePwd):
                            fileByteString = open(filePwd, 'rb').read()

                            fileString = base64.b64encode(fileByteString).decode('utf-8')

                            infoFile = {
                                "ext": fileExt,
                                "name": fileName,
                                "file": fileString
                            }

                            data["file"] = infoFile

                    print("\n")
                    input("Для отправка введенных данных нажмите Enter")
                    print("\n")

                    response = httpObj.sendData("http://" + verServerIP + ":80/api/users/reg",data, walletPassword)

                    if(response["success"] == False):
                        os.remove(wallet_priv)
                        os.remove(wallet_pub)
                        
                    print(response)
            elif(choice == "2"):
                if(not os.path.exists(wallet_priv)):
                    print("Сначала вам необходимо зарегистрироваться")
                else:
                    response = httpObj.sendData("http://" + verServerIP + ":80/api/users/reg",data, walletPassword)
            else:
                print("Неверный ввод, выбирите что то другое")
                print("\n")
                continue
        except Exception as err:
            print("\n")
            print("Ошибка ввода, попробуйте еще раз")
            print("\n")
            continue

main()