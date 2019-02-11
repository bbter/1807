'''
匿名函数
    没有名字的函数,使用关键字lambda声明
'''
import keyword

print('lambda' in keyword.kwlist)

sum00 = lambda a, b: a + b

print(sum00(3, 5))

c = 10
# 能范围lambda表达式以外的参数
tt = lambda a, b: a + b + c
print(tt(2, 3))
