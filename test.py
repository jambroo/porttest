# Potentially use bottle framework here

from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)




import socket;

def test_port_v4(ip, port):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

  result = sock.connect((ip, port))

  if result == 0:
    print("Port is open")
  else:
    print("Port is not open")


def test_port_v6(ip, port):
  print("Testing", ip)
  sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)

  result = sock.connect((ip, port, 0, 0))

  if result == 0:
    print("Port is open")
  else:
    print("Port is not open")

#test_port_v6("2001:4860:4860:0:0:8888", 80)
#test_port_v4("127.0.0.1", 80)

def get_ip_6(host, port=0):
  # search for all addresses, but take only the v6 ones
  ips = []
  alladdr = socket.getaddrinfo(host, port, socket.AF_INET6, socket.SOCK_DGRAM)
  print(alladdr)
  for addr in alladdr:
    if len(addr) > 3:
      ip = addr[4]
      if ip[0].find(":") != -1 and ip not in ips:
        ips.append(ip)
  return(ips)

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
serversocket.bind((socket.gethostname(), 80))
# become a server socket
serversocket.listen(80)


#
# ip6s = get_ip_6('porttest.net', 80)
# if len(ip6s) > 0:
#
#   ip6 = ip6s[0][0]
#
#   #test_port_v6(ip6[0], 80)
#
#   sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
#   result = sock.connect_ex((ip6, 80))
#
#   print(result)
#
#   if result == 0:
#     print("Port is open")
#   else:
#     print("Port is not open")
