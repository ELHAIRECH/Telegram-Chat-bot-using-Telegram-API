from flask import Flask, jsonify, request,Response
import requests 

from config import *
from utils import *
from db import DBHelper


app = Flask("TelegramBot")
db = DBHelper()
codes = [2,3,11,13,42,69,111,666]

@app.route("/",methods=["POST", "GET"])
def index():
    if request.method == "POST":
       
        message = request.get_json()
        chat_id, msg_txt = parse_message(message)

        #write_json(message, "telegram_request.json")

        resp_msg = message_response(msg_txt)
        logger.debug(f"message recived : {msg_txt}, response : {resp_msg}")
        send_message(chat_id, resp_msg)
        if msg_txt == '/track':
            message = request.get_json()
            #code = int(message["message"]["text"])
            code = message["message"]["text"]
            mask = db.check(code)
            if mask[0]==1:
                resp_msg = "your code is on the system!"
                send_message(chat_id, resp_msg)
                
            else :
                resp_msg = "this code does not exist in the system!" 
                send_message(chat_id, resp_msg)
           

        
        return jsonify({'job_done' : 'ok','status' : 200})

    else:
        return jsonify({"status" : "stable"})
    


@app.route("/setwebhook/")
def setwebhook():
    resp = requests.get(f"{API_URL}/bot{TOKEN}/setWebhook?url={URL}")

  
    if resp.status_code == 200:
        return jsonify({'status' : 'ok'})
    else:
        return jsonify({'status' : 'error'})


if __name__ == '__main__':
    app.run(debug=True)