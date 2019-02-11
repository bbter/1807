'''

公司核心代码
    测试这段代码运行消耗的时间
'''
import time


def deco():

    start_time = time.time()

    print("hello")
    time.sleep(1)
    print("world")

    end_time = time.time()

    total_time = end_time - start_time
    print("这段代码共消耗时间%s" % total_time)
deco()