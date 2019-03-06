from bottle import run, post, route, template, request

with open('conf.json') as json_data_file:
    conf = json.load(json_data_file)

@post('/')  # our python function based endpoint
def bot_in():  
    data = request.json
    print(data)
    return 

@route('/')
def index():
    return '<b>Hello!</b>!'

if __name__ == '__main__':  
    run(host='localhost', port=conf['port'], debug=True)
