import rsa
import base64
import os
import components.http as http

httpObj = http.http()

response = httpObj.sendData("http://" + os.environ.get('VER_SERVER_IP') + ":80/api/verification/create")

print(response)

with open("./new_user/user_id.id", "w") as text_file:
            text_file.write(str(response["data"]["id"]))
