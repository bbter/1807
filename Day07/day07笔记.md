## 07.01_Python语言基础(函数的参数的传递)(掌握)

> 具体的细分：
    可变对象和不可变对象（值传递，引用传递）

### A: 不可变对象参数的传递
* 不可变对象
	* 定义：表示该值不能发生变化
* 不可变的数据类型
 	* String  tuple  number(int,float,bool,complax)

#
	"""
	String
	tuple
	number
	"""
	def add(num):
	    num = num + 10
	    return num
	
	d = 2
	e = add(d)
	print(d)#2
	print(e)#12
	
	def fun(num):
	    print(id(num))
	    num = 10
	    print(id(num))
	temp = 20
	print(id(temp))
	fun(temp)
	print(temp)
	
	"""
> 总结：
  在python中，对于不可变对象，调用自身的任意函数，并不会改变对象自身的内容



### B: 可变对象

* 定义：
   * 值发生改变
* 可变对象的数据类型有哪些？   
   * list dict set

#   
	"""
	list
	dict
	set
	"""
	#以列表为例
	def change(num):
	    num.append(1)
	d = [0]
	
	change(d)
	print(d)
	
	def fun(list):
	    list[0] = 100
	
	li = [1,2,3,4,5]
	fun(li)
	print(li)
	
	
	a = 10
	b = 10
	b = 40
	print(id(a),id(b))
	
	c = 20
	d = 30
	print(id(c),id(d))
	
	d = c
	print(id(c),id(d))



> 总结：
  在python中，对于可变对象，调用自身的任意函数，可能改变对象自身的内容，id不会改变



## 07.02_Pythony语言基础(关键字参数)(掌握)
### Python允许函数调用时参数顺序和定义时不一致
#
	def myPrint(str,age):
	    print(str,age)
	
	myPrint("zhangsan","18")
	myPrint(age = 18,str = "张三")

#案例2：
#
   	#关键字参数: **kw
	def person(name,age,**kw):
	    print("name:",name,"age:",age,"other:",kw)
	
	person("zhangsan","12")
	person("zhangsan",12,city = "北京")
	person("张三",15,gender = "M",job = "engineer")
 

## 07.03_Pythony语言基础（默认参数/缺省参数)(掌握)
>概述：
    python为了简化函数的调用，提供默认参数机制，调用函数时，缺省参数的值如果没有传入，则会被认为是默认值
    
#
	#定义一个函数
	def printInfo(name,age = 35):
	    print("name:",name)
	    print("age:",age)
	
	printInfo("张三")
	printInfo(name = "张三")
	printInfo(age = 18,name = "haha")
	
	def pow(x ,n = 2):
	    r = 1
	    while n > 0:
	        r *= x
	        n -= 1
	    return r   
	
	p = pow(2)
	print(p)
	
	def printInfo1(name,sex = "nam",age = 35):
	    print(name,sex,age)
	    
	printInfo1("张三","男")

>注意：


    #带有默认值的参数一定要位于参数列表的最后面
    #必选参数必须在前面
    #设置何种参数为默认值，一般将参数值变化较小的设置为默认参数



## 07.04_Pythony语言基础（不定长参数)(掌握)
>概述：
   一个函数能够处理比当初声明时更多的参数称为不定长参数，声明时一般不会命名
* 格式：
	* def function(args,*args,**kwargs):

#
	def function(args,*args,**kwargs):
	加了一个*号的变量args会存放所有未命名的变量参数，相当于  元组
	加了**号，存放所有命名的变量参数，相当于表达式  key  =  value   kwargs为字典

#
	print("-" * 20)
	
	# 经典方式
	def fun(a, b, *args, **kwargs):
	    print("a= ", a)
	    print("b= ", b)
	    print("args= ", args)
	    print("kwargs= ", kwargs)
	    print("*" * 30)
	    for key, value in kwargs.items():
	        print(key, "=", value)
	
	
	fun(1, 2, 3, 4, 5, 6, 6, 8, 9, m=6, n=7, p=8)
	
	# 另一种方式
	c = (3, 4, 5)
	d = {"m": 6, "n": 7, "p": 8}
	print("_" * 50)
	fun(1, 2, *c, **d)
	print("_" * 50)
	# 再一种方式
	fun(1, 2, c, d)
	
	
	def fun1(*args, **kwargs):
	    print(args)
	    print(kwargs)
	
	# fun1(1, 2, 3, 4, m=5)
运行输出结果：
#
	--------------------
	a=  1
	b=  2
	args=  (3, 4, 5, 6, 6, 8, 9)
	kwargs=  {'m': 6, 'n': 7, 'p': 8}
	******************************
	m = 6
	n = 7
	p = 8
	__________________________________________________
	a=  1
	b=  2
	args=  (3, 4, 5)
	kwargs=  {'m': 6, 'n': 7, 'p': 8}
	******************************
	m = 6
	n = 7
	p = 8
	__________________________________________________
	a=  1
	b=  2
	args=  ((3, 4, 5), {'m': 6, 'n': 7, 'p': 8})
	kwargs=  {}
	******************************


## 07.05_Python语言基础（匿名函数)(掌握)
### 匿名函数概述
* 定义：
    * 不使用def这样关键字来定义函数
    * 使用lambda来创建一个匿名函数
* 原则：
    * 用lambda关键字能够创建小型匿名函数，可以省略用def声明函数的标准步骤
* 格式：
   * lambda[args1,args2....]:expression


 匿名函数的基本定义
#
	a = 1
	sum = lambda args1,args2:args1 + args2
	print(sum(10,20))

>特点：

#
	1.lambda只是一个表达式，比函数def声明简单
	2.lambda的主体也是一个表达式，而不是代码块，只能在lambda表达式中封装简单的逻辑
	3.lambda函数有总计的命名空间，能访问自由参数列表以外或者全局命名空间的参数
	4.lambda函数能够接受任何数量的参数，只能返回一个表达式的值



## 07.06_Pythony语言基础（匿名函数的应用场景)(掌握)
* 作为自定义函数的参数进行传递
	* 类似调用函数中传入的实参
* 匿名函数的应用场景（作为自定义函数的参数进行传递）
#
	def fun(a,b,opt):
	    print(a)
	    print(b)
	    print(opt(10,20))
	fun(1,2,lambda x,y:x + y)

* 作为内置函数的参数
	* 字典存储姓名和年龄的数据，把字典内的元素按照姓名或年龄排序
####
	stus = [
    {"name": "张三", "age": 18}, 
    {"name": "李四", "age": 35}, 
    {"name": "王五", "age": 22}]
	stus.sort(key=lambda x: x["age"])
	print(stus)


## 07.07_Pythony语言基础（装饰器的概述)(熟悉)
* 装饰器的基本格式
	* @函数名

* 定义：是一个闭包，把一个函数当作参数，
     * python装饰器就是用于拓展原来函数功能的一种函数，这个函数的特殊之处在于它的返回值也是一个函数，
     * 使用python装饰器的好处就是在不用更改原函数的代码前提下给函数增加新的功能。 
     * 一般而言，我们要想拓展原来函数代码，最直接的办法就是侵入代码里面修改，
<pre>
例如：
import time
def func():
    print("hello")
    time.sleep(1)
    print("world")

这是我们最原始的的一个函数，然后我们试图记录下这个函数执行的总时间，那最简单的做法就是：
#原始侵入，篡改原函数
import time
def func():
    startTime = time.time()

    print("hello")
    time.sleep(1)
    print("world")
    endTime = time.time()

    msecs = (endTime - startTime)*1000
    print("time is %d ms" %msecs)


但是如果你的Boss在公司里面和你说：“小祁，这段代码是我们公司的核心代码，
你不能直接去改我们的核心代码。”那该怎么办呢，我们仿照装饰器先自己试着写一下：
#避免直接侵入原函数修改，但是生效需要再次执行函数
import time

def deco(func):
    startTime = time.time()
    func()
    endTime = time.time()
    msecs = (endTime - startTime)*1000
    print("time is %d ms" %msecs)


def func():
    print("hello")
    time.sleep(1)
    print("world")

if __name__ == '__main__':
    f = func
    deco(f)#只有把func()或者f()作为参数执行，新加入功能才会生效
    print("f.__name__ is",f.__name__)#f的name就是func()
    print()
    #func()

这里我们定义了一个函数deco，它的参数是一个函数，然后给这个函数嵌入了计时功能。
然后你可以拍着胸脯对老板说，看吧，不用动你原来的代码，我照样拓展了它的函数功能。 
然后你的老板有对你说：“小祁，我们公司核心代码区域有一千万个func()函数，从func01()
到func1kw(),按你的方案，想要拓展这一千万个函数功能，就是要执行一千万次deco()函数，
这可不行呀，我心疼我的机器。” 
好了，你终于受够你老板了，准备辞职了，然后你无意间听到了装饰器这个神器，
突然发现能满足你老板的要求了。 
我们先实现一个最简陋的装饰器，不使用任何语法糖和高级语法，看看装饰器最原始的面貌

#既不需要侵入，也不需要函数重复执行
import time

def deco(func):
    def wrapper():
        startTime = time.time()
        func()
        endTime = time.time()
        msecs = (endTime - startTime)*1000
        print("time is %d ms" %msecs)
    return wrapper


@deco
def func():
    print("hello")
    time.sleep(1)
    print("world")

if __name__ == '__main__':
    f = func #这里f被赋值为func，执行f()就是执行func()
    f()


这里的deco函数就是最原始的装饰器，它的参数是一个函数，然后返回值也是一个函数。
其中作为参数的这个函数func()就在返回函数wrapper()的内部执行。
然后在函数func()前面加上@deco，func()函数就相当于被注入了计时功能，现在只要调用func()，
它就已经变身为“新的功能更所以这里装饰器就像一个注入符号多”的函数了。 
：有了它，拓展了原来函数的功能既不需要侵入函数内更改代码，
也不需要重复执行原函数。


#带有参数的装饰器
import time

def deco(func):
    def wrapper(a,b):
        startTime = time.time()
        func(a,b)
        endTime = time.time()
        msecs = (endTime - startTime)*1000
        print("time is %d ms" %msecs)
    return wrapper


@deco
def func(a,b):
    print("hello，here is a func for add :")
    time.sleep(1)
    print("result is %d" %(a+b))

if __name__ == '__main__':
    f = func
    f(3,4)
    #func()

然后你满足了Boss的要求后，Boss又说：“小祁，我让你拓展的函数好多可是有参数的呀，
有的参数还是个数不定的那种，你的装饰器搞的定不？”然后你嘿嘿一笑，深藏功与名！


#带有不定参数的装饰器
import time

def deco(func):
    def wrapper(*args, **kwargs):
        startTime = time.time()
        func(*args, **kwargs)
        endTime = time.time()
        msecs = (endTime - startTime)*1000
        print("time is %d ms" %msecs)
    return wrapper


@deco
def func(a,b):
    print("hello，here is a func for add :")
    time.sleep(1)
    print("result is %d" %(a+b))

@deco
def func2(a,b,c):
    print("hello，here is a func for add :")
    time.sleep(1)
    print("result is %d" %(a+b+c))


if __name__ == '__main__':
    f = func
    func2(3,4,5)
    f(3,4)
    #func()




</pre>
## 07.08_Python语言基础(装饰器的应用场景)(掌握)

#
	1.引入日志
	2.函数的执行时间统计
	3.执行函数前的预备处理
	4.函数执行后的清理工作
	5.权限的校验
	6.缓存




## 07.09_Python语言基础(装饰器的示例)(掌握)
#
	from time import ctime, sleep
	
	无参数的函数
	
	
	def timeFun(func):
	    def wrapped():
	        print("%s called at %s" % (func.__name__, ctime()))
	        func()
	
	    return wrapped
	
	
	@timeFun
	def foo():
	    print("i am foo")
	
	
	# foo()
	# sleep(2)
	# foo()
	
	f = timeFun(foo)
	f()

	#被装饰的函数有参数
	
	def timeFun(func):
	    def wrapped(a, b):
	        print("%s called at %s" % (func.__name__, ctime()))
	        func(a, b)
	
	    return wrapped
	
	
	@timeFun
	def foo(a, b):
	    print(a + b)
	
	
	foo(3, 5)
	
	sleep(2)
	foo(2, 4)
	
	
	# 3.被修饰的函数有不定长参数
	def timeFun(func):
	    def wrapped(*args, **kwargs):
	        print("%s called at %s" % (func.__name__, ctime()))
	        func(*args, **kwargs)
	
	    return wrapped
	
	
	@timeFun
	def foo(a, b, c):
	    print(a + b + c)
	
	
	foo(3, 5, 7)
	
	#装饰器中的return
	def timeFun(func):
	    def wrapped():
	        print("%s called at %s" % (func.__name__, ctime()))
	        func()
	    return wrapped
	@timeFun
	def foo():
	    print("i am foo")
	@timeFun
	def getInfo():
	    return "---haha----"
	
	
	foo()
	print(getInfo())




## 07.10_Python语言基础(作业)
#
	1.用函数编写计算器，要求可以计算多个值的加减乘除
	多个值的加减乘除，应当使用不定长参数，
	可以设置关键字参数的**kwargs部分表达符号

#  
	2.编写“商品管理系统”，要求如下：
	必须使用自定义函数，完成对程序的模块化
	学生信息至少包含：商品、日期、物流码，除此以外可以适当添加
	必须完成的功能：添加、删除、修改、查询（单个查询/显示所有）、退出
