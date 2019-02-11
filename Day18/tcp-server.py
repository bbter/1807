import socket



tcp_server = socket.socket(type=socket.SOCK_STREAM)

tcp_server.bind(('10.31.156.17',8900))

tcp_server.listen(5)

conn,addr = tcp_server.accept()

data = conn.recv(1024)
