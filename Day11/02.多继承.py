'''
多继承
    一个子类同时继承多个父类
    子类可以拥有多个父类的属性和方法
        继承属性的时候会发生覆盖的情况,继承顺序在前面的可以被访问到,后面会被覆盖
        可以调用多个父类的__init__方法来解决这个问题
        方法不会出现这个问题
    如果多个父类中有重复的方法,调用顺序是:和继承顺序保持一致
    查看获取属性获取方法的使用顺序
        类名.__mro__,返回一个元组，包含本类和所有父类
'''


class Father(object):

    def __init__(self):
        self.height = "2米"
        self.hair = "直发"


    def hobby(self):
        print("抽烟喝酒烫头")


class Mother(object):
    def __init__(self):
        self.eyes = "双眼皮"


    def show(self):
        print("洗衣做饭带孩子")


    def hobby(self):
        print("逛街")


class Son(Mother,Father):
    def __init__(self):
        Mother.__init__(self)
        Father.__init__(self)


xiaoMing = Son()
xiaoMing.hobby()
print(xiaoMing.height)
print(xiaoMing.eyes)


















