'''


偏函数和进制转换
'''

str00 = "123"
str00 = int(str00)
print(str00)


def int2(x,base):
    return int(x,base)


from functools import partial

int22 = partial(int2,base=2)
print(int22)

print(int22("0100"))



