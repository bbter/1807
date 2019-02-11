'''

局部变量
    在规定区域起作用的变量
    参与局部运算的变量
    定义在函数内部的变量
        正常情况下,在外部无法使用,
        只能在函数范围内部使用,函数内部的函数可以调用函数外部的变量
        不同函数中可以定义相同名字的局部变量,它们之间互不影响
'''

occupation = "健身教练"
def show():
    name = input("请输入名字:")
    age = input("请输入年龄:")
    hobby = input("请输入爱好:")
    print("这个人的名字是:%s,今年%s岁,平时喜欢%s," % (name,age,hobby))
    def demo():
        print(name)
    demo()



show()


# print("%s隔壁的小伙小张和他的关系很好" % name)


def show00():
    name = "老李"
    print("%s是一个勤劳勇敢的Python程序员" % name)


show00()