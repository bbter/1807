'''
生成器
    无法直接输出生成器里面的内容
    生成器保存的是数据的算法/规则,每一次调用产生一个
    生成器创建使用yield关键字
        函数可以有返回值,返回值返回给调用者
        yield 跟 return功能类似,
            return直接返回直观结果
            yield返回给调用者的不是直观结果,是数据存放的算法,规则
'''
#
# generator00 = (x * 2 for x in range(10))
# print(generator00)
# print(type(generator00))

# for gen in generator00:
#     print(gen)

'''
print(next(generator00))
print(next(generator00))
print(next(generator00))
print(next(generator00))
'''

# print(len(generator00))

# i = 0
# while i < 5:
#     print(next(generator00))
#     i += 1

# a = 0
# b.txt = 1
# c = 0
# while a < 10:
#     b.txt,c = c,b.txt+c
#     print(b.txt)
#     a+=1



# def show():
#     a = 0
#     b.txt = 1
#     c = 0
#     while a < 10:
#         b.txt, c = c, b.txt + c
#         yield b.txt # return b.txt
#         a += 1
#
#
# fib = show()
# print(fib)
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))




# def fib():
#     a = 0
#     b.txt = 1
#     c = 0
#     while a < 10:
#         b.txt,c = c,b.txt+c
#         yield b.txt
#         a += 1
#
#
# print(fib())



# def gen1():
#     for i in range(4):
#         yield i

# t = gen1()
# print(t)
# for i in t:
#     print(i)


# i = 0
# a = 1
# b = 0

def fib(n):
    i = 0
    a = 1
    b = 0
    while i < n:
        a,b = b, a + b
        yield b
        i += 1


fib = fib(100)
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))










