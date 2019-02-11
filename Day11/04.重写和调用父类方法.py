'''
重写
    overrides method in XXX
    就是子类中,有一个和父亲相同名字的方法,在子类中的方法会覆盖父类中的方法
    必须有继承关系 + 方法名相同 ---》 覆盖已经继承父类的方法
    方法名                                     作用
    父类名.__init__(self)              调用指定父类中的__init__方法,获取其中定义的属性
                                        如果所调用的类的init方法中有参数，调用时也要加上参数
    super(类名,self).__init__()          调用指定类的父类中的__init__方法,获取其中定义的属性
                                            如果所调用的类的init方法中有参数，调用时也要加上参数
    super().__init()                    只能调用一个父类中的__init__方法,获取其中定义的属性
                                            如果所调用的类的init方法中有参数，调用时也要加上参数
 '''

class DemoFu(object):
    def __init__(self,cook):
        self.Kongfu = "天下第一"
        self.cook = cook
    def demo(self):
        print("我是父类中的方法")


class DemoSon(DemoFu):
    def __init__(self,cure):
        # 轻功是怎样练成的
        self.QingGong = "水上飞"
        self.cure = cure

    def demo(self):
        print("我是子类中的方法")


# 报错:如果本类继承有父类和爷爷类等更高级的类,在继承顺序中要把辈分最小的那个写在前面,后面也按照这个规则
class DemoGrandSon(DemoSon,DemoFu):
    def __init__(self):
        # 调用父类中的__init__方法
        # super(DemoGrandSon, self).__init__()
        # super(DemoSon, self).__init__()
        DemoSon.__init__(self,"痔疮")
        DemoFu.__init__(self,"苏格兰打卤面")
        # 只能获取直接父类的__init__方法
        # super().__init__()
        self.NeiGong = "乾坤大挪移"

    def demo(self):
        print("我是孙子类中的方法")



grandson = DemoGrandSon()
grandson.demo()

print(DemoGrandSon.__mro__)
print(grandson.QingGong)
print(grandson.Kongfu)
print(grandson.NeiGong)






