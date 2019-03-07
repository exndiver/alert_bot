import json
import requests
from bottle import run, post, route, template, request, response

with open('conf.json') as json_data_file:
    conf = json.load(json_data_file)

bot_api="https://api.telegram.org/bot"+conf['token']+"/"


def getchatid(data):
	chat_id = data['message']['chat']['id']
	return chat_id

def prepare_msg(data):
	answer = "some text"
	msg_data  ={
		"chat_id": getchatid(data),
		"text": answer
	}
	return msg_data

def send_message(msg_data):
	msg_api = bot_api+'sendMessage'
	requests.post(msg_api, json=msg_data)


def preparealertmsg(data):
	alert_msg="ALERT!"
	if 'msg' in data:
		alert_msg=data['msg']
	return alert_msg


@post('/')
def bot_in():
	data = request.json
	print(data)
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

        alert_msg=preparealertmsg(alert_data)
	for cid in conf['alertchatid']:
		print(conf['alertchatid'][cid])
		msg_data  ={
			"chat_id": conf['alertchatid'][cid],
			"text": alert_msg
		}
		send_message(msg_data)
	return


@route('/')
def index():
    return '<b>Hello!</b>!'

if __name__ == '__main__':
    run(host='localhost', port=conf['port'], debug=True)
