import json

from bot import *
from bot_msg import *
from alerts import send_alert_admin

def checkreg(data):
	regs=get_data("regs")
	for user in regs:
		if data["message"]["chat"]["username"]==user["username"] and data["message"]["chat"]["id"]==user["chat_id"] and user["verified"]=="true" : return 1
	return 0

def regrequest(data):
	regreq=get_data("subscriptions")
	for req in regreq:
		log_message (req)
		if req["chat_id"] == data["message"]["chat"]["id"]:
			send_message(prepare_msg(data,"You already requested registration!"))
			log_message("Already requested chatid="+str(data["message"]["chat"]["id"]))
			return
	regreq.append({
		"username": data["message"]["chat"]["username"],
		"chat_id": data["message"]["chat"]["id"],
		"name": data["message"]["chat"]["first_name"]+" "+data["message"]["chat"]["last_name"],
		"verified":"false"
	})
	with open('data/regs.json', 'w') as outfile:
		json.dump(regreq, outfile)
	outfile.close()
	send_alert_admin("New registration request from user "+str(data["message"]["chat"]["first_name"])+" "+str(data["message"]["chat"]["last_name"])+", username "+str(data["message"]["chat"]["username"])+" with chat id "+str(data["message"]["chat"]["id"]))
	send_message(prepare_msg(data,strings["reg_success"]))
	return
