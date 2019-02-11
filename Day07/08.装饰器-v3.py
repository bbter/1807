'''

公司核心代码
    测试这段代码运行消耗的时间
    改良上一次的代码
'''
import time


# def deco():
#
#     start_time = time.time()
#
#     print("hello")
#     time.sleep(1)
#     print("world")
#
#     end_time = time.time()
#
#     total_time = end_time - start_time
#     print("这段代码共消耗时间%s" % total_time)
# deco()

# 把核心代码当作参数传递

def deco():
    print("hello")
    time.sleep(1)
    print("world")

def func(fun):
    start_time = time.time()
    fun()
    end_time = time.time()

    total_time = end_time - start_time
    print("这段代码共消耗时间%s" % total_time)

func(deco)


# def xxx(func):
#     def inner():
#         start_time = time.time()
#         func()
#         end_time = time.time()
#
#         total_time = end_time - start_time
#         print("这段代码共消耗时间%s" % total_time)
#         return func
#
#     return inner
#
# deco = xxx(deco)
#
# deco()