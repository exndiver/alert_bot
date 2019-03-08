import json

with open('configs/conf.json') as json_data_file:
    conf = json.load(json_data_file)
json_data_file.close()
bot_api="https://api.telegram.org/bot"+conf['token']+"/"
