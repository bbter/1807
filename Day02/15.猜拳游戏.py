'''
石头 剪刀 布
要求：
   电脑随机生成一个0~2之间的正整数0，1，2，
   剪刀（0），石头（1），布（2）
   ，要求用户通过键盘录入的方式驶入0~2之间的正整数，产生结果

   生成随机数需要导入一个包    random  -->import random
   生成一个0~2    randint(0,2)
'''
import random
computer = random.randint(0,2)
myself = int(input("请出招(剪刀（0），石头（1），布（2）):"))
if computer == 0:
    print("电脑出的是剪刀")
elif computer == 1:
    print("电脑出的是石头")
else:
    print("电脑出的是布")
if (computer == 0 and myself == 2) or (computer == 1 and myself == 0) or (computer == 2 and myself == 1):
    print("YOU LOSE")
elif computer == myself:
    print("平局，再来一次")
else:
    print("YOU WIN")

















