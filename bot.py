import json

with open('configs/conf.json') as json_data_file:
    conf = json.load(json_data_file)
json_data_file.close()

with open('configs/strings.json') as json_data_file:
    strings = json.load(json_data_file)
json_data_file.close()

bot_api="https://api.telegram.org/bot"+conf['token']+"/"

def get_data(filename):
    with open('data/'+filename+'.json', 'r') as json_data_file:
        filedata = json.load(json_data_file)
    json_data_file.close()
    return filedata

def write_data(filename,data):
    with open('data/'+filename+'.json', 'w') as json_data_file:
        json.dump(data, json_data_file)
    json_data_file.close()

def log_message(msg):
    print("-------------------------------")
    print(msg)
    print("-------------------------------")