from bottle import request, route, run, template
import socket;

def test_port(ip, port):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  result = sock.connect_ex((ip, port))

  return(result == 0)

@route('/test/<port>')
def test(port):
    ip = request.remote_addr

    return "1" if test_port(ip, int(port)) else "0"

@route('/')
def index():
    return 'Hej'

run(host='localhost', port=8080)
