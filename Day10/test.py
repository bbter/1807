# import keyword
#
# print("self" in keyword.kwlist)




# class Student(object):
#     def __init__(self,stuNo,name,sex,age):
#         self.stuNo = stuNo
#         self.name = name
#         self.sex = sex
#         self.__age = age
#
#     def setAge(self,age):
#         if age >0 and age < 130:
#             self.__age = age
#         else:
#             self.__age = -1
#
#
#     def getAge(self):
#         return self.__age
#
#
#     def show(self):
#         print("这个学生的学号为%s,名字为%s,性别为%s,年龄为%s" %(self.stuNo,self.name,self.sex,self.__age))
#
#
#
# xiaohong = Student(20160307144,"小红","女",18)
# xiaohong.show()
# xiaohong.__age = 80
# xiaohong.show()
# xiaohong.setAge(300)
# xiaohong.show()
# print(xiaohong.getAge())






import math

class trigon(object):
    def __init__(self,length_a,length_b,length_c):
        if length_a > 0 and length_b > 0 and length_c >0:
            if length_a + length_b > length_c and length_a + length_c > length_b and length_b + length_c > length_a:
                self.length_a = length_a
                self.length_b = length_b
                self.length_c = length_c
            else:
                print("您的输入有误")
        else:
            print("您的输入有误")

    def get_perimeter(self):
        total_length = self.length_a + self.length_b + self.length_c
        return "周长为%s" % total_length

    def get_area(self):
        p = (self.length_a + self.length_b + self.length_c)/2
        area = math.sqrt(p*(p-self.length_a)*(p-self.length_b)*(p-self.length_c))
        return "面积为%s" % area



aa = trigon(3,3,3)
print(aa.get_perimeter())
print(aa.get_area())



# class BakedBun(object):
#     def __init__(self):
#         # 几成熟
#         self.cook_level = 0
#         # 文字描述
#         self.cook_string = "生的"
#         # 佐料
#         self.condiments = []
#
#     # 烤制的方法，可以传入时间,每一分钟相当于一成熟
#     def cook(self,cook_time):
#         self.cook_level += cook_time
#         # 根据cook_level的数值,改变cook_string的描述信息
#         if self.cook_level <= 3:
#             self.cook_string = "还没熟"
#         elif self.cook_level <= 5:
#             self.cook_string = "表明熟啦,里面还是生的"
#         elif self.cook_level <= 8:
#             self.cook_string = "可以吃了,烤制的刚刚好"
#         elif self.cook_level < 10:
#             self.cook_string = "马上就烤焦了"
#         else:
#             self.cook_string = "扔了吧,都焦了"
#
#     # 添加佐料的方法
#     def add_condiments(self,condiment):
#         self.condiments.append(condiment)
#
#     def __str__(self):
#         return "已经烤制了%s分钟,现在是%s,添加的佐料有%s" % (self.cook_level,self.cook_string,self.condiments)
#
#
#
# bb = BakedBun()
#
# bb.add_condiments("盐")
# bb.cook(6)
# print(bb)






# class Bank(object):
#     def __init__(self,user,password):
#         self.user = user
#         self.pssword = password
#         self.__money = 0
#
#
#     def saveMoney(self,money):
#         self.__money += money
#
#     def drawMoney(self,money):
#         if self.__money >= money:
#             self.__money -= money
#         else:
#             print("余额不足")
#
#
#     def checkMoney(self):
#         return self.__money
#
#
#     def Transfer_accounts(self,user,money):
#         if self.__money >= money:
#             self.__money -= money
#             user.__money += money
#         else:
#             print("余额不足")
#
# count = 3
# user = "dushine"
# pwd = 123
# while 1:
#     username = input("请输入用户名:")
#     password = int(input("请输入密码:"))
#
#     if username == user and password == pwd:
#         print("登录成功")
#         p1 = Bank(username,password)
#         while True:
#             print("1.存、2.取、3.查询、4.转账、0.退出")
#             select = input("请输入你需要的服务:")
#             if select.isdigit():
#                 select = int(select)
#                 if select == 0:
#                     break
#                 elif select == 1:
#                     print("欢迎使用存功能")
#                     money = int(input("请输入金额"))
#                     p1.saveMoney(money)
#                 elif select == 2:
#                     print("欢迎使用取功能")
#                     money = int(input("请输入金额"))
#                     p1.drawMoney(money)
#                 elif select == 3:
#                     print("欢迎使用查询功能")
#                     print(p1.checkMoney())
#                 elif select == 4:
#                     print("欢迎使用转账功能")
#                     user = input("请输入用户名")
#                     money = int(input("请输入金额"))
#                     p1.Transfer_accounts(user, money)
#                 else:
#                     print("输入有误")
#             else:
#                 print("输入有误,请重新输入")
#     else:
#         print("登录失败")
#         count -= 1
#         if count == 0:
#             break


