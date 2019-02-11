## 04.01_Python语言基础(Python中的数据类型)(了解)
* Number
* Stirng
* List
* Tuple
* Sets
* Dictionary

## 04.02_Python语言基础(Num数据类型)(掌握)
* Python3中Num支持的数据类型有以下几类:
	* int
	* float
	* bool
	* complex

## 04.03_Python语言基础(int类型)(掌握)
* int表示长整型，Python3.X只有这一种整数类型，包含正整数和负整数
#
	a = 123
	b = -345
	# 接下来的写法和上面的写法作用相同
	# a, b = 123, 345
	print(a + b)
	print(a - b)
	print(a * b)
	print(a / b)
*
	输出结果
#
	-222
	468
	-42435
	-0.3565217391304348

## 04.04_Python语言基础(float类型)(掌握)
* float表示小数，只有这一种小数类型，包含正小数和负小数
#
	i = 11.1
	j = -22.2
	print(i + j)
	print(i - j)
	print(i * j)
	print(i / j)
* 
	输出结果
#
	-11.1
	33.3
	-246.42
	-0.5

## 04.05_Python语言基础(bool类型)(掌握)
* Python3中表示真或假的类型
	* Python3中bool类型只有两个值：True和False
	* python2中没有True和False，用0和1表示
	* True和False可以直接和数字运算
#
	h = True
	k = False
	print(h + k)
	print(h + 1)
	print(h - k)
	print(h * k)
	print(h / k)	# 报错
 
输出结果
#
	1
	2
	1
	0
	Traceback (most recent call last):
	File "Demos/Demo_Key.py", line 42, in <module>
    print(h / k)
	ZeroDivisionError: division by zero

## 04.06_Python语言基础(complex类型)(掌握)
* complex在Python中表示复数类型
	* 这里的复数解释为常量和变量的组合
	* 例如:k = 123+45j
		* 123表示常量
		* 45j表示变量
#
	g = 123+45j
	print(g)
	print(g.real)
	print(g.imag)

输出结果：
#
	(123+45j)
	123.0
	45.0

## 04.07_Python语言基础(math模块)(掌握)
###Math模块
* 绝对值	fabs
* 最大值	max
* 最小值 min
* 四舍五入 round
* 幂pow
* 天花板数字 ceil
* 地板数字	floor
* 取整数和小数部分	modf
* 开平方		sprt
#
	print(math.ceil(13.4))
	print(math.ceil(-13.4))
	print(math.floor(13.4))
	print(math.floor(-13.4))
	print(math.copysign(-18, 15))
	print(math.fabs(18.9))
	print(round(-18.9))
	print(math.modf(12.34))
	print(math.sqrt(7))
	print(random.randint(1, 10))
输出结果：
#
	14
	-13
	13
	-14
	18.0
	18.9	
	-19
	(0.33999999999999986, 12.0)
	2.6457513110645907
	10
## 04.08_Python语言基础(random模块)(掌握)
### Python随机数
* 从序列里面取值 choice
* 按指定的规则随机取数字 randrange(range(1,100,2)
* 产生随机数 random.random()范围是0--1
* 随机排序 shuffle(list)
* 随机产生规定范围内的小数uniform(3,9)
* 随机产生规定范围内的一个整数ranInt()
#
	import random
	print(dir(random))
	#返还一个随机的0-1之间的随机数
	print(random.random())
	#choice()返回随机的一个元素
	print(random.choice('abcdefg'))

	#randrange()随机返回一个元素  做微信随机抢红包
	print(random.randrange(1,10,2))
	"""
	randrange(start,stop,step)
	start起始值
	stop结束值
	step步长
	"""
	#shuffle()可以随机打乱列表里面的元素值
	list = [3,1,6,20,4,True,'abc']
	print(list)
	random.shuffle(list)
	print(list)
输出结果：
#
	['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_BuiltinMethodType', '_MethodType', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_inst', '_itertools', '_log', '_pi', '_random', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
	0.05391211483671399
	g
	5
	[3, 1, 6, 20, 4, True, 'abc']
	[1, 3, 20, 6, True, 4, 'abc']




## 04.09_Python语言基础(string模块)(掌握)
* 字符串简介
* 字符串定义方式
	* 书写规则单引号或者双引号
	* 字符串不可变
* 字符串输出
	* print("hello")
	* print("%s" % "hello")
* 字符串的输入
	* input()获取键盘录入数据
	* 输入的所有内容都是以字符串存储的
* 下标和切片
	* 下标：编号，超市柜子的号码，车票的位置,可以是负数：从最后一位往前数
		* 字符串/列表和元组支持切片
		* name = "abcd",print(name[0])
		* 如果修改某个位置的数据，可以通过下标实现
	* 切片：截取目标对象的一部分数据
		* 字符串/列表和元组支持切片 
		* 格式:[开始：结束：步长]
#
	word = "abcdef"
	print(word[0:3])
	print(word[0:5])
	print(word[2:5])
	print(word[1:])
	print(word[1:-1])
	print(word[:3])
	print(word[::2])
	print(word[1:5:2])
	print(word[5:1:2])
	print(word[5:1:-2])
	print(word[::-2])
*
	输出结果：
#
	3
	abc
	abcde
	cde
	bcdef
	bcde
	abc
	ace
	bd
	
	fd
	fdb
* 字符串常见操作
	* 字符串连接，使用+实现
	* 输出重复字符串print("--" * 10)
	* 切割字符串  split()
	* find()
	* index()
	* count()
	* replace()
	* capitalze()把第一个字符大写
	* title()
	* swapcase()大小写转换
	* startswith()
	* endswith()
	* lower()
	* upper()
	* isupper()
	* islower()
	* ljust()左对齐
	* rjust()右对齐
	* center()
	* zfill()右对齐补0
	* strip()去除两端的空字符
	* rfind()从右侧查找
	* rindex()从右侧查找索引
	* partition()以传入内容分割三部分
#
	# 下标index
	name = 'xiao huaWWW'
	print(name[len(name) - 1])

	# 把字符串切片,后面的数字表示要切几次，如果超出元素个数就以最大来执行
	print(name.split("a", 0))
	print(name[0:5:2])
	print(name[6:1:-2])
	print(name[::-1])

	# 重复输出字符串
	print("*" * 50)

	# 查找字符串元素第一次出现的位置,后面的参数表示从哪里开始
	print(name.find("a", 3))

	# 替换字符串
	print(name.replace("a", "w", 1))

	# 把首字母大写
	print(name.capitalize())

	# 把所有单词的首字母大写
	print(name.title())
	
	# 大小写转换
	print(name.swapcase())
	
	# 判断开头或者结尾是否是以什么开始/结束的
	print(name.startswith("xiao"))
	print(name.endswith("xiao"))

	num = ord("a")
	word = chr(num - 32)
	print(word)
	
	# 左侧对齐，width表示这个元素的总宽度，如果字符长度不够用空格补齐
	word = "abcdefg"
	print(word.ljust(20))
	print(word.ljust(20), "*")
	
	# 右侧对齐，width表示这个元素的总宽度，如果字符长度不够用空格补齐
	print(word.rjust(20))
	print(word.rjust(20), "*")
	
	# 居中显示，width表示这个元素的总宽度，如果字符长度不够用空格补齐
	print(word.center(20))
	print(word.center(20), "*")
	
	# zfill()右对齐，左补0
	print(word.zfill(20))
	
	# strip() 去除空格
	word = "   word  wordw  "
	print(word.strip())
	print(word.strip().strip("w"))
	
	# rfind从右侧开始查找
	# aaa.aaa.aaa.txt
	print(word.rfind("w"))
	# print(word.rfind("w", 14, 20))
	
	# index查找下标
	# print(word.index("a"))
	
	# rindex
	print(word.rindex("w"))
	
	# partition()
	print(word.partition("w"))
	print(word.rpartition("w"))
输出结果：
#
	W
	['xiao huaWWW']
	xa 
	u a
	WWWauh oaix
	**************************************************
	7
	xiwo huaWWW
	Xiao huawww
	Xiao Huawww
	XIAO HUAwww
	True
	False
	A
	abcdefg             
	abcdefg              *
	             abcdefg
	             abcdefg *
	      abcdefg       
	      abcdefg        *
	0000000000000abcdefg
	word  wordw
	ord  word
	13
	13
	('   ', 'w', 'ord  wordw  ')
	('   word  word', 'w', '  ')
### 转义字符：把普通的字符串转化成具有特殊含义的字符串
* \n
* \t
* r""--消除转义功能
#
	# 转义字符
	print("hello01", end="\t")
	print("hello02", end="\n")
	print("hello03", end="\r")
	print("hello04", end="\r\n")
	print("hello05", end="\r")
	print("hello06", end="\r")
输出结果：
#
	hello01	hello02
	hello04
	hello06


## 04.10_day01总结
* 把今天的知识点总结一遍。