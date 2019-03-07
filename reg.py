import json

from bot import *
from bot_msg import *

def checkreg(data):
	for cid in conf['alertchatid']:
		if conf['alertchatid'][cid]: return 1
	return 0

def regrequest(data):
	with open('regreq.json') as json_data_file:
		regs = json.load(json_data_file)
	json_data_file.close()
	for req in regs:
		if req["chat_id"] == data["message"]["chat"]["id"]:
			msg=prepare_msg(data,"You already requested registration!")
			send_message(msg)
			return
	regs.append({
		"username": data["message"]["chat"]["username"],
		"chat_id": data["message"]["chat"]["id"],
		"name": data["message"]["chat"]["first_name"]+" "+data["message"]["chat"]["last_name"]
	})
	with open('regreq.json', 'w') as outfile:
		json.dump(regs, outfile)
	outfile.close()
	msg=prepare_msg(data,"Now you have to wait for review. It will be done manually")
	send_message(msg)