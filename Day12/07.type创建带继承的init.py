'''
type创建带继承关系和init方法的类
    在自定义的init方法



'''
class Demo14(object):
    def __init__(self):
        self.y = "yyy"

class Demo15(object):
    def __init__(self):
        self.z = "zzz"

    def xxx(self):
        print("Xxx")




def __init__(self):
    Demo14.__init__(self)
    Demo15.__init__(self)


Demo12 = type("Demo12",(Demo14,Demo15,),{"__init__":__init__})

demo12 = Demo12()
print(demo12.y)
print(demo12.z)
demo12.xxx()