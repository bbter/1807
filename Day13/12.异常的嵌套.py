'''

IndexError
ValueError
ZeroDivisionError
异常的嵌套
    如果出现异常那么它这个异常子集的代码将无法继续运行
    和他平行的那一级可以正常执行
'''

print("代码开始运行")

try:
    print("异常处理的第一层")
    try:
        print(1/ int(input("请输入一个整数")))
        try:
            print(input("请输入一个很长的字符串")[10])
        except Exception as e:
            print(e)
        try:
            print("拉力赛累死了")
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)
except Exception as e:
    print(e)

print("代码运行结束")