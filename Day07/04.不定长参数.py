'''

不定长参数
        能处理比定义时更多的参数
        很多编程语言中方法有重写@override和重载@overload
        但是Python并不支持多个方法的存在,所以有的时候传入参数的长度不能确定
        不定长参数很好的解决了这个问题
        不定长参数本质上是一个元组
        如果参数列表中同时有arg和*args，那么先满足arg的数量,剩余的全部给*args


        *args 中 args 可以使用其他名字替换,但不建议这么干,因为官方都使用*args
'''


def add2num(a, b):
    return a + b


def add2num(a, b, c):
    return a + b + c


# print(add2num(3,5))
print(add2num(2,3,5))



def get_num(*args):
    print(args)
    print(type(args))
    sum00 = 0
    for i in args:
        sum00 += i
    return sum00


get_num()

sum01 = get_num(1, 2, 3, 4, 5)
print(sum01)



def get_mul(a,*args):
    result = a
    print(a)
    print(args)
    for i in args:
        result *= i
    return result


print(get_mul(2,3,4,5))




