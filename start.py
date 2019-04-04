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
        logger.info('%s %s %s %s %s - %s ---- %s' % (request_time,
										request.remote_addr,
                                        request.method,
                                        request.url,
                                        response.status,
										dict(request.headers),
					dict(request.body)))
        return actual_response
    return _log_to_logger

def graf_decor_data(odata,data):
	title="ALERT!"
	if 'title' in odata: title = odata["title"]
	title_decore_begin="**"
	title_decore_end="**"
	if '[Alerting]' in title:
		title_decore_begin="\U0000274C **"
		title_decore_end="** \U0000274C"
	if '[OK]' in title:
		title_decore_begin="\U00002705 **"
		title_decore_end="** \U00002705"
	if '[No Data]' in title:
		title_decore_begin="\U00002753 **"
		title_decore_end="** \U00002753"
	message=data['msg']		 
	return "%s%s%s\n%s" % (title_decore_begin,title,title_decore_end,message)

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
	log_message(alert_data)
	#For
	if 'message' in alert_data:
		original_data=alert_data
		alert_data=json.loads(alert_data['message'])
		alert_data['msg']=graf_decor_data(original_data,alert_data)
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
