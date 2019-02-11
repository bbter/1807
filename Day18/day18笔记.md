## 19.01_Python语言基础(TCP/IP概述)(了解)
* 对互联网大家都很熟悉，实际上计算机网络的出现比互联网要早很多。



#### 通讯协议
	计算机为了联网，就必须规定通信协议，都是由各厂商自己规定早期的计算机网络一套协议
	IBM、Apple和Microsoft都有各自的网络协议，互不兼容，这就好比一群人有的说英语，
	有的说中文，有的说德语，说同一种语言的人可以交流，不同的语言之间就不行了。
	
	为了把全世界的所有不同类型的计算机都连接起来，就必须规定一套全球通用的协议，
	为了实现互联网这个目标，互联网协议簇（Internet Protocol Suite）就是通用协议标准。
	Internet是由inter和net两个单词组合起来的，原意就是连接“网络”的网络，
	有了Internet，任何私有网络，只要支持这个协议，就可以联入互联网。



#### TCP\IP协议
	互联网协议包含了上百种协议标准，最重要的两个协议是TCP和IP协议，
	所以，大家经常把互联网的协议简称TCP/IP协议。



#### 通讯原理
	通信的时候，双方必须知道对方的标识，好比发邮件必须知道对方的邮件地址。
	互联网上每个计算机的唯一标识就是IP地址，类似123.123.123.123。
	如果一台计算机同时接入到两个或更多的网络，比如路由器，它就会有两个或多个IP地址，
	所以，IP地址对应的实际上是计算机的网络接口，通常是网卡。



#### IP协议
	IP协议负责把数据从一台计算机通过网络发送到另一台计算机。
	数据被分割成一小块一小块，然后通过IP包发送出去。
	由于互联网链路复杂，两台计算机之间经常有多条线路，
	因此，路由器就负责决定如何把一个IP包转发出去。
	IP包的特点是按块发送，途径多个路由，但不保证能到达，也不保证顺序到达。
	



#### TCP协议
	TCP协议则是建立在IP协议之上的。TCP协议负责在两台计算机之间建立可靠连接，保证数据包按顺序到达。
	TCP协议会通过握手建立连接，然后，对每个IP包编号，确保对方按顺序收到，如果包丢掉了，就自动重发。

	许多常用的更高级的协议都是建立在TCP协议基础上的，比如用于浏览器的HTTP协议、发送邮件的SMTP协议等。




#### 端口
	一个IP包除了包含要传输的数据外，还包含源IP地址和目标IP地址，源端口和目标端口。
	端口有什么作用？在两台计算机通信时，只发IP地址是不够的，因为同一台计算机上跑着多个网络程序。
	一个IP包来了之后，到底是交给浏览器还是QQ，就需要端口号来区分。
	每个网络程序都向操作系统申请唯一的端口号，
	这样，两个进程在两台计算机之间建立网络连接就需要各自的IP地址和各自的端口号。
	一个进程也可能同时与多个计算机建立链接，因此它会申请很多端口。



## 19.02_Python语言基础(网络编程)(了解)
Socket又称"套接字"，应用程序通常通过"套接字"向网络发出请求或者应答网络请求，
使主机间或者一台计算机上的进程间可以通讯。
Socket是网络编程的一个抽象概念。通常我们用一个Socket表示“打开了一个网络链接”，而打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型即可。


Python 中，我们用 socket（）函数来创建套接字，语法格式如下：
socket.socket([family[, type[, proto]]])
family: 套接字家族可以使AF_UNIX或者AF_INET
type: 套接字类型可以根据是面向连接的还是非连接分为SOCK_STREAM或SOCK_DGRAM
protocol: 一般不填默认为0.



#### socket编程有UDP和TCP两种传输协议

## 19.03_Python语言基础(UDP编程)(熟练)
UDP则是面向无连接的协议。
使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包。
但是，能不能到达就不知道了。
虽然用UDP传输数据不可靠，但它的优点是速度快(和TCP比)，对于不要求可靠到达的数据，就可以使用UDP协议。
我们来看看如何通过UDP协议传输数据。使用UDP的通信双方分为客户端和服务器。
服务器首先需要绑定端口：

UDP编程步骤要简单许多，分别如下：
#
	 	 
#### UDP编程的服务器端一般步骤是： 
		"""
	　　UDP 服务端
	    1、创建一个socket使用函数socket()
	    2、绑定IP地址、端口信息到socket上，使用bind()
	    3、循环接受数据使用recvfrom()
	    4、关闭网络连接
		"""
#### UDP客户端的server写法
	import socket
	
	# 创建socket对象
	server_udp = socket.socket(type=socket.SOCK_DGRAM)
	# 绑定ip和端口号
	ip_port = ("192.168.1.104", 12345)
	# 绑定端口号和ip
	server_udp.bind(ip_port)
	# 接收数据
	data, addr = server_udp.recvfrom(1024)
	
	print(data,addr)
	
	# 断开连接
	server_udp.close()

	
#### UDP编程的客户端一般步骤是： 
		"""
		udp客户端
		1、创建socket对象
		2、设置目标的ip和端口号
		3、发送数据，使用sendto
		4、断开连接
		"""

#### UDP客户端的client写法
	import socket
	# 创建socket对象
	client_udp = socket.socket(type=socket.SOCK_DGRAM)
	# 设置ip地址和端口号
	ip_port = ("192.168.1.104", 12345)
	# 消息内容
	msg = "hello Python"
	# 发送数据
	client_udp.sendto(bytes(msg, encoding="utf-8"), ip_port)
	# 关闭连接
	client_udp.close()



## 19.04_Python语言基础(TCP编程)(熟练)
#### TCP服务端server的写法：
	"""
	1、创建socket对象
	2、绑定ip和端口号
	3、服务端开启监听
	4、服务端接受请求
	5、接受数据
	6、断开连接
	"""
		
	# 1、创建socket对象
	tcp_server = socket.socket()
	# 2、绑定ip和端口号
	ip_port = ("192.168.1.104", 12346)
	# 3、服务端开启监听
	tcp_server.bind(ip_port)
	tcp_server.listen(5)
	# 4、服务端接受请求
	conn, addr = tcp_server.accept()
	# 5、接受数据
	data = conn.recv(1024)
	print(data)
	# 6、断开连接
	tcp_server.close()
	

#### TCP客户端的client写法
	"""
	1、创建socket对象
	2、向服务端ip建立连接
	3、发送消息
	4、断开连接
	"""


	import socket
	# 1、创建socket对象
	tcp_client = socket.socket()
	# 2、向服务端ip建立连接
	ip_port = ("192.168.1.104", 12346)
	tcp_client.connect(ip_port)
	# 3、发送消息
	msg = "python hello"
	tcp_client.sendall(bytes(msg,encoding="utf-8"))
	# 4、断开连接
	tcp_client.close()


## 19.05_Python语言基础(TCP编程加强版)(熟练)
#### 客户端加强版
	import socket
	
	# 创建socket对象
	client_tcp = socket.socket()
	ip_port = ("172.16.5.236", 10086)
	# 建立客户端连接
	client_tcp.connect(ip_port)
	
	while True:
	    # 发送消息
	    msg = input("请输入消息：")
	    if len(msg) == 0:
	        continue
	    elif msg == "exit":
	        break
	    client_tcp.sendall(bytes(msg, encoding="utf-8"))
	
	    # 接收消息
	    data = client_tcp.recv(1024)
	    print(str(data, encoding="utf-8"))
	
	# 断开连接
	client_tcp.close()


#### 服务端加强版
	import socket
	
	# 创建socket对象
	server_tcp = socket.socket()
	# 主机地址和端口号
	ip_port = ("172.16.5.236", 10086)
	# 绑定主机地址和端口号
	server_tcp.bind(ip_port)
	# 监听
	server_tcp.listen(5)
	# 接受客户端请求
	conn, addr = server_tcp.accept()
	
	while True:
	    # 接收消息
	    data = conn.recv(1024)
	    if not data:
	        break
	    else:
	        print(str(data, encoding="utf-8"))
	    # 回复消息
	    msg = input("请回复：").strip()
	    if len(data) == 0:
	        continue
	    conn.sendall(bytes(msg, encoding="utf-8"))
	
	# 断开连接
	conn.close()


## 19.06_Python语言基础(TCP和UDP比较)(熟练)
* TCP与UDP的区别
#### 基于连接与无连接 
	对系统资源的要求（TCP较多，UDP少） 
	UDP程序结构较简单 
	流模式与数据报模式 
	TCP保证数据正确性，UDP可能丢包 
	TCP保证数据顺序，UDP不保证 
	部分满足以下几点要求时，应该采用UDP 面向数据报方式 网络数据大多为短消息 
	拥有大量Client 
	对数据安全性无特殊要求 
	网络负担非常重，但对响应速度要求高 
	具体编程时的区别 socket()的参数不同 
	UDP Server不需要调用listen和accept 
	UDP收发数据用sendto/recvfrom函数 
	TCP：地址信息在connect/accept时确定 
	UDP：在sendto/recvfrom函数中每次均 需指定地址信息 
	UDP：shutdown函数无效

* 编程区别

#### UDP和TCP编程步骤也有些不同，如下： 
####TCP编程的服务器端一般步骤是： 
	1、创建一个socket，用函数socket()； 
	2、设置socket属性，用函数setsockopt(); * 可选 
	3、绑定IP地址、端口等信息到socket上，用函数bind(); 
	4、开启监听，用函数listen()； 
	5、接收客户端上来的连接，用函数accept()； 
	6、收发数据，用函数send()和recv()，或者read()和write(); 
	7、关闭网络连接； 
	8、关闭监听；

#### TCP编程的客户端一般步骤是： 
	1、创建一个socket，用函数socket()； 
	2、设置socket属性，用函数setsockopt();* 可选 
	3、绑定IP地址、端口等信息到socket上，用函数bind();* 可选 
	4、设置要连接的对方的IP地址和端口等属性； 
	5、连接服务器，用函数connect()； 
	6、收发数据，用函数send()和recv()，或者read()和write(); 
	7、关闭网络连接；

* 与之对应的UDP编程步骤要简单许多，分别如下： 
#### UDP编程的服务器端一般步骤是： 
	1、创建一个socket，用函数socket()； 
	2、设置socket属性，用函数setsockopt();* 可选 
	3、绑定IP地址、端口等信息到socket上，用函数bind(); 
	4、循环接收数据，用函数recvfrom(); 
	5、关闭网络连接；

#### UDP编程的客户端一般步骤是： 
	1、创建一个socket，用函数socket()； 
	2、设置socket属性，用函数setsockopt();* 可选 
	3、绑定IP地址、端口等信息到socket上，用函数bind();* 可选 
	4、设置对方的IP地址和端口等属性; 
	5、发送数据，用函数sendto(); 
	6、关闭网络连接；