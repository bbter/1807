'''
*
* *
* * *
* * * *
* * * * *

'''

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# b.txt = 0
# c = 1
# for i in range(10):
#     # b.txt,c  = c, b.txt+c
#     # 引入第三个变量交互变量的值
#     temp = c
#     c = b.txt + c
#     b.txt = temp
#     print(b.txt)

# 百元买百鸡
for gong in range(1,20):
    for mu in range(1,33):
        for xiao in range(3,99,3):
            if gong + mu + xiao == 100 and gong * 5 + mu * 3 + xiao / 3 == 100:
                print("公鸡:%d,母鸡:%d,雏鸡:%d" % (gong,mu,xiao))












