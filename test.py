import socket;

def test_port(ip, port):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  result = sock.connect_ex((ip, port))

  return(result == 0)

def get_ip(host, port=0):
  # search for all addresses, but take only the v6 one
  alladdr = socket.getaddrinfo(host, port, socket.AF_INET, socket.SOCK_DGRAM)
  for addrs in alladdr:
    for addr in addrs:
        if type(addr) is tuple and len(addr) == 2:
            return addr[0]

ip = get_ip('www.porttest.net')
print(test_port(ip, 80))
