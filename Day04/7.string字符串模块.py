'''
str模块
    什么是字符串
    使用时不用导入
    字符串是以单引号或双引号括起来的任意文本
    'abc'
    "def"
    字符串不可变
    变量指向的字符串一旦改变，那么他在内存中指向的位置也随之改变
'''

str00 = "hello"
str01 = "True"
str02 = "None"

print(str00)
print(str01)
print(str02)
print(type(str00))
print(type(str01))
print(type(str02))

str03 = "hello"
print(id(str03))
str03 = str03 + "world"
print(str03)
print(id(str03))

print("%s" % str03)
print("{0},{1}".format(25,36))
print("{},{}".format("lalala","hahah"))



str04 = input()
print(type(str04))
print(type(bool(str04)))








