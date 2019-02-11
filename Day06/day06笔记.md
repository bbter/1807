## 06.01_Python语言基础(函数概述)(掌握)
#
	例如：
	   现在有一段代码：
	   print("天王盖地虎")
	   print("小鸡炖蘑菇")
	   
	 在来一段：
	    if 条件1：
	       print("天王盖地虎")
	    elif 条件2：
	       print("小鸡炖蘑菇")
	    elif 条件3：
	       print("天王盖地虎")
	       print("小鸡炖蘑菇")
   
>总结：
    如果在开发的时候，需要某段代码多次执行，但是为提高代码的编写效率和代码的重用，所以把具有独立功能的代码块组织为一个小模块,这样的模块我们成为：函数
 
* 查一查：函数在数学中的定义是什么？



## 06.02_Python语言基础(函数的定义和调用)(掌握)

* 函数的定义
#
	函数定义的格式：
	   def 函数名():
	   	    代码
	例如：
	 #函数的定义
	def printInfo():
	    print("----------")
	    print("人生苦短,我用python")
	    print("----------")


* 函数的调用
#
	格式：
	   函数名()
	printInfo()


* 做一做：定义函数，能够完成输入、输出自己的姓名和年龄，并让函数执行
#
	# 使用def定义函数
	# 编写完函数后需要调用，通过函数名()进行调用
	# 定义函数
	def info():
	    name = input("请输入你的姓名:")
	    age = input("请输入您的年龄:")
	    print("您的姓名为:%s,年龄:%s"%(name,age))
	
	#调用函数
	info()



## 06.03_Python语言基础(函数的参数)(掌握)

* 定义带有参数的函数
#
	# 定义函数
	def addnum():
	    a = 33
	    b = 22
	    c = a + b
	    print(c)
	# 调用函数
	addnum()
	
	# 定义函数
	def add2Num(a,b):#形参
	    c = a + b
	    print(c)
	# 调用函数
	add2Num(11,22)#实参


>做一做：定义一个函数，完成前两个数的加法运算，在对第三个数进行减法，调用该函数，完成计算并打印结果？
#
	def add(a,b,c):
	    d = a + b
	    e = d - c
	    print(e)
	
	add(10,20,30)



## 06.04_Python语言基础(调用函数注意事项)(掌握)
* 形参和实参必须一一对应
* 函数调用时参数的顺序
#
	def test(a,b):
	    print(a,b)
	test(1,2)
	test(b = 1, a = 2)



## 06.05_Python语言基础(参数总结)(掌握)
* 形参：定义时小括号中的参数，用来接受参数
* 实参：调用时小括号中的参数，用来传递给函数使用

>做一做：模拟一个简单的两位数的计算器，功能（加减乘除）

#
	#定义一个函数,完成计算器的加法运算
	def add(a,b):
	    c = a + b
	    print(c)
	
	
	# 定义一个函数,完成计算器的减法运算
	def minus(a, b):
	    c = a - b
	    print(c)
	
	
	# 定义一个函数,完成计算器的乘法运算
	def cheng(a, b):
	    c = a + b
	    # print(c)
	
	
	# 定义一个函数,完成计算器的除法运算
	def chu(c, d):
	    c = c / d
	    print(c)

	add(1,2)
	minus(2,1)
	cheng(1,2)
	chu(1,2)



## 06.06_Python语言基础(函数的返回值)(掌握)

*  函数的返回值概述
	* 定义： 返回值：就是程序中函数完成一件事后将结果返回给调用者


* 带有返回值的函数
#
	#定义函数
	def add2num(a,b):
	    c = a + b
	    return c
	    #或者
	    # return a + b
	
	sum = add2num(1,2)
	print(sum)


* 保存带有返回值的函数
#
	#定义函数
	def add2num(a,b):
	    c = a + b
	    return c
	    #或者
	    # return a + b
	
	sum = add2num(1,2)
	print(sum)


* 函数的类型

## 06.07_Python语言基础(函数的类型)(掌握)
#
	函数根据有没有参数，有没有返回值，可以相互组合，一共有4中
	无参数，无返回值
	无参数，有返回值
	有参数，无返回值
	有参数，有返回值



### A: 无参数，无返回值
此类函数，不能接受参数，也没有返回值，一般情况下，打印提示灯类似的功能，使用该类函数
#
	#无参数,无返回值
	def printInfo():
	    print("------------")
	    print("人生苦短,我用python")
	    print("-----------")
	
	printInfo()



### B: 无参数，有返回值
此类函数，不能接受参数，但是可以返回某个数据，一般情况，像数据采集，
#
	#无参数,有返回值
	def getTemp():
	    return 24
	
	temp = getTemp()
	print("当前的温度为:%d"%temp)



### C:  有参数，无返回值
此类函数可以接受参数，但是不可以返回数据，一般情况适用于变量设置数据，而不需要结果
#
	#有参数,无返回值
	def add2num(a,b):
	    result = a + b
	    print(result)
	
	add2num(11,22)


### D: 有参数，有返回值
此类函数，不仅接受参数，同时可以返回某个数据，
#
	"""
	1.是否需要传参
	    是   
	         需要传几个
	                传一个        
	2.是否需要返回
	    有     return   将数据返回,二次处理
	    没有  

	"""
	def calculateNum(num):
	    i = 0
	    sum = 0
	    while i <= num:
	        sum += i
	        i += 1
	    return sum

	result = calculateNum(100)
	calculateNum(200)
	print(result)

案例2：
#
	#定义一个函数
	def get_wendu(a):
	    wendu = 22
	    print("当前的温度为:%d"%wendu)
	    return wendu
	def get_wendu_huashi(wendu):
	    print("======4========")
	    wendu = wendu + 3
	    print("=====5=====")
	    print("当前的温度为:%d"%wendu)
	    print("======6======")
	print("====1======")
	result = get_wendu(1000)
	print("=======2=======")
	get_wendu_huashi(result)
	print("=======3======")


### 总结
* 函数是否有参数和返回值，决定函数的格式（4种）



## 06.08_Python语言基础(函数的嵌套调用)(掌握)

* 概述：
    * 函数的嵌套调用:	一个函数中又调用了另外一个函数

示例：
#
	def testB():
	    print("----testB-----")
	
	def testA():
	    print("-----testA-----")
	    testB()
	    
	testA()


#### 想一想：
#
	案例1：
	   1.写一个函数打印一条横线（20个“-”）
	   2.打印自定义行数的横线
	
	分析：
	    是否参数
	         需要	传递一个参数   确定“-”号的个数
	         不需要   
	    是否返回值
	         需要	返回给调用者
	         不需要    
	
	 内容：
	    打印一条横线
	         有参   无返回 
	            def test(n):
	                print(n*"-")
	                
	         有参   有返回
	               def test(n):
	                    return n * "-"
	                    
	         无参  无返回
	              def test():
	                   print(20*"-")
	                   
	         无参 有返回
	               def test():
	                   retrun "-" * 20


代码：
#
	# n:确定-号的个数
	#打印一行-号
	def printOneLine(n):
	    print(n * "-")
	
	# 打印多条横线
	def printNumLine(num):
	    i = 0 
	    while i < num:
	        printOneLine(20)
	        i += 1
	
	# 调用函数
	printOneLine(20)
	printNumLine(3)


案例2:



#
	代码思路：
      参数
          需要   三个
      
      返回值
         需要


实现代码：
#
	def sum3Number(a,b,c):
	    return a + b + c
	
	sum = sum3Number(1,2,3)
	print(sum)
	
	#定义一个函数,完成3个数的平均值
	def average3Number(aaa):
	    averageResult = sum / 3.0
	    return averageResult
	
	ave = average3Number(sum)
	print(ave)