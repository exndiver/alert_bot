import json

from bot import *
from bot_msg import *
from alerts import send_alert_admin

def checkreg(data):
	with open('configs/regs.json', 'r') as json_data_file:
		regs = json.load(json_data_file)
	json_data_file.close()
	for user in regs:
		if data["message"]["chat"]["username"]==user["username"] and data["message"]["chat"]["id"]==user["chat_id"]: return 1
	return 0

def regrequest(data):
	with open('configs/regreq.json', 'r') as json_data_file:
		regreq = json.load(json_data_file)
	json_data_file.close()
	for req in regreq:
		log_message (req)
		if req["chat_id"] == data["message"]["chat"]["id"]:
			msg=prepare_msg(data,"You already requested registration!")
			send_message(msg)
			log_message("Already requested chatid="+str(data["message"]["chat"]["id"]))
			return
	regreq.append({
		"username": data["message"]["chat"]["username"],
		"chat_id": data["message"]["chat"]["id"],
		"name": data["message"]["chat"]["first_name"]+" "+data["message"]["chat"]["last_name"]
	})
	
	with open('configs/regreq.json', 'w') as outfile:
		json.dump(regreq, outfile)
	outfile.close()
	alert_data = "New registration request from user "+str(data["message"]["chat"]["first_name"])+" "+str(data["message"]["chat"]["last_name"])+", username "+str(data["message"]["chat"]["username"])+" with chat id "+str(data["message"]["chat"]["id"])
	send_alert_admin(alert_data)
	msg=prepare_msg(data,"Now you have to wait for review. It will be done manually")
	send_message(msg)
	return
