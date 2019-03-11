import json
from reg import *
from bot_msg import *
from bot import log_message

def direct_message(data):
    if not check_is_command(data):
        send_message(prepare_msg(data,strings["not_a_command"]))
        return
    execute_command(data)

def check_is_command(data):
    if 'entities' in data['message']:
        if 'type' in data['message']['entities'][0]:
            if data['message']['entities'][0]['type'] == "bot_command":
                return 1
    return 0


def check_permissions(data):
    if data["message"]["text"].split(" ")[0] == "/regme":
        if checkreg(data):
            send_message(prepare_msg(data,strings["already_registred_when_try_reg"]))
            return 0
        else: return 1
    elif not checkreg(data):
        send_message(prepare_msg(data, strings["unauth_reg_required_message"]))
        return 0
    else: return 1

def unknown_command(data):
    log_message("Some strange command ---> "+data["message"]["text"].split(" ")[0]+" <---")
    msg=prepare_msg(data,strings['unknown_command'])
    send_message(msg)

def help(data):
    log_message("Help requested")
    send_message(prepare_msg(data, strings["help_text_command"]))

def subscribe_command(data):
    log_message("Subscription started")
    listofsubscriptions=get_data("subscriptions")
    if len(data["message"]["text"].split(" "))==1:
        response_msg="List of Subscriptions:\n"
        for subscription in listofsubscriptions:
            response_msg+="   * "+subscription+" - "+ listofsubscriptions[subscription]["description"]+"\n"
        response_msg+="To subscribe send /subscribe <channel>"
        send_message(prepare_msg(data,response_msg))
    elif data["message"]["text"].split(" ")[1] in listofsubscriptions:
        if str(data['message']['chat']['id']) not in listofsubscriptions[data["message"]["text"].split(" ")[1]]["list"].split(","):
            listofsubscriptions[data["message"]["text"].split(" ")[1]]["list"]+=str(data['message']['chat']['id'])+","
            with open('data/subscriptions.json', 'w') as json_data_file:
                json.dump(listofsubscriptions, json_data_file)
            json_data_file.close()
            send_message(prepare_msg(data, strings['subscribe_success']))
        else:
            send_message(prepare_msg(data, strings["already_subscribed"]))
            log_message("User already subscribed")
    else:
        send_message(prepare_msg(data,strings["unknown_channel"]))
        log_message("User entered unknown channel")

def list_subscriptions(data):
    log_message("List of subscriptions started")
    listofchannels=get_data("subscriptions")
    sub_num=0
    users_sub=""
    for channel in listofchannels:
        if str(data['message']['chat']['id']) in listofchannels[channel]["list"].split(","):
            sub_num+=1
            users_sub+="   - " + channel + "\n"
    if sub_num: msg="You subscribe to " + str(sub_num) + " channels.\nList of yours subscriptions: \n" + users_sub
    else: msg = "You have no subscribtions"
    send_message(prepare_msg(data,msg))

def unsubscribe_command(data):
    log_message("Unsubscribe started")

def execute_command(data):
    if check_permissions(data):
        if data["message"]["text"].split(" ")[0] == "/help": help(data)
        elif data["message"]["text"].split(" ")[0] == "/subscribe": subscribe_command(data)
        elif data["message"]["text"].split(" ")[0] == "/mysubscriptions": list_subscriptions(data)
        elif data["message"]["text"].split(" ")[0] == "/unsubscribe": unsubscribe_command(data)
        elif data["message"]["text"].split(" ")[0] == "/regme": regrequest(data)
        else: unknown_command(data)    
        log_message("Done")
        return
    else:
        log_message("Fail")
        return
  