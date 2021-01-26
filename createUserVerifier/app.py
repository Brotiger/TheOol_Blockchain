import rsa
import base64
import os
import components.http as http

httpObj = http.http()

if (not os.environ.get('VER_SERVER_IP')):
    verServerIP = "127.0.0.1"
else:
    verServerIP = os.environ.get('VER_SERVER_IP')

response = httpObj.sendData("http://" + verServerIP + ":80/api/verification/create")

print(response)

with open("./new_user/user_id.id", "w") as text_file:
            text_file.write(str(response["data"]["id"]))
