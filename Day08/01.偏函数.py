'''
偏函数
    偏:以偏概全的偏
        函数中已经定义了一部分参数
        更加方便和准确的调用函数
'''

from functools import partial
def add2(a,b):
    res = a + b
    return res

result = add2(3,5)
print(result)


# 创建一个偏函数,传入函数和其中一部分参数
add5 = partial(add2,5)
print(add5)
result1 = add5(3)
# 调用偏函数,获取返回值:返回值是偏函数中原函数的返回值
print(result1)





def datecount(year,month,day):
    list = [31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]
    if month == 1:
        count = day
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        if month > 1 and month < 13:
            count = list[month - 2] + day
    else:
        if month > 1 and month < 13:
            count = list[month - 2] + day - 1
    return '第' + str(count) + '天,第'






























