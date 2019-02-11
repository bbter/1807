'''
可迭代对象:可以直接作用于for循环的对象统称为可迭代对象
（Iterable）可以用isinstance()去判断一个对象是否是可迭代对象

可以直接作用于for的数据类型一般分两种:
1,集合数据类型，如list,tuple,dict,set,string
2,是generator,包括生成器和带yield的generator function

'''

# for i in range(10):
#     print(i)
#     i -=1
#     print("*"*20)
#     print(i)
#
# i = 0
# while i < 10:
#     print(i)
#     i -= 1

num00 = 12345
str00 = "12345"
list00 = [1,2,3,4,5]
tuple00 = (1,2,3,4,5)
dict00 = {1:1,2:2,3:3}
set00 = {1,2,3,4,5}
generator = (x for x in range(10))

from collections import Iterable
print(isinstance(num00,Iterable))
print(isinstance(str00,Iterable))
print(isinstance(list00,Iterable))
print(isinstance(tuple00,Iterable))
# 字典默认暴露key,迭代的时候获取的也是key
print(isinstance(dict00,Iterable))
print(isinstance(set00,Iterable))
print(isinstance(generator,Iterable))

print("*"*50)
from collections import Iterator
print(isinstance(num00,Iterator))
print(isinstance(str00,Iterator))
print(isinstance(list00,Iterator))
print(isinstance(tuple00,Iterator))
# 字典默认暴露key,迭代的时候获取的也是key
print(isinstance(dict00,Iterator))
print(isinstance(set00,Iterator))
print(isinstance(generator,Iterator))

print(next(generator))
print(next(list00))






