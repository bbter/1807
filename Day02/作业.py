# hour = 89
# day = hour // 24
# h = hour % 24
# print("共%d天零%d小时" % (day, h))

# a = 50
# b.txt = 30
# print(a & b.txt)
# print(a | b.txt)
# print(a ^ b.txt)


# username = input("请输入你的用户名:")
# password = int(input("请输入你的密码:"))
# userName = "小白"
# passWord = 123456
# if username == userName and password == passWord:
#     print("欢迎进入xxx的世界")
# else:
#     print("密码或者用户名错误")


# print(2<<2)
# year = int(input("请输入一个四位数的年份:"))
# if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#     print("是闰年")
# else:
#     print("不是闰年")
# a = 10
# b.txt = 20
# c = b.txt
# b.txt = a
# a = c
# print("**************")
# a = a+b.txt
# b.txt = a-b.txt
# a = a-b.txt
#
# print(a,b.txt)

# a, b.txt = 20, 10
# print(a, b.txt)
# a = int(input("请输入一个数:"))
# b.txt = int(input("请输入一个数:"))
# c = int(input("请输入一个数:"))
# if a > b.txt and b.txt > c:
#     print("最大值为%d,中间值为%d,最小值为%d" % (a, b.txt, c))
# elif a > c and c > b.txt:
#     print("最大值为%d,中间值为%d,最小值为%d" % (a, c, b.txt))
# elif b.txt > a and a > c:
#     print("最大值为%d,中间值为%d,最小值为%d" % (b.txt, a, c))
# elif b.txt > c and c > a:
#     print("最大值为%d,中间值为%d,最小值为%d" % (b.txt, c, a))
# elif b.txt > c and c > a:
#     print("最大值为%d,中间值为%d,最小值为%d" % (b.txt, c, a))
# elif c > b.txt and b.txt > a:
#     print("最大值为%d,中间值为%d,最小值为%d" % (c, b.txt, a))
# elif c > a and a > b.txt:
#     print("最大值为%d,中间值为%d,最小值为%d" % (c, a, b.txt))

# import math
#
# a = int(input("请输入一个整数:"))
# b.txt = int(input("请输入一个整数:"))
# c = int(input("请输入一个整数:"))
# if a + b.txt > c and b.txt + c > a and a + c > b.txt:
#     print("可以构成三角形")
#     per = a + b.txt + c
#     p = per / 2
#     area = math.sqrt(p * (p - a) * (p - b.txt) * (p - c))
#     # area = (math.sqrt((a + b.txt + c) * (a + b.txt - c) * (a + c - b.txt) * (b.txt + c - a))) / 4
#     print("三角形的周长为%d,面积为%d" % (per, area))
#     if (a ** 2 + b.txt ** 2 == c ** 2) or (a ** 2 + c ** 2 == b.txt ** 2) or (b.txt ** 2 + c ** 2 == a ** 2):
#         print("为直角三角形")
#     elif a == b.txt or a == c or b.txt == c:
#         if a == b.txt == c:
#             print("等边三角形")
#         else:
#             print("等腰三角形")
#     else:
#         print("普通三角形")
# else:
#     print("不能构成三角形")

# grade = int(input("岳灵珊的成绩为:"))
# if grade == 100:
#     print("父亲给她买辆车")
# elif grade > 100:
#     print("成绩有误")
# elif grade >= 90:
#     print("母亲（宁中则）给她买台笔记本电脑")
# elif grade >= 60:
#     print("母亲给她买部手机")
# elif grade >= 0:
#     print("没有礼物")
# else:
#     print("成绩有误")


# height = int(input("请输入您的身高:"))
# weight = int(input("请输入您的体重:"))
# if (height-108)*2 <= weight + 10 and (height-108)*2 >= weight - 10:
#     print("恭喜你很健康")
# else:
#     print("不健康")

num = int(input("请输入5个数"))
ge = num % 10
shi = num // 10 % 10
bai = num // 100 % 10
qian = num // 1000 % 10
wan = num // 10000
if wan == ge and qian == shi:
    print("是回文数")
else:
    print("不是回文数")
