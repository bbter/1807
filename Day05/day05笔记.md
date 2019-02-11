## 05.01_Python语言基础(列表List)(掌握)

>想一想：
    前面学习的字符串可以用来存储一串信息，那么想一想，怎样存储咱们班所有同学的名字呢？
    定义100个变量，每个变量存放一个学生的姓名可行吗？有更好的办法吗？
>答曰

	列表
* 列表介绍
>
	序列是Python中最基本的数据结构。
	序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。
	列表是常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。
	列表可以进行的操作包括索引，切片，加，乘，检查成员。
	此外，Python已经内置确定列表的长度以及确定最大和最小的元素的方法。
	列表的数据项不需要具有相同的类型

##05.02_Python语言基础(创建列表)(掌握)
* 列表格式： 列表名 = [列表选项1,列表选项2,....,列表选项n]，示例如下：
#	
	# 创建列表
	list1 = [1, 2, 3, 4, 5]
	list2 = ["a", "b", "c", "d"]
	list3 = [True, False]
	list4 = ["a", 1, True, None]
	list5 = []
	# 控制台运行输出列表
	print(list1)
	print(list2)
	print(list3)
	print(list4)
	print(list5)
	print(type(list4))
	print(type(list5))
运行输出结果：
#
	[1, 2, 3, 4, 5]
	['a', 'b', 'c', 'd']
	[True, False]
	['a', 1, True, None]
	[]
	<class 'list'>
	<class 'list'>
想一想：list6 = [None]，print(list6)在控制台运行输出的是什么结果



##05.03_Python语言基础(运行输出列表)(掌握)


* A: 可以调用print()函数直接打印
#
	# 创建列表
	list1 = [1, 2, 3, 4, 5]
	list2 = ["a", "b", "c", "d"]
	# 运行输出列表
	print(list1)
	print(list2)
运行输出结果
#
	[1, 2, 3, 4, 5]
	['a', 'b', 'c', 'd']


* B: 使用下标运行输出列表中的每一个元素
#
	# 创建列表
	list1 = ["a", "b", "c", "d"]
	# 运行输出列表
	print(list1[0])
	print(list1[1])
	print(list1[2])
	print(list1[3])
运行输出结果：
#
	a
	b
	c
	d


* C: 使用for循环运行输出列表的每个数据
#
	#使用for循环
	namesList = ['xiaoWang', 'xiaoZhang', 'xiaoHua']
	for name in namesList:
	    print(name)
运行输出结果：
#
	xiaoWang
	xiaoZhang
	xiaoHua


* D: 使用while循环运行输出列表的每个数据
#
	#使用while循环
	namesList = ['xiaoWang', 'xiaoZhang', 'xiaoHua']
	length = len(namesList)
	i = 0
	while i < length:
	    print(namesList[i])
	    i += 1
运行输出结果：
#
	xiaoWang
	xiaoZhang
	xiaoHua


* E: 列表重复运行输出
#
	namesList = ['xiaoWang', 'xiaoZhang', 'xiaoHua']
	print(namesList * 2)
运行输出结果：
#
	['xiaoWang', 'xiaoZhang', 'xiaoHua', 'xiaoWang', 'xiaoZhang', 'xiaoHua']



##05.04_Python语言基础(列表常用操作)(掌握)
### 我们对数据常用的操作一般可以总结为：增、删、改、查，下面我们来学习关于列表的常用操作


* A: 访问列表元素
#
	namesList = ['xiaoWang', 'xiaoZhang', 'xiaoHua']
	print(namesList[0])
	print(namesList[1])
	print(namesList[2])
运行输出结果：
#
	xiaoHua
	xiaoZhang
	xiaoHua
想一想：print(namesList[3])在控制台运行输出的结果是什么


* B: 更改列表元素
#
	namesList = ['xiaoWang', 'xiaoZhang', 'xiaoHua']
	print("更改前的nameList：%s" % namesList)
	namesList[0] = "小王"
	print("更改后的nameList：%s" % namesList)
运行输出结果：
#
	更改前的nameList：['xiaoWang', 'xiaoZhang', 'xiaoHua']
	更改后的nameList：['小王', 'xiaoZhang', 'xiaoHua']


* C: 增加列表元素--append(object)
	* 通过append可以向列表中添加元素,添加的元素放在最后
#
	# 列表增加元素
	namesList = ['xiaoWang', 'xiaoZhang', 'xiaoHua']
	print("添加元素前的nameList：%s" % namesList)
	namesList.append("xiaoMing")
	print("添加元素后的nameList：%s" % namesList)
运行输出结果：
#
	添加元素前的nameList：['xiaoWang', 'xiaoZhang', 'xiaoHua']
	添加元素后的nameList：['xiaoWang', 'xiaoZhang', 'xiaoHua', '小明']


* D: 增加列表元素--insert(index,object)
	* 通过insert可以向列表指定位置添加元素
#
	# 列表增加元素--insert(index, object)
	namesList = ['xiaoWang', 'xiaoZhang', 'xiaoHua']
	print("添加元素前的nameList：%s" % namesList)
	namesList.insert(1, "小明")
	print("添加元素后的nameList：%s" % namesList)
运行输出结果：
#
	添加元素前的nameList：['xiaoWang', 'xiaoZhang', 'xiaoHua']
	添加元素后的nameList：['xiaoWang', '小明', 'xiaoZhang', 'xiaoHua']


* E: 增加列表元素--extend(index,object)
#
	# 列表增加元素--extend(list)
	namesList1 = ['xiaoWang', 'xiaoZhang', 'xiaoHua']
	namesList2 = ['小王', '小张', '小华']
	print("添加元素后的nameList：%s" % namesList1)
	namesList1.extend(namesList2)
	print("添加元素后的nameList：%s" % namesList1)
运行输出结果：
#
	添加元素后的nameList：['xiaoWang', 'xiaoZhang', 'xiaoHua']
	添加元素后的nameList：['xiaoWang', 'xiaoZhang', 'xiaoHua', '小王', '小张', '小华']


* F: 列表相加
# 
	# 列表相加
	namesList1 = ['xiaoWang', 'xiaoZhang', 'xiaoHua']
	namesList2 = ['小王', '小张', '小华']
	namesList3 = namesList1 + namesList2
	print(namesList3)
运行输出结果：
#
	['xiaoWang', 'xiaoZhang', 'xiaoHua', '小王', '小张', '小华']


* G: 查找元素（in, not in, index, count）
	* in(存在):如果存在返回的结果为True,反之False
 	* not in(不存在):如果不存在结果为True,反之False
 	* index(str, start, end)	查找元素第一次出现的下标
 	* count(str)	查找元素个数目
#
	# 查找列表元素
	namesList1 = ['xiaoWang', 'xiaoZhang', 'xiaoHua']
	# 获取用户要查找的名字
	findName = input("请输入需要查找的名字:")
	# 查找判断,是否存在
	if findName in namesList1:
	    print("找到有这个人...")
	elif findName not in namesList1:
	    print("查无此人....")
运行输出结果：
#
	请输入需要查找的名字:aaa
	查无此人....

	请输入需要查找的名字:xiaoHua
	找到有这个人...
 index()案例:
#
	# index /count
	a = ["a", "b", "c", "b", "d", "a"]
	print(a.index("b"))
	print(a.index("b", 2, 5))
	print(a.count("a"))
运行输出结果：
#
	1
	3
	2
想一想：print(a.index("e"))和print(a.count("e"))运行输出什么结果


* G: 删除元素（del/pop/remove）
	* del list[index] 删除指定位置的元素
	* pop(index)  删除一个元素，把删除的这个元素返回，index不写时默认是最后一个
	* remove(onject)
	
del案例：
#
	# 删除元素（del list[index]）
	word = ["a", "b", "c", "b", "d", "a"]
	print("删除元素前的word：%s" % word)
	del word[1]
	print("删除元素后的word：%s" % word)
运行输出结果：
#
	删除元素前的word：['a', 'b', 'c', 'b', 'd', 'a']
	删除元素后的word：['a', 'c', 'b', 'd', 'a']

pop()案例：
#
	# 删除元素（pop(index)）
	word = ["a", "b", "c", "b", "d", "e"]
	print("删除指定位置元素", word.pop(1))
	print("删除默认位置元素", word.pop())
运行输出结果：
#
	删除指定位置元素 b
	删除默认位置元素 e

remove()案例：
#
	# 删除元素（remove(object)）
	word = ["a", "b", "c", "b", "d", "e"]
	print("删除元素前的word：%s" % word)
	word.remove("a")
	print("删除元素后的word：%s" % word)
	word.remove("a")


* H：列表排序sort()
	* sort将列表按照特定的顺序重新的排列，默认由小到大
#
	# 列表排序sort(reverse=False)
	word = ["a", "b", "c", "b", "d", "e"]
	print("排序前的word：%s" % word)
	word.sort(reverse=False)
	print("顺序排序后的word：%s" % word)
	word.sort(reverse=True)

	print("逆序排序后的word：%s" % word)
运行输出结果：
#
	排序前的word：['a', 'b', 'c', 'b', 'd', 'e']
	顺序排序后的word：['a', 'b', 'b', 'c', 'd', 'e']
	逆序排序后的word：['e', 'd', 'c', 'b', 'b', 'a']

* I：列表的嵌套
	* 类似while、for循环的嵌套，列表也支持嵌套
	* 一个列表中的列表作为一个元素
	* 格式：列表名 = [ [ ], [ ], [ ] ]
	* 例如：schoolNames = [["清华大学"，"北京大学"],["哈尔滨佛学院"],[]]
	* 练习： 一个学校，有3个办公室，现在有8个老师等待分配工位，请编写程序，完成随机分配
#
	# 列表嵌套
	namesList = [["赵毅", "钱尔", "孙三"], ["里斯", "周武"], ["吴柳", "郑琦"]]
	for cls in namesList:
	    for name in cls:
	        print(name, end=",")
	    print()
运行输出结果：
#
	赵毅,钱尔,孙三,
	里斯,周武,
	吴柳,郑琦,


* J：获取列表中的最大/最小值
	* max(list)
	* min(list)
#
	# 获取最大值
	word = ["a", "b", "c", "b", "d", "e"]
	print(max(word))
	print(min(word))
运行输出结果：
#
	e
	a



## 05.05_Python语言基础(元组概述)(熟练)
* 元组概述
	* python的元组和列表类似，不同之处在于元组的元素不能修改，
* 元组格式：
    * 元组名 = (元组元素1，元组元素2.....元组元素n)
* 创建元组
#
	tuple1 = ()
	tuple2 = (1, 2, 3)
	tuple3 = (1, 2, 3, "hello", True)
	
	print(tuple1)
	print(tuple2)
	print(tuple3)
	
	print(type(tuple1))
	print(type(tuple2))
	print(type(tuple3))
运行输出结果：
#
	(1, 2, 3)
	(1, 2, 3, 'hello', True)
	<class 'tuple'>
	<class 'tuple'>
>做一做：tuple0 = (1)，print(type(tuple0))运行输出结果是什么



## 05.06_Python语言基础(访问元组)(熟练)
* 访问元组内容
	* 通过下标访问,格式：元组名[下标],下标从0开始
#
	# 访问元组元素
	tuple4 = (1, 2, 3, "hello", True)
	print(tuple4[2])
	print(tuple4[3])
运行输出结果：
#
	3
	hello
>试一试：print(tuole4[-2])运行输出结果是什么


#### 遍历元组
	# 遍历元组
	tuple5 = (1, 2, 3, "hello", True)
	for t in tuple5:
	    print(t)
运行输出结果：
#	
	1
	2
	3
	hello
	True
>做一做：使用while循环遍历元组


* 重复运行输出元组
#
	tuple1 = (1,2,3)
	print(tuple1 * 3)
运行输出结果：
#
	(1, 2, 3, 1, 2, 3, 1, 2, 3)


## 05.07_Python语言基础(元组常用操作)(掌握)
 	
#
	# 修改元组
	tuple6 = (1, 2, 3, "hello", True)
	tuple6[1] = 100
	print(tuple6)
运行输出结果：
#
	Traceback (most recent call last):
	  File "Day06/Tuple_Demo01.py", line 26, in <module>
	    tuple6[1] = 100
	TypeError: 'tuple' object does not support item assignment
>元组内一旦创建，不可更改
# 
	tuple5 = (1, 2, 3, 4, True, [5, 6, 7])
	# tuple5[0] = 100		#报错,元组不能修改
	# tuple5[-1] = [7,8,9]	#报错,
	tuple5[5][0] = 500
	print(tuple5)
运行输出结果
#	
	(1, 2, 3, 4, True, [500, 6, 7])
>元组被改变了,这个是什么情况呢？


* 删除元组
	* del可以删除元组，但是后果很严重。。。
#
	tuple6 = (1, 2, 3)
	del tuple6
	print(tuple6)
运行输出结果：
#
	Traceback (most recent call last):
	  File "/Day06/Tuple_Demo01.py", line 61, in <module>
	    print(tuple6)
	NameError: name 'tuple6' is not defined
>元组被删除的很彻底,直接从内存中抹去了

	* 试一试：del tuple6[1]运行输出什么结果


* 元组相加
#
	# 元组相加
	tuple1 = (1, 2, 3)
	tuple2 = (4, 5, 6)
	tuple3 = tuple1 + tuple2
	print(tuple3)
	print(type(tuple3))
	print(tuple1)
	print(tuple2)
运行输出结果：
#
	(1, 2, 3, 4, 5, 6)
	<class 'tuple'>
	(1, 2, 3)
	(4, 5, 6)


* 判断元组是否存在XX元素
	* 使用in,not in可以判断某个元素是否在目标元组
#
	# in, not in
	tuple4 = (1, 2, 3)
	print(3 in tuple4)
	print(3 not in tuple4)
	print(tuple_demo009.index("c"))
	print(tuple_demo009.count("c"))
运行输出结果：
#
	True
	False
>对比一下列表的in,not in


* 截取元组内容
	* 格式: 元组名[开始 : 结束 ：步长]（含头不含尾）
	* 案例：
#
	# 截取元组内容
	tuple6 = (1, 2, 3, 4, 5, 6, 7, 8)
	print(tuple6[:])
	print(tuple6[3:7])
	print(tuple6[3:])
	print(tuple6[:7])
	print(tuple6[:-1])
	print(tuple6[-1::-1])
运行输出结果：
#
	(1, 2, 3, 4, 5, 6, 7, 8)
	(4, 5, 6, 7)
	(4, 5, 6, 7, 8)
	(1, 2, 3, 4, 5, 6, 7)
	(1, 2, 3, 4, 5, 6, 7)
	(8, 7, 6, 5, 4, 3, 2, 1)


* 元组嵌套
 	* 元组的嵌套(二维元组),元素是一维元组
	* 格式:元组名 = ((),(),().....)
	* 案例：
#
	# 元组嵌套
	tuple7 = ((1, 2, 3), (4, 5, 6), (True, False))
	print(tuple7[1][1])
	for tuple0 in tuple7:
	    for num in tuple0:
	        print(num, end=",")
	    print()
运行输出结果：
#	
	5
	1,2,3,
	4,5,6,
	True,False,


## 05.08_Python语言基础(字典概述)(掌握)
* 字典概述
#
想一想：

    如果有列表如下：
         nameList = ['xiaoZhang', 'xiaoWang', 'xiaoLi'];

    需要对"xiaoWang"这个名字写错了，通过代码修改：
         nameList[1] = 'xiaoxiaoWang'

    如果列表的顺序发生了变化，如下
         nameList = ['xiaoWang', 'xiaoZhang',  'xiaoLi'];

    此时就需要修改下标，才能完成名字的修改
         nameList[0] = 'xiaoxiaoWang'

>**有没有方法，既能存储多个数据，还能在访问元素的很方便就能够定位到需要的那个元素呢？**

### 》》》字典能很好的解决这种问题，你印象中的字典是什么样的？
#
	》》》另一个场景：
	学生信息列表，每个学生信息包括学号、姓名、年龄等，如何从中找到某个学生的信息？
	>>> studens = [[1001, "王宝强", 24], [1002, "马蓉", 23], [1005, "宋喆"，24], ...]


* 字典格式
	* 格式：{key1 : value1, key2 : value2, key3 : value3, ....}


* 创建字典
	* 定义一个变量info为字典类型
#
	info = {"name" : "zhangsan", "id" : 1234, "address" : "北京"}


* 说明：
	* 字典和列表相似，存储多种数据
	* 字典中找元素，根据名字（就是:前面的那个值--》key）
	* 字典中的每一个元素分为两个部分，键   值
   	* 例如：
      name   --------->   key
      zhangsan    ----->  value


## 05.09_Python语言基础(字典常用操作)(掌握)
* 添加字典内容
	* 变量名["键"] = 数据时,如果该键在字典中不存在,会自动创建
#
	# 字典添加元素
	info = {"id": 100, "address": "北京", "name": "zhangsan"}
	print("添加元素前的字典info:", info)
	info["phoneNum"] = 10086
	print("添加元素后的字典info:", info)
运行输出结果：
#
	添加元素前的字典info: {'id': 100, 'address': '北京', 'name': 'zhangsan'}
	添加元素后的字典info: {'id': 100, 'address': '北京', 'name': 'zhangsan', 'phoneNum': 10086}


* 修改字典内容
	* 变量名["键"] = 数据时,如果该键在字典中存在,会改变原值
	* 变量名["键"] = 数据时,如果该键在字典中不存在,会自动创建
#
	info = {"id": 100, "address": "北京", "name": "zhangsan"}
	print("修改前的字典info:", info)
	# 格式:
	# 变量名["键"] = 数据时,如果该键在字典中存在,会改变原值
	# 变量名["键"] = 数据时,如果该键在字典中不存在,会自动创建
	newAddr = input("请输入您所在的城市:")
	info["address"] = newAddr
	newAge = int(input("请输入您的年龄:"))
	info["age"] = newAge
	print("修改后的字典info:", info)
运行输出结果：
#
	修改前的字典info: {'id': 100, 'address': '北京', 'name': 'zhangsan'}
	请输入您所在的城市:上海
	请输入您的年龄:18
	修改后的字典info: {'id': 100, 'address': '上海', 'name': 'zhangsan', 'age': 18}


* 删除字典元素
	* del  :删除指定的元素
	* clear()：清空字典
	* 案例：
del案例
#
	# 删除字典元素
	info = {"id": 100, "address": "北京", "name": "zhangsan"}
	print("删除元素前的字典info:", info)
	del info["address"]
	print("删除元素后的字典info:", info)
运行输出结果：
#
	删除元素前的字典info: {'id': 100, 'address': '北京', 'name': 'zhangsan'}
	删除元素后的字典info: {'id': 100, 'name': 'zhangsan'}


clear()案例
#
	# clear()
	print("clear()前的字典info:", info)
	info.clear()
	print("clear()后的字典info:", info)
运行输出结果：
#
	clear()前的字典info: {'id': 100, 'name': 'zhangsan'}
	clear()后的字典info: {}
>使用clear()会把字典清空，不会把字典从内存中抹去


* 查看字典元素
	* get()函数：在我们不确定字典中是否存在某一个键而又想获取它的值，可以使用get(),可以设置默认值
	* 案例：
#
	# get()函数
	info = {"id": 100, "address": "北京", "name": "zhangsan"}
	age = info.get("age")  # age键不存在,所以age的值为None
	print(age)
	# 如果info中不存在age,设置默认值
	age = info.get("age", 18)
	print(age)
运行输出结果：
#
	None
	18


## 05.10_Python语言基础(字典常用函数)(掌握)
* 字典长度
	* len(dict)
* 获取所有的键key
	* dict.keys()
* 获取所有的值value
	* dict.values() 
* 获取所有的键值对
	* dict.items()
* 遍历字典
	* 使用for循环可以搞定
* 案例：
# 
	# 字典常用函数
	info = {"id": 100, "address": "北京", "name": "zhangsan"}
	# len()
	len0 = len(info)
	print("字典info的长度是：", len0)
	# keys()
	keys = info.keys()
	print("字典info的键集合是：", keys)
	# values()
	values = info.values()
	print("字典info的值集合是：", values)
	# items()
	items = info.items()
	print("字典info的键值对集合是：", items)
运行输出结果：
#
	字典info的长度是： 3
	字典info的键集合是： dict_keys(['id', 'address', 'name'])
	字典info的值集合是： dict_values([100, '北京', 'zhangsan'])
	字典info的键值对集合是： dict_items([('id', 100), ('address', '北京'), ('name', 'zhangsan')])

字典的遍历：
#
	# 字典的遍历
	# 遍历字典中的key
	info = {"id": "100", "address": "北京", "name": "zhangsan"}
	print("--------遍历字典中的key--------")
	b = info.keys()
	print(type(b))
	for key in b:
	    print(key, end=",")
	
	print("\n--------遍历字典中的value--------")
	# 遍历字典获取字典中所有的值
	c = info.values()
	for value in c:
	    print(value, end=",")
	
	print("\n--------遍历字典中的键值对--------")
	# 获取键值对
	itmes = info.items()
	for itme in itmes:
	    print(itme)
	print("\n--------遍历字典中的键值对改良版--------")
	# 改进
	for key, value in itmes:
	    print("key = %s,value = %s" % (key, value))
运行输出结果：
#
	--------字典的遍历--------
	--------遍历字典中的key--------
	<class 'dict_keys'>
	id,address,name,
	--------遍历字典中的value--------
	100,北京,zhangsan,
	--------遍历字典中的键值对--------
	('id', '100')
	('address', '北京')
	('name', 'zhangsan')
	key = id,value = 100
	key = address,value = 北京
	key = name,value = zhangsan

>想一想，如何实现带下标索引的遍历
第一种方式：输出时直接加上
#
	chars = ['a', 'b', 'c', 'd']
	i = 0
	for chr in chars:
	     print("%d %s"%(i, chr))
	     i += 1
	运行输出结果：
	0 a
	1 b
	2 c
	3 d
* 第二种方式：使用enumerate()解决
#
	print("第二种方式：")
	for i, c in enumerate(chars):
	    print(i, c)
	运行输出结果：
	0 a
	1 b
	2 c
	3 d

## 05.11_Python语言基础(字典和列表优缺点比较)(掌握)
* 字典和列表比较：
	* 优点
		* 字典查找和插入的速度较快，不会随着key-value的增加而变慢
		* 列表需要从头遍历，列表的顺序变化后查找参数也要改变
	* 缺点
		* 字典需要占用较大的内存
		* 列表结构比较简单，占用内存比较小

## 05.12_Python语言基础(集合概述)(掌握)
* 集合与之前的列表和元组类似，可以存储多个类型数据，这些数据不能重复
	* 理解
		* 相对于字典，是一组key,没有value
	* 本质：
		* 无序，无重复元素元素的集合
		* 集合的对象支持union(联合)，intersection(交)，difference(差)，system-difference(系统差集)等运算
	* 特点：
		* 不能存储重复元素

## 05.13_Python语言基础(集合的格式和创建)(掌握)
* 创建集合：
	* 集合的创建 ,需要列表、元组、字典等可迭代类型作为元素输入集合
	* 重复的元素在集合中会被自动过滤掉
	* set = {}，print(type(set))运行得到的结果不是集合
	* set = set()
	
创建集合案例：
#
	set01 = set([1, 6, 9, 3, 6])
	set02 = set({"id": "100", "address": "北京", "name": "zhangsan"})
	set03 = {}		# 创建的不是集合，是字典
	set04 = set("abcde")
	print(set01)
	print(set02)
	print(set03)
	print(set04)
	print(type(set03))
	print(type(set04))
运行输出结果：
#
	{1, 3, 6, 9}
	{'name', 'id', 'address'}
	{}
	{'e', 'a', 'c', 'd', 'b'}
	<class 'dict'>
	<class 'set'>



## 05.14_Python语言基础(集合的常用操作)(掌握)
* 向集合添加元素
	* 集合添加元素使用add()
	* 格式：set.add(obj)

集合添加数据案例：
#
	# 集合添加元素
	print("---------add---------")
	# 添加add
	s1 = set([1, 2, 3, 4, 5])
	s1.add(6)
	print(s1)
	s1.add(3)  # 添加重复的元素,没有效果
	print(s1)
运行输出结果：
#
	---------add---------
	{1, 2, 3, 4, 5, 6}
	{1, 2, 3, 4, 5, 6}
>向集合内添加重复元素不报错，也没作用

读一下代码，说出运行结果：
#
	s1.add([7, 8, 9])  		# set的元素不能是列表,列表是可变的
	print(s1)
	s1.add({1: "haha"})  	# set的元素不能是字典,字典也是可变的
	print(s1)
	s1.add(7, 8, 9)  		# set的元素不能连续添加
	print(s1)
	s1.add((7, 8, 9))  		# set的元素可以是字典,字典也是不可变的
	print(s1)

* 集合更新update()
	* 插入(更新)update()
	* 可以插入list/tuple/String打碎插入(无序,去重)
	
update()案例：
#
	# 插入(更新)update()
	# 可以插入list/tuple/String打碎插入(无序,去重)
	print("----------Update()----------")
	s2 = set([1, 2, 3])
	s2.update([4, 5, 6])
	print(s2)
	
	s2.update((9, 10))
	print(s2)
	s2.update("haha")
	print(s2)
	s2.update("哈哈")
	print(s2)
运行输出结果：
#
	----------Update()----------
	{1, 2, 3, 4, 5, 6}
	{1, 2, 3, 4, 5, 6, 9, 10}
	{'h', 1, 2, 3, 4, 5, 6, 9, 10, 'a'}
	{'h', 1, 2, 3, 4, 5, 6, 9, 10, '哈', 'a'}

>可迭代元素被打碎放入集合，
>重复元素会被消除，
>更新后的集合无序


* 删除集合元素
	* 删除集合元素使用remove(object)

删除元素案例：
#
	# 删除集合元素
	print("------remove------")
	# 删除remove()
	s3 = set([1, 2, 3, 4, 5])
	s3.remove(4)  # 删除是具体的元素
	print(s3)
	s3.remove(9)  # 这个元素是不存在的
	print(s3)
运行输出结果：
#
	------remove------
	{1, 2, 3, 4, 5}
	{1, 2, 3, 5}
	
删除不存在元素：
#
	# 删除集合元素
	print("------remove------")
	# 删除remove()
	s3 = set([1, 2, 3, 4, 5])
	s3.remove(9)  # 这个元素是不存在的
	print(s3)
运行输出结果：
#
	Traceback (most recent call last):
	File "/Day06/Set_Demo01.py", line 58, in <module>
	s3.remove(9)  # 这个元素是不存在的
	KeyError: 9


* 遍历集合
	* 集合是可迭代类型数据
	* 使用for循环可以遍历集合
	* set集合没有索引，无法使用while进行遍历
	* 如果想要得到索引和对应的值,使用enumerate


遍历集合案例：
#
	# 遍历集合
	print("---------for循环遍历集合——----")
	s4 = set([1, 2, 3, 4, 5])
	for i in s4:
	    print(i, end=",")

	print("-------带索引的遍历方式-------")
	s5 = set("床前明月光")
	for index, i in enumerate(s5):
	    print(index, i)
运行输出结果：
#	
	1,2,3,4,5,
	-------带索引的遍历方式-------
	0 前
	1 床
	2 月
	3 光
	4 明


* 集合的交集和并集
	* 交集：返回两个集合相同的元素，返回数据类型是集合
	* 并集：返回两个集合内多有的元素并去除重复，返回数据类型是集合

交集和并集案例：
#
	print("--------交集-------")
	# 交集，使用运算符	"&"
	s5 = set([1, 2, 3])
	s6 = set([4, 5, 6, 2, 3])
	# 交集  &
	s7 = s5 & s6
	print(s7)
	
	print("--------并集-------")
	# 并集，使用运算符	"|"
	s8 = s5 | s6
	print(s8)
	print(type(s8))
运行输出结果：
#
	--------交集-------
	{2, 3}
	--------并集-------
	{1, 2, 3, 4, 5, 6}
	<class 'set'>



## 05.15_Python语言基础(生成器)(熟练)
* Python的生成器是一个返回可以迭代对象的函数。
* 先看案例：
创建一个列表，元素为0--20以内的偶数
#
	list01 = [2, 4, 6, 8, 10, 12, 14, 16, 18]
	list02 = [x * 2 for x in range(1, 10)]
	Generator01 = (x * 2 for x in range(1, 10))
	print(list01)
	print(list02)
	print(Generator01)
	for i in Generator01:
	    print(i, end=",")
运行输出结果：
#
	[2, 4, 6, 8, 10, 12, 14, 16, 18]
	[2, 4, 6, 8, 10, 12, 14, 16, 18]
	<generator object <genexpr> at 0x0000014043D37200>
	2,4,6,8,10,12,14,16,18,

* 创建生成器的方式有多种，只要把一个列表生成式的[]改成()
* 创建list和Generator区别在于外层[],(),list表示一个列表，Generator表示生成器
* 遍历生成器内容：
	* next()
	* for循环
	
next()读取生成器内容
#
	# next
	# 定义一个生成器
	Generator = (x * 2 for x in range(5))
	temp = next(Generator)
	print(temp)
	temp = next(Generator)
	print(temp)
	temp = next(Generator)
	print(temp)
	temp = next(Generator)
	print(temp)
	temp = next(Generator)
	print(temp)
	
	temp = next(Generator)# 注意:如果一直写next()函数,当超出了元素的个数范围的时候会直接报错
	print(temp)
运行输出结果：
#
	0
	2
	4
	6
	8
	Traceback (most recent call last):
	  File "/Day06/Generator_Demo01.py", line 24, in <module>
    temp = next(Generator)
	StopIteration

for循环遍历生成器内容：
#
	# 循环遍历
	Generator = (x*2 for x in range(5))
	for temp in Generator:
	    print(temp)
运行输出结果：
#
	0
	2
	4
	6
	8
>读取到最后一个元素自动结束，不会报错

#
	总结:
	生成器保存的是一个算法,每次调用next()函数,就能计算出生成器下一个元素的值,直到最后一个元素，
	如果超出了元素的最大长度范围,报错,
	通过for循环来迭代他,并且不用关心超出界限的问题



## 05.16_Python语言基础(函数实现生成器)(熟悉)
* 函数来实现生成器(函数后面学习)
#
	函数的定义:
	格式: def 函数名():
		方法体语句

	函数的调用:函数名()

* 练习:菲波拉锲数列
#
	1 1 2 3 5 8 13    除第一个和第二个外,任意的数都是由前两个数相加得到

	a = 0
	b = 0
	c = 1
	while a < 5:
	    temp = c
	    c = b + c
	    b = temp
     	a += 1
	    print(b)


* 函数（方式一）
#
	def fib1():
	    a = 0
	    b = 0
	    c = 1
	    while a < 5:
	        temp = c
	        c = b + c
	        b = temp
	        a += 1
	        print(b)
	fib1()


* 函数（方式二）
#
	def fib2():
    	a = 0
    	b,c = 0,1
    	while a < 5:
	        print(c)
	        b, c = c , b + c
	        # b = c
	        # c = b + c
	        a += 1

	fib2()
解释一下代码：
#
	a = 0
	b = 1
	a,b = b, a + b
	相当于
	temp = b
	b = a + b
	a = temp
	
	或者:
	   a, b = b , a + b 


## 05.17_Python语言基础(生成器--yield)(熟悉)
* 先看代码：
#
	print("-----fib3()---------")
	def fib3():
	    a = 0
	    b, c = 0, 1
	    while a < 5:
	        # print(c)
	        yield c
	        b, c = c, b + c
	        a += 1

	f = fib3()#生成器
	print(f)
	print(next(f))
	print(next(f))
	print(next(f))
	print(next(f))
	print(next(f))
运行输出结果：
#
	-----fib3()---------
	<generator object fib3 at 0x000002352A007360>
	1
	1
	2
	3
	5
* yield是一个类似return的关键字,迭代一次遇到yield的时候返回(右侧,后面的值)
* 重点:
	* 下一次迭代时,从上一次迭代遇到yield后面的代码(下一行)开始执行
		* return返回一个值,并且记住返回值的位置,
    	* 下次迭代的时候就从这个记录的位置开始
	* 输出时注意调用next()的次数，超出内容会报错



## 05.18_Python语言基础(迭代器概述)(掌握)
* 迭代：
   * 迭代是重复反馈过程的活动，其目的通常是为了逼近所需目标或结果。
   * 每一次对过程的重复称为一次“迭代”，而每一次迭代得到的结果会作为下一次迭代的初始值。
   * 计算机中的迭代：对计算机特定程序中需要反复执行的子程序*(一组指令)，进行一次重复，即重复执行程序中的循环，直到满足某条件为止，亦称为迭代
   * Python中的迭代是访问集合元素的一种方式
* 迭代器：
   * 可以被next()函数调用并且不断的返回下一个值的对象(迭代器 Iterator)
* 迭代对象：
   * 是一个可以记住遍历位置的对象
   * 迭代器对象从集合的第一个元素开始访问，直到所有的元素访问完毕为止
* 迭代器的特点：
  * 只能往前，不会后退


## 05.19_Python语言基础(可迭代对象)(掌握)
* 直接可用for循环遍历的数据类型有哪些？
	* 一类：list  tuple  dict  set  str
	* 一类：生成器
* 这些可以直接作用与for循环的对象的统称----》可迭代对象（Iterable）
* **怎么判断是否可以迭代？**
	* 可以使用isinstance()来判断一个对象是否是Iterable，返回值是True或者False
	* 需要使用一个模块collections

#
	from collections import Iterable
	a = isinstance([],Iterable)
	b = isinstance((),Iterable)
	c = isinstance({},Iterable)
	d = isinstance("aaaa",Iterable)
	e = isinstance(1000,Iterable)#false
	f = isinstance((x for x in range(5)),Iterable)
	print(a)
	print(b)
	print(c)
	print(d)
	print(e)
	print(f)
运行输出结果：
#
	True
	True
	True
	True
	False
	True


## 05.20_Python语言基础(迭代器)(掌握)
* 迭代器：
   * 可以被next()函数调用并且不断的返回下一个值的对象(迭代器 Iterator)
* 判断一个元素是不是迭代器：isinstance（ocject, Iterator）
#
	print("--------Iterator---------")
	from collections import Iterator
	
	a = isinstance([], Iterator)
	b = isinstance((), Iterator)
	c = isinstance({}, Iterator)
	d = isinstance("aaaa", Iterator)
	e = isinstance(1000, Iterator)
	f = isinstance((x for x in range(5)), Iterator)
	print(a)
	print(b)
	print(c)
	print(d)
	print(e)
	print(f)

	运行输出结果：
	
	--------Iterator---------
	False
	False
	False
	False
	False
	True

#
	Python中 list、truple、str、dict这些都可以被迭代，但他们并不是迭代器。为什么？

	因为和迭代器相比有一个很大的不同，list、truple、map、dict这些数据的大小是确定的，
	也就是说有多少事可知的。
	但迭代器不是，迭代器不知道要执行多少次，所以可以理解为不知道有多少个元素，
	每调用一次next()，就会往下走一步，是惰性的。

	判断是不是可以迭代，用Iterable
	判断是不是迭代器，用Iterator

	所以，
	凡是可以for循环的，都是Iterable
	凡是可以next()的，都是Iterator

	集合数据类型如list、truple、dict、str都是Itrable不是Iterator，
	但可以通过iter()函数获得一个Iterator对象

	Python中的for循环就是通过next实现的
 


## 05.21_Python语言基础(Iter()函数)(掌握)
* 生成器都是Iterator对象，但是list、dict、str都是迭代对象但是不是迭代器
* 使用iter()函数可以把这些可迭代对象转换为迭代器
案例代码：
#
	print("-----------Iter()-------------")
	from collections import Iterator
	
	words = [1, 5, 8, 3, 5]
	a = isinstance(iter(words), Iterator)
	b = isinstance(iter(()), Iterator)
	c = isinstance(iter({}), Iterator)
	d = isinstance(iter("hhaha"), Iterator)
	f = isinstance((x for x in range(5)), Iterator)
	print(a)
	print(b)
	print(c)
	print(d)
	print(f)
	
	words = iter(words)
	print(next(iter(words)))
	print(next(iter(words)))
	print(next(iter(words)))
运行输出结果：
#
	-----------Iter()-------------
	True
	True
	True
	True
	True
	1
	5
	8



## 05.22_Python语言基础(迭代器总结)(掌握)
#
	1.凡是可以作用与for循环对象都是Iterable类型
	2.可以作用与next()函数的对象都是Iterator类型
	3.集合数据类型list、tuple、dict、str等是Iterable但不是Iterator
	4.集合数据类型list、tuple、dict、str等通过iter()可以将其转换为Iterator