## 03.01_Python语言基础(循环语句)(掌握)
* 循环语句的介绍
	* 生活中的场景：
		* 跑道
		* 风扇
		* cf中的加特林
		
##### 软件开发中的使用场景：
	# 跟媳妇表白，说一万遍“我想你”
		print("我想你。。。。")
		print("我想你。。。。")
		print("我想你。。。。")
		print("我想你。。。。")
	# 使用循环语句：
		i = 0   
		while i < 1000 :
			print("媳妇，我想你")
			i += 1
	     
>总结：<br/>
   一般情况下，需要多次重复执行的代码，都可以使用循环的方式来完成<br/>
   循环不是必须的，但是为了提高代码的执行效率，在开发时采用循环
***










## 03.02_Python语言基础(while概述)(掌握)
##### while循环的格式
	格式：
	while 条件:
	     条件满足，做事情1
	     条件满足，做事情2
	     条件满足，做事情3
	     .....
	案例：
	i = 0
	while i < 5:
	    print("当前的是第%d次执行循环"%(i))
	    i += 1





## 03.03_Python语言基础(while循环的应用)(掌握)
	while使用案例：
	案例1：
	   计算1~100之间的累计和（包含1和100）
	案例2：
	   计算1~100之间偶数的累计和（包含1和100）
	"""
	#定义一个起始的变量
	i = 1
	sum = 0
	while i <= 100:
	    sum = sum + i
	    i += 1
	print(sum)
	
	#定义一个起始的变量
	j = 1
	sum = 0
	while j <= 100:
	    if j % 2 == 0:
	        sum = sum + j
	    j += 1
	print("1~100之间的偶数和为%d"%sum)






## 03.04_Python语言基础(while...else)(掌握)
	格式：
	while 判断表达式：
	     语句1
	else:
	     语句2
	逻辑：
	   在条件语句（判断表达式）为false，执行else中的语句2
   


	#定义一个起始变量
	a = 1
	#使用循环语句
	while a <= 3:
	    print("haha")
	    a += 1
	else:
	    print("heihei")
	
	print("完了")





## 03.05_Python语言基础(while循环的嵌套)(掌握)
	while循环，while里面嵌套一个while
	格式：
	    while 条件1：
	          条件1满足，做事情1
	          条件1满足，做事情2
	          条件1满足，做事情3
	          .....
	          while 条件2：
	               条件2满足，做事情1
	               条件2满足，做事情2
	               条件2满足，做事情3

	# while循环嵌套的应用
	案例1.打印一个矩形
	    ******
	    ******
	    ******
    	******
	#定义一个起始变量
	i = 1
	#定义外层循环来控制行数
	while i <= 4:
	    #定义起始变量
	    j = 1
	    #定义内层循环
	    while j <= 6:
	        print("*",end="")
	        j += 1
	    print("")
	    i += 1



	案例2:打印等腰三角
    *
    *  *
    *  *  *
    *  *  *  *
    *  *  *  *  *
	i = 1
	while i <= 5:
	    j = 1
	    while j <= i:
	        print("*",end=" ")
	        j += 1
	    print("\n")
	    i += 1

	案例3：打印9*9  乘法表
	1 * 1 = 1
	1 * 2 = 2  2 * 2 = 4
	1 * 3 = 3  2 * 3 = 6  3 * 3 = 9
	。。。 。。。

	#定义一个起始变量
	i = 1
	#定义while循环，控制行数
	while i <= 9:
	    j = 1
	    while j <= i:
	        print("%d * %d = %d"%(j,i,i*j),end=" ")
	        j += 1
	    print("\n")
	    i += 1
	-------------
	这个图形应该怎么实现呢？
	*
	* *
	* * *
	* * * *
	* * *
	* *
	*



## 03.06_Python语言基础(for循环概述)(掌握)
	#像while循环一样，for循环可以完成循环的功能
	#完成遍历任何序列的项目，String
	"""
	for 循环的基本格式：
		for 临时变量 in 列表或者字符串等:
			循环满足条件时执行的代码
		else:
			循环条件呢不满足，执行代码
	"""
	# for循环使用案例：
	案例1：
	    循环得到一个字符串中的每一个字符
	    name = "xiaoming"
	    # name = "xiaoming"
		for temp in name:
			print(temp)
	
	#案例2：循环得到一个空字符串
		name = ""
		for temp in name:
		    print(temp)
		else:
		    print("没有数据")


	
## 03.07_Python语言基础(range()函数)(掌握)
	range()函数的作用
	作用：创建一个整数列表，一般在for循环中使用
	基本语法：
	    range(start,stop,step)
	参数说明：
		start :   计数从start开始，默认从0开始，
					例如：range(5)等价与range(0,5)<左闭右开型>
		stop  :   计数到stop结束，但是不包括stop例如range(0,5)  [0,1,2,3,4]
		step  :   步长  默认是1，例如range(0,5)等价与：range(0,5,1)
	print(list(range(1, 4)))
	[1,2,3]


## 03.08_Python语言基础(for循环的嵌套)(掌握)
	和while一样，for循环也可以嵌套执行
	格式：
	   for 临时变量 in 列表或者字符串等:
	        for 临时变量 in 列表或者字符串等:
	              执行代码
	案例1：
	   打印5*5的星号的矩形
		for x in range(5):
			for y in range(5):
				print("*",end="")
		    print("")
    
	案例2：
	   使用for循环完成9*9乘法表
	for x in range(1,10,1):
	    for y in range(1,x+1,1):
	        print("%d * %d = %d"%(y,x,x*y),end="\t")
	    print("")


##### 扩展：
	enumrate()函数，同时遍历下标和元素
	name = "xiaoming"
	for temp in name:
	    print(temp)
	
	for i in range(len(name)):  		# len()表示获取序列的最大长度
	    print(i + 1, name[i])
	
	for i, item in enumerate(name, 1):  # 第二个参数表示索引起始的位置
	    print(i, item) 




## 03.09_Python语言基础(死循环)(掌握)
* 死循环：循环一直执行下去
* 死循环的危害：
	* 1.会造成cpu满负荷工作，会损坏硬件
    * 2.导致内存溢出
	* 格式：
   		* while True:
        	* 执行的代码
        	* 如何跳出来（结束死循环）
        



## 03.10_Python语言基础(break)(掌握)
#### for循环与break
	# 普通for循环
	name = "zhangsan"
	for temp in name:
		print(temp)
	# 运行的效果为字符串中的每一个字符
	
	# 加入break
	name = "zhangsan"
	for temp in name:
	    if temp == "g":
	        break
	    print(temp)


#### while循环与break
	# 普通while循环
	i = 0
	while i < 10:
	    i += 1
	    print("-------")
	    print(i)

	# 使用break
	i = 0
	while i < 10:
	    i += 1
	    print("-------")
	    if i == 5:
	        break
	    print(i)

>总结：<br/>
	break作用：用来结束整个循环
***

## 03.11_Python语言基础(continue)(掌握)
#### for循环与continue
	name = "qianfeng"
	for x in name:
	    print("-----千锋-----")
	    if x == "f":
	        continue
	    print(x)



##### while循环与continue
	i = 0
	while i < 10:
	    i += 1
	    print("--------")
	    if i == 5:
	        continue
	    print(i)

>总结:<br/>
	continue作用：用来结束本次循环，紧接着执行下一次循环
***

#### 注意点
	1.break和continue只能用于循环语句，除此之外不能单独使用
	2.break /continue  在嵌套循环中，只对最近的一层循环起作用


## 03.12_day01总结
* 把今天的知识点总结一遍。





