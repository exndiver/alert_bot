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

def get_alert_list(channel):
	subs=get_data("subscriptions")
	if channel not in subs: return subs["default"]["list"]
	else: return subs[channel]["list"]

def send_alert(alert_data):
	alert_msg = preparealertmsg(alert_data)
	if 'channel' not in alert_data: regs=get_alert_list("default")
	else: regs=get_alert_list(alert_data["channel"])
	if regs =="": return
	for user in regs.split(","):
		if user=="": continue
		msg_data = {
			"chat_id": int(user),
			"text": alert_msg,
			"parse_mode": "Markdown"
		}
		send_message(msg_data)


def send_alert_admin(alert_data):
	alert_msg = alert_data
	msg_data = {
		"chat_id": conf['alertchatid'],
		"text": alert_msg
	}
	send_message(msg_data)
