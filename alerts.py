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
    for cid in conf['alertchatid']:
	    print(conf['alertchatid'][cid])
	    msg_data = {
	        "chat_id": conf['alertchatid'][cid],
		    "text": alert_msg
	    }
	    send_message(msg_data)
    return