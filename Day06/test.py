import random
# list00  = [x for x in range(20)]
# list01 = random.shuffle(list00)
# num = int(input("请随机输入一个数:"))
# if num in list00:
#     index = list00.index(num)
#     print("该数的下标为%d" % index)
# else:
#     print("不存在")

# list02 = []
# i = 0
# while i < 10:
#     num = random.randint(0,9)
#     list02.append(num)
#     i += 1
# print(list02)
# print("列表中最大值为%d,列表中最小值为%d" %(max(list02),min(list02)))


# def product(n1,n2):
#     return n1 * n2
#
# print(product(6,8))


# def maxNum(a,b.txt,c):
#     max = a
#     if b.txt > a:
#         max = b.txt
#     if c > max:
#         max = c
#     return max
#
#
# print(maxNum(10,20,0))


# def create_list():
#     n = int(input("请输入一个整型:"))
#     list00 = []
#     list01 = random.sample(range(0,100),n)
#     list00.extend(list01)
#     print(list00)
#     return list00
#
# # create_list()
# # list1 = create_list()
#
# def bianli(*args):
#     for i in args:
#         for x in i:
#             print(x)
#
# bianli(create_list())





# def exchange1(a,b.txt):
#     a,b.txt = b.txt,a
#     return a,b.txt
#
# def exchange2(a,b.txt):
#     c = a
#     a = b.txt
#     b.txt = c
#     return a,b.txt
#
# def exchange3(a,b.txt):
#     a = a + b.txt
#     b.txt = a - b.txt
#     a = a - b.txt
#     return a,b.txt

# dic1 = {}
# while 1:
#         # 提示用户输入数
#     print("1.存款 2.取款 3.查询 0.退出")
#     n = input("请选择你要办理的业务:")
#     # 判断用户输入内容的合法性
#     if n.isdigit():
#         if n == 1:
#             save_money = int(input("请输入存款金额:"))
#             if save_money < 0:
#                 print("您存储的金额有误")
#             else:
#                 dic1["money"] = save_money
#                 print("---------\n存款成功！")
#         elif n == 2:
#             reduce_money = int(input("请输入取款金额："))
#             if reduce_money >= dic1["money"]:
#                 print("您的余额不足")
#             else:
#                 dic1["money"] -= reduce_money
#                 print("---------\n取款成功！")
#         elif n == 0:
#             print("O(∩_∩)O谢谢您的使用，欢迎下次光临！")
#             break
#         elif n == 3:
#             print("---您当前账户余额：%d元---" %dic1["money"])
#         else:
#             print("您输入的业务有误")
#     else:
#         print("您输入的业务有误")



# def xxx(a):
#     if isinstance(a,str):
#         if a.islower():
#             return True
#         return False
#     else:
#         return False


# print(xxx("SSDSDdd"))



# strA = ""
# strB = ""
# str01 = input("请输入一个字符串:")
# for index,v in enumerate(str01):
#     if index % 2 == 0:
#         strA += str01[index]
#     else:
#         strB += str01[index]
#
# print(strA+strB)

# dict1 = {}
# str01 = input("请输入一个字符串:")
# str02 = str01.lower()
# for i in str02:
#     dict1[i] = str02.count(i)
# print(dict1)







# l1 = ["sdsdsd"]
# l2 = ["Sdsdskd"]
#
# b.txt = "".join(l1+l2)
# print(b.txt)








