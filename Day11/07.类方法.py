'''
类方法
    使用@classmethod修饰的方法,参数中必须有cls
    类方法可以直接使用类名调用
    类不能直接调用实例方法
        为什么类对象直接调用实例属性、方法
        类属性加载的时机早于实例对象，
    类方法中可以修改类属性
'''


class ClassRoom(object):
    height = 3

    def __init__(self):
        self.area = 60
        self.location = "旺田"


    @staticmethod
    def decorate():
        # print("本房间的高度为%s" % height)
        print("哈哈哈哈哈")


    @classmethod
    def show(cls):
        print("本教室位于杭州市江干区九堡镇牛田村旺田大酒店四楼")
        print("本房间的高度为%s" % cls.height)

    def desc(self):
        print("这里是普通的描述信息")


ClassRoom.show()



phone1000 = ClassRoom()
phone1000.show()
phone1000.desc()
print("*"*20)
ClassRoom.decorate()
phone1000.decorate()
# print(phone1000.decorate())
# print(ClassRoom.decorate())

































