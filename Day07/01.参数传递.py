'''

值传递

引用传递
'''


def add2num(a,b):
    a += b
    print("函数中a的id:",id(a))


# 这个时候的a只是把a的值10传递给函数使用,a本身没有参与运算
a = 10
b = 5
print(a)
print(id(a))
add2num(a,b)
print(a)
print(id(a))


def append2num(list01):
    list01.append(4)
    print("函数中list01的id",id(list00))

# 引用传递,直接把指向位置传递给了调用者,改变后就真的改变了
list00 = [1,2,3]
print(list00)
print(id(list00))
append2num(list00)
print(list00)
print(id(list00))
