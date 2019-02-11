'''
导入一部分内容
    有时候只需要模块中的某一个函数,
    如果全部导入会消耗更多内存,
    同样加载时间也会很长
导入模块中多个函数
    from 模块 import 函数1,函数2，函数3...
    这样可以单次导入模块中的多个函数
    这样导入的函数不需要使用模块名字调用
导入一个模块中的所有函数
    from 模块名 import *
    这样可以导入一个模块中的所有函数
    和import 模块作用一样
    但是可以不用模块名称直接调用函数
'''
from random import randint
from math import fabs,ceil

from time import *

sleep(2)
print(time())
print(randint(1,100))

print(fabs(-10))
print(ceil(2.3))












