# a = (1,2,3)
#
# print(list(a))
#
# def add2():
#     print("bbt is a good man!")
#
#
# a = set([1,2,34,5])
# print(a)
#
# a.add(add2)
# print(a)

# a = "sdsd"
# print(type(a))

#
# s = 'hijklmn'
#
#
# print(s[-2:-5])

# a = 1
# b = 2*a/4
#
# print(b)



# a = 1
# for i in range(5):
#     if i == 2:
#             break
#     a += 1
# else:
#     a += 1
# print(a)




# name=" aleX"
#
# # print(name.strip())
# # print(name.upper())
# # print(name.lower())
# # print(name[-2:])
# print(name[:-1])






# for a in range(1,100):
#     for b in range(1,100):
#         for c in range(3,100,3):
#             if (a*5 + b*3 + c/3) == 100 and a + b + c == 100:
#                 print(a,b,c)


# import random
# while 1:
#     str01 = ""
#     for i in range(4):
#         str02 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
#         str01 += str02
#
#     print(str01)
#     res = input("请输入验证码")
#     if res.upper() == str01.upper():
#         print("输入正确")
#         break


# hight = 100
# x = hight/2
#
# for i in range(2,11):
#     hight += x *2
#     x /= 2
#
# print(hight,x)

# height = 100.0
# H = height / 2
#
# for n in range(2, 11):
#     height += 2 * H
#     H /= 2
#
# print(height,H)

# taozi = 1
# day = 9
#
# while day > 0 :
#     taozi = (taozi + 1) * 2
#     day -= 1
#
# print(taozi)


# import random
#
# num1 = random.randint(1,99999)
# print(num1)
# print("这个数是%d位数" % len(str(num1)))
# print(str(num1)[::-1])
#
# count = 0
# str00 = input("请输入一串字符")


import string
# def is_chinese(uchar):
#     """判断一个unicode是否是汉字"""
#     if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
#         return True
#     else:
#         return False
# str11 = "Sdsadsd哈哈哈"
# for sd in str11:
#     if string.is:
#         print(sd)


# for i in str00:
#     if i.



# def is_chinese(uchar):
#     """判断一个unicode是否是汉字"""
#     if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
#         return True
#     else:
#         return False
#
# import string
#
# zhongyingwen = 0
# numCount = 0
# space = 0
# other = 0
# str00 = input("请输入一串字符:")
# for i in str00:
#     if is_chinese(i) or i in string.ascii_letters:
#         zhongyingwen += 1
#     elif i.isdigit():
#         numCount += 1
#     elif i.isspace():
#         space += 1
#     else:
#         other += 1
#
# print(zhongyingwen,numCount,space,other)


# travel_map_dict = {
#         "浙江": {"杭州": ["西湖", "千岛湖", "灵隐寺", "宋城"],
#                "绍兴": ["鲁迅故居", "沈园", "安昌古镇", "会稽山大禹陵"],
#                "温州": ["温州乐园", "江心屿景区", "南麂列岛", "楠溪江丽水街"]},
#
#         "福建": {"福州": ["三坊七巷", "鼓山", "鼓岭", "于山"],
#            "厦门": ["鼓浪屿", "南普陀寺", "曾厝垵", "胡里山炮台"],
#            "泉州": ["南少林寺遗址", "开元寺", "泉州崇武古城", "清源山"]}}
#
# while 1:
#     province = input("请输入省份:")
#     for keys in travel_map_dict.keys():
#         if province == keys:
#             while 1:
#                 city = input("请输入城市:")
#                 for citys in travel_map_dict[province].keys():
#                     if city == citys:
#                         print(travel_map_dict[province][city])
#                 break
#     else:
#         break



# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d * %d = %d" %(j,i,i*j),end=" ")
#     print()
#
# for i in range(1,10):
#     print(i)


def multiplication_table(n):
    if n < 1:
        return
    multiplication_table(n - 1)
    for m in range(1, n + 1):
        print("%d * %d = %d" % (m, n, m * n), end="\t")
    print()

multiplication_table(9)

# x = 10
# y = 100
# z = 121
# x += y
# x = (y = z + 1)
#
# x = "\nsd"
# y = "Sds"
# min = x if x < y else y
A = range(100)
print(A[2-3])