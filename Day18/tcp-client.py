import socket



tcp_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp_client.connect(('10.31.156.45',56689))


while True:
    data = input("请输入给服务器发送的数据")
    tcp_client.send(data.encode("utf-8"))
    info = tcp_client.recv(1024)
    print("服务器说:",info.decode("utf-8"))

