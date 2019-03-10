import json
from reg import *
from bot_msg import *
from bot import log_message

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
            return 0
        else:
            regrequest(data)
            return 1
    elif not checkreg(data):
        msg=prepare_msg(data,"I don't know hwo you are! Please make a register request /regme")
        send_message(msg)
        return 0

def execute_command(data):
    if check_permissions(data):
        log_message("Done")
        return
    else:
        log_message("Fail")
        return
  