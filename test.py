# Potentially use bottle framework here

import socket;

def test_port_v4(ip, port):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

  result = sock.connect((ip, port))
  
  if result == 0:
    print("Port is open")
  else:
    print("Port is not open")


def test_port_v6(ip, port):
  sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)

  result = sock.connect((ip, port, 0, 0))
  
  if result == 0:
    print("Port is open")
  else:
    print("Port is not open")

#test_port_v6("2001:4860:4860:0:0:8888", 80)
#test_port_v4("127.0.0.1", 80)
