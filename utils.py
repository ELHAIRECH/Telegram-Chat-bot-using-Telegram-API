import requests
import json
from config import *

def parse_message(message):
    msg_text = message["message"]["text"]
    #sender_name = resp["message"]["from"]["first_name"]
    chat_id = message["message"]["chat"]["id"]

    return chat_id, msg_text

#Creating basic commands outputs for 
#/track
#/menu
#/end
#/Greeetings

def message_response(msg_txt):
    commands = {"/start":"Greetings!I am Chatbot_DS_99. I was devoloped by ELHAIRECH Saifeddine, DAH Hamza and MENANI Abdelkabir.I am here to help you Track your code whithin the system\n To get help press /help.",
    "/track" : "Please type your code", 
    "/menu" : "How can I help you? /track or /end to end conversation.", 
    "/end" : "good bye!",
    "/Greetings" : "How can I help you"}
    if msg_txt in commands.keys():
        return commands[msg_txt]
    else:
        return "Sorry! Did you mean ? /track to track the code. /end to end conversation."

def send_message(chat_id, msg):
    url = "{}/bot{}/sendMessage".format(API_URL,TOKEN)
    payload = {
        "text":msg,
        "chat_id":chat_id
        }
    
    resp = requests.post(url, json=payload)
    #write_json(resp)
    return resp

def write_json(data, filename="response.json"):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=True)

