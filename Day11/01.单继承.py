'''
单继承
    抽取所有类共同的特征,形成一个父类,子类继承这个父类获取里面所有公开的内容
    减少重复代码,提高开发效率
'''

class Cat(object):
    def __init__(self):
        self.legs = 4
        self.eyes = 2


    def miao(self):
        print("喵喵喵")

class BosiCat(Cat):
    def CatchMouse(self):
        print("昨天晚上捉了四只老鼠")


class BaliCat(Cat):
    weight = "十斤"

    def __init__(self):
        # 如果想重写父类的方法,可以调用父类的初始化方法
        Cat.__init__(self)


    def show(self):
        print("这是一只臭猫")



LittleWhite = BosiCat()
LittleWhite.miao()
print(LittleWhite.eyes)
print(LittleWhite.legs)

LittleWhite.CatchMouse()


print("*"*20)

LittleBlack = BaliCat()

LittleBlack.show()