import socket


udp_client = socket.socket(type=socket.SOCK_DGRAM)

data = "hello"

udp_client.sendto(data.encode("utf-8"),('10.31.156.45',56789))

udp_client.close()






