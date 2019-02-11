# def printinfo():
#     name = input("请输入自己的名字")
#     age = input("请输入自己的年龄")
#     print("你的名字是%s，年龄为%s" % (name, age))
#
#
# printinfo()

'''
    函数的分类:
        无参数,无返回值
        有参数,无返回值
        无参数,有返回值
        有参数,有返回值
'''


# 无参数,无返回值
def notice():
    print("天干物燥,小心火烛,三更天啦")


# 有参数,无返回值
def play_movie(movie_name):
    print("准备好,马上开始播放大片:%s" % movie_name)

play_movie("羞羞的铁拳")


# 无参数,有返回值
def LuDaShi():
    info = "CPU:i9 9900k,GPU:2080..."
    return info

print(LuDaShi())

def add2num(a,b):
    return a+b,a*b

print(add2num(6,8))
add,mul = add2num(7,8)
print(add,mul)

res = add2num(7,8)
print(res)
