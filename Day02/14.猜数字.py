import random
num = random.randint(0,100)

for i in range(1,8):
    my_num = int(input("请输入你猜的数字:"))
    if my_num > num:
        print("大了")
    elif my_num < num:
        print("小了")
    else:
        print("猜对啦！用了%d次机会" % i)
        break
else:
    print("你到底还是没猜对")














