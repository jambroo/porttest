from bottle import route, run, template

@route('/test/<port>')
def test(port):
    return port

@route('/')
def index():
    return 'Hej'

run(host='localhost', port=8080)
