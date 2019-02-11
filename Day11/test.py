# class Person(object):
#     hight = 170
#
#     @classmethod
#     def play(cls):
#         cls.hight = 180
#         print("我在打架")
#
#
#     @staticmethod
#     def run():
#         print("run......")
#
#     def eat(self):
#         print("eat......")
#
# Person.play()
#
# xiaobai = Person()
# xiaobai.play()
#
# xiaobai.run()
# Person.run()
#
#
# xiaobai.run()
# # Person.eat()
#
# Person.play()
# print(Person.hight)


# class People(object):
#     weight = 70
#     def __init__(self,name):
#         self.name = name
#         self.hand = 2
#
#     @classmethod
#     def setWeight(cls,w):
#         cls.weight = w
#         return cls.weight
#     def run(self):
#         print("我正在走路")
#
#
# #外部
# People.weight = 100
# print(People.weight)
#
# #内部
# print(People.setWeight(90))
#
#
#
# class Student(People):
#     def __init__(self,idNum,name):
#         People.__init__(self,name)
#         self.id = idNum
#
#     def __str__(self):
#         return "我的名字叫%s,学号是%s" % (self.name,self.id)
#
#
# xiaohong = Student(10086,"小红")
# xiaohong.run()
#
# print(xiaohong)

# poke_color = ["♥","♠","♣","♦"]
# poke_num = ['A',2,3,4,5,6,7,8,9,10,'J','Q','k']
# poke = []
# for x in poke_num:
#     x1 = str(x)
#     for c in poke_color:
#         t = x1 + c
#         poke.append(t)
#
# poke.extend(["大王","小王"])
# print(poke)
#
# player = []
#
# import random
# for i in range(3):
#     player_list = random.sample(poke,17)
#     for poke_name in player_list:
#         poke.remove(poke_name)
#     player.append(player_list)
#
# print(player)
# print(poke)





# class Test(object):
#     pass
#
# test = Test()
# print(test)
# print(Test)
#
#
#
# def info(o):
#     print(o)
# #可以将类作为参数传递函数
# info(test)
# info(Test)
# print(hasattr(Test,"new_attribute"))
# Test.new_attribute = "haha"
# print(hasattr(Test,"new_attribute"))
# print(Test.new_attribute)
#
# test1 = Test
# print(test1)




# def choose_name(name):
#     if name == "haha":
#         class haha(object):
#             pass
#         return haha
#     else:
#         class heihei(object):
#             pass
#         return heihei
#
#
# myClass = choose_name("haha")
# # myClass = choose_name("haa")
# print(myClass)
# print(myClass())
#
# print(type(1))
# print(type("1"))
# print(type(choose_name("haha")))#类的类型  返回值-->type



# Test01 = type("Test01",(),{})
# print(Test01)
# print(Test01())
#
# Test02 = type("Test01", (), {"name": "hello", "age": 18})
# print(Test02)
# print(Test02.name)
# print(Test02.age)
# print(Test02())
# print(Test02().name)
# print(Test02().age)


# Test01 = type("Test01", (), {"name": "hello", "age": 18})
# print(Test01)
# print(Test01())
# print(Test01().name)
# print(Test01().age)
#
#
# Test02 = type("Test02", (Test01,), {})
# print(Test02)
# print(Test02())
# print(Test02.name)
# print(Test02.age)
# print(Test02().name)
# print(Test02().age)
# print(Test02.__mro__)

# 添加实例方法

# Test01 = type("Test01", (), {"name": "hello", "age": 18})
# print(Test01)
# print(Test01())
# print(Test01().name)
# print(Test01().age)
#
#
# def test(self):
#     print("haha")
#
#
# Test02 = type("Test02", (Test01,), {"test": test})
# print(Test02)
# print(Test02())
# print(Test02().test)
# # demo02 = Test02().
# Test02().test()
# print(Test02.__mro__)


# 1，添加静态方法
# @staticmethod
# def test03():
#     print("hahaha--test03")
#     return "test03"
#
#
# Test003 = type("Test003", (Test01,), {"test03": test03})
# print(Test003)
# print(Test003().test03())

# 2，添加类方法
# @classmethod
# def test04(cls):
#     print("hahaha--test04")
#     return "test04"
#
#
# Test004 = type("Test004", (Test01,), {"test04": test04})
# print(Test004)
# print(Test004().test04())

# class Person(object):
#     def __init__(self, name=None, age=None):
#         self.name = name
#         self.age = age
#
#
# P = Person("小明", "22")
# P.sex = "male"
# print(P.sex)
#
# p = Person("小丽", "23")
# Person.sex = None
# print(p.sex)

# class Person(object):
#     def __init__(self, name=None, age=None):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print("吃饭....")
#
# def run(self, speed):
#     print("%s在移动,速度%s" % (self.name, speed))
#
# p = Person("老王", 23)
# p.eat()
#
# # p.run()
# person = type("person", (Person,), {"run": run})
# print(person)
# P = person("小王", "24")
# P.run("220")


# import types
#
# class Person(object):
#     def __init__(self, name=None, age=None):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print("吃饭....")
#
# def run(self, speed):
#     print("%s在移动,速度%s" % (self.name, speed))
#
# P = Person("小王","24")
# # P.run("220")
#
# P.run = types.MethodType(run,P)#第一个参数L:需要添加的方法,参数二:添加到该类的实例对象
# P.run("100")
#
#
#
#
#
# print("*"* 30)
# # 定义一个类方法
# @classmethod
# def testClass(cls):
#     cls.num = 150
#
#
# # 定义一个静态方法
# @staticmethod
# def testStatic():
#     print("----static method-----")
# P = Person("老王",22)
# Person.testClass = testClass    # 把静态方法加入到类中
# Person.testClass()              # 调用类的静态方法,执行方法中的方法体
# print(Person.num)               # 输出调用内容
#
# print("$" * 30)
# # 添加静态方法
# Person.testStatic = testStatic
# Person.testStatic()





# class Person(object):
#     __slots__ = ("name", "age")
#
# P = Person()
# P.name = "老王"
# P.age = 80
#
# print(P.name)
# print(P.age)
# # P.sex = "male"
# # print(P.sex)
# # 试一试这个限制是否对子类起作用
# class Demo(Person):
#     pass
#
# d = Demo()
# d.sex = "male"
# print(d.sex)




# class Money(object):
#     def __init__(self):
#         self.__money = 0
#
#     def getMoney(self):
#         return self.__money
#
#     def setMoney(self, value):
#         if isinstance(value, int):
#             self.__money = value
#         else:
#             print("error:不是整型")
# # 先后调用两个方法,调用set方法的值,通过set设置
#     money = property(getMoney, setMoney)
#
#
# a = Money()
# print(a.money)
# a.money = 100
# print(a.money)
#
# print(a.getMoney())
# a.setMoney(1000)
# print(a.getMoney())
#




# class Money:
#     def __init__(self):
#         self.__money = 0
#
#     @property
#     def money(self):
#         return self.__money
#
#     @money.setter
#     def money(self, value):
#         if isinstance(value, int):
#             self.__money = value
#         else:
#             print("error....")
#
#
# a = Money()
# print(a.money)
# a.money = 189
#




#使用set和get方法
# class Person(object):
#     def __init__(self,name,age):
#         #属性直接对外暴露
#         # self.age = 12
#         #限制属性
#         self.__name = name
#         self.__age = age
#     def getAge(self):
#         return self.__age
#     def setAge(self,age):
#         if age < 0:
#             age = 0
#         self.__age = age

# 使用修饰器实现set和get功能
print("*" * 30)


class Person:
    def __init__(self):
        self.__name = "oo"
        self.__age = 34

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 0 and age < 100:
            self.__age = age


p = Person()
print(p.age)
p.age = 55
print(p.age)











