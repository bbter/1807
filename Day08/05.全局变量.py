'''

全局变量
    定义在函数外部的变量
    对所有函数起作用

    
'''

occupation = "健身教练"
occupation_lsit = ["健身教练","营养师"]
def show():
    name = input("请输入名字:")
    age = input("请输入年龄:")
    hobby = input("请输入爱好:")
    occupation_lsit.append("程序员鼓励师")
    print("这个人的名字是:%s,今年%s岁,平时喜欢%s,他的职业是%s" % (name,age,hobby,occupation_lsit))
    def demo():
        print(name)
    demo()

show()


# print("%s隔壁的小伙小张和他的关系很好" % name)


def show00():
    name = "老李"
    print("%s是一个勤劳勇敢的Python程序员,平时兼职%s" % (name,occupation_lsit))


show00()