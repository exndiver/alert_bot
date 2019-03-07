import json
import requests
from bottle import run, post, route, template, request, response

from bot import *

def getchatid(data):
	chat_id = data['message']['chat']['id']
	return chat_id

def prepare_msg(data,text):
	answer = text
	msg_data  ={
		"chat_id": getchatid(data),
		"text": answer
	}
	return msg_data

def send_message(msg_data):
	msg_api = bot_api+'sendMessage'
	requests.post(msg_api, json=msg_data)