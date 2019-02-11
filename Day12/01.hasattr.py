class Demo04(object):
    def __init__(self):
        self.f = "fff"
        self.g = "ggg"


    def demo04(self):
        print("demo04")



print(hasattr(Demo04,"demo04"))
print(hasattr(Demo04,"f"))




Demo04.h = "hhh"
print(Demo04.h)
demo004 = Demo04()
print(hasattr(Demo04,"f"))
print(hasattr(demo004,"f"))
print(hasattr(demo004,"demo04"))


print(demo004.h)
# 使用hasattr判断类属性,方法,如果存在结果返回true
# 使用hasattr判断实例属性，如果obj写的是类名,返回False,如果obj写的对象,结果存在返回true
print(hasattr(Demo04,"h"))