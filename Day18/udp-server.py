import socket

# 1、创建socket对象
udp_server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_server.bind(('10.31.156.17',8900))
data,addr = udp_server.recvfrom(1024)
print(data)
udp_server.close()







