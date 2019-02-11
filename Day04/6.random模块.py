'''
random
        随机数模块
        使用时候必须先导入模块random

variable --> v
function --> f
class --> c
'''

import random
import math
print(math.ceil(random.random()*23))

print(random.randint(1,23))
# 从指定集合或者列表中获取X个元素，返回一个列表，列表中的元素无序，不重复，x要小于等于列表的长度
res = random.sample(range(33),6)
print(res)
# 获取指定范围的一个数字，一般是float类型
print(random.uniform(1,10))
# 从一个列表或者集合中随机抽取一个元素
print(random.choice(range(1,16)))

print(random.choices(population=range(1,33),k=6))

res.sort()
print(res)
# 打乱列表元素的顺序
random.shuffle(res)
print("打乱顺序的列表",res)

# str00 = "hello world!"
# print(random.shuffle(str00))

# 随机选取指定范围内的一个元素可以设置步长
print(random.randrange(1,33,2))








