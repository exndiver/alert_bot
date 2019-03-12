import json
import requests
from bottle import Bottle, run, post, route, template, request, response
import logging
from functools import wraps
from datetime import datetime

from bot_msg import *
from bot_com import *
from alerts import *
from bot import *

logger = logging.getLogger('aller_bot')

logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs/alerts_bot.log', mode='a')
formatter = logging.Formatter('%(msg)s')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def log_to_logger(fn):
    @wraps(fn)
    def _log_to_logger(*args, **kwargs):
        print("logged")
        request_time = datetime.now()
        actual_response = fn(*args, **kwargs)
        logger.info('%s %s %s %s %s - %s' % (request_time,
										request.remote_addr,
                                        request.method,
                                        request.url,
                                        response.status,
										dict(request.headers)))
        return actual_response
    return _log_to_logger

app = Bottle()
app.install(log_to_logger)

@app.post('/')
def bot_in():
	data = request.json
	log_message(data)
	if 'message' in data: direct_message(data)
	elif 'channel_post' in data: log_message("It is a group chat. Teach me ho to work eith groups!!!")
	return

@app.post('/SendAlert')
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


@app.route('/')
def index():
	return '<b>Hello!</b>!'

if __name__ == '__main__':
    app.run(host='localhost', port=conf['port'], debug=False)
