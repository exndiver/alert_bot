import json

from bot import *
from bot_msg import *

def checkreg(data):
	with open('configs/regs.json') as json_data_file:
		regs = json.load(json_data_file)
	json_data_file.close()
	for user in regs:
		if data["message"]["chat"]["username"]==user["username"] and data["message"]["chat"]["id"]==user["chat_id"]: return 1
	return 0

def regrequest(data):
	with open('configs/regreq.json') as json_data_file:
		regreq = json.load(json_data_file)
	json_data_file.close()
	for req in regreq:
		if req["chat_id"] == data["message"]["chat"]["id"]:
			msg=prepare_msg(data,"You already requested registration!")
			send_message(msg)
			return
	regreq.append({
		"username": data["message"]["chat"]["username"],
		"chat_id": data["message"]["chat"]["id"],
		"name": data["message"]["chat"]["first_name"]+" "+data["message"]["chat"]["last_name"]
	})
	with open('configs/regreq.json', 'w') as outfile:
		json.dump(regs, outfile)
	outfile.close()
	alert={
		"chat_id": conf['alertchatid'],
		"text": "New registration request from user "+data["message"]["chat"]["first_name"]+" "+data["message"]["chat"]["last_name"]+", username"+data["message"]["chat"]["username"]+" with chat id "+data["message"]["chat"]["id"]
	}
	msg=prepare_msg(data,"Now you have to wait for review. It will be done manually")
	send_message(msg)
