# l1 = (1,2,3,4)
#
# print(l1[-2])
# import math
#
# for i in range(-99, 100000):
#     if (math.sqrt(i+100)) % 1 == 0 and (math.sqrt(i+268)) % 1 ==0:
#         print(i)


# count = 0
# for a in range(1,5):
#     for b.txt in range(1, 5):
#         for c in range(1, 5):
#             if (a != b.txt) and (a != c) and (b.txt != c):
#                 count +=1
#                 print(a,b.txt,c,end="\t")
# print(count)



# n=int(input("请输入正整数："))
# print(n,end="=")
# prime=int(2)
# if n==prime:
#     print(n)
# else:
#     while (n>=prime):
#         k = n % prime
#         if( k == 0):
#             print(prime,end="*")
#             n=n/prime
#         else:
#             prime=prime+1



# import string
# word = "ghSk 45s Df,9 87.fs sF&09f8ff "
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




# list1 = [['Iphone8',6888],['MacPro',14800],['小米6',2499],['Coffee',31],['Book',80],['Nike Shoes',799]]
# list_cart = []
# while 1:
#     for produce in enumerate(list1):
#         print(produce)
#     select = input("请输入一个编号:")
#     if select.isdigit():
#         select = int(select)
#         if select < 6:
#             list_cart.append(list1[select])
#     elif select == "q":
#         break
# sum = 0
# for i in list_cart:
#     sum += i[1]
#
# print("已选是商品为:",list_cart)
# print("商品总价为:%d" % sum)


# import random
# while 1:
#     str01 = ""
#     for i in range(4):
#         char1 = random.choice([chr(random.randint(65, 90)), chr(random.randint(97, 122))])
#         str01 += char1
#     print(str01)
#     str02 = input("请输入验证码")
#     if str02.upper() == str01.upper():
#         print("验证码正确")
#         break
#     else:
#         print("验证码输入,请重新输入")
# import random
# sort_room = []
# name_list = ["张默", "宁财神", "李代沫", "房祖名", "柯震东", "高虎","张耀扬","满文军","呜啦啦"]
# for i in range(3):
#     room_list = random.sample(name_list,3)
#     for name in room_list:
#         name_list.remove(name)
#     sort_room.append(room_list)
# print(sort_room)
#
# travel_map_dict = {
# 		    "浙江": {"杭州": ["西湖", "千岛湖", "灵隐寺", "宋城"],
#                    "绍兴": ["鲁迅故居", "沈园", "安昌古镇", "会稽山大禹陵"],
#                    "温州": ["温州乐园", "江心屿景区", "南麂列岛", "楠溪江丽水街"]},
#
# 		    "福建": {"福州": ["三坊七巷", "鼓山", "鼓岭", "于山"],
# 			   "朝阳": ["鼓浪屿", "南普陀寺", "曾厝垵", "胡里山炮台"],
# 			   "泉州": ["南少林寺遗址", "开元寺", "泉州崇武古城", "清源山"]}}
#
# while 1:
#     province = input("请输入省份")
#     for keys in travel_map_dict.keys():
#         if province == keys:
#             while 1:
#                 city = input("请输入城市")
#                 for citys in travel_map_dict[province].keys():
#                     if city == citys:
#                         print(travel_map_dict[province][city])
#                 else:
#                     break
#     break
#
#
dict1 = {}
import random
red = sorted(random.sample(range(1,34),6))
dict1["红球"] = red
blue = random.sample(range(1,16),1)
dict1["篮球"] = blue
print(dict1)














