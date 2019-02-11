def add2(a,b):
    return a+b

#导入类
from functools import partial

# 创建对象--> 使用partial类--> 中的构造方法--> 创建偏函数对象
add22 = partial(add2,3)


