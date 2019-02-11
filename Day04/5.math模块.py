'''

math
    数学模块，封装了很多数学方法
'''

import math
# 天花板数字 向上取整
print(math.ceil(4.4))

# 地板数字 向下取整
print(math.floor(4.8))

# help是Python自带的函数，通过help(XXX)可以查看XXX的所有帮助信息
help(math.floor)
help(print)
help(help)

print(math.degrees(10))
print(math.pi)
print(math.pow(2,3))
# 把2当作基数，求它的指数
print(math.log2(4))
# 前面的参数是结果，后面的参数是基数，求指数
print(math.log(9,3))
# 获取一个数字的整数部分和小数部分，返回的是一个元组，元组0位是小数 1位是整数
print(math.modf(3.5))
# 返回这个数字的绝对值，返回值是float类型
print(math.fabs(-1))
print(math.fabs(-3.3))
print(math.ceil(-4.6))
print(math.floor(-4.3))
# 返回最大公因子

print(math.gcd(10,20))















