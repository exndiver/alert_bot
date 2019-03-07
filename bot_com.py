import json
from reg import *
from bot_msg import *

def check_is_command(data):
    if 'entities' in data['message']:
        if 'type' in data['message']['entities'][0]:
            if data['message']['entities'][0]['type'] == "bot_command":
                return 1
    return 0


def check_permissions(data):
    if data["message"]["text"] == "/regme":
        if checkreg(data):
            msg=prepare_msg(data,"You already registred!")
            send_message(msg)
            return
        else:
            regrequest(data)
    elif not checkreg(data):
        msg=prepare_msg(data,"I don't know hwo you are! Please make a register request /regme")
        send_message(msg)
        return

def execute_command(data):
    if check_permissions(data):
        print("Done")
        return
    return
  