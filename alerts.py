import json
import requests
from bottle import run, post, route, template, request, response

from bot_msg import *
from reg import *
from start import *

def preparealertmsg(data):
	alert_msg="ALERT!"
	if 'msg' in data:
		alert_msg=data['msg']
	return alert_msg

def send_alert(alert_data):
	alert_msg = preparealertmsg(alert_data)
	regs=get_data("subscriptions")
	if regs is None: return
	for user in regs:
		msg_data = {
			"chat_id": user['chat_id'],
			"text": alert_msg
		}
		send_message(msg_data)

def send_alert_admin(alert_data):
	alert_msg = alert_data
	msg_data = {
		"chat_id": conf['alertchatid'],
		"text": alert_msg
	}
	send_message(msg_data)