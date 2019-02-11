# import math
# for i in range(10000):
#     x = int(math.sqrt(i+100))
#     y = int(math.sqrt(i+268))
#     if (x * x == i +100) and (y * y == i +268):
#         print(i)

# for a in range(1,5):
#     for b.txt in range(1, 5):
#         for c in range(1, 5):
#             if (a != b.txt) and (a != c) and (b.txt != c):
#                 print(a,b.txt,c)


# year = int(input("请输入年份:"))
# month = int(input("请输入月份:"))
# day = int(input("请输入日:"))
# list = [31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]
# if month == 1:
#     count = day
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     if month > 1 and month < 13:
#         count = list[month - 2] + day
# else:
#     if month > 1 and month < 13:
#         count = list[month - 2] + day - 1
# print('第' + str(count) + '天')



# profit = int(input("请输入当月利润"))
# if profit <= 100000:
#     bonus = profit * 0.1
#     print("应发放奖金总数为:%f" % bonus)
# elif profit <= 200000:
#     bonus = (profit - 100000)*0.075 + 100000 * 0.1
#     print("应发放奖金总数为:%f" % bonus)
# elif profit <= 400000:
#     bonus = (profit - 100000)*0.075 + 100000 * 0.1 + (profit - 200000)*0.05
#     print("应发放奖金总数为:%f" % bonus)
# elif profit <= 600000:
#     bonus = (profit - 100000)*0.075 + 100000 * 0.1 + (profit - 200000)*0.05 + (profit - 400000)*0.03
#     print("应发放奖金总数为:%f" % bonus)
# elif profit <= 1000000:
#     bonus = (profit - 100000) * 0.075 + 100000 * 0.1 + (profit - 200000) * 0.05 + (profit - 400000) * 0.03 + (profit - 600000)*0.015
# else:
#     bonus = (profit - 100000) * 0.075 + 100000 * 0.1 + (profit - 200000) * 0.05 + (profit - 400000) * 0.03 \
#     + (profit - 600000) * 0.015 + (profit - 1000000) * 0.01
#
#     print("应发放奖金总数为:%f" % bonus)






# print((300000 - 100000)*0.075 + 100000 * 0.1 + (300000 - 200000)*0.05)



# num = input("请输入一个正整数")
# k = 2
# print(num + "=")
# while int(num) > k:
#     if int(num) % k == 0:
#         print(str(k) + "x")
#         num = int(num) / k
#     elif int(num) % k != 0:
#         k += 1
#     print(k,end="\t")

# n=int(input("请输入正整数："))
# prime=int(2)
# if n==prime:
#     print(n)
# else:
#     while (n>=prime):
#         k=n%prime
#         if( k == 0):
#             print(prime,end="\t")
#             n=n/prime
#         else:
#             prime=prime+1


import string
# word = "ghSk 45s Df,9 87.fs sF&09f8ff "
# newword = ""
# for i in word:
#     if i.isdigit():
#         newword += i
# print(newword)
# print(newword)
# print(word.upper())
# print(word.swapcase())
# yinwen = 0
# space = 0
# shuzi = 0
# other = 0
# for i in word:
#     if i in string.ascii_letters:
#         yinwen += 1
#     elif i.isspace():
#         space += 1
#     elif i.isdigit():
#         shuzi += 1
#     else:
#         other += 1
# print("word中英文字母、空格、数字和其它字符的个数分别是:",yinwen,space,shuzi,other)
# count = 3
# user = "dushine"
# pwd = 123
# while 1:
#     username = input("请输入用户名:")
#     password = int(input("请输入密码:"))
#
#     if username == user and password == pwd:
#         print("登录成功")
#         break
#     else:
#         print("登录失败")
#         count -= 1
#         if count == 0:
#             break



# i = 2
# sum = 0
# while i <= 100:
#     if i % 2 == 0:
#         sum += i
#     else:
#         sum -= i
#     i += 1
# print(sum)
# import random
# zhu = []
# red = random.sample(range(36),6)
# blue = random.sample(range(15),1)
# zhu.extend(red)
# zhu.extend(blue)
# print(zhu)

# name = " aleX "
# print(name.strip())
# print(name.startswith("al"))
# print(name.endswith("X"))
# print(name.replace("l","p"))
# a = name.split("l")
# print(type(a))
# print(name.upper())
# print(name.lower())
# print(name[:3])
# print(name[-2:])
# print(name.index("e"))
# print(name.find("e"))

# x = 2
# y = 1
# sum = 0
# for i in range(20):
#     sum += x/y
#     y,x = x,x+y
#
# print(sum)
# n = int(input('请输入项数： '))
#
# fenzi = 2  # 分子
# fenmu = 1  # 分母
# l = []
# s = 0

# for i in range(1, n + 1):
#     a = fenzi
#     b.txt = fenmu
#
#     s += (a / b.txt)
#     l.append('%s/%s' % (a, b.txt))
#
#     fenzi = a + b.txt
#     fenmu = a
#
# print('+'.join(str(i) for i in l), end='')
# print("s)
#
#

# sub = 0
# for i in range(1,101):
#     if i % 2 == 0:
#         sub -= 1.0/i
#     else:
#         sub += 1.0/i
#
# print("结果为:%.4f" % sub)




sum = 0
for i in range(3, 100, 2):
    sum += (i-2)/i
print(sum)















