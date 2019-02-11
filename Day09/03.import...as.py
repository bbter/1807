'''
import ... as ...
    把导入进来的模块或者函数重命名
        有的是因为模块或函数名太长
        有点因为不认识
        改成自己认识的更好用
    一旦使用as把模块或者函数重命名之后,原来的名字在本文件中将不生效
'''



from functools import partial as pian_han_shu


def add2(a,b):
    return a+b


pian = pian_han_shu(add2,3)
print(pian(5))
