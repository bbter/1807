'''

>练习：<br/>
01.从键盘输入刀子的长度，如果刀子长度没有超过10cm，允许上火车，反之不允许<br/>
02.在控制台输入一个4位数年份，判断它是否是闰年

'''


# knife_len = int(input("请输入刀子的长度(cm):"))
# if knife_len <= 10:
#     print("可以带上火车")
# else:
#     print("禁止带上火车")

year = int(input("请输入一个四位数的年份:"))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("是闰年")
else:
    print("不是闰年")