import json
import requests
from bottle import run, post, route, template, request, response

from bot_msg import *
from bot_com import *
from alerts import *
from bot import *


@post('/')
def bot_in():
	data = request.json
	print(data)
	if not check_is_command(data):
		msg=prepare_msg(data,"Hello! Anything I can help? (Need a command)")
		send_message(msg)
		return
	execute_command(data)
	return


@post('/SendAlert')
def bot_alert():
	alert_data = request.json
	if alert_data is None:
		response.status = 403
		return
	if 'secret' not in alert_data:
		response.status = 403
		return
	if alert_data['secret']!=conf['secret']:
		response.status = 403
		return
	send_alert(alert_data)
	return


@route('/')
def index():
    return '<b>Hello!</b>!'

if __name__ == '__main__':
    run(host='localhost', port=conf['port'], debug=True)
